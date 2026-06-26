# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def MacroSections():
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
    p = mdb.models['MyFirstModel'].parts['FLUID']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#f ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['FLUID']
    p.SectionAssignment(region=region, sectionName='FLUID_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p1 = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#f ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    p.SectionAssignment(region=region, sectionName='STEEL_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p1 = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.48, 
        farPlane=3151.08, width=6.55289, height=2.94006, cameraPosition=(
        0.550932, -6245.28, 1.9922), cameraTarget=(0.550932, -3725, 0.410418))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#8 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='SHALE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='SANDSTONE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='SHALE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(faces=faces)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    p.SectionAssignment(region=region, sectionName='HALITE_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def MacroAssembly():
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
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['FLUID']
    a1.Instance(name='FLUID-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['PIPE']
    a1.Instance(name='PIPE-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['ROCK']
    a1.Instance(name='ROCK-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1879.79, 
        farPlane=6245.21, width=2.38268, height=1.07595, cameraPosition=(
        0.620956, -6245, 1.32304), cameraTarget=(0.620956, -3724.8, 
        0.00520486))
    a1 = mdb.models['MyFirstModel'].rootAssembly
    a1.translate(instanceList=('ROCK-1', ), vector=(0.0, -10.0, 0.0))
    a1 = mdb.models['MyFirstModel'].rootAssembly
    a1.translate(instanceList=('ROCK-1', ), vector=(0.0, 10.0, 0.0))
    a = mdb.models['MyFirstModel'].rootAssembly
    a.deleteFeatures(('FLUID-1', 'PIPE-1', 'ROCK-1', ))
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['FLUID']
    a1.Instance(name='FLUID-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['PIPE']
    a1.Instance(name='PIPE-1', part=p, dependent=ON)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    p = mdb.models['MyFirstModel'].parts['ROCK']
    a1.Instance(name='ROCK-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])


def MacroSets():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.87, 
        farPlane=3148.73, width=4.63154, height=2.09147, cameraPosition=(
        1.46594, -6243.3, 2.13651), cameraTarget=(1.46594, -3723.2, 0.0258625))
    p1 = mdb.models['MyFirstModel'].parts['FLUID']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1888.05, 
        farPlane=3148.55, width=2.41492, height=1.09051, cameraPosition=(
        0.676116, -6243.3, 2.12438), cameraTarget=(0.676116, -3723.2, 
        0.0137331))
    p = mdb.models['MyFirstModel'].parts['FLUID']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='FASEI_FLUIDO')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Set(edges=edges, name='FASEI_FLUIDO_BASE')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    p.Set(edges=edges, name='FASEI_FLUIDO_ID')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
    p.Set(edges=edges, name='FASEI_FLUIDO_OD')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    p.Set(edges=edges, name='FASEI_FLUIDO_TOP')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    p.Set(edges=edges, name='FASEI_OPEN_WELL')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='ALLROCK')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.73, 
        farPlane=3148.87, width=5.44236, height=2.45761, cameraPosition=(
        1.39037, -6243.3, 2.104), cameraTarget=(1.39037, -3723.2, -0.00665549))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
    p.Set(edges=edges, name='L1-I_BASE')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#200 ]', ), )
    p.Set(edges=edges, name='L1-I_ID')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1886.63, 
        farPlane=3149.97, width=18.156, height=8.19872, cameraPosition=(
        5.78218, -6243.3, 3.30278), cameraTarget=(5.78218, -3723.2, 1.19213))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#80 ]', ), )
    p.Set(edges=edges, name='L1-I_OD')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    p.Set(edges=edges, name='L1-I_TOP')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Set(faces=faces, name='L1-I')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Set(faces=faces, name='L2-I')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.78, 
        farPlane=3148.82, width=4.95113, height=2.23579, cameraPosition=(
        2.04034, -6243.3, 2.31539), cameraTarget=(2.04034, -3723.2, 0.20474))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(edges=edges, name='L2-I_BASE')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#40 ]', ), )
    p.Set(edges=edges, name='L2-I_ID')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.05, 
        farPlane=3149.55, width=16.752, height=7.56471, cameraPosition=(
        5.99645, -6243.3, 2.50852), cameraTarget=(5.99645, -3723.2, 0.397873))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#10 ]', ), )
    p.Set(edges=edges, name='L2-I_OD')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#20 ]', ), )
    p.Set(edges=edges, name='L2-I_TOP')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(faces=faces, name='L3-I')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Set(edges=edges, name='L3-I_BASE')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Set(edges=edges, name='L3-I_ID')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
    p.Set(edges=edges, name='L3-I_OD')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(edges=edges, name='L3-I_TOP')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a1 = mdb.models['MyFirstModel'].rootAssembly
    a1.regenerate()
    a = mdb.models['MyFirstModel'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1888.04, 
        farPlane=3148.56, width=2.75317, height=1.24326, cameraPosition=(
        1.13212, -6243.3, 2.15284), cameraTarget=(1.13212, -3723.2, 0.0421889))
    p1 = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.18, 
        farPlane=3151.37, width=11.8645, height=5.35768, cameraPosition=(
        2.87561, -6245.28, 1.60123), cameraTarget=(2.87561, -3725, -0.50957))
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1888.01, 
        farPlane=3148.59, width=2.76833, height=1.2501, cameraPosition=(
        0.908102, -6243.3, 2.03867), cameraTarget=(0.908102, -3723.2, 
        -0.071982))
    p = mdb.models['MyFirstModel'].parts['FLUID']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p1 = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p1 = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['MyFirstModel'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['MyFirstModel'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['MyFirstModel'].rootAssembly
    f1 = a.instances['FLUID_INST'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
    f2 = a.instances['PIPE_INST'].faces
    faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
    a.Set(faces=faces1+faces2, name='FASEI')
    p1 = mdb.models['MyFirstModel'].parts['FLUID']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['MyFirstModel'].parts['FLUID']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='FASEI_ANNULAR')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Set(edges=edges, name='FASEI_ANNULAR_BASE')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    p.Set(edges=edges, name='FASEI_ANNULAR_ID')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
    p.Set(edges=edges, name='FASEI_ANNULAR_OD')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    p.Set(edges=edges, name='FASEI_ANNULAR_TOP')
    p = mdb.models['MyFirstModel'].parts['FLUID']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
    p.Set(edges=edges, name='FASEI_ANNULAR_TT')
    a = mdb.models['MyFirstModel'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['PIPE_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#242 ]', ), )
    a.Set(edges=edges1, name='FASEI_COMPLETED_WELL')
    p1 = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    a = mdb.models['MyFirstModel'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1887.21, 
        farPlane=3149.38, width=10.3887, height=4.69123, cameraPosition=(
        3.47742, -6243.3, 2.61765), cameraTarget=(3.47742, -3723.2, 0.506997))
    a = mdb.models['MyFirstModel'].rootAssembly
    f1 = a.instances['FLUID_INST'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
    f2 = a.instances['PIPE_INST'].faces
    faces2 = f2.getSequenceFromMask(mask=('[#7 ]', ), )
    f3 = a.instances['ROCK_INST'].faces
    faces3 = f3.getSequenceFromMask(mask=('[#7 ]', ), )
    r3 = a.instances['ROCK_INST'].referencePoints
    refPoints3=(r3[2], )
    a.Set(faces=faces1+faces2+faces3, referencePoints=refPoints3, name='ALL')
    cliCommand("""face_obj = p.sets['ALL']""")
    cliCommand("""p =mdb.models['MyFirstModel']""")
    cliCommand("""face_obj = p.sets['ALL']""")
    cliCommand("""a = mdb.models['MyFirstModel'].rootAssembly""")
    cliCommand("""set_all = a.sets['ALL']""")
    cliCommand("""print(set_all.faces)""")


def MacroAssembly2():
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
    p1 = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
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
    p = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
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
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1829.51, 
        farPlane=3211.04, width=938.469, height=300.447, cameraPosition=(
        -7.26975, -6206.36, 441.208), cameraTarget=(-7.26975, -3724.37, 
        3.56785))
    session.viewports['Viewport: 1'].view.rotate(xAngle=-10, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1886.1, 
        farPlane=3153.2, width=48.1457, height=15.4136, cameraPosition=(2.4987, 
        -6244.65, 0.583685), cameraTarget=(2.4987, -3724.37, 0.585333))
    session.viewports['Viewport: 1'].view.rotate(xAngle=10, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1842.98, 
        farPlane=3196.52, width=847.259, height=271.246, cameraPosition=(
        4.48503, -6209.73, 419.062), cameraTarget=(4.48503, -3727.74, 
        -18.5778))
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
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.1, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1880.8, 
        farPlane=3164.18, width=159.393, height=51.0289, cameraPosition=(
        -1.76484, -6246.54, 69.298), cameraTarget=(-1.76484, -3727.25, 
        -1.07066))
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1888.11, 
        farPlane=3156.91, width=59.2263, height=18.961, cameraPosition=(
        -0.81714, -6247.36, 27.4238), cameraTarget=(-0.81714, -3727.22, 
        1.03365))
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1891.66, 
        farPlane=3153.33, width=12.6099, height=4.03699, cameraPosition=(
        0.71139, -6247.49, 4.80639), cameraTarget=(0.71139, -3727.23, 
        -0.470494))
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.01, 
        farPlane=3151.55, width=17.0548, height=5.46002, cameraPosition=(
        0.32291, -6245.27, 4.93576), cameraTarget=(0.32291, -3725, -0.341134))
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.01, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.View(name='User-1', nearPlane=1889, farPlane=3151.5, width=17.055, 
        height=5.46, projection=PARALLEL, cameraPosition=(0.32291, -6245.3, 
        3.1763), cameraUpVector=(0, 0.0013964, 1), cameraTarget=(0.32291, 
        -3725, -0.34113), viewOffsetX=0, viewOffsetY=0, autoFit=OFF)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.74, 
        farPlane=3150.86, width=7.62981, height=2.44265, cameraPosition=(
        0.509158, -6245.3, 3.57949), cameraTarget=(0.509158, -3725, 0.062056))
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.98, 
        farPlane=3150.62, width=4.37184, height=1.39963, cameraPosition=(
        0.238789, -6245.3, 2.34269), cameraTarget=(0.238789, -3725, 0.0569115))
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.14, 
        farPlane=3150.46, width=2.21346, height=0.708628, cameraPosition=(
        0.354532, -6245.3, 1.10099), cameraTarget=(0.354532, -3725, 0.0468576))
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.viewports['Viewport: 1'].view.rotate(xAngle=-0.001, yAngle=0, zAngle=0, 
        mode=MODEL)
    session.View(name='User-2', nearPlane=1890.1, farPlane=3150.5, width=2.2135, 
        height=0.70863, projection=PARALLEL, cameraPosition=(0.35453, -6245.3, 
        0.96903), cameraUpVector=(0, 0.00036666, 1), cameraTarget=(0.35453, 
        -3725, 0.046858), viewOffsetX=0, viewOffsetY=0, autoFit=OFF)
    p = mdb.models['MyFirstModel'].parts['FLUID']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-2'])
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    p1 = mdb.models['MyFirstModel'].parts['PIPE']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['MyFirstModel'].parts['PIPE']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='FASEI_REV')
    p = mdb.models['MyFirstModel'].parts['PIPE']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='FASEI_REV_ABOVE_TOC')
    p = mdb.models['MyFirstModel'].parts['PIPE']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_BASE')
    p = mdb.models['MyFirstModel'].parts['PIPE']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_ID')
    p = mdb.models['MyFirstModel'].parts['PIPE']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#98 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_OD')
    p = mdb.models['MyFirstModel'].parts['PIPE']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#100 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_TOP')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.96, 
        farPlane=3150.04, width=0.581237, height=0.18608, cameraPosition=(
        0.313568, -6245, 0.795443), cameraTarget=(0.313568, -3725, -0.126615))
    p = mdb.models['MyFirstModel'].parts['PIPE']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#125 ]', ), )
    p.Set(edges=edges, name='FASEI_REV_TT')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1888.44, 
        farPlane=3152.12, width=24.8391, height=7.95213, cameraPosition=(
        0.538064, -6245.27, 3.2646), cameraTarget=(0.538064, -3725, -0.252811))
    p = mdb.models['MyFirstModel'].parts['ROCK']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(faces=faces, name='FASEI_SLAVE')
    p = mdb.models['MyFirstModel'].parts['ROCK']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#242 ]', ), )
    p.Set(edges=edges, name='FASEI_WELL')
    a = mdb.models['MyFirstModel'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].view.setValues(session.views['User-2'])
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['FLUID_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
    a.Set(edges=edges1, name='MESH_TT_ANNULARS')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.22, 
        farPlane=3150.38, width=1.05345, height=0.337257, cameraPosition=(
        0.373484, -6245.3, 0.836782), cameraTarget=(0.373484, -3725, 
        -0.0853901))
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['PIPE_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
    a.Set(edges=edges1, name='MESH_TT_PIPES')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.14, 
        farPlane=3150.46, width=2.38381, height=0.763165, cameraPosition=(
        0.457162, -6245.3, 0.848339), cameraTarget=(0.457162, -3725, 
        -0.0738335))
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['ROCK_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#125 ]', ), )
    a.Set(edges=edges1, name='MESH_TT_ROCK')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.13, 
        farPlane=3150.47, width=2.26832, height=0.726193, cameraPosition=(
        12.2706, -6245.3, 0.931715), cameraTarget=(12.2706, -3725, 0.00954194))
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['PIPE_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#2da ]', ), )
    e2 = a.instances['ROCK_INST'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#2da ]', ), )
    a.Set(edges=edges1+edges2, name='MESH_VERTICAL')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.19, 
        farPlane=3150.4, width=1.3644, height=0.436807, cameraPosition=(
        0.155108, -6245.3, 1.12248), cameraTarget=(0.155108, -3725, 0.200303))
    a = mdb.models['MyFirstModel'].rootAssembly
    r1 = a.instances['ROCK_INST'].referencePoints
    refPoints1=(r1[2], )
    a.Set(referencePoints=refPoints1, name='REFPT')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.87, 
        farPlane=3150.72, width=5.7391, height=1.83735, cameraPosition=(
        10.2085, -6245.3, 1.05657), cameraTarget=(10.2085, -3725, 0.134393))
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['ROCK_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#98 ]', ), )
    a.Set(edges=edges1, name='ROCK_BC')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1889.64, 
        farPlane=3150.95, width=8.85981, height=2.83643, cameraPosition=(
        2.28987, -6245.3, 1.2209), cameraTarget=(2.28987, -3725, 0.298724))
    a = mdb.models['MyFirstModel'].rootAssembly
    f1 = a.instances['ROCK_INST'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
    a.Set(faces=faces1, name='ROCK_OUTPUT')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.2, 
        farPlane=3150.4, width=1.30133, height=0.416615, cameraPosition=(
        0.633475, -6245.3, 0.69774), cameraTarget=(0.633475, -3725, -0.224433))
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['PIPE_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
    e2 = a.instances['FLUID_INST'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#4 ]', ), )
    e3 = a.instances['ROCK_INST'].edges
    edges3 = e3.getSequenceFromMask(mask=('[#4 ]', ), )
    a.Set(edges=edges1+edges2+edges3, name='YSYM_BASE')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.24, 
        farPlane=3150.36, width=0.791405, height=0.253365, cameraPosition=(
        0.497677, -6245.3, 1.10371), cameraTarget=(0.497677, -3725, 0.181541))
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['ROCK_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#100 ]', ), )
    e2 = a.instances['FLUID_INST'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#100 ]', ), )
    e3 = a.instances['PIPE_INST'].edges
    edges3 = e3.getSequenceFromMask(mask=('[#100 ]', ), )
    a.Set(edges=edges1+edges2+edges3, name='YSYM_TOP')


def MacroView():
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


def MacroAssembly3():
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
    del mdb.models['MyFirstModel'].rootAssembly.sets['FASEI_OPEN_WELL']
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['ROCK_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#242 ]', ), )
    a.Set(edges=edges1, name='FASEI_OPEN_WELL')


def MacroAssembly4():
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
    a = mdb.models['MyFirstModel'].rootAssembly
    e1 = a.instances['PIPE_INST'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#242 ]', ), )
    a.Set(edges=edges1, name='FASEI_COMPLETED_WELL')


