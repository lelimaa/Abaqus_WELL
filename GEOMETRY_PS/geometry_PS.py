# -*- coding: utf-8 -*-
from abaqusConstants import *
from abaqus import mdb
import numpy as np
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import sys
# import os

from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

class PlaneStrainPart:

    def __init__(self, name, data, span="half"):
        self.name = name
        self.data = data
        self.span = span
        self.get_geometry()

    # def parameterize_geometry(self):
    #     standoff = self.data.get("standoff", 0.0)
    #     self.geometry["center1"][0] += standoff
    #     self.geometry["center2"][0] += standoff

    #     min_wallthickness = self.data.get("excentricity", 0.0)
    #     self.geometry["center1"][0] += min_wallthickness
    #     self.geometry["center2"][1] += min_wallthickness

    #     ovalization = self.data.get("ovalization", 0.0)
    #     self.geometry["center1"][0] += ovalization
    #     self.geometry["center2"][1] += ovalization
    #     pass

    def get_geometry(self):
        center1 = self.data.get("center1", [0,0])
        center2 = self.data.get("center2", [0,0])
        Ro1 = self.data.get("outer_radius")
        Ro2 = self.data.get("outer_radius")
        Ri1 = Ro1 - self.data.get("thickness")
        Ri2 = Ro2 - self.data.get("thickness")
        self.geometry = {
            "center1": center1,
            "center2": center2,
            "Ro1": Ro1,
            "Ro2": Ro2,
            "Ri1": Ri1,
            "Ri2": Ri2
        }

    def create_part(self, modelName):
        m = mdb.models[modelName]
        sketch_name = '__profile__' + self.name
        s = m.ConstrainedSketch(name=sketch_name, sheetSize=200.0)
        s.setPrimaryObject(option=STANDALONE)

        g1 = s.ArcByCenterEnds(center=self.geometry["center1"], point1 = (self.geometry["Ro1"], 0.0), point2 = (self.geometry["Ro2"], 0.0), direction=COUNTERCLOCKWISE)
        g2 = s.ArcByCenterEnds(center=self.geometry["center2"], point1 = (self.geometry["Ri1"], 0.0), point2 = (self.geometry["Ri2"], 0.0), direction=COUNTERCLOCKWISE)

        if self.span == "half":
            g3 = s.Line(point1=(-self.geometry["Ro1"], 0.0), point2=(self.geometry["Ro1"], 0.0))
            s.autoTrimCurve(curve1=g1, point1=(self.geometry["center1"][0], -self.geometry["Ro2"]))
            s.autoTrimCurve(curve1=g2, point1=(self.geometry["center2"][0], -self.geometry["Ri2"]))
            s.autoTrimCurve(curve1=g3, point1=self.geometry["center1"])
        elif self.span == "quarter":
            g3 = s.Line(point1=(self.geometry["center1"][0], 0.0), point2=(self.geometry["Ro1"], 0.0))
            g4 = s.Line(point1=(self.geometry["center1"][0], 0.0), point2=(0.0, self.geometry["Ro2"]))
            s.autoTrimCurve(curve1=g1, point1=(self.geometry["center1"][0], -self.geometry["Ro2"]))
            s.autoTrimCurve(curve1=g2, point1=(self.geometry["center2"][0], -self.geometry["Ri2"]))
            s.autoTrimCurve(curve1=g3, point1=self.geometry["center1"])
            s.autoTrimCurve(curve1=g4, point1=self.geometry["center1"])
        p = m.Part(name=self.name, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        del m.sketches[sketch_name]
        return p

    def set_Mesh():
        pass
        # self.elemTypes = (CPE4, CPE3)
        # elemType1 = mesh.ElemType(elemCode=self.elemTypes[0], elemLibrary=STANDARD)
        # elemType2 = mesh.ElemType(elemCode=self.elemTypes[1], elemLibrary=STANDARD)

        # p.setMeshControls(regions=p.faces, technique=STRUCTURED)
        # p.setElementType(regions=(p.faces,), elemTypes=(elemType1, elemType2))

        # ec = geomAuxiliar.filterEdges(p.edges, geomAuxiliar.isCircularEdge)
        # eh = geomAuxiliar.filterEdges(p.edges, geomAuxiliar.isHorizontalEdge)

        # p.seedEdgeByNumber(edges=eh, number=self.numElems[0], constraint=FINER)
        # p.seedEdgeByNumber(edges=ec, number=self.numElems[1], constraint=FINER)
        # p.generateMesh()

    def add_to_assembly(self, modelName):
        m = mdb.models[modelName]
        m.rootAssembly.Instance(name=self.name,
                                part=m.parts[self.name],
                                dependent=ON)
        m.rootAssembly.regenerate()

    def create_base_sets(self, modelName):

        m = mdb.models[modelName]
        p = m.parts[self.name]

        p.Set(name='ALL', faces=p.faces)
        if self.span == "half":
            angles = (0.25*np.pi, 0.75*np.pi)
        elif self.span == "quarter":
            angles = (0.25*np.pi,)
        else:
            angles = (0.25*np.pi, 0.75*np.pi, 1.25*np.pi, 1.75*np.pi)
        od_edges = p.edges[:0]
        id_edges = p.edges[:0]
        for angle in angles:
            xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
                   self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1], 0.0)
            xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
                   self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1], 0.0)
            od_edges += p.edges.findAt((xy1,))
            id_edges += p.edges.findAt((xy2,))
        p.Set(name='OD', edges = od_edges)
        p.Set(name='ID', edges = id_edges)

    def create_spec_sets(self, modelName):
        pass

    def create_contact_sets(self):
        pass

# if __name__ == "__main__":
#     mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')
#     AnnulusPart = PlaneStrainPart("AnnulusPart1",
#                      data={"center1": [0,0],
#                            "center2": [0,0],
#                            "outer_radius": 10,
#                            "thickness": 2},)
#     AnnulusPart.create_part("MyFirstModel")
#     AnnulusPart.create_base_sets("MyFirstModel")
#     AnnulusPart.add_to_assembly("MyFirstModel")
#     print("Annulus created and added to assembly.")

#     RockPart = PlaneStrainPart("RockPart1",
#                      data={"center1": [0,0],
#                            "center2": [0,0],
#                            "outer_radius": 100,
#                            "thickness": 90},)
#     RockPart.create_part("MyFirstModel")
#     RockPart.create_base_sets("MyFirstModel")
#     RockPart.add_to_assembly("MyFirstModel")
#     print("Rock created and added to assembly.")

#     CasingPart = PlaneStrainPart("CasingPart1",
#                      data={"center1": [0,0],    
#                            "center2": [0,0],
#                            "outer_radius": 8,
#                            "thickness": 2},)
#     CasingPart.create_part("MyFirstModel")
#     CasingPart.create_base_sets("MyFirstModel")
#     CasingPart.add_to_assembly("MyFirstModel")
#     print("Casing created and added to assembly.")