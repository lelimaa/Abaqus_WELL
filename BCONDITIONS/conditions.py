from abaqus import mdb
from abaqusConstants import *

# def interpolate_stress(depth_aim, list_stresses, key):

#     depth_aim_actual = abs(depth_aim)

#     x = [item["Depth"] for item in list_stresses]
#     y = [item[key] for item in list_stresses]

#     if depth_aim_actual <= x[0]: return y[0]

#     if depth_aim_actual >= x[-1]: return y[-1]

#     for i in range(len(x) - 1):
#         if x[i] <= depth_aim_actual <= x[i+1]:
#             x0, x1 = x[i], x[i+1]
#             y0, y1 = y[i], y[i+1]

#             return y0 + (depth_aim_actual - x0) * ((y1 - y0) / (x1 - x0))
        

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
    
    # Verificar como automatizar para as diferentes camadas de rocha #############################
    
    # region = a.instances['ROCK_INST'].sets['L1-I']
    # m.GeostaticStress(name='S_L1-I', region=region, 
    #     stressMag1=-31412800.0, vCoord1=-2500.0, stressMag2=-40566400.0, 
    #     vCoord2=-2900.0, lateralCoeff1=1.0, lateralCoeff2=None)
    
    # region = a.instances['ROCK_INST'].sets['L2-I']
    # m.GeostaticStress(name='S_L2-I', region=region, 
    #     stressMag1=-40566400.0, vCoord1=-2900.0, stressMag2=-45805200.0, 
    #     vCoord2=-3200.0, lateralCoeff1=1.0, lateralCoeff2=None)
    
    # region = a.instances['ROCK_INST'].sets['L3-I']
    # m.GeostaticStress(name='S_L3-I', region=region, 
    #     stressMag1=-45805200.0, vCoord1=-3200.0, stressMag2=-51044000.0, 
    #     vCoord2=-3500.0, lateralCoeff1=1.0, lateralCoeff2=None)

    
    
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
    
    # Perguntar sobre essa definição para poder atualizar para n camadas de rocha #############################
    
    # delta_T = 3.2e-4
    # v1 = 1.06404

    # # Create dict with keys from -2500 to -3500 with -2.5 intervals
    # gridPointData1 = {}
    # for index, depth in enumerate(np.arange(-2500, -3502.5, -2.5)):
    #     val = v1+(index)*delta_T
    #     gridPointData1[str(depth)] = (
    #         (1.79769313486232e+308, 0.0, 100.0),
    #         (0.0, val, val),
    #         (100.0, val, val)
    #     )
    # m.MappedField(name='Geotermico', description='', 
    #     regionType=POINT, partLevelData=False, localCsys=None, 
    #     pointDataFormat=GRID, fieldDataType=SCALAR, gridPointPlane=PLANE13, 
    #     gridPointData=gridPointData1)
    
    ##########################################################################################################

    # region = a.instances['Analise-1-1'].sets['FASEI']
    # m.Temperature(name='NT_FASEI', createStepName='TempDefine', 
    #     region=region, distributionType=FIELD, 
    #     crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
    #     field='Geotermico', magnitudes=(277.15, ))

    # region = a.instances['Analise-1-1'].sets['FASEI_COMPLETED_WELL']
    # m.Temperature(name='NT_FASEI_ID', 
    #     createStepName='TempDefine', region=region, distributionType=FIELD, 
    #     crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
    #     field='Geotermico', magnitudes=(277.15, ))
    
