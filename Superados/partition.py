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

import numpy as np

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

pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
# del mdb.models['Model-1'].sketches['__profile__']
