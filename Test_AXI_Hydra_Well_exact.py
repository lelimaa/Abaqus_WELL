# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
# import Superados.assembly as assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

import numpy as np


# Creation of the part
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
# defining the type of the model as axisymmetric
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
# Construction of the geometry
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.108445, -2500.0), point2=(15.0, -3500.0))
p = mdb.models['Model-1'].Part(name='Analise-1', dimensionality=AXISYMMETRIC, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Analise-1']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Analise-1']
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Analise-1']
# Creating a reference point at the top of the model
p.ReferencePoint(point=(0.0, -2500, 0.0))
mdb.models['Model-1'].parts['Analise-1'].features.changeKey(fromName='RP', 
    toName='RP_2500_0')

# Partitioning the part to create sets for materials and boundary conditions
p = mdb.models['Model-1'].parts['Analise-1']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    7.55422, 500.0, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=2039.6, gridSpacing=50.99, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Analise-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)


# creating horizontal lines for partitioning
s1.Line(point1=(-7.55422, -3000.0), point2=(191.212499999953, 
    -3000.0)) # first line at the top

s1.Line(point1=(-7.55422, -3333.3), point2=(191.212499999953, 
    -3333.3)) # second line at the middle 1
s1.HorizontalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.CoincidentConstraint(entity1=v[4], entity2=g[6], addUndoState=False)


s1.Line(point1=(-7.55422, -3666.6), point2=(203.96, 
    -3666.6)) # third line at the middle 2
s1.HorizontalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[8], addUndoState=False)
s1.CoincidentConstraint(entity1=v[6], entity2=g[6], addUndoState=False)

s1.Line(point1=(-7.55422, -4000.0), point2=(203.96, 
    -4000.0)) # last line at the bottom



s1.Line(point1=(-7.445778, -2500.0), point2=(-7.445778, 
    -4500.0)) # first vertical line at the inner radius of the casing

s1.Line(point1=(-7.4288105, -2500.0), point2=(-7.4288105, 
    -4500.0)) # second vertical line at the outer radius of the casing

s1.Line(point1=(-7.4224605, -2500.0), point2=(-7.4224605, 
    -4500.0)) # third vertical line at the inner radius of the well

s1.Line(point1=(-6.8954105, -2500.0), point2=(-6.8954105, 
    -4500.0)) # fourth vertical line at the middle of the rock


s1.VerticalConstraint(entity=g[11], addUndoState=False)
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces


# Partitioning the faces with the created lines
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']


# Creating sets for materials and boundary conditions
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#fff ]', ), )
r = p.referencePoints
refPoints=(r[2], )
p.Set(faces=faces, referencePoints=refPoints, name='ALL')
p1 = mdb.models['Model-1'].parts['Analise-1']
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#fff ]', ), )
p.Set(faces=faces, name='ALL')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#da4 ]', ), )
p.Set(faces=faces, name='ALLROCK')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#25b ]', ), )
p.Set(faces=faces, name='FASEI')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#248 ]', ), )
p.Set(faces=faces, name='FASEI_ANNULAR')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1000 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#8028 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_ID')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10402000 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_OD')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#800000 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_TOP')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#a05000 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_TT')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10082 ]', ), )
p.Set(edges=edges, name='FASEI_COMPLETED_WELL')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#248 ]', ), )
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10082 ]', ), )
p.Set(edges=edges, faces=faces, name='FASEI_FLUIDO')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10082 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#180aa ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_ID')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10412082 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_OD')
p1 = mdb.models['Model-1'].parts['Analise-1']
mdb.models['Model-1'].parts['Analise-1'].deleteSets(setNames=('FASEI_FLUIDO', 
    'FASEI_FLUIDO_BASE', 'FASEI_FLUIDO_ID', 'FASEI_FLUIDO_OD', ))
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#248 ]', ), )
p.Set(faces=faces, name='FASEI_FLUIDO')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1000 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_BASE')
e = p.edges
edges = e.getSequenceFromMask(mask=('[#8028 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_ID')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10402000 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_OD')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#800000 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_TOP')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10402000 ]', ), )
p.Set(edges=edges, name='FASEI_OPEN_WELL')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#13 ]', ), )
p.Set(faces=faces, name='FASEI_REV')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#13 ]', ), )
p.Set(faces=faces, name='FASEI_REV_ABOVE_TOC')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
p.Set(edges=edges, name='FASEI_REV_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10082 ]', ), )
p.Set(edges=edges, name='FASEI_REV_ID')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#8028 ]', ), )
p.Set(edges=edges, name='FASEI_REV_OD')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#40 ]', ), )
p.Set(edges=edges, name='FASEI_REV_TOP')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#55 ]', ), )
p.Set(edges=edges, name='FASEI_REV_TT')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d00 ]', ), )
p.Set(faces=faces, name='FASEI_SLAVE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10402000 ]', ), )
p.Set(edges=edges, name='FASEI_WELL')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10402000 ]', ), )
p.Set(edges=edges, name='FASEI_WELL_CIMENTO_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#420 ]', ), )
p.Set(faces=faces, name='L1-I')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#20020000 ]', ), )
p.Set(edges=edges, name='L1-I_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#400000 ]', ), )
p.Set(edges=edges, name='L1-I_ID')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#40000 ]', ), )
p.Set(edges=edges, name='L1-I_OD')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#40080000 ]', ), )
p.Set(edges=edges, name='L1-I_TOP')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#880 ]', ), )
p.Set(faces=faces, name='L2-I')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#8000800 ]', ), )
p.Set(edges=edges, name='L2-I_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#10000000 ]', ), )
p.Set(edges=edges, name='L2-I_ID')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1000000 ]', ), )
p.Set(edges=edges, name='L2-I_OD')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#20020000 ]', ), )
p.Set(edges=edges, name='L2-I_TOP')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#104 ]', ), )
p.Set(faces=faces, name='L3-I')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#4000200 ]', ), )
p.Set(edges=edges, name='L3-I_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#2000 ]', ), )
p.Set(edges=edges, name='L3-I_ID')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#400 ]', ), )
p.Set(edges=edges, name='L3-I_OD')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#8000800 ]', ), )
p.Set(edges=edges, name='L3-I_TOP')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#a05000 ]', ), )
p.Set(edges=edges, name='MESH_TT_ANNULARS')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#55 ]', ), )
p.Set(edges=edges, name='MESH_TT_PIPES')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#a0a00 ]', ), )
p.Set(edges=edges, name='MESH_TT_ROCK_FAR')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#6c000000 ]', ), )
p.Set(edges=edges, name='MESH_TT_ROCK_NEAR')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.Set(edges=edges, name='MESH_VERTICAL')
p = mdb.models['Model-1'].parts['Analise-1']
r = p.referencePoints
refPoints=(r[2], )
p.Set(referencePoints=refPoints, name='REFPT')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#1040400 ]', ), )
p.Set(edges=edges, name='ROCK_BC')
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d00 ]', ), )
p.Set(faces=faces, name='ROCK_OUTPUT')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#4001204 ]', ), )
p.Set(edges=edges, name='YSYM_BASE')
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#40880040 ]', ), )
p.Set(edges=edges, name='YSYM_TOP')

## creating the surfaces for the interaction properties

p = mdb.models['Model-1'].parts['Analise-1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#10c03000 ]', ), )
side2Edges = s.getSequenceFromMask(mask=('[#8028 ]', ), )
p.Surface(side1Edges=side1Edges, side2Edges=side2Edges, name='FASEI_ANNULAR')

p = mdb.models['Model-1'].parts['Analise-1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#10082 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_COMPLETED_WELL')

p = mdb.models['Model-1'].parts['Analise-1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#10402000 ]', ), )
side2Edges = s.getSequenceFromMask(mask=('[#8028 ]', ), )
p.Surface(side1Edges=side1Edges, side2Edges=side2Edges, name='FASEI_FLUIDO')

p = mdb.models['Model-1'].parts['Analise-1']
s = p.edges
side2Edges = s.getSequenceFromMask(mask=('[#8028 ]', ), )
p.Surface(side2Edges=side2Edges, name='FASEI_MASTER')

p = mdb.models['Model-1'].parts['Analise-1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#10402000 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_OPEN_WELL')

p = mdb.models['Model-1'].parts['Analise-1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#100c6 ]', ), )
side2Edges = s.getSequenceFromMask(mask=('[#8028 ]', ), )
p.Surface(side1Edges=side1Edges, side2Edges=side2Edges, name='FASEI_REV')

p = mdb.models['Model-1'].parts['Analise-1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#10402000 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_WELL')

# Defining materials

mdb.models['Model-1'].Material(name='FLUIDO')
mdb.models['Model-1'].materials['FLUIDO'].Conductivity(table=((0.702, ), ))
mdb.models['Model-1'].materials['FLUIDO'].Density(table=((1.0, ), ))
mdb.models['Model-1'].materials['FLUIDO'].Elastic(table=((10000.0, 0.0), ))
mdb.models['Model-1'].materials['FLUIDO'].SpecificHeat(table=((2060.0, ), ))
mdb.models['Model-1'].Material(name='L1-I-FOLHELHO')
mdb.models['Model-1'].materials['L1-I-FOLHELHO'].Conductivity(table=((1.592, ), 
    ))
mdb.models['Model-1'].materials['L1-I-FOLHELHO'].Density(table=((
    2332.73533930301, ), ))
mdb.models['Model-1'].materials['L1-I-FOLHELHO'].Elastic(table=((20001698760.0, 
    0.29), ))
mdb.models['Model-1'].materials['L1-I-FOLHELHO'].SpecificHeat(table=((0.209946, 
    ), ))
mdb.models['Model-1'].materials['L1-I-FOLHELHO'].MohrCoulombPlasticity(table=((
    28.0, 7.0), ))
mdb.models['Model-1'].materials['L1-I-FOLHELHO'].mohrCoulombPlasticity.MohrCoulombHardening(
    table=((20001698.76, 0.0), ))
mdb.models['Model-1'].materials['L1-I-FOLHELHO'].mohrCoulombPlasticity.TensionCutOff(
    temperatureDependency=OFF, dependencies=0, table=((0.0, 0.0), ))
mdb.models['Model-1'].Material(name='L2-I-ARENITO')
mdb.models['Model-1'].materials['L2-I-ARENITO'].Conductivity(table=((1.869, ), 
    ))
mdb.models['Model-1'].materials['L2-I-ARENITO'].Density(table=((
    1780.08814332222, ), ))
mdb.models['Model-1'].materials['L2-I-ARENITO'].Elastic(table=((24062022924.0, 
    0.25), ))
mdb.models['Model-1'].materials['L2-I-ARENITO'].SpecificHeat(table=((0.209946, 
    ), ))
mdb.models['Model-1'].materials['L2-I-ARENITO'].MohrCoulombPlasticity(table=((
    30.0, 7.5), ))
mdb.models['Model-1'].materials['L2-I-ARENITO'].mohrCoulombPlasticity.MohrCoulombHardening(
    table=((20001698.76, 0.0), ))
mdb.models['Model-1'].materials['L2-I-ARENITO'].mohrCoulombPlasticity.TensionCutOff(
    temperatureDependency=OFF, dependencies=0, table=((0.0, 0.0), ))
mdb.models['Model-1'].Material(name='L3-I-HALITA')
mdb.models['Model-1'].materials['L3-I-HALITA'].Conductivity(table=((5.55, ), ))
mdb.models['Model-1'].materials['L3-I-HALITA'].Creep(temperatureDependency=ON, 
    table=((1.01924e-41, 3.0, 0.7, 9.5), ))  # works on Abaqus 2020
# mdb.models['Model-1'].materials['L3-I-HALITA'].Creep(law=DOUBLE_POWER, 
#         table=((0.0077864000,6042.9046228220,2.9400000000,0.0076093000,6042.9046228220,8.1500000000,10300006.1216400005), ))  # works on Abaqus 2024 
mdb.models['Model-1'].materials['L3-I-HALITA'].Density(table=((
    1780.08814332222, ), ))
mdb.models['Model-1'].materials['L3-I-HALITA'].Elastic(table=((20400009045.2, 
    0.36), ))
mdb.models['Model-1'].materials['L3-I-HALITA'].SpecificHeat(table=((0.209946, 
    ), ))
mdb.models['Model-1'].Material(name='VM11013CRSS')
mdb.models['Model-1'].materials['VM11013CRSS'].Conductivity(table=((45.3452, ), 
    ))
mdb.models['Model-1'].materials['VM11013CRSS'].Density(table=((7950.0, ), 
    ))
mdb.models['Model-1'].materials['VM11013CRSS'].Elastic(table=((
    206842800000.0, 0.3), ))
mdb.models['Model-1'].materials['VM11013CRSS'].Plastic(
    temperatureDependency=ON, table=((758423600.0, 0.0, 273.15), (
    758423600.0, 0.25, 273.15), (756375856.28, 0.0, 298.15), (756375856.28, 
    0.25, 298.15), (725659700.48, 0.0, 373.15), (725659700.48, 0.25, 
    373.15), (705182263.28, 0.0, 423.15), (705182263.28, 0.25, 423.15), (
    684704826.08, 0.0, 473.15), (684704826.08, 0.25, 473.15), (
    664227388.88, 0.0, 523.15), (664227388.88, 0.25, 523.15)))
mdb.models['Model-1'].materials['VM11013CRSS'].SpecificHeat(table=((
    342.2186813, ), ))


# Assigning the materials
mdb.models['Model-1'].HomogeneousSolidSection(name='FLUIDO', material='FLUIDO', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='L1-I-FOLHELHO', 
    material='L1-I-FOLHELHO', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='L2-I-ARENITO', 
    material='L2-I-ARENITO', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='L3-I-HALITA', 
    material='L3-I-HALITA', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='VM11013CRSS', 
    material='VM11013CRSS', thickness=None)

p = mdb.models['Model-1'].parts['Analise-1']
region = p.sets['FASEI_REV']
p = mdb.models['Model-1'].parts['Analise-1']
p.SectionAssignment(region=region, sectionName='VM11013CRSS', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Analise-1']
region = p.sets['FASEI_FLUIDO']
p = mdb.models['Model-1'].parts['Analise-1']
p.SectionAssignment(region=region, sectionName='FLUIDO', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Analise-1']
region = p.sets['L1-I']
p = mdb.models['Model-1'].parts['Analise-1']
p.SectionAssignment(region=region, sectionName='L1-I-FOLHELHO', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Analise-1']
region = p.sets['L2-I']
p = mdb.models['Model-1'].parts['Analise-1']
p.SectionAssignment(region=region, sectionName='L2-I-ARENITO', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Analise-1']
region = p.sets['L3-I']
p = mdb.models['Model-1'].parts['Analise-1']
p.SectionAssignment(region=region, sectionName='L3-I-HALITA', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Analise-1']

# Creation of the instance

a = mdb.models['Model-1'].rootAssembly
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), 
    point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
p = mdb.models['Model-1'].parts['Analise-1']
a.Instance(name='Analise-1-1', part=p, dependent=ON)


# Creation of steps and application of boundary conditions
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['FASEI_WELL_CIMENTO_BASE']
mdb.models['Model-1'].XsymmBC(name='FIX_FASEI_WELL', createStepName='Initial', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['FASEI_REV']
mdb.models['Model-1'].PinnedBC(name='PIN_FASEI', createStepName='Initial', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['ROCK_BC']
mdb.models['Model-1'].XsymmBC(name='XSYM_ROCK_BC', createStepName='Initial', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['YSYM_BASE']
mdb.models['Model-1'].YsymmBC(name='YSYM_BASE', createStepName='Initial', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['YSYM_TOP']
mdb.models['Model-1'].YsymmBC(name='YSYM_TOP', createStepName='Initial', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['FASEI_REV']
mdb.models['Model-1'].GeostaticStress(name='S_FASEI_REV', region=region, 
    stressMag1=133997000.0, vCoord1=-2000.0, stressMag2=-21981800.0, 
    vCoord2=-4000.0, lateralCoeff1=0.0, lateralCoeff2=0.0)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L1-I']
mdb.models['Model-1'].GeostaticStress(name='S_L1-I', region=region, 
    stressMag1=-31412800.0, vCoord1=-2500.0, stressMag2=-40566400.0, 
    vCoord2=-2900.0, lateralCoeff1=1.0, lateralCoeff2=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L2-I']
mdb.models['Model-1'].GeostaticStress(name='S_L2-I', region=region, 
    stressMag1=-40566400.0, vCoord1=-2900.0, stressMag2=-45805200.0, 
    vCoord2=-3200.0, lateralCoeff1=1.0, lateralCoeff2=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L3-I']
mdb.models['Model-1'].GeostaticStress(name='S_L3-I', region=region, 
    stressMag1=-45805200.0, vCoord1=-3200.0, stressMag2=-51044000.0, 
    vCoord2=-3500.0, lateralCoeff1=1.0, lateralCoeff2=None)
mdb.models['Model-1'].GeostaticStep(name='Geostatic', previous='Initial', 
    nlgeom=ON)
regionDef=mdb.models['Model-1'].rootAssembly.allInstances['Analise-1-1'].sets['FASEI_REV']
mdb.models['Model-1'].FieldOutputRequest(name='FASEI_REV', 
    createStepName='Geostatic', variables=('S', 'MISES', 'E', 'PE', 'U', 
    'NT'), region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].suppress()
del mdb.models['Model-1'].fieldOutputRequests['F-Output-1']
regionDef=mdb.models['Model-1'].rootAssembly.allInstances['Analise-1-1'].sets['ROCK_OUTPUT']
mdb.models['Model-1'].FieldOutputRequest(name='ROCK_OUTPUT', 
    createStepName='Geostatic', variables=('U', 'TEMP'), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].suppress()
del mdb.models['Model-1'].historyOutputRequests['H-Output-1']
a = mdb.models['Model-1'].rootAssembly
region =a.instances['Analise-1-1'].sets['FASEI_FLUIDO']
mdb.models['Model-1'].ModelChange(name='MC_FASEI_FLUIDO', 
    createStepName='Geostatic', region=region, activeInStep=False, 
    includeStrain=False)
a = mdb.models['Model-1'].rootAssembly
region =a.instances['Analise-1-1'].sets['FASEI_REV']
mdb.models['Model-1'].ModelChange(name='MC_FASEI_REV', 
    createStepName='Geostatic', region=region, activeInStep=False, 
    includeStrain=False)
mdb.models['Model-1'].Gravity(name='GRAVITY', createStepName='Geostatic', 
    comp2=-9.81, distributionType=UNIFORM, field='')



mdb.models['Model-1'].StaticStep(name='Transition', previous='Geostatic', 
    timePeriod=2.0, initialInc=1.0, minInc=2e-05, maxInc=2.0)
mdb.models['Model-1'].TimePoint(name='timePoint', points=((1.0, ), (3600.0, ), 
    (7200.0, ), (14400.0, ), (28800.0, ), (57600.0, ), (86400.0, ), (
    172800.0, ), (345600.0, ), (691200.0, ), (1382400.0, ), (2764800.0, ), 
    (5529600.0, ), (11059200.0, ), (22118400.0, ), (31536000.0, ), (
    63072000.0, ), (126144000.0, ), (252288000.0, ), (504576000.0, ), (
    946080000.0, )))
mdb.models['Model-1'].fieldOutputRequests['FASEI_REV'].setValuesInStep(
    stepName='Transition', timePoint='timePoint')
mdb.models['Model-1'].fieldOutputRequests['ROCK_OUTPUT'].setValuesInStep(
    stepName='Transition', timePoint='timePoint')
mdb.models['Model-1'].StaticStep(name='TempDefine', previous='Transition', 
    timePeriod=3.0, initialInc=1.0, minInc=3e-05, maxInc=3.0)


delta_T = 3.2e-4
v1 = 1.06404

# Create dict with keys from -2500 to -3500 with -2.5 intervals
gridPointData1 = {}
for index, depth in enumerate(np.arange(-2500, -3502.5, -2.5)):
    val = v1+(index)*delta_T
    gridPointData1[str(depth)] = (
        (1.79769313486232e+308, 0.0, 100.0),
        (0.0, val, val),
        (100.0, val, val)
    )
mdb.models['Model-1'].MappedField(name='Geotermico', description='', 
    regionType=POINT, partLevelData=False, localCsys=None, 
    pointDataFormat=GRID, fieldDataType=SCALAR, gridPointPlane=PLANE13, 
    gridPointData=gridPointData1)

# mdb.models['Model-1'].MappedField(name='Geotermico', description='', 
#     regionType=POINT, partLevelData=False, localCsys=None, 
#     pointDataFormat=GRID, fieldDataType=SCALAR, gridPointPlane=PLANE13, 
#     gridPointData={'-2500.0':((1.79769313486232e+308, 0.0, 100.0), (0.0, 
#     1.0, 1.0), (100.0, 1.0, 1.0)), '-2502.5':((1.79769313486232e+308, 0.0, 
#     100.0), (0.0, 1.06436, 1.06436), (100.0, 1.06436, 1.06436)), 
#     '-2505.0': ((1.79769313486232e+308, 0.0, 100.0), (0.0, 1.06469, 
#     1.06469), (100.0, 1.06469, 1.06469)), '-3445.0':((
#     1.79769313486232e+308, 0.0, 100.0), (0.0, 1.18509, 1.18509), (100.0, 
#     1.18509, 1.18509)), '-3500.0':((1.79769313486232e+308, 0.0, 100.0), (
#     0.0, 1.19213, 1.19213), (100.0, 1.19213, 1.19213)), '0':((
#     1.79769313486232e+308, 0.0, 100.0), (0.0, 1.0, 1.0), (100.0, 1.0, 
#     1.0))})
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['FASEI']
mdb.models['Model-1'].Temperature(name='NT_FASEI', createStepName='TempDefine', 
    region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
    field='Geotermico', magnitudes=(277.15, ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['FASEI_COMPLETED_WELL']
mdb.models['Model-1'].Temperature(name='NT_FASEI_ID', 
    createStepName='TempDefine', region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
    field='Geotermico', magnitudes=(277.15, ))
mdb.models['Model-1'].ExpressionField(name='NT_L1-I', localCsys=None, 
    description='', 
    expression='(0.035500000000000156*pow(-Y,1))/294.9+(206.1499999999996*pow(-Y,0))/294.9')
mdb.models['Model-1'].ExpressionField(name='NT_L2-I', localCsys=None, 
    description='', 
    expression='(0.035499999999999685*pow(-Y,1))/309.1+(206.15000000000103*pow(-Y,0))/309.1')
mdb.models['Model-1'].ExpressionField(name='NT_L3-I', localCsys=None, 
    description='', 
    expression='(0.03549999999999965*pow(-Y,1))/319.75+(206.1500000000011*pow(-Y,0))/319.75')
mdb.models['Model-1'].ExpressionField(name='P_FASEI_COMPLETED_WELL', 
    localCsys=None, description='', 
    expression='(9991.726615395*pow(-Y,1))/19983453.23079+(2.6341780319308768e-09*pow(-Y,0))/19983453.23079')
mdb.models['Model-1'].ExpressionField(name='P_FASEI_FLUIDO', localCsys=None, 
    description='', 
    expression='(9991.726615395*pow(-Y,1))/19983453.23079+(2.6341780319308768e-09*pow(-Y,0))/19983453.23079')
mdb.models['Model-1'].ExpressionField(name='P_FASEI_OPEN_WELL', localCsys=None, 
    description='', 
    expression='(9991.726615395*pow(-Y,1))/19983453.23079+(2.6341780319308768e-09*pow(-Y,0))/19983453.23079')
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L1-I']
mdb.models['Model-1'].Temperature(name='NT_L1-I', createStepName='TempDefine', 
    region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, field='NT_L1-I', 
    magnitudes=(294.9, ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L1-I_OD']
mdb.models['Model-1'].Temperature(name='NT_L1-I_OD', 
    createStepName='TempDefine', region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, field='NT_L1-I', 
    magnitudes=(294.9, ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L2-I']
mdb.models['Model-1'].Temperature(name='NT_L2-I', createStepName='TempDefine', 
    region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, field='NT_L2-I', 
    magnitudes=(309.1, ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L2-I_OD']
mdb.models['Model-1'].Temperature(name='NT_L2-I_OD', 
    createStepName='TempDefine', region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, field='NT_L2-I', 
    magnitudes=(309.1, ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L3-I']
mdb.models['Model-1'].Temperature(name='NT_L3-I', createStepName='TempDefine', 
    region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, field='NT_L3-I', 
    magnitudes=(319.75, ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].sets['L3-I_OD']
mdb.models['Model-1'].Temperature(name='NT_L3-I_OD', 
    createStepName='TempDefine', region=region, distributionType=FIELD, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, field='NT_L3-I', 
    magnitudes=(319.75, ))



mdb.models['Model-1'].StaticStep(name='Perf_10_375', previous='TempDefine')
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].surfaces['FASEI_OPEN_WELL']
mdb.models['Model-1'].Pressure(name='P_FASEI_OPEN_WELL', 
    createStepName='Perf_10_375', region=region, distributionType=UNIFORM, 
    field='', magnitude=19983500.0, amplitude=UNSET)
mdb.models['Model-1'].loads['P_FASEI_OPEN_WELL'].setValues(
        distributionType=FIELD, field='P_FASEI_OPEN_WELL')
mdb.models['Model-1'].boundaryConditions['FIX_FASEI_WELL'].deactivate(
    'Perf_10_375')
mdb.models['Model-1'].ViscoStep(name='Perf_10_375_Creep', 
    previous='Perf_10_375', timePeriod=172800.0, maxNumInc=1000000, 
    initialInc=1.0, minInc=1e-15, maxInc=172800.0, cetol=0.01)
mdb.models['Model-1'].StaticStep(name='Rev_9_875', 
    previous='Perf_10_375_Creep', minInc=1e-15)
mdb.models['Model-1'].ContactProperty('C_FASEI')
mdb.models['Model-1'].interactionProperties['C_FASEI'].TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
    pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
    table=((0.5, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
    fraction=0.005, elasticSlipStiffness=None)
mdb.models['Model-1'].interactionProperties['C_FASEI'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
a = mdb.models['Model-1'].rootAssembly
region1=a.instances['Analise-1-1'].surfaces['FASEI_MASTER']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Analise-1-1'].sets['FASEI_SLAVE']
# mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='C_FASEI', 
#     createStepName='Rev_9_875', master=region1, slave=region2, 
#     sliding=FINITE, thickness=ON, interactionProperty='C_FASEI', 
#     adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
#     clearanceRegion=None)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='C_FASEI', 
    createStepName='Rev_9_875', main=region1, secondary=region2, 
    sliding=FINITE, thickness=ON, interactionProperty='C_FASEI', 
    adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
    clearanceRegion=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].surfaces['FASEI_COMPLETED_WELL']
mdb.models['Model-1'].Pressure(name='P_FASEI_COMPLETED_WELL', 
    createStepName='Rev_9_875', region=region, distributionType=FIELD, 
    field='P_FASEI_COMPL' \
    'ETED_WELL', magnitude=19983500.0, amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Analise-1-1'].surfaces['FASEI_FLUIDO']
mdb.models['Model-1'].Pressure(name='P_FASEI_FLUIDO', 
    createStepName='Rev_9_875', region=region, distributionType=FIELD, 
    field='P_FASEI_FLUIDO', magnitude=19983500.0, amplitude=UNSET)
mdb.models['Model-1'].loads['P_FASEI_OPEN_WELL'].deactivate('Rev_9_875')
mdb.models['Model-1'].interactions['MC_FASEI_REV'].setValuesInStep(
    stepName='Rev_9_875', activeInStep=True)
mdb.models['Model-1'].boundaryConditions['PIN_FASEI'].deactivate('Rev_9_875')
mdb.models['Model-1'].ViscoStep(name='Rev_9_875_Creep', previous='Rev_9_875', 
    timePeriod=945907000.0, maxNumInc=1000000, initialInc=1.0, 
    minInc=1e-15, maxInc=15552000.0, cetol=0.01)

# Mesh seeding

p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, ratio=5.0, number=4, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, ratio=5.0, number=100, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, ratio=5.0, number=80, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, ratio=5.0, number=70, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, ratio=2.0, number=70, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, ratio=5.0, number=70, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, minSize=1.0, maxSize=10.0, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#2c000000 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#40000000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, minSize=1.0, maxSize=5.0, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#20a00 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#80000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, minSize=5.0, maxSize=10.0, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges1 = e.getSequenceFromMask(mask=('[#20a00 ]', ), )
pickedEdges2 = e.getSequenceFromMask(mask=('[#80000 ]', ), )
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
    end2Edges=pickedEdges2, minSize=5.0, maxSize=20.0, constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#a05000 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=5.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#a05000 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=1.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#55 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=1.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#55 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=0.5, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=2.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=5.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=8.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=15.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=20.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=30.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=50.0, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Analise-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1355a5aa ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=30.0, deviationFactor=0.1, 
    constraint=FINER)
elemType1 = mesh.ElemType(elemCode=CAX4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CAX3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#fff ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
elemType1 = mesh.ElemType(elemCode=CAX4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CAX3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['Model-1'].parts['Analise-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#fff ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p = mdb.models['Model-1'].parts['Analise-1']
p.generateMesh()

# session.viewports['Viewport: 1'].enableMultipleColors()
# session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
# cmap = session.viewports['Viewport: 1'].colorMappings['Material']
# cmap.updateOverrides(overrides={'FLUIDO':(True, '#CCCCCC', 'Default', 
#     '#CCCCCC'), 'L1-I-FOLHELHO':(True, '#00FF8C', 'Default', '#00FF8C'), 
#     'L2-I-ARENITO': (True, '#FFFF00', 'Default', '#FFFF00'), 
#     'L3-I-HALITA': (True, '#00CCFF', 'Default', '#00CCFF'), 
#     'VM11013CRSS': (True, '#800000', 'Default', '#800000')})
# session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
# session.viewports['Viewport: 1'].disableMultipleColors()


a = mdb.models['Model-1'].rootAssembly
del a.features['Datum csys-1']

# mdb.Job(name='Analise-1', model='Model-1', description='', type=ANALYSIS, 
#     atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
#     memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
#     explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
#     modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
#     scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=14, 
#     numDomains=14, numGPUs=0)

