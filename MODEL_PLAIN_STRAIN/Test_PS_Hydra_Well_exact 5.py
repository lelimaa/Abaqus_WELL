from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
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
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(15.0, 0.0), point2=(-15.0, 0.0), 
    direction=COUNTERCLOCKWISE)
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.131763, 0.0), point2=(-0.131763, 
    0.0), direction=COUNTERCLOCKWISE)
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.125412, 0.0), point2=(-0.125412, 
    0.0), direction=COUNTERCLOCKWISE)
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.108445, 0.0), point2=(-0.108445, 
    0.0), direction=CLOCKWISE)
s.undo()
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.108445, 0.0), point2=(-0.108445, 
    0.0), direction=COUNTERCLOCKWISE)
s.undo()
s.undo()
s.undo()
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.131763, 0.0), point2=(-0.131763, 
    0.0), direction=CLOCKWISE)
s.undo()
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.131763, 0.0), point2=(-0.131763, 
    0.0), direction=COUNTERCLOCKWISE)
s.Line(point1=(0.131763, 0.0), point2=(15.0, 0.0))
s.HorizontalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(-0.131763, 0.0), point2=(-15.0, 0.0))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts.changeKey(fromName='Part-1', toName='ROCK')
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.131763, 0.0), point2=(
    -0.131763, 0.0), direction=COUNTERCLOCKWISE)
s1.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.125412, 0.0), point2=(
    -0.125412, 0.0), direction=COUNTERCLOCKWISE)
s1.Line(point1=(0.125412, 0.0), point2=(0.131763, 0.0))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(-0.125412, 0.0), point2=(-0.131763, 0.0))
s1.HorizontalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts.changeKey(fromName='Part-2', toName='FLUID')
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.125412, 0.0), point2=(-0.125412, 
    0.0), direction=COUNTERCLOCKWISE)
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.108445, 0.0), point2=(-0.108445, 
    0.0), direction=COUNTERCLOCKWISE)
s.Line(point1=(0.108445, 0.0), point2=(0.125412, 0.0))
s.HorizontalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(-0.108445, 0.0), point2=(-0.125412, 0.0))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
p = mdb.models['Model-1'].Part(name='PIPE', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['PIPE']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['PIPE']
p.ReferencePoint(point=(0.0, 0.0, 0.0))
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['ROCK']
p.ReferencePoint(point=(0.0, 0.0, 0.0))
p = mdb.models['Model-1'].parts['FLUID']
p = mdb.models['Model-1'].parts['FLUID']
p.ReferencePoint(point=(0.0, 0.0, 0.0))
session.viewports['Viewport: 1'].setValues(displayedObject=p)

# REFERENCE POINT nas partes
mdb.models['Model-1'].parts['FLUID'].features.changeKey(fromName='RP', 
    toName='REFPTF')
p1 = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].parts['PIPE'].features.changeKey(fromName='RP', 
    toName='REFPTP')
p1 = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].parts['ROCK'].features.changeKey(fromName='RP', 
    toName='REFPTR')

p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['FLUID']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(0.0, 
    0.081878, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.58, gridSpacing=0.01, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['FLUID']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(0.0, -0.081878), point2=(0.0, 0.07))
s1.VerticalConstraint(entity=g[6], addUndoState=False)
p = mdb.models['Model-1'].parts['FLUID']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
f1, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    0.0, 0.07457, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.56, 
    gridSpacing=0.01, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['PIPE']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.Line(point1=(0.0, -0.07457), point2=(0.0, 0.07))
s.VerticalConstraint(entity=g[6], addUndoState=False)
p = mdb.models['Model-1'].parts['PIPE']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['ROCK']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(0.0, 
    6.366685, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=67.02, gridSpacing=1.67, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['ROCK']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(0.0, -6.366685), point2=(0.0, 11.69))
s1.VerticalConstraint(entity=g[6], addUndoState=False)
p = mdb.models['Model-1'].parts['ROCK']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']


# p = mdb.models['Model-1'].parts['FLUID']
# f = p.faces
# faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# p.Set(faces=faces, name='FASEI_ANNULAR')
# p = mdb.models['Model-1'].parts['FLUID']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Set(edges=edges, name='FASEI_ANNULAR_ID')
# p = mdb.models['Model-1'].parts['FLUID']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
# p.Set(edges=edges, name='FASEI_ANNULAR_OD')
# # p = mdb.models['Model-1'].parts['FLUID']
# # e = p.edges
# # edges = e.getSequenceFromMask(mask=('[#5 ]', ), )
# # p.Set(edges=edges, name='FASEI_ANNULAR_TT')
# p = mdb.models['Model-1'].parts['FLUID']
# f = p.faces
# faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# p.Set(faces=faces, name='FASEI_FLUIDO')
# p = mdb.models['Model-1'].parts['FLUID']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Set(edges=edges, name='FASEI_FLUIDO_ID')
# p = mdb.models['Model-1'].parts['FLUID']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
# p.Set(edges=edges, name='FASEI_FLUIDO_OD')
# p = mdb.models['Model-1'].parts['FLUID']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#a ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_ANNULAR')
# p = mdb.models['Model-1'].parts['FLUID']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#a ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_FLUIDO')
# # p = mdb.models['Model-1'].parts['FLUID']
# # s = p.edges
# # side1Edges = s.getSequenceFromMask(mask=('[#8 ]', ), )
# # p.Surface(side1Edges=side1Edges, name='FASEI_MASTER')


# p = mdb.models['Model-1'].parts['PIPE']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p = mdb.models['Model-1'].parts['PIPE']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Set(edges=edges, name='FASEI_COMPLETED_WELL')
# p = mdb.models['Model-1'].parts['PIPE']
# f = p.faces
# faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# p.Set(faces=faces, name='FASEI_REV')
# p = mdb.models['Model-1'].parts['PIPE']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Set(edges=edges, name='FASEI_REV_ID')
# p = mdb.models['Model-1'].parts['PIPE']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
# p.Set(edges=edges, name='FASEI_REV_OD')
# # p = mdb.models['Model-1'].parts['PIPE']
# # e = p.edges
# # edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
# # p.Set(edges=edges, name='FASEI_REV_TT')

# p = mdb.models['Model-1'].parts['PIPE']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Set(edges=edges, name='PROD_ANNULAR')
# p = mdb.models['Model-1'].parts['PIPE']
# r = p.referencePoints
# refPoints=(r[2], )
# p.Set(referencePoints=refPoints, name='REFPTP')
# p = mdb.models['Model-1'].parts['PIPE']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_COMPLETED_WELL')
# p = mdb.models['Model-1'].parts['PIPE']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#2 ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_MASTER')
# p = mdb.models['Model-1'].parts['PIPE']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_REV_ID')
# p = mdb.models['Model-1'].parts['PIPE']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#2 ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_REV_OD')
# p = mdb.models['Model-1'].parts['PIPE']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Surface(side1Edges=side1Edges, name='PROD_ANNULAR')

# p1 = mdb.models['Model-1'].parts['ROCK']
# session.viewports['Viewport: 1'].setValues(displayedObject=p1)
# p = mdb.models['Model-1'].parts['ROCK']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Set(edges=edges, name='FASEI_OPEN_WELL')
# p = mdb.models['Model-1'].parts['ROCK']
# f = p.faces
# faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# p.Set(faces=faces, name='FASEI_SLAVE')
# p = mdb.models['Model-1'].parts['ROCK']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Set(edges=edges, name='FASEI_WELL')
# session.viewports['Viewport: 1'].view.setValues(width=1.01208, height=0.378658, 
#     viewOffsetX=0.0548229, viewOffsetY=-7.40001)
# p = mdb.models['Model-1'].parts['ROCK']
# f = p.faces
# faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# p.Set(faces=faces, name='L1-I')
# # p = mdb.models['Model-1'].parts['ROCK']
# # e = p.edges
# # edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
# # p.Set(edges=edges, name='L1-I_TT')
# p = mdb.models['Model-1'].parts['ROCK']
# r = p.referencePoints
# refPoints=(r[2], )
# p.Set(referencePoints=refPoints, name='REFPTR')
# p = mdb.models['Model-1'].parts['ROCK']
# f = p.faces
# faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# p.Set(faces=faces, name='ROCK_OUTPUT')
# p = mdb.models['Model-1'].parts['ROCK']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_OPEN_WELL')
# p = mdb.models['Model-1'].parts['ROCK']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#8 ]', ), )
# p.Surface(side1Edges=side1Edges, name='FASEI_WELL')
# p = mdb.models['Model-1'].parts['ROCK']
# s = p.edges
# side1Edges = s.getSequenceFromMask(mask=('[#2 ]', ), )
# p.Surface(side1Edges=side1Edges, name='ROCK_BC')

# ############################################################################################

# # p = mdb.models['Model-1'].parts['FLUID']
# # session.viewports['Viewport: 1'].setValues(displayedObject=p)
# # p = mdb.models['Model-1'].parts['FLUID']
# # f, e, d1 = p.faces, p.edges, p.datums
# # t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(0.0, 
# #     0.081878, 0.0))
# # s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
# #     sheetSize=0.58, gridSpacing=0.01, transform=t)
# # g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
# # s1.setPrimaryObject(option=SUPERIMPOSE)
# # p = mdb.models['Model-1'].parts['FLUID']
# # p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
# # s1.Line(point1=(0.0, -0.081878), point2=(0.0, 0.07))
# # s1.VerticalConstraint(entity=g[6], addUndoState=False)
# # p = mdb.models['Model-1'].parts['FLUID']
# # f = p.faces
# # pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# # e1, d2 = p.edges, p.datums
# # p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
# # s1.unsetPrimaryObject()
# # del mdb.models['Model-1'].sketches['__profile__']
# # p = mdb.models['Model-1'].parts['PIPE']
# # session.viewports['Viewport: 1'].setValues(displayedObject=p)
# # p = mdb.models['Model-1'].parts['PIPE']
# # f1, e, d1 = p.faces, p.edges, p.datums
# # t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
# #     0.0, 0.07457, 0.0))
# # s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.56, 
# #     gridSpacing=0.01, transform=t)
# # g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
# # s.setPrimaryObject(option=SUPERIMPOSE)
# # p = mdb.models['Model-1'].parts['PIPE']
# # p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# # s.Line(point1=(0.0, -0.07457), point2=(0.0, 0.07))
# # s.VerticalConstraint(entity=g[6], addUndoState=False)
# # p = mdb.models['Model-1'].parts['PIPE']
# # f = p.faces
# # pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# # e1, d2 = p.edges, p.datums
# # p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
# # s.unsetPrimaryObject()
# # del mdb.models['Model-1'].sketches['__profile__']
# # p = mdb.models['Model-1'].parts['ROCK']
# # session.viewports['Viewport: 1'].setValues(displayedObject=p)
# # p = mdb.models['Model-1'].parts['ROCK']
# # f, e, d1 = p.faces, p.edges, p.datums
# # t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(0.0, 
# #     6.366685, 0.0))
# # s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
# #     sheetSize=67.02, gridSpacing=1.67, transform=t)
# # g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
# # s1.setPrimaryObject(option=SUPERIMPOSE)
# # p = mdb.models['Model-1'].parts['ROCK']
# # p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
# # s1.Line(point1=(0.0, -6.366685), point2=(0.0, 11.69))
# # s1.VerticalConstraint(entity=g[6], addUndoState=False)
# # p = mdb.models['Model-1'].parts['ROCK']
# # f = p.faces
# # pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
# # e1, d2 = p.edges, p.datums
# # p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
# # s1.unsetPrimaryObject()
# # del mdb.models['Model-1'].sketches['__profile__']

# ####################################################################################

# p1 = mdb.models['Model-1'].parts['FLUID']
# session.viewports['Viewport: 1'].setValues(displayedObject=p1)
# p = mdb.models['Model-1'].parts['FLUID']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#25 ]', ), )
# p.Set(edges=edges, name='FASEI_ANNULAR_TT')
# p = mdb.models['Model-1'].parts['PIPE']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p1 = mdb.models['Model-1'].parts['PIPE']
# session.viewports['Viewport: 1'].setValues(displayedObject=p1)
# p = mdb.models['Model-1'].parts['PIPE']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#25 ]', ), )
# p.Set(edges=edges, name='FASEI_REV_TT')
# p = mdb.models['Model-1'].parts['FLUID']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p = mdb.models['Model-1'].parts['PIPE']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p = mdb.models['Model-1'].parts['ROCK']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p1 = mdb.models['Model-1'].parts['ROCK']
# session.viewports['Viewport: 1'].setValues(displayedObject=p1)
# p = mdb.models['Model-1'].parts['ROCK']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#25 ]', ), )
# p.Set(edges=edges, name='L1-I_TT')
# session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
#     engineeringFeatures=ON)
# session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
#     referenceRepresentation=OFF)


### Alternative way to define sets and surfaces #######

p = mdb.models['Model-1'].parts['FLUID']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.Set(faces=faces, name='FASEI_ANNULAR')
p = mdb.models['Model-1'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#42 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_ID')
p = mdb.models['Model-1'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#18 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_OD')
p = mdb.models['Model-1'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#25 ]', ), )
p.Set(edges=edges, name='FASEI_ANNULAR_TT')
p = mdb.models['Model-1'].parts['FLUID']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.Set(faces=faces, name='FASEI_FLUIDO')
p = mdb.models['Model-1'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#42 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_ID')
p = mdb.models['Model-1'].parts['FLUID']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#18 ]', ), )
p.Set(edges=edges, name='FASEI_FLUIDO_OD')
p = mdb.models['Model-1'].parts['FLUID']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#5a ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_FLUIDO')
p = mdb.models['Model-1'].parts['FLUID']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#5a ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_ANNULAR')
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#42 ]', ), )
p.Set(edges=edges, name='FASEI_COMPLETED_WELL')
p = mdb.models['Model-1'].parts['PIPE']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.Set(faces=faces, name='FASEI_REV')
p = mdb.models['Model-1'].parts['PIPE']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#42 ]', ), )
p.Set(edges=edges, name='FASEI_REV_ID')
p = mdb.models['Model-1'].parts['PIPE']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#18 ]', ), )
p.Set(edges=edges, name='FASEI_REV_OD')
p = mdb.models['Model-1'].parts['PIPE']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#25 ]', ), )
p.Set(edges=edges, name='FASEI_REV_TT')
p = mdb.models['Model-1'].parts['PIPE']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#42 ]', ), )
p.Set(edges=edges, name='PROD_ANNULAR')
p = mdb.models['Model-1'].parts['PIPE']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#42 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_COMPLETED_WELL')
p = mdb.models['Model-1'].parts['PIPE']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#18 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_MASTER')
p = mdb.models['Model-1'].parts['PIPE']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#42 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_REV_ID')
p = mdb.models['Model-1'].parts['PIPE']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#18 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_REV_OD')
p = mdb.models['Model-1'].parts['PIPE']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#42 ]', ), )
p.Surface(side1Edges=side1Edges, name='PROD_ANNULAR')
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.7365, 
    farPlane=67.4276, width=2.83827, height=1.27344, viewOffsetX=0.10612, 
    viewOffsetY=-7.0123)
p = mdb.models['Model-1'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#42 ]', ), )
p.Set(edges=edges, name='FASEI_OPEN_WELL')
p = mdb.models['Model-1'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.Set(faces=faces, name='FASEI_SLAVE')
p = mdb.models['Model-1'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#42 ]', ), )
p.Set(edges=edges, name='FASEI_WELL')
p = mdb.models['Model-1'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.Set(faces=faces, name='L1-I')
p = mdb.models['Model-1'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#25 ]', ), )
p.Set(edges=edges, name='L1-I_TT')
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.4357, 
    farPlane=73.7284, width=60.9878, height=27.3632, viewOffsetX=5.31324, 
    viewOffsetY=-1.92099)
p = mdb.models['Model-1'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.Set(faces=faces, name='ROCK_OUTPUT')
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.8686, 
    farPlane=67.2955, width=1.75273, height=0.786391, viewOffsetX=0.12019, 
    viewOffsetY=-7.23314)
p1 = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['ROCK']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#18 ]', ), )
p.Set(edges=edges, name='ROCK_BC')
p = mdb.models['Model-1'].parts['ROCK']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#42 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_OPEN_WELL')
p = mdb.models['Model-1'].parts['ROCK']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#42 ]', ), )
p.Surface(side1Edges=side1Edges, name='FASEI_WELL')
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.0289, 
    farPlane=72.1352, width=46.5293, height=20.8761, viewOffsetX=-0.13581, 
    viewOffsetY=0.0261269)
p = mdb.models['Model-1'].parts['ROCK']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#18 ]', ), )
p.Surface(side1Edges=side1Edges, name='ROCK_BC')

# # # Definition of the materials ########################################################

mdb.models['Model-1'].Material(name='FLUIDO')
mdb.models['Model-1'].materials['FLUIDO'].Conductivity(table=((0.702, ), ))
mdb.models['Model-1'].materials['FLUIDO'].Density(table=((1.0, ), ))
mdb.models['Model-1'].materials['FLUIDO'].Elastic(table=((1000.0, 0.0), ))
mdb.models['Model-1'].materials['FLUIDO'].SpecificHeat(table=((2060.0, ), ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.9255, 
    farPlane=70.2386, width=31.8524, height=11.9173, viewOffsetX=2.96229, 
    viewOffsetY=-5.87972)
mdb.models['Model-1'].Material(name='Material-2')
mdb.models['Model-1'].materials['Material-2'].Conductivity(table=((5.55, ), ))
mdb.models['Model-1'].materials['Material-2'].Density(table=((2170.23, ), ))
mdb.models['Model-1'].materials['Material-2'].Elastic(table=((20400009045.2, 
    0.36), ))
mdb.models['Model-1'].materials['Material-2'].SpecificHeat(table=((0.209946, ), 
    ))
mdb.models['Model-1'].materials.changeKey(fromName='Material-2', 
    toName='L1-I-HALITA')
# mdb.models['Model-1'].materials['L1-I-HALITA'].Creep(temperatureDependency=ON, 
#     table=((1.01924e-41, 3.0, 0.7, 9.5), ))  # works on Abaqus 2020
mdb.models['Model-1'].materials['L1-I-HALITA'].Creep(law=DOUBLE_POWER,
    table=((0.0077864000,6042.9046228220,2.9400000000,0.0076093000,6042.9046228220,8.1500000000,10300006.1216400005), ))  # works on Abaqus 2024
mdb.models['Model-1'].Material(name='STEEL')
mdb.models['Model-1'].materials['STEEL'].Conductivity(table=((45.3452, ), ))
mdb.models['Model-1'].materials['STEEL'].Density(table=((7950.0, ), ))
mdb.models['Model-1'].materials['STEEL'].Elastic(table=((206842800000.0, 0.3), 
    ))
mdb.models['Model-1'].materials['STEEL'].SpecificHeat(table=((342.2186813, 
    ), ))
mdb.models['Model-1'].materials['STEEL'].Plastic(temperatureDependency=ON, 
    scaleStress=None, table=((758423600.0, 0.0, 273.15), (758423600.0, 
    0.25, 273.15), (756375856.28, 0.0, 298.15), (756375856.28, 0.25, 
    298.15), (725659700.48, 0.0, 373.15), (725659700.48, 0.25, 373.15), (
    705182263.28, 0.0, 423.15), (705182263.28, 0.25, 423.15), (
    684704826.08, 0.0, 473.15), (684704826.08, 0.25, 473.15), (
    664227388.88, 0.0, 523.15), (664227388.88, 0.25, 523.15)))

# # Associating the materials to the parts #######################################################

p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].HomogeneousSolidSection(name='FLUID', material='FLUIDO', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='L1-I-HALITA', 
    material='L1-I-HALITA', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='STEEL', material='STEEL', 
    thickness=None)
p = mdb.models['Model-1'].parts['FLUID']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['FLUID']
p.SectionAssignment(region=region, sectionName='FLUID', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['PIPE']
p.SectionAssignment(region=region, sectionName='STEEL', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['ROCK']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['ROCK']
p.SectionAssignment(region=region, sectionName='L1-I-HALITA', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)


a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.998, 
    farPlane=67.166, width=0.753377, height=0.281869, viewOffsetX=-0.02943, 
    viewOffsetY=-7.38179)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['FLUID']
a.Instance(name='FLUID-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['PIPE']
a.Instance(name='PIPE-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['ROCK']
a.Instance(name='ROCK-1', part=p, dependent=OFF)
a = mdb.models['Model-1'].rootAssembly


# a = mdb.models['Model-1'].rootAssembly
# r1 = a.instances['ROCK-1'].referencePoints
# refPoints1=(r1[2], )
# a.Set(referencePoints=refPoints1, name='REFPT')
# a = mdb.models['Model-1'].rootAssembly
# region = a.sets['REFPT']


# a = mdb.models['Model-1'].rootAssembly
# a.ReferencePoint(point=(0.0, 0.0, 0.0))
# session.viewports['Viewport: 1'].view.setValues(nearPlane=10.1736, 
#     farPlane=10.2632, width=0.368264, height=0.165228, 
#     viewOffsetX=0.0152376, viewOffsetY=-0.0299753)
# a = mdb.models['Model-1'].rootAssembly
# r1 = a.referencePoints
# refPoints1=(r1[11], )
# a.Set(referencePoints=refPoints1, name='REFPT')

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 0.0))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[8], )
a.Set(referencePoints=refPoints1, name='REFPT')




# a.regenerate()

# session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
#     engineeringFeatures=OFF)
# session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
#     referenceRepresentation=ON)
# p1 = mdb.models['Model-1'].parts['FLUID']
# session.viewports['Viewport: 1'].setValues(displayedObject=p1)
# p = mdb.models['Model-1'].parts['FLUID']
# s = p.features['Shell planar-1'].sketch
# mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
# s2 = mdb.models['Model-1'].sketches['__edit__']
# g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
# s2.setPrimaryObject(option=SUPERIMPOSE)
# p.projectReferencesOntoSketch(sketch=s2, 
#     upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)

# s2.unsetPrimaryObject()
# del mdb.models['Model-1'].sketches['__edit__']
# p = mdb.models['Model-1'].parts['PIPE']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p = mdb.models['Model-1'].parts['ROCK']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# a = mdb.models['Model-1'].rootAssembly
# session.viewports['Viewport: 1'].setValues(displayedObject=a)

# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()
# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()

# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()

# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()

# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()

# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()


# # Creating sets for the contact surfaces ####################################################

# a = mdb.models['Model-1'].rootAssembly
# # f1 = a.instances['FLUID-1'].faces
# # faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# # f2 = a.instances['PIPE-1'].faces
# # faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
# # r2 = a.instances['PIPE-1'].referencePoints
# # refPoints2=(r2[2], )
# # f3 = a.instances['ROCK-1'].faces
# # faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
# # r3 = a.instances['ROCK-1'].referencePoints
# # refPoints3=(r3[2], )
# # a.Set(faces=faces1+faces2+faces3, referencePoints=(refPoints2, refPoints3, ), 
# #     name='ALL')

# f1 = a.instances['FLUID-1'].faces
# faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# f2 = a.instances['PIPE-1'].faces
# faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
# f3 = a.instances['ROCK-1'].faces
# faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
# a.Set(faces=faces1+faces2+faces3, name='ALL')

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=10.1125, 
    farPlane=10.3244, width=0.870483, height=0.390556, cameraPosition=(0, 
    0.0658815, 10.2184), viewOffsetX=-0.0984172, viewOffsetY=-0.061495)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['FLUID-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
f2 = a.instances['PIPE-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
f3 = a.instances['ROCK-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
a.Set(faces=faces1+faces2+faces3, name='ALL')

# session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9423, 
#     farPlane=67.2218, width=1.52328, height=0.530515, 
#     viewOffsetX=0.00450476, viewOffsetY=-7.40223)
# a = mdb.models['Model-1'].rootAssembly
# f1 = a.instances['PIPE-1'].faces
# faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# f2 = a.instances['FLUID-1'].faces
# faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
# a.Set(faces=faces1+faces2, name='FASEI')

a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['FLUID-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
f2 = a.instances['PIPE-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
a.Set(faces=faces1+faces2, name='FASEI')

# a = mdb.models['Model-1'].rootAssembly
# s1 = a.instances['FLUID-1'].edges
# side1Edges1 = s1.getSequenceFromMask(mask=('[#18 ]', ), )
# s2 = a.instances['PIPE-1'].edges
# side1Edges2 = s2.getSequenceFromMask(mask=('[#18 ]', ), )
# a.Surface(side1Edges=side1Edges1+side1Edges2, name='FASEI_FLUIDO_ALT')

a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['PIPE-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#18 ]', ), )
s2 = a.instances['ROCK-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#42 ]', ), )
a.Surface(side1Edges=side1Edges1+side1Edges2, name='FASEI_FLUIDO_ALT')

# p = mdb.models['Model-1'].parts['ROCK']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p = mdb.models['Model-1'].parts['PIPE']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# p = mdb.models['Model-1'].parts['FLUID']
# session.viewports['Viewport: 1'].setValues(displayedObject=p)
# a = mdb.models['Model-1'].rootAssembly
# session.viewports['Viewport: 1'].setValues(displayedObject=a)

# a = mdb.models['Model-1'].rootAssembly
# e1 = a.instances['ROCK-1'].edges
# edges1 = e1.getSequenceFromMask(mask=('[#24 ]', ), )
# e2 = a.instances['FLUID-1'].edges
# edges2 = e2.getSequenceFromMask(mask=('[#24 ]', ), )
# e3 = a.instances['PIPE-1'].edges
# edges3 = e3.getSequenceFromMask(mask=('[#24 ]', ), )
# a.Set(edges=edges1+edges2+edges3, name='YSYM')


a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#24 ]', ), )
e2 = a.instances['FLUID-1'].edges
edges2 = e2.getSequenceFromMask(mask=('[#24 ]', ), )
e3 = a.instances['PIPE-1'].edges
edges3 = e3.getSequenceFromMask(mask=('[#24 ]', ), )
a.Set(edges=edges1+edges2+edges3, name='YSYM')

# a = mdb.models['Model-1'].rootAssembly
# v1 = a.instances['PIPE-1'].vertices
# verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
# a.Set(vertices=verts1, name='FASEI_SPRING')

# a = mdb.models['Model-1'].rootAssembly
# v1 = a.instances['PIPE-1'].vertices
# verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
# a.Set(vertices=verts1, name='FASEI_SPRING2')




# mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='FASEI_SPRING', 
#     toName='FASEI_SPRING1')


a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['PIPE-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Set(vertices=verts1, name='FASEI_SPRING1')
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['PIPE-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(vertices=verts1, name='FASEI_SPRING2')


# p1 = mdb.models['Model-1'].parts['FLUID']
# session.viewports['Viewport: 1'].setValues(displayedObject=p1)
# del mdb.models['Model-1'].parts['FLUID'].surfaces['FASEI_MASTER']

# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()
# session.viewports['Viewport: 1'].setValues(displayedObject=a)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
#     constraints=ON, connectors=ON, engineeringFeatures=ON)

# a = mdb.models['Model-1'].rootAssembly
# rgn1pair0=a.instances['PIPE-1'].sets['REFPTP']
# a = mdb.models['Model-1'].rootAssembly
# rgn2pair0=a.sets['FASEI_SPRING1']
# a = mdb.models['Model-1'].rootAssembly
# rgn1pair1=a.instances['PIPE-1'].sets['REFPTP']
# a = mdb.models['Model-1'].rootAssembly
# rgn2pair1=a.sets['FASEI_SPRING2']
# region=((rgn1pair0, rgn2pair0), (rgn1pair1, rgn2pair1), )
# mdb.models['Model-1'].rootAssembly.engineeringFeatures.TwoPointSpringDashpot(
#     name='Springs/Dashpots-1', regionPairs=region, axis=FIXED_DOF, dof1=1, 
#     dof2=1, orientation=None, springBehavior=ON, springStiffness=100.0, 
#     dashpotBehavior=OFF, dashpotCoefficient=0.0)

session.viewports['Viewport: 1'].view.setValues(nearPlane=10.1232, 
    farPlane=10.3137, width=0.885682, height=0.397376, 
    viewOffsetX=0.0844006, viewOffsetY=0.0874774)
a = mdb.models['Model-1'].rootAssembly
rgn1pair0=a.sets['REFPT']
a = mdb.models['Model-1'].rootAssembly
rgn2pair0=a.sets['FASEI_SPRING1']
a = mdb.models['Model-1'].rootAssembly
rgn1pair1=a.sets['REFPT']
a = mdb.models['Model-1'].rootAssembly
rgn2pair1=a.sets['FASEI_SPRING2']
region=((rgn1pair0, rgn2pair0), (rgn1pair1, rgn2pair1), )
mdb.models['Model-1'].rootAssembly.engineeringFeatures.TwoPointSpringDashpot(
    name='SPRINGS_FASEI-SPRING', regionPairs=region, axis=FIXED_DOF, 
    dof1=1, dof2=1, orientation=None, springBehavior=ON, 
    springStiffness=100.0, dashpotBehavior=OFF, dashpotCoefficient=0.0)



# session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
#     predefinedFields=ON, interactions=OFF, constraints=OFF, 
#     engineeringFeatures=OFF)
# a = mdb.models['Model-1'].rootAssembly
# region = a.instances['ROCK-1'].sets['FASEI_WELL']
# p = mdb.models['Model-1'].parts['ROCK']
# e = p.edges
# edges = e.getSequenceFromMask(mask=('[#18 ]', ), )
# p.Set(edges=edges, name='ROCK_BC')
# a = mdb.models['Model-1'].rootAssembly
# a.regenerate()

######## COMENTEI OS TIMEPOINT - para podermos saber o momento exato em que a rocha encostou no Casing

# mdb.models['Model-1'].TimePoint(name='timePoint', points=((1.0, ), (3600.0, ), 
#     (7200.0, ), (14400.0, ), (28800.0, ), (57600.0, ), (86400.0, ), (
#     172800.0, ), (345600.0, ), (691200.0, ), (1382400.0, ), (2764800.0, ), 
#     (5529600.0, ), (11059200.0, ), (22118400.0, ), (31536000.0, ), (
#     63072000.0, ), (126144000.0, ), (252288000.0, ), (504576000.0, ), (
#     946080000.0, )))

mdb.models['Model-1'].ContactProperty('C_FASEI')
mdb.models['Model-1'].interactionProperties['C_FASEI'].TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
    pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
    table=((0.5, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
    fraction=0.005, elasticSlipStiffness=None)
mdb.models['Model-1'].interactionProperties['C_FASEI'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)

# # Starting of the creation of the steps ##########################################################

a = mdb.models['Model-1'].rootAssembly
region = a.instances['ROCK-1'].sets['FASEI_WELL']
mdb.models['Model-1'].EncastreBC(name='FIX_FASEI_WELL', createStepName='Initial', 
    region=region, localCsys=None)

# mdb.models['Model-1'].EncastreBC(name='FASEI_WELL', 
#     createStepName='Initial', region=region, localCsys=None)


p1 = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.0747, 
    farPlane=71.0894, width=43.5371, height=15.1627, viewOffsetX=4.96453, 
    viewOffsetY=-4.63494)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['ROCK-1'].sets['ROCK_BC']
mdb.models['Model-1'].EncastreBC(name='FIX_ROCK_BC', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9117, 
    farPlane=67.2524, width=1.64129, height=0.571613, viewOffsetX=0.103147, 
    viewOffsetY=-7.3242)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['PIPE-1'].sets['FASEI_REV']
mdb.models['Model-1'].PinnedBC(name='PIN_FASEI', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9068, 
    farPlane=67.2573, width=1.68874, height=0.588141, 
    viewOffsetX=0.0358649, viewOffsetY=-7.35252)

a = mdb.models['Model-1'].rootAssembly
region = a.sets['REFPT']
mdb.models['Model-1'].EncastreBC(name='REFPT', createStepName='Initial', 
    region=region, localCsys=None)

# a = mdb.models['Model-1'].rootAssembly
# region = a.instances['PIPE-1'].sets['REFPTP']
# mdb.models['Model-1'].EncastreBC(name='REFPT_FIX', createStepName='Initial', 
#     region=region, localCsys=None)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9374, 
#     farPlane=67.2266, width=1.57605, height=0.548892, viewOffsetX=0.162342, 
#     viewOffsetY=-7.34754)


a = mdb.models['Model-1'].rootAssembly
region = a.sets['YSYM']
mdb.models['Model-1'].YsymmBC(name='YSYM', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9587, 
    farPlane=67.2053, width=1.34417, height=0.468138, viewOffsetX=0.120014, 
    viewOffsetY=-7.34794)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['PIPE-1'].sets['FASEI_REV']
mdb.models['Model-1'].Stress(name='S_FASEI_REV', region=region, 
    distributionType=UNIFORM, sigma11=0.0, sigma22=0.0, 
    sigma33=-16570100.0, sigma12=0.0, sigma13=None, sigma23=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['ROCK-1'].sets['L1-I']
mdb.models['Model-1'].Stress(name='S_L1-I', region=region, 
    distributionType=UNIFORM, sigma11=-54536500.0, sigma22=-54536500.0, 
    sigma33=-54536500.0, sigma12=0.0, sigma13=None, sigma23=None)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0268, 
#     farPlane=67.1372, width=0.531882, height=0.185239, 
#     viewOffsetX=-0.0258772, viewOffsetY=-7.42378)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
#     predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].GeostaticStep(name='Geostatic', previous='Initial', 
    nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Geostatic')


############################################################################################

regionDef=mdb.models['Model-1'].rootAssembly.allInstances['PIPE-1'].sets['FASEI_REV']
mdb.models['Model-1'].FieldOutputRequest(name='FASEI_REV', 
    createStepName='Geostatic', variables=('S', 'MISES', 'E', 'PE', 'U', 
    'NT'), region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
regionDef=mdb.models['Model-1'].rootAssembly.allInstances['ROCK-1'].sets['ROCK_OUTPUT']
mdb.models['Model-1'].FieldOutputRequest(name='ROCK_OUTPUT', 
    createStepName='Geostatic', variables=('U', 'TEMP'), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
del mdb.models['Model-1'].fieldOutputRequests['F-Output-1']
del mdb.models['Model-1'].historyOutputRequests['H-Output-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
region =a.instances['FLUID-1'].sets['FASEI_FLUIDO']
mdb.models['Model-1'].ModelChange(name='MC_FASEI_FLUIDO', 
    createStepName='Geostatic', region=region, activeInStep=False, 
    includeStrain=False)
a = mdb.models['Model-1'].rootAssembly
region =a.instances['PIPE-1'].sets['FASEI_REV']
mdb.models['Model-1'].ModelChange(name='MC_FASEI_REV', 
    createStepName='Geostatic', region=region, activeInStep=False, 
    includeStrain=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9546, 
    farPlane=67.2095, width=1.04692, height=0.46972, viewOffsetX=0.0893608, 
    viewOffsetY=-7.32034)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Transition', previous='Geostatic', 
    timePeriod=2.0, initialInc=1.0, minInc=2e-05, maxInc=2.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Transition')
mdb.models['Model-1'].fieldOutputRequests['FASEI_REV'].setValuesInStep(
    stepName='Transition', timePoint='timePoint')
mdb.models['Model-1'].fieldOutputRequests['ROCK_OUTPUT'].setValuesInStep(
    stepName='Transition', timePoint='timePoint')
mdb.models['Model-1'].StaticStep(name='TempDefine', previous='Transition', 
    timePeriod=3.0, initialInc=1.0, minInc=3e-05, maxInc=3.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='TempDefine')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['FASEI']
mdb.models['Model-1'].Temperature(name='NT_FASEI', createStepName='TempDefine', 
    region=region, distributionType=UNIFORM, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
    ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['PIPE-1'].sets['FASEI_COMPLETED_WELL']
mdb.models['Model-1'].Temperature(name='NT_FASEI_ID', 
    createStepName='TempDefine', region=region, distributionType=UNIFORM, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
    ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['ROCK-1'].sets['L1-I']
mdb.models['Model-1'].Temperature(name='NT_L1-I', createStepName='TempDefine', 
    region=region, distributionType=UNIFORM, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
    ))
a = mdb.models['Model-1'].rootAssembly
region = a.instances['ROCK-1'].sets['ROCK_BC']
mdb.models['Model-1'].Temperature(name='NT_ROCK_BC', 
    createStepName='TempDefine', region=region, distributionType=UNIFORM, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
    ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Perf_10_375', previous='TempDefine', 
    minInc=1e-15)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Perf_10_375')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['ROCK-1'].surfaces['FASEI_OPEN_WELL']
mdb.models['Model-1'].Pressure(name='P_FASEI_OPEN_WELL', 
    createStepName='Perf_10_375', region=region, distributionType=UNIFORM, 
    field='', magnitude=36969400.0, amplitude=UNSET)
mdb.models['Model-1'].boundaryConditions['FIX_FASEI_WELL'].deactivate(
    'Perf_10_375')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].ViscoStep(name='Perf_10_375_Creep', 
    previous='Perf_10_375', timePeriod=172800.0, maxNumInc=1000000, 
    initialInc=1.0, minInc=1e-15, maxInc=172800.0, cetol=0.01)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Perf_10_375_Creep')
mdb.models['Model-1'].StaticStep(name='Rev_9_875', 
    previous='Perf_10_375_Creep', minInc=1e-15)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Rev_9_875')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
region1=a.instances['PIPE-1'].surfaces['FASEI_MASTER']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['ROCK-1'].sets['FASEI_SLAVE']
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='C_FASEI', 
    createStepName='Rev_9_875', main=region1, secondary=region2, 
    sliding=FINITE, thickness=ON, interactionProperty='C_FASEI', 
    adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
    clearanceRegion=None)
mdb.models['Model-1'].interactions['MC_FASEI_REV'].setValuesInStep(
    stepName='Rev_9_875', activeInStep=True)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['PIPE-1'].surfaces['FASEI_COMPLETED_WELL']
mdb.models['Model-1'].Pressure(name='P_FASEI_COMPLETED_WELL', 
    createStepName='Rev_9_875', region=region, distributionType=UNIFORM, 
    field='', magnitude=36969400.0, amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
region = a.surfaces['FASEI_FLUIDO_ALT']
# region = a.instances['FLUID-1'].surfaces['FASEI_FLUIDO']
mdb.models['Model-1'].Pressure(name='P_FASEI_FLUIDO', 
    createStepName='Rev_9_875', region=region, distributionType=UNIFORM, 
    field='', magnitude=36969400.0, amplitude=UNSET)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0722, 
#     farPlane=67.0919, width=0.0806275, height=0.0361748, 
#     viewOffsetX=-0.0871388, viewOffsetY=-7.40481)
# mdb.models['Model-1'].loads['P_FASEI_FLUIDO'].setValues(magnitude=36969400.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0382, 
    farPlane=67.1259, width=0.407362, height=0.18277, viewOffsetX=0.022939, 
    viewOffsetY=-7.40691)
# a = mdb.models['Model-1'].rootAssembly
# s1 = a.instances['FLUID-1'].edges
# side1Edges1 = s1.getSequenceFromMask(mask=('[#18 ]', ), )
# s2 = a.instances['PIPE-1'].edges
# side1Edges2 = s2.getSequenceFromMask(mask=('[#18 ]', ), )
# a.Surface(side1Edges=side1Edges1+side1Edges2, name='FASEI_FLUIDO_ALT')
# a = mdb.models['Model-1'].rootAssembly
# region = a.surfaces['FASEI_FLUIDO_ALT']
# mdb.models['Model-1'].loads['P_FASEI_FLUIDO'].setValues(region=region, 
#     magnitude=36969400.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0472, 
    farPlane=67.1169, width=0.324098, height=0.145412, 
    viewOffsetX=0.0199922, viewOffsetY=-7.3944)
# a = mdb.models['Model-1'].rootAssembly
# s1 = a.instances['PIPE-1'].edges
# side1Edges1 = s1.getSequenceFromMask(mask=('[#18 ]', ), )
# s2 = a.instances['ROCK-1'].edges
# side1Edges2 = s2.getSequenceFromMask(mask=('[#42 ]', ), )
# a.Surface(side1Edges=side1Edges1+side1Edges2, name='FASEI_FLUIDO_ALT')
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0766, 
    farPlane=67.0875, width=0.0447671, height=0.0200855, 
    viewOffsetX=-0.0760309, viewOffsetY=-7.40799)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0019, 
    farPlane=67.1622, width=0.74442, height=0.333996, 
    viewOffsetX=0.0473046, viewOffsetY=-7.36244)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.011, 
    farPlane=67.1531, width=0.583661, height=0.261869, 
    viewOffsetX=0.0523948, viewOffsetY=-7.39282)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    nodeLabels=ON)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['PIPE'].setValues(geometryRefinement=FINE)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['FLUID'].setValues(geometryRefinement=FINE)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9464, 
    farPlane=67.2177, width=1.11424, height=0.499924, 
    viewOffsetX=0.0057551, viewOffsetY=-7.26826)
mdb.models['Model-1'].parts['ROCK'].setValues(geometryRefinement=FINE)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['ROCK'].setValues(geometryRefinement=COARSE)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['ROCK'].setValues(geometryRefinement=FINE)
p = mdb.models['Model-1'].parts['PIPE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['FLUID'].setValues(geometryRefinement=COARSE)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0235, 
    farPlane=67.1406, width=0.54425, height=0.244187, viewOffsetX=0.14104, 
    viewOffsetY=-7.44055)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['FLUID'].setValues(geometryRefinement=EXTRA_COARSE)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.026, 
    farPlane=67.138, width=0.459771, height=0.206284, viewOffsetX=0.051862, 
    viewOffsetY=-7.43058)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9972, 
    farPlane=67.1669, width=0.788129, height=0.353607, 
    viewOffsetX=0.162968, viewOffsetY=-7.41113)
mdb.models['Model-1'].loads['P_FASEI_OPEN_WELL'].deactivate('Rev_9_875')
mdb.models['Model-1'].boundaryConditions['PIN_FASEI'].deactivate('Rev_9_875')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Geostatic')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].ViscoStep(name='Rev_9_875_Creep', previous='Rev_9_875', 
    timePeriod=945907000.0, maxNumInc=1000000, initialInc=1.0, 
    minInc=1e-15, maxInc=15552000.0, cetol=0.01)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Rev_9_875_Creep')


############################################################################################




# regionDef=mdb.models['Model-1'].rootAssembly.allInstances['PIPE-1'].sets['FASEI_REV']
# mdb.models['Model-1'].FieldOutputRequest(name='FASEI_REV', 
#     createStepName='Geostatic', variables=('S', 'MISES', 'E', 'PE', 'U', 
#     'NT'), region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
# regionDef=mdb.models['Model-1'].rootAssembly.allInstances['ROCK-1'].sets['ROCK_OUTPUT']
# mdb.models['Model-1'].FieldOutputRequest(name='ROCK_OUTPUT', 
#     createStepName='Geostatic', variables=('U', 'TEMP'), region=regionDef, 
#     sectionPoints=DEFAULT, rebar=EXCLUDE)
# del mdb.models['Model-1'].fieldOutputRequests['F-Output-1']
# del mdb.models['Model-1'].historyOutputRequests['H-Output-1']
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
#     constraints=ON, connectors=ON, engineeringFeatures=ON, 
#     adaptiveMeshConstraints=OFF)
# a = mdb.models['Model-1'].rootAssembly
# region =a.instances['FLUID-1'].sets['FASEI_FLUIDO']
# mdb.models['Model-1'].ModelChange(name='MC_FASEI_FLUIDO', 
#     createStepName='Geostatic', region=region, activeInStep=False, 
#     includeStrain=False)
# a = mdb.models['Model-1'].rootAssembly
# region =a.instances['PIPE-1'].sets['FASEI_REV']
# mdb.models['Model-1'].ModelChange(name='MC_FASEI_REV', 
#     createStepName='Geostatic', region=region, activeInStep=False, 
#     includeStrain=False)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
#     constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
#     adaptiveMeshConstraints=ON)
# mdb.models['Model-1'].StaticStep(name='Step-2', previous='Geostatic', 
#     timePeriod=2.0, initialInc=1.0, minInc=2e-05, maxInc=2.0)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
# mdb.models['Model-1'].steps.changeKey(fromName='Step-2', toName='Transition')

# # mdb.models['Model-1'].fieldOutputRequests['FASEI_REV'].setValuesInStep(
# #     stepName='Transition', timePoint='timePoint')
# # mdb.models['Model-1'].fieldOutputRequests['ROCK_OUTPUT'].setValuesInStep(
# #     stepName='Transition', timePoint='timePoint')
# # mdb.models['Model-1'].StaticStep(name='TempDefine', previous='Transition', 
# #     timePeriod=3.0, initialInc=1.0, minInc=3e-05, maxInc=3.0)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='TempDefine')
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
# #     predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
# # a = mdb.models['Model-1'].rootAssembly
# # region = a.sets['FASEI']
# # mdb.models['Model-1'].Temperature(name='NT_FASEI', createStepName='TempDefine', 
# #     region=region, distributionType=UNIFORM, 
# #     crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
# #     ))
# # a = mdb.models['Model-1'].rootAssembly
# # region = a.instances['PIPE-1'].sets['FASEI_COMPLETED_WELL']
# # mdb.models['Model-1'].Temperature(name='NT_FASEI_ID', 
# #     createStepName='TempDefine', region=region, distributionType=UNIFORM, 
# #     crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
# #     ))
# # a = mdb.models['Model-1'].rootAssembly
# # region = a.instances['ROCK-1'].sets['L1-I']
# # mdb.models['Model-1'].Temperature(name='NT_L1-I', createStepName='TempDefine', 
# #     region=region, distributionType=UNIFORM, 
# #     crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
# #     ))
# # a = mdb.models['Model-1'].rootAssembly
# # region = a.instances['ROCK-1'].sets['ROCK_BC']
# # mdb.models['Model-1'].Temperature(name='NT_ROCK_BC', 
# #     createStepName='TempDefine', region=region, distributionType=UNIFORM, 
# #     crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(337.5, 
# #     ))
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
# #     predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
# # mdb.models['Model-1'].StaticStep(name='Perf_10_375', previous='TempDefine')
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Perf_10_375')
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
# #     predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
# # a = mdb.models['Model-1'].rootAssembly
# # region = a.instances['ROCK-1'].surfaces['FASEI_OPEN_WELL']
# # mdb.models['Model-1'].Pressure(name='P_FASEI_OPEN_WELL', 
# #     createStepName='Perf_10_375', region=region, distributionType=UNIFORM, 
# #     field='', magnitude=36969400.0, amplitude=UNSET)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
# #     predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
# # mdb.models['Model-1'].ViscoStep(name='Perf_10_375_Creep', 
# #     previous='Perf_10_375', timePeriod=172800.0, maxNumInc=1000000, 
# #     initialInc=1.0, minInc=1e-15, maxInc=172800.0, cetol=0.01)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(
# #     step='Perf_10_375_Creep')
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
# #     predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
# # mdb.models['Model-1'].boundaryConditions['FIX_FASEI_WELL'].deactivate(
# #     'Perf_10_375_Creep')
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
# #     predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
# # mdb.models['Model-1'].StaticStep(name='Rev_9_875', 
# #     previous='Perf_10_375_Creep', minInc=1e-15)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Rev_9_875')
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
# #     constraints=ON, connectors=ON, engineeringFeatures=ON, 
# #     adaptiveMeshConstraints=OFF)
# # session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
# #     engineeringFeatures=ON)
# # session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
# #     referenceRepresentation=OFF)
# # p = mdb.models['Model-1'].parts['ROCK']
# # session.viewports['Viewport: 1'].setValues(displayedObject=p)
# # session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
# #     engineeringFeatures=OFF)
# # session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
# #     referenceRepresentation=ON)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=66.4549, 
# #     farPlane=67.7092, width=6.83054, height=2.37888, viewOffsetX=-0.34863, 
# #     viewOffsetY=-7.11833)
# # a = mdb.models['Model-1'].rootAssembly
# # session.viewports['Viewport: 1'].setValues(displayedObject=a)

# # a = mdb.models['Model-1'].rootAssembly
# # region1=a.instances['PIPE-1'].surfaces['FASEI_MASTER']
# # a = mdb.models['Model-1'].rootAssembly
# # region2=a.instances['ROCK-1'].sets['FASEI_SLAVE']
# # mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='C_FASEI', 
# #     createStepName='Rev_9_875', main=region1, secondary=region2, 
# #     sliding=FINITE, thickness=ON, interactionProperty='C_FASEI', 
# #     adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
# #     clearanceRegion=None)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
# #     predefinedFields=ON, interactions=OFF, constraints=OFF, 
# #     engineeringFeatures=OFF)
# # a = mdb.models['Model-1'].rootAssembly
# # region = a.instances['PIPE-1'].surfaces['FASEI_COMPLETED_WELL']
# # mdb.models['Model-1'].Pressure(name='P_FASEI_COMPLETED_WELL', 
# #     createStepName='Rev_9_875', region=region, distributionType=UNIFORM, 
# #     field='', magnitude=36969400.0, amplitude=UNSET)
# # a = mdb.models['Model-1'].rootAssembly
# # region = a.instances['FLUID-1'].surfaces['FASEI_FLUIDO']
# # mdb.models['Model-1'].Pressure(name='P_FASEI_FLUIDO', 
# #     createStepName='Rev_9_875', region=region, distributionType=UNIFORM, 
# #     field='', magnitude=36969400.0, amplitude=UNSET)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
# #     predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
# # mdb.models['Model-1'].ViscoStep(name='Rev_9_875_Creep', previous='Rev_9_875', 
# #     timePeriod=945907000.0, maxNumInc=1000000, initialInc=1.0, 
# #     minInc=1e-15, maxInc=15552000.0, cetol=0.01)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(
# #     step='Rev_9_875_Creep')
# # mdb.models['Model-1'].boundaryConditions['PIN_FASEI'].deactivate(
# #     'Rev_9_875_Creep')
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
# #     predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
# #     predefinedFields=OFF, connectors=OFF)

# # ### SO FAR THE BOUNDARY CONDITIONS WERE CREATED #######################################

# CREATION OF MESH ######################################################################

session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2162, 
    farPlane=73.9479, width=63.0121, height=28.2714, viewOffsetX=-2.81838, 
    viewOffsetY=-0.627983)
mdb.models['Model-1'].setValues(absoluteZero=0, stefanBoltzmann=5.670374e-8)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0538, 
    farPlane=67.1103, width=0.231348, height=0.104078, 
    viewOffsetX=0.147395, viewOffsetY=-7.51936)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['FLUID-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['PIPE-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9981, 
    farPlane=67.166, width=0.777919, height=0.349968, viewOffsetX=0.138166, 
    viewOffsetY=-7.49593)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['PIPE-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['PIPE-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['FLUID-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['FLUID-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.3119, 
    farPlane=71.8521, width=44.0167, height=19.8021, viewOffsetX=-1.30822, 
    viewOffsetY=-0.948479)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7315, 
    farPlane=72.4326, width=49.3482, height=22.2006, viewOffsetX=-1.53232, 
    viewOffsetY=1.34662)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
    number=50, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.975, 
    farPlane=67.189, width=0.876352, height=0.394251, 
    viewOffsetX=0.0468343, viewOffsetY=-7.35592)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['FLUID'].setValues(geometryRefinement=FINE)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.8126, 
    farPlane=67.3515, width=2.66703, height=1.19984, viewOffsetX=0.396591, 
    viewOffsetY=-7.20051)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
f2 = a.instances['FLUID-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
f3 = a.instances['PIPE-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions = faces1+faces2+faces3
a.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0167, 
    farPlane=67.1474, width=0.535399, height=0.240864, 
    viewOffsetX=0.0329022, viewOffsetY=-7.36317)
elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
f2 = a.instances['FLUID-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
f3 = a.instances['PIPE-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =((faces1+faces2+faces3), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9826, 
    farPlane=67.1815, width=0.814616, height=0.366478, 
    viewOffsetX=0.0730661, viewOffsetY=-7.42382)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
    a.instances['PIPE-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9399, 
    farPlane=67.2242, width=1.31687, height=0.592431, viewOffsetX=0.146894, 
    viewOffsetY=-7.36686)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)

# mdb.Job(name='WellClosureJob', model='Model-1', description='', type=ANALYSIS, 
#     atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
#     memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
#     explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
#     modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
#     scratch='', resultsFormat=ODB)
# mdb.jobs['WellClosureJob'].submit(consistencyChecking=OFF)

session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.3236, 
    farPlane=73.8405, width=62.2496, height=28.0047, viewOffsetX=8.87877, 
    viewOffsetY=0.795325)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
a.deleteMesh(regions=pickedRegions)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
    number=25, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0258, 
    farPlane=67.1383, width=0.46052, height=0.207178, 
    viewOffsetX=0.0476179, viewOffsetY=-7.3527)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
    a.instances['PIPE-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.472, 
    farPlane=72.6921, width=51.7272, height=23.2709, viewOffsetX=13.6218, 
    viewOffsetY=-5.35468)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
a.deleteMesh(regions=pickedRegions)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
    number=15, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0415, 
    farPlane=67.1226, width=0.331893, height=0.149311, 
    viewOffsetX=0.0441403, viewOffsetY=-7.37747)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
    a.instances['PIPE-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.9215, 
    farPlane=72.2425, width=47.6211, height=21.4237, viewOffsetX=8.88429, 
    viewOffsetY=-0.214458)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
a.deleteMesh(regions=pickedRegions)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
    number=12, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.994, 
    farPlane=67.1701, width=0.720802, height=0.324273, 
    viewOffsetX=0.180791, viewOffsetY=-7.34833)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
    a.instances['PIPE-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
# mdb.jobs['WellClosureJob'].submit(consistencyChecking=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
a.deleteMesh(regions=pickedRegions)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=100.0, 
    number=10, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0346, 
    farPlane=67.1295, width=0.38847, height=0.174764, 
    viewOffsetX=0.0930145, viewOffsetY=-7.35942)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
    a.instances['PIPE-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.7598, 
    farPlane=74.4043, width=67.4671, height=30.3519, viewOffsetX=10.6945, 
    viewOffsetY=0.169439)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
a.deleteMesh(regions=pickedRegions)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=100.0, 
    number=8, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0033, 
    farPlane=67.1608, width=0.645095, height=0.290214, 
    viewOffsetX=0.131527, viewOffsetY=-7.43003)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
    a.instances['PIPE-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.5295, 
    farPlane=73.6346, width=60.4059, height=27.1752, viewOffsetX=11.2663, 
    viewOffsetY=-2.12963)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)

#########################################################################################

session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2162, 
    farPlane=73.9479, width=63.0121, height=28.2714, viewOffsetX=-2.81838, 
    viewOffsetY=-0.627983)
mdb.models['Model-1'].setValues(absoluteZero=0, stefanBoltzmann=5.670374e-8)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0538, 
    farPlane=67.1103, width=0.231348, height=0.104078, 
    viewOffsetX=0.147395, viewOffsetY=-7.51936)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['FLUID-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['PIPE-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9981, 
    farPlane=67.166, width=0.777919, height=0.349968, viewOffsetX=0.138166, 
    viewOffsetY=-7.49593)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['PIPE-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['PIPE-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['FLUID-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['FLUID-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.3119, 
    farPlane=71.8521, width=44.0167, height=19.8021, viewOffsetX=-1.30822, 
    viewOffsetY=-0.948479)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7315, 
    farPlane=72.4326, width=49.3482, height=22.2006, viewOffsetX=-1.53232, 
    viewOffsetY=1.34662)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['ROCK-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
    number=50, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.975, 
    farPlane=67.189, width=0.876352, height=0.394251, 
    viewOffsetX=0.0468343, viewOffsetY=-7.35592)
p = mdb.models['Model-1'].parts['FLUID']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['FLUID'].setValues(geometryRefinement=FINE)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.8126, 
    farPlane=67.3515, width=2.66703, height=1.19984, viewOffsetX=0.396591, 
    viewOffsetY=-7.20051)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
f2 = a.instances['FLUID-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
f3 = a.instances['PIPE-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions = faces1+faces2+faces3
a.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0167, 
    farPlane=67.1474, width=0.535399, height=0.240864, 
    viewOffsetX=0.0329022, viewOffsetY=-7.36317)
elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ROCK-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
f2 = a.instances['FLUID-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
f3 = a.instances['PIPE-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =((faces1+faces2+faces3), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9826, 
    farPlane=67.1815, width=0.814616, height=0.366478, 
    viewOffsetX=0.0730661, viewOffsetY=-7.42382)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
    a.instances['PIPE-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9399, 
    farPlane=67.2242, width=1.31687, height=0.592431, viewOffsetX=0.146894, 
    viewOffsetY=-7.36686)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)


# mdb.Job(name='WellClosureJob', model='Model-1', description='', type=ANALYSIS, 
#     atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
#     memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
#     explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
#     modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
#     scratch='', resultsFormat=ODB)


# mdb.jobs['WellClosureJob'].submit(consistencyChecking=OFF)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
# session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
#     meshTechnique=ON)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=60.3236, 
#     farPlane=73.8405, width=62.2496, height=28.0047, viewOffsetX=8.87877, 
#     viewOffsetY=0.795325)
# a = mdb.models['Model-1'].rootAssembly
# f1 = a.instances['ROCK-1'].faces
# pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# a.deleteMesh(regions=pickedRegions)
# a = mdb.models['Model-1'].rootAssembly
# e1 = a.instances['ROCK-1'].edges
# pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
#     number=25, constraint=FINER)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0258, 
#     farPlane=67.1383, width=0.46052, height=0.207178, 
#     viewOffsetX=0.0476179, viewOffsetY=-7.3527)
# a = mdb.models['Model-1'].rootAssembly
# partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
#     a.instances['PIPE-1'], )
# a.generateMesh(regions=partInstances)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=61.472, 
#     farPlane=72.6921, width=51.7272, height=23.2709, viewOffsetX=13.6218, 
#     viewOffsetY=-5.35468)
# a = mdb.models['Model-1'].rootAssembly
# f1 = a.instances['ROCK-1'].faces
# pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# a.deleteMesh(regions=pickedRegions)
# a = mdb.models['Model-1'].rootAssembly
# e1 = a.instances['ROCK-1'].edges
# pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
#     number=15, constraint=FINER)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0415, 
#     farPlane=67.1226, width=0.331893, height=0.149311, 
#     viewOffsetX=0.0441403, viewOffsetY=-7.37747)
# a = mdb.models['Model-1'].rootAssembly
# partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
#     a.instances['PIPE-1'], )
# a.generateMesh(regions=partInstances)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=61.9215, 
#     farPlane=72.2425, width=47.6211, height=21.4237, viewOffsetX=8.88429, 
#     viewOffsetY=-0.214458)
# a = mdb.models['Model-1'].rootAssembly
# f1 = a.instances['ROCK-1'].faces
# pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# a.deleteMesh(regions=pickedRegions)
# a = mdb.models['Model-1'].rootAssembly
# e1 = a.instances['ROCK-1'].edges
# pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
#     number=12, constraint=FINER)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=66.994, 
#     farPlane=67.1701, width=0.720802, height=0.324273, 
#     viewOffsetX=0.180791, viewOffsetY=-7.34833)
# a = mdb.models['Model-1'].rootAssembly
# partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
#     a.instances['PIPE-1'], )
# a.generateMesh(regions=partInstances)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
# session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
#     meshTechnique=OFF)
# mdb.jobs['WellClosureJob'].submit(consistencyChecking=OFF)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
# session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
#     meshTechnique=ON)
# a = mdb.models['Model-1'].rootAssembly
# f1 = a.instances['ROCK-1'].faces
# pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# a.deleteMesh(regions=pickedRegions)
# a = mdb.models['Model-1'].rootAssembly
# e1 = a.instances['ROCK-1'].edges
# pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=100.0, 
#     number=10, constraint=FINER)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0346, 
#     farPlane=67.1295, width=0.38847, height=0.174764, 
#     viewOffsetX=0.0930145, viewOffsetY=-7.35942)
# a = mdb.models['Model-1'].rootAssembly
# partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
#     a.instances['PIPE-1'], )
# a.generateMesh(regions=partInstances)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=59.7598, 
#     farPlane=74.4043, width=67.4671, height=30.3519, viewOffsetX=10.6945, 
#     viewOffsetY=0.169439)
# a = mdb.models['Model-1'].rootAssembly
# f1 = a.instances['ROCK-1'].faces
# pickedRegions = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# a.deleteMesh(regions=pickedRegions)
# a = mdb.models['Model-1'].rootAssembly
# e1 = a.instances['ROCK-1'].edges
# pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=100.0, 
#     number=8, constraint=FINER)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0033, 
#     farPlane=67.1608, width=0.645095, height=0.290214, 
#     viewOffsetX=0.131527, viewOffsetY=-7.43003)
# a = mdb.models['Model-1'].rootAssembly
# partInstances =(a.instances['ROCK-1'], a.instances['FLUID-1'], 
#     a.instances['PIPE-1'], )
# a.generateMesh(regions=partInstances)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=60.5295, 
#     farPlane=73.6346, width=60.4059, height=27.1752, viewOffsetX=11.2663, 
#     viewOffsetY=-2.12963)
# session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
# session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
#     meshTechnique=OFF)
# mdb.jobs['WellClosureJob'].submit(consistencyChecking=OFF)
# session.mdbData.summary()
# o3 = session.openOdb(
#     name='C:/Users/juani/Documents/PUC/GTEP/Codes/PS/WellClosureJob.odb')
# session.viewports['Viewport: 1'].setValues(displayedObject=o3)
# session.viewports['Viewport: 1'].makeCurrent()
# session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
#     CONTOURS_ON_DEF, ))
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=20 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=21 )
# session.viewports['Viewport: 1'].view.setValues(nearPlane=78.0259, 
#     farPlane=111.711, width=0.590738, height=0.265045, 
#     viewOffsetX=0.052967, viewOffsetY=-6.07567)
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=20 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=19 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=18 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=17 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=16 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=15 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=14 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=13 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=12 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=11 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=10 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=9 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=8 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=7 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=6 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=5 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=4 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=3 )
# session.viewports['Viewport: 1'].odbDisplay.setFrame(step=6, frame=2 )
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Perf_10_375_Creep', frame=0)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Geostatic', frame=0)
# session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
#     variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
#     'Magnitude'), )
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=21)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=21)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=78.0042, 
#     farPlane=111.732, width=0.870161, height=0.390412, 
#     viewOffsetX=0.155927, viewOffsetY=-6.08309)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=21)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=21)
# session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
#     DEFORMED, ))
# session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
#     CONTOURS_ON_DEF, ))
# session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
#     deformationScaling=UNIFORM, uniformScaleFactor=100)
# session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
#     uniformScaleFactor=5)
# session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
#     uniformScaleFactor=10)
# session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
#     uniformScaleFactor=50)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=0)
# session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
#     uniformScaleFactor=10)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=7)
# session.viewports['Viewport: 1'].view.setValues(nearPlane=78.0532, 
#     farPlane=111.683, width=0.366153, height=0.164281, 
#     viewOffsetX=0.00168578, viewOffsetY=-6.13777)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=21)
# session.viewports[session.currentViewportName].odbDisplay.setFrame(
#     step='Rev_9_875_Creep', frame=21)


#########################################################################################


# # # mdb.Job(name='WellClosureJob', model='Model-1', description='', type=ANALYSIS, 
# # #     atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
# # #     memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
# # #     explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
# # #     modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
# # #     scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
# # #     multiprocessingMode=DEFAULT, numCpus=14, numDomains=14, numGPUs=0)

# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['PIPE-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0372, 
# #     farPlane=67.1269, width=0.430851, height=0.150438, 
# #     viewOffsetX=0.0894232, viewOffsetY=-7.47302)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['FLUID-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0281, 
# #     farPlane=67.136, width=0.586987, height=0.204956, 
# #     viewOffsetX=0.0871319, viewOffsetY=-7.45282)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['PIPE-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeBySize(edges=pickedEdges, size=0.017, deviationFactor=0.1, 
# #     constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['PIPE-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeBySize(edges=pickedEdges, size=0.008, deviationFactor=0.1, 
# #     constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['PIPE-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeBySize(edges=pickedEdges, size=0.007, deviationFactor=0.1, 
# #     constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['FLUID-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeBySize(edges=pickedEdges, size=0.007, deviationFactor=0.1, 
# #     constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeBySize(edges=pickedEdges, size=0.007, deviationFactor=0.1, 
# #     constraint=FINER)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=62.5125, 
# #     farPlane=71.6516, width=49.2761, height=17.2055, viewOffsetX=8.87955, 
# #     viewOffsetY=-3.24425)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
# # a.seedEdgeBySize(edges=pickedEdges, size=0.007, deviationFactor=0.1, 
# #     constraint=FINER)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0205, 
# #     farPlane=67.1435, width=0.590946, height=0.206338, 
# #     viewOffsetX=-0.107768, viewOffsetY=-7.42764)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['PIPE-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['PIPE-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['FLUID-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['FLUID-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#42 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges = e1.getSequenceFromMask(mask=('[#18 ]', ), )
# # a.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FINER)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=63.1461, 
# #     farPlane=71.018, width=42.6547, height=14.8936, viewOffsetX=-0.204498, 
# #     viewOffsetY=-3.15782)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=5.0, 
# #     number=50, constraint=FINER)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=61.8136, 
# #     farPlane=72.3504, width=57.0261, height=19.9116, viewOffsetX=-1.02849, 
# #     viewOffsetY=-1.64703)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=1.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=10.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=20.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=30.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=40.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=50.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=60.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=100.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # e1 = a.instances['ROCK-1'].edges
# # pickedEdges1 = e1.getSequenceFromMask(mask=('[#25 ]', ), )
# # a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=200.0, 
# #     number=50, constraint=FINER)
# # a = mdb.models['Model-1'].rootAssembly
# # f1 = a.instances['FLUID-1'].faces
# # faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# # f2 = a.instances['PIPE-1'].faces
# # faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
# # f3 = a.instances['ROCK-1'].faces
# # faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
# # pickedRegions = faces1+faces2+faces3
# # a.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0015, 
# #     farPlane=67.1625, width=0.699715, height=0.244316, 
# #     viewOffsetX=0.0945402, viewOffsetY=-7.4472)
# # a = mdb.models['Model-1'].rootAssembly

# # elemType1 = mesh.ElemType(elemCode=CPS4, elemLibrary=STANDARD)
# # elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
# # a = mdb.models['Model-1'].rootAssembly
# # f1 = a.instances['FLUID-1'].faces
# # faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# # f2 = a.instances['PIPE-1'].faces
# # faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
# # f3 = a.instances['ROCK-1'].faces
# # faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
# # pickedRegions =((faces1+faces2+faces3), )
# # a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=59.5332, 
# #     farPlane=74.6309, width=81.5409, height=28.4713, viewOffsetX=2.26988, 
# #     viewOffsetY=-1.24526)
# # p = mdb.models['Model-1'].parts['ROCK']
# # session.viewports['Viewport: 1'].setValues(displayedObject=p)
# # session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
# # session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
# #     meshTechnique=ON)
# # session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
# #     referenceRepresentation=OFF)
# # a = mdb.models['Model-1'].rootAssembly
# # session.viewports['Viewport: 1'].setValues(displayedObject=a)
# # a = mdb.models['Model-1'].rootAssembly
# # partInstances =(a.instances['FLUID-1'], a.instances['PIPE-1'], 
# #     a.instances['ROCK-1'], )
# # a.generateMesh(regions=partInstances)
# # session.viewports['Viewport: 1'].view.setValues(nearPlane=60.4775, 
# #     farPlane=73.6866, width=37.5527, height=21.9331, viewOffsetX=0.697315, 
# #     viewOffsetY=-0.0292723)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
# # session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
# #     meshTechnique=OFF)

# # mdb.Job(name='WellClosureJob2', model='Model-1', description='', type=ANALYSIS, 
# #     atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
# #     memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
# #     explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
# #     modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
# #     scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
# #     multiprocessingMode=DEFAULT, numCpus=14, numDomains=14, numGPUs=0)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
# # session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
# #     meshTechnique=ON)

# # ### AQUI TIVE QUE REDEFINIR O TIPO DE ELEMENTO PARA PLASE STRAIN
# # elemType1 = mesh.ElemType(elemCode=CPE4R, elemLibrary=STANDARD, 
# #     secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
# #     distortionControl=DEFAULT)
# # elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
# # a = mdb.models['Model-1'].rootAssembly
# # f1 = a.instances['FLUID-1'].faces
# # faces1 = f1.getSequenceFromMask(mask=('[#3 ]', ), )
# # f2 = a.instances['PIPE-1'].faces
# # faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
# # f3 = a.instances['ROCK-1'].faces
# # faces3 = f3.getSequenceFromMask(mask=('[#3 ]', ), )
# # pickedRegions =((faces1+faces2+faces3), )
# # a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
# # a = mdb.models['Model-1'].rootAssembly
# # partInstances =(a.instances['FLUID-1'], a.instances['PIPE-1'], 
# #     a.instances['ROCK-1'], )
# # a.generateMesh(regions=partInstances)
# # session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
# # session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
# #     meshTechnique=OFF)
# # mdb.jobs['WellClosureJob2'].submit(consistencyChecking=OFF)
# # session.mdbData.summary()
# # o3 = session.openOdb(
# #     name='C:/Users/hidalgo/Desktop/PlaneStrain/WellClosureJob2.odb')
# # session.viewports['Viewport: 1'].setValues(displayedObject=o3)
# # session.viewports['Viewport: 1'].makeCurrent()
# # session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
# #     CONTOURS_ON_DEF, ))
# # a = mdb.models['Model-1'].rootAssembly
# # session.viewports['Viewport: 1'].setValues(displayedObject=a)
# # a = mdb.models['Model-1'].rootAssembly
# # session.viewports['Viewport: 1'].setValues(displayedObject=a)
# # # o3 = session.openOdb(
# # #     name='C:/Users/hidalgo/Desktop/PlaneStrain/WellClosureJob2.odb')
# # a = mdb.models['Model-1'].rootAssembly
# # # o3 = session.openOdb(
# # #     name='C:/Users/hidalgo/Desktop/PlaneStrain/WellClosureJob2.odb')






