from abaqus import mdb
from abaqusConstants import *

def CreateSteps(name_model):
    m = mdb.models[name_model]
    a = m.rootAssembly
    region = a.sets['FASEI_OPEN_WELL']
    m.XsymmBC(name='FIX_FASEI_WELL', createStepName='Initial', 
    region=region, localCsys=None)

    region = a.instances['PIPE_INST'].sets['FASEI_REV']
    m.PinnedBC(name='PIN_FASEI', createStepName='Initial', 
        region=region, localCsys=None)
    
    region = a.sets['ROCK_BC']
    m.XsymmBC(name='XSYM_ROCK_BC', createStepName='Initial', 
        region=region, localCsys=None)
    
    region = a.sets['YSYM_BASE']
    m.YsymmBC(name='YSYM_BASE', createStepName='Initial', 
        region=region, localCsys=None)
    
    region = a.sets['YSYM_TOP']
    m.YsymmBC(name='YSYM_TOP', createStepName='Initial', 
        region=region, localCsys=None)
    
    region = a.instances['PIPE_INST'].sets['FASEI_REV']
    m.GeostaticStress(name='S_FASEI_REV', region=region, 
        stressMag1=133997000.0, vCoord1=-2000.0, stressMag2=-21981800.0, 
        vCoord2=-4000.0, lateralCoeff1=0.0, lateralCoeff2=0.0)
    
    # Verificar como automatizar para as diferentes camadas de rocha
    
    region = a.instances['ROCK_INST'].sets['L1-I']
    m.GeostaticStress(name='S_L1-I', region=region, 
        stressMag1=-31412800.0, vCoord1=-2500.0, stressMag2=-40566400.0, 
        vCoord2=-2900.0, lateralCoeff1=1.0, lateralCoeff2=None)
    
    region = a.instances['ROCK_INST'].sets['L2-I']
    m.GeostaticStress(name='S_L2-I', region=region, 
        stressMag1=-40566400.0, vCoord1=-2900.0, stressMag2=-45805200.0, 
        vCoord2=-3200.0, lateralCoeff1=1.0, lateralCoeff2=None)
    
    region = a.instances['ROCK_INST'].sets['L3-I']
    m.GeostaticStress(name='S_L3-I', region=region, 
        stressMag1=-45805200.0, vCoord1=-3200.0, stressMag2=-51044000.0, 
        vCoord2=-3500.0, lateralCoeff1=1.0, lateralCoeff2=None)
    
    #######################################################################
    
    m.GeostaticStep(name='Geostatic', previous='Initial', 
    nlgeom=ON)

    regionDef=m.rootAssembly.instances['PIPE_INST'].sets['FASEI_REV']
    m.FieldOutputRequest(name='FASEI_REV', 
        createStepName='Geostatic', variables=('S', 'MISES', 'E', 'PE', 'U', 
        'NT'), region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
    m.fieldOutputRequests['F-Output-1'].suppress()
    del m.fieldOutputRequests['F-Output-1']

    regionDef=m.rootAssembly.sets['ROCK_OUTPUT']
    m.FieldOutputRequest(name='ROCK_OUTPUT', 
        createStepName='Geostatic', variables=('U', 'TEMP'), region=regionDef, 
        sectionPoints=DEFAULT, rebar=EXCLUDE)

    m.historyOutputRequests['H-Output-1'].suppress()
    del m.historyOutputRequests['H-Output-1']

    region =a.instances['FLUID_INST'].sets['FASEI_FLUIDO']
    m.ModelChange(name='MC_FASEI_FLUIDO', 
        createStepName='Geostatic', region=region, activeInStep=False, 
        includeStrain=False)

    region =a.instances['PIPE_INST'].sets['FASEI_REV']
    m.ModelChange(name='MC_FASEI_REV', 
        createStepName='Geostatic', region=region, activeInStep=False, 
        includeStrain=False)
    m.Gravity(name='GRAVITY', createStepName='Geostatic', 
        comp2=-9.81, distributionType=UNIFORM, field='')
    
    m.StaticStep(name='Transition', previous='Geostatic', 
    timePeriod=2.0, initialInc=1.0, minInc=2e-05, maxInc=2.0)
    m.TimePoint(name='timePoint', points=((1.0, ), (3600.0, ), 
        (7200.0, ), (14400.0, ), (28800.0, ), (57600.0, ), (86400.0, ), (
        172800.0, ), (345600.0, ), (691200.0, ), (1382400.0, ), (2764800.0, ), 
        (5529600.0, ), (11059200.0, ), (22118400.0, ), (31536000.0, ), (
        63072000.0, ), (126144000.0, ), (252288000.0, ), (504576000.0, ), (
        946080000.0, )))
    m.fieldOutputRequests['FASEI_REV'].setValuesInStep(
        stepName='Transition', timePoint='timePoint')
    m.fieldOutputRequests['ROCK_OUTPUT'].setValuesInStep(
        stepName='Transition', timePoint='timePoint')
    m.StaticStep(name='TempDefine', previous='Transition', 
        timePeriod=3.0, initialInc=1.0, minInc=3e-05, maxInc=3.0)