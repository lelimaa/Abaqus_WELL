from abaqus import *
from abaqusConstants import *

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import Superados.assembly as assembly
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


def Assembly(name_model, partsNames, top_depth=3200, base_depth=3600):
    model = mdb.models[name_model]
    a = model.rootAssembly
    depth = base_depth - top_depth
    #   Create a global cylindrical coordinate system
    a.DatumCsysByThreePoints(name='GlobalCSYS', coordSysType=CYLINDRICAL, 
                             origin=(0.0, -top_depth-(depth/2), 0.0),
                             point1=(-1.0, 0.0, 0.0), point2=(0.0, 1.0, 0.0))
    instances = {}

    for name in partsNames:
        if name not in model.parts:
            raise ValueError("Part '%s' not found in model '%s'." % (name, name_model))

        p = model.parts[name]
        instName = name + '_INST'
        a.Instance(name=instName, part=p, dependent=OFF)
        inst = a.instances[instName]
        instances[name] = inst
    
    a.regenerate()
    print("Assembly completed with active sets:", a.sets.keys())