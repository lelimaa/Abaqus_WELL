from abaqus import *
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

# if 'MyFirstModel' not in mdb.models:
#     mdb.Model(name='MyFirstModel')

def Assembly(modelName, partsNames, top_depth, base_depth):
    model = mdb.models[modelName]
    a = model.rootAssembly
    depth = base_depth - top_depth
    #   Create a global cylindrical coordinate system
    a.DatumCsysByThreePoints(name='GlobalCSYS', coordSysType=CYLINDRICAL, 
                             origin=(0.0, -top_depth-(depth/2), 0.0),
                             point1=(-1.0, 0.0, 0.0), point2=(0.0, 1.0, 0.0))
    instances = {}

    for name in partsNames:
        if name not in model.parts:
            raise ValueError("Part '%s' not found in model '%s'." % (name, modelName))

        p = model.parts[name]
        instName = name + '_INST'
        a.Instance(name=instName, part=p, dependent=ON)
        inst = a.instances[instName]
        instances[name] = inst

    if inst.cells:
        a.Set(cells=inst.cells[:], name=inst.name + '_Set')
    elif inst.faces:
        a.Set(faces=inst.faces[:], name=inst.name + '_Set')
    elif inst.edges:
        a.Set(edges=inst.edges[:], name=inst.name + '_Set')
    

    # if 'MyFirstModel' not in mdb.models:
    #     mdb.Model(name='MyFirstModel')
    
    a.regenerate()
    print("Assembly completed with active sets:", a.sets.keys())

