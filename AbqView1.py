from abaqus import mdb
from abaqusConstants import *


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

p = mdb.models['MyFirstModel'].parts['ROCK']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1798.41, 
    farPlane=3242.15, width=965.673, height=435.512, cameraPosition=(
    -29.6373, -6206.49, 440.466), cameraTarget=(-29.6373, -3724.5, 
    2.82566))
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1877.79, 
    farPlane=3161.96, width=117.809, height=53.1309, cameraPosition=(
    6.38347, -6243.3, 89.0209), cameraTarget=(6.38347, -3724.56, 1.06613))
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1886.68, 
    farPlane=3153, width=30.1988, height=13.6195, cameraPosition=(1.58207, 
    -6244.8, 13.6803), cameraTarget=(1.58207, -3724.57, 0.485716))
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.31, 
    farPlane=3150.37, width=5.01994, height=2.26396, cameraPosition=(
    0.894763, -6244.84, 2.45092), cameraTarget=(0.894763, -3724.57, 
    -0.186823))
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.71, 
    farPlane=3149.98, width=1.2868, height=0.580338, cameraPosition=(
    0.489007, -6244.84, 0.462298), cameraTarget=(0.489007, -3724.57, 
    -0.0640702))
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
    mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.rotate(xAngle=-0.0001, yAngle=0, 
    zAngle=0, mode=MODEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.73, 
    farPlane=3149.95, width=1.21454, height=0.547749, cameraPosition=(
    0.430032, -6244.84, 0.053531), cameraTarget=(0.430032, -3724.57, 
    -0.0725551))
session.View(name='User-1', nearPlane=1889.7, farPlane=3150, width=1.2145, 
    height=0.54775, projection=PARALLEL, cameraPosition=(0.43003, -6244.8, 
    0.053531), cameraUpVector=(0, 5.0687e-05, 1), cameraTarget=(0.43003, 
    -3724.6, -0.072555), viewOffsetX=0, viewOffsetY=0, autoFit=OFF)