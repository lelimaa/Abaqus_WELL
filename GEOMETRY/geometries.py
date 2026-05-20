# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import Superados.assembly as assembly
import sys
import os

from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

def Pipe(name_model, name_part, inner_radius, base_depth, top_depth, thickness):

    # Creation of Sketch - Geometry of the Pipe
    sketch_name = '__profile__' + name_part
    s = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=10000.0)
    s.sketchOptions.setValues(viewStyle=AXISYM)
    s.setPrimaryObject(option=STANDALONE)

    # Creation of the Axisymmetric Line
    axis = s.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s.FixedConstraint(entity=axis)

    # Construction of the Pipe Geometry
    s.rectangle(point1=(inner_radius, -(top_depth)),
                point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(
        name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    return p


def Fluid(name_model, name_part, inner_radius, base_depth, top_depth, thickness):

    # Creation of Sketch - Geometry of the Fluid/Annular
    sketch_name = '__profile__' + name_part
    s1 = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=1000.0)
    s1.sketchOptions.setValues(viewStyle=AXISYM)
    s1.setPrimaryObject(option=STANDALONE)

    # Creation of the Axisymmetric Line
    axis = s1.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s1.FixedConstraint(entity=axis)

    # Construction of the Fluid/Annular Geometry
    s1.rectangle(point1=(inner_radius, -(top_depth)),
                point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(
        name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    return p


def Rock(name_model, name_part, inner_radius, base_depth, top_depth, thickness):


    # Creation of Sketch - Geometry of the Rock
    sketch_name = '__profile__' + name_part
    s2 = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=1000.0)
    s2.sketchOptions.setValues(viewStyle=AXISYM)
    s2.setPrimaryObject(option=STANDALONE)

    # Creation of the Axisymmetric Line
    axis = s2.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s2.FixedConstraint(entity=axis)

    # Construction of the Rock Geometry
    s2.rectangle(point1=(inner_radius, -(top_depth)),
                point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s2)
    s2.unsetPrimaryObject()
    # Creation of Reference Points at the top depths
    s2.Line(point1=(0, top_depth), point2=(1000, top_depth))
    rp_top = p.ReferencePoint(point=(0.0, -(top_depth), 0.0))
    p.Set(name='RP_TOP_%s' % top_depth, referencePoints=(p.referencePoints[rp_top.id], ))
    # Creation of Reference Points at the base depths
    s2.Line(point1=(0, base_depth), point2=(1000, base_depth))
   
    return p


# Creating Partitions

def PartitionLayersByDepth(model_name, part_name, layer_depths):
    """
    Cria partições horizontais (camadas) em uma Part axisimétrica
    usando planos em profundidades especificadas.
    """
    model = mdb.models[model_name]
    p = model.parts[part_name]

    for depth in layer_depths:
        y_coord = -depth  # convenion of your model

        # Create horizontal datum plane
        dp = p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y_coord)
        datum_id = dp.id

        # Partition all faces cut by the plane
        p.PartitionFaceByDatumPlane(datumPlane=p.datums[datum_id],
                                    faces=p.faces[:]
                                    )

def CreateGeometry(name_model, name, data):
    print("Creating Geometry: ", name)

    geometry = {
        "ROCK": Rock,
        "FLUID": Fluid,
        "PIPE": Pipe
    }

    geom_func = geometry.get(name)
    if geom_func is not None:
        return geom_func(name_model,
                         name,
                         data["inner_radius"],
                         data["base_depth"],
                         data["top_depth"],
                         data["thickness"]
                         )
    else:
        raise ValueError("Geometry type '%s' is not recognized." % name)