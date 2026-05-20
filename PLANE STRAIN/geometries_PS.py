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

    # depth = base_depth - top_depth
    # Crianção do Sketch - Geometria do Revestimento
    sketch_name = '__profile__' + name_part
    s = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=10000.0)
    s.sketchOptions.setValues(viewStyle=AXISYM)
    s.setPrimaryObject(option=STANDALONE)

    # Criação da Linha de Axisimetria
    axis = s.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s.FixedConstraint(entity=axis)

    # Construção da Geometria do Revestimento
    s.rectangle(point1=(inner_radius, -(top_depth)),
                point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(
        name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    return p


def Fluid(name_model, name_part, inner_radius, base_depth, top_depth, thickness):

    # depth = base_depth - top_depth
    # Criação do Sketch - Geometria do Revestimento
    sketch_name = '__profile__' + name_part
    s1 = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=1000.0)
    s1.sketchOptions.setValues(viewStyle=AXISYM)
    s1.setPrimaryObject(option=STANDALONE)

    # Criação da Linha de Axisimetria
    axis = s1.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s1.FixedConstraint(entity=axis)

    # Construção da Geometria do Fluido/Anular
    s1.rectangle(point1=(inner_radius, -(top_depth)),
                point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(
        name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    return p


def Rock(name_model, name_part, inner_radius, base_depth, top_depth, thickness):

    # base_depth = int(base_depth)
    # top_depth = int(top_depth)

    # depth = base_depth - top_depth
    # Criação do Sketch - Geometria da Rocha
    sketch_name = '__profile__' + name_part
    s2 = mdb.models[name_model].ConstrainedSketch(
        name=sketch_name, sheetSize=1000.0)
    s2.sketchOptions.setValues(viewStyle=AXISYM)
    s2.setPrimaryObject(option=STANDALONE)

    # Criação da Linha de Axisimetria
    axis = s2.ConstructionLine(point1=(0.0, -10000.0), point2=(0.0, 10000.0))
    s2.FixedConstraint(entity=axis)

    # Construção da Geometria da Rocha
    s2.rectangle(point1=(inner_radius, -(top_depth)),
                point2=(inner_radius + thickness, -(base_depth)))

    p = mdb.models[name_model].Part(name=name_part, dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s2)
    s2.unsetPrimaryObject()
    # Criação dos Reference Points nas profundidades de topo
    s2.Line(point1=(0, top_depth), point2=(1000, top_depth))
    rp_top = p.ReferencePoint(point=(0.0, -(top_depth), 0.0))
    p.Set(name='RP_TOP_%s' % top_depth, referencePoints=(p.referencePoints[rp_top.id], ))
    # Criação dos Reference Points nas profundidades de base
    s2.Line(point1=(0, base_depth), point2=(1000, base_depth))
    # rp_base = p.ReferencePoint(point=(0.0, -(base_depth), 0.0))
    # p.Set(name='RP_BASE_%s' % base_depth, referencePoints=(p.referencePoints[rp_base.id], ))
   
    return p

# try:
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# except NameError:
#     Abaqus/CAE interactive mode
#     BASE_DIR = os.getcwd()

# if BASE_DIR not in sys.path:
#     sys.path.insert(0, BASE_DIR)

# Creating Partitions

def PartitionLayersByDepth(model_name, part_name, layer_depths):
    """
    Cria partições horizontais (camadas) em uma Part axisimétrica
    usando planos em profundidades especificadas.
    """
    model = mdb.models[model_name]
    p = model.parts[part_name]

    # Todas as faces do shell axisimétrico
    # faces = p.faces[:]

    for depth in layer_depths:
        y_coord = -depth  # convenção do seu modelo

        # Cria plano datum horizontal
        dp = p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y_coord)
        datum_id = dp.id

        # Particiona todas as faces cortadas pelo plano
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