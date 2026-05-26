from abaqus import mdb
from abaqusConstants import *
import numpy as np

def ConvertStressesJSON(in_situ_stresses):

    convertion_factor = 119.826 * 9.81

    table_sv_pa = {}

    for item in in_situ_stresses:
        depth = item["Depth"]
        emw_ppg = item["Overburden"]

        sv_pa = - (emw_ppg * convertion_factor * depth)

        table_sv_pa[depth] = sv_pa

    return table_sv_pa

def GetStressesExact(z, table):
    depths = sorted(table.keys())

    if z <= depths[0]: return table[depths[0]]
    if z >= depths[-1]: return table[depths[-1]]

    for i in range(len(depths)-1):
        z0, z1 = depths[i], depths[i+1]
        if z0 <= z <= z1:
            s0, s1 = table[z0], table[z1]

            return s0 + (z - z0) * ((s1 - s0) / (z1 - z0))
        
        
def UpdateMaterialDensities(name_model, filtered_layers, stresses_table):
    m = mdb.models[name_model]

    gravity=9.81

    print("\n>>> Updating densities of layers via pressure gradient...")

    layer_counter = 1 

    for layer in filtered_layers:
        z_top = layer['Top']
        z_bottom = layer['Bottom']

        lname = "LAYER_%02d" % layer_counter
        layer_counter += 1

        layer_name = lname + "_" + layer['Rock']

        p_top = GetStressesExact(z_top, stresses_table)
        p_bottom = GetStressesExact(z_bottom, stresses_table)

        print(f"The pressure at the top of layer '{layer_name}' (depth {z_top} m) is approximately {p_top/1e6:.2f} MPa.")
        print(f"The pressure at the bottom of layer '{layer_name}' (depth {z_bottom} m) is approximately {p_bottom/1e6:.2f} MPa.")

        delta_z = abs(z_bottom - z_top)

        if delta_z > 0:

            rho_calculated = abs(p_bottom - p_top) / (gravity * delta_z)
            print(f"Calculated density for layer '{layer_name}': {rho_calculated:.2f} kg/m³ based on pressure gradient.")

            rho_final = round(rho_calculated, 2)

            if layer_name in m.materials.keys():
                m. materials[layer_name].Density(table=((rho_final, ), ))
                print(f" Material {layer_name}: Density adjusted to {rho_final} kg/m³")
            else:
                print(f" [WARNING] Material {layer_name} not found to uptade density.")              



def ApplyGeostaticStresses(name_model, filtered_layers, stresses_table):
    m = mdb.models[name_model]
    a = m.rootAssembly
    inst_rock = a.instances['ROCK_INST']

    def GetStressesExact(z, table):
        depths = sorted(table.keys())

        if z <= depths[0]: return table[depths[0]]
        if z >= depths[-1]: return table[depths[-1]]

        for i in range(len(depths)-1):
            z0, z1 = depths[i], depths[i+1]
            if z0 <= z <= z1:
                s0, s1 = table[z0], table[z1]

                return s0 + (z-z0) * ((s1 - s0) / (z1 - z0))
            
    for i, layer in enumerate(filtered_layers):

        z_top = layer['Top']
        z_bottom = layer['Bottom']

        layer_num = i + 1
        set_name = f'L{layer_num}-I'  

        stress_top = GetStressesExact(z_top, stresses_table)
        stress_bottom = GetStressesExact(z_bottom, stresses_table)

        region = inst_rock.sets[set_name]
        
        m.GeostaticStress(
            name = f'S_{set_name}',
            region=region,
            stressMag1=stress_top,
            vCoord1=-z_top,
            stressMag2=stress_bottom,
            vCoord2=-z_bottom,
            lateralCoeff1=1.0,
            # lateralCoeff2=None
            lateralCoeff2=1.0
        )

        name_material = layer['Rock']

        print(f"[{set_name}-{name_material}] Stresses: Top ({z_top}m) = {stress_top/1e6:.2f} MPa | Bottom ({z_bottom}m) = {stress_bottom/1e6:.2f} MPa")
    
    print("All the geostatic stresses were successfully applied!")


def CreateNormalizedGeothermalGrid(name_model, top_depth, top_temp_C, bottom_depth, bottom_temp_C, start_mesh_depth, end_mesh_depth):
        
    m = mdb.models[name_model]

    T_ref = top_temp_C + 273.15

    gradient = (bottom_temp_C -top_temp_C) / (bottom_depth - top_depth)

    gridPointData1 = {}

    step = 2.5

    for depth in np.arange(start_mesh_depth, end_mesh_depth + (step/2), step):

        temp_celsius = top_temp_C + (depth - top_depth) * gradient
        temp_norm = (temp_celsius + 273.15) / T_ref

        gridPointData1[str(-depth)] = (
            (1.79769313486232e+308, 0.0, 100.0),
            (0.0, temp_norm, temp_norm),
            (100.0, temp_norm, temp_norm)
        )

    if 'Geothermal' in m.analyticalFields.keys():
        del m.analyticalFields['Geothermal']


    m.MappedField(
        name='Geothermal', description='Thermical Profile Normalized',
        regionType=POINT, partLevelData=False, localCsys=None,
        pointDataFormat=GRID, fieldDataType=SCALAR, gridPointPlane=PLANE13,
        gridPointData=gridPointData1
    )
    print(f"Mappedfield 'Geothermal' successfully created! (T_ref = {T_ref} K)")


def ApplyCasingInitialStresses(name_model, z_top, z_bottom, stress_top, stress_bottom):
    m = mdb.models[name_model]
    a = m.rootAssembly

    coord_top = -abs(z_top)
    coord_bottom = -abs(z_bottom)

    region = a.instances['PIPE_INST'].sets['FASEI_REV']
    name_condition = 'S_FASEI_REV'

    m.GeostaticStress(
        name=name_condition,
        region=region,
        stressMag1=stress_top,
        vCoord1=coord_top,
        stressMag2=stress_bottom,
        vCoord2=coord_bottom,
        lateralCoeff1=0.0,
        lateralCoeff2=0.0
    )


def CreateSteps(name_model):
    """
    Create the steps of the model. It is subdivided into other definitions.
    """
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

    
    #######################################################################
    
    ### FUNÇÃO ApplyCasingInitialStresses #################################  
    
    #######################################################################


    #######################################################################
    
    ### FUNÇÃO ApplyGeostaticStresses #####################################    
    
    #######################################################################

def CreateStepsPartOne(name_model):
    """
    Create the steps of the model. Correspondes to initial definitions.
    """
    m = mdb.models[name_model]
    a = m.rootAssembly
    
    m.GeostaticStep(name='Geostatic', previous='Initial', 
    nlgeom=ON)

    # Here we define the field outputs that we want to be able to export later in the post-processing phase. 

    regionDef=m.rootAssembly.instances['PIPE_INST'].sets['FASEI_REV']
    m.FieldOutputRequest(name='FASEI_REV', 
        createStepName='Geostatic', variables=('S', 'MISES', 'E', 'PE', 'U', 
        'NT', 'CSTRESS'), region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
    
    if 'F-Output-1' in m.fieldOutputRequests.keys():
        del m.fieldOutputRequests['F-Output-1']

    regionDef=m.rootAssembly.sets['ROCK_OUTPUT']
    m.FieldOutputRequest(name='ROCK_OUTPUT', 
        createStepName='Geostatic', variables=('U', 'TEMP','NT', 'S', 'MISES'), region=regionDef, 
        sectionPoints=DEFAULT, rebar=EXCLUDE)

    if 'H-Output-1' in m.historyOutputRequests.keys():
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
        stepName='Transition')
        # stepName='Transition', timePoint='timePoint')
    m.fieldOutputRequests['ROCK_OUTPUT'].setValuesInStep(
        stepName='Transition')
        # stepName='Transition', timePoint='timePoint')
    

    m.StaticStep(name='TempDefine', previous='Transition', 
        timePeriod=3.0, initialInc=1.0, minInc=3e-05, maxInc=3.0)
    
    ##########################################################################################################
    
    ### FUNÇÃO CreateNormalizedGeothermalGrid #####################################
    
    ##########################################################################################################

def CreateStepsPartTwo(name_model):
    """
    Create the steps of the model. Corresponds to initial conditions with temperature.
    """
    m = mdb.models[name_model]
    a = m.rootAssembly

    region = a.sets['FASEI']
    # m.Temperature(name='NT_FASEI', createStepName='TempDefine', 
    m.Temperature(name='NT_FASEI', createStepName='Initial', 
        region=region, distributionType=FIELD, 
        crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
        field='Geothermal', magnitudes=(277.15, ))

    region = a.sets['FASEI_COMPLETED_WELL']
    m.Temperature(name='NT_FASEI_ID', 
        # createStepName='TempDefine', region=region, distributionType=FIELD, 
        createStepName='Initial', region=region, distributionType=FIELD, 
        crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
        field='Geothermal', magnitudes=(277.15, ))
    

    
def ApplyExpressionFieldsGeothermal(name_model, filtered_layers, top_depth=2000.0, top_temp_C=4.0, bottom_depth=4000.0, bottom_temp_C=75.0):
    """
    Create geothermal fields.
    """ 
    m = mdb.models[name_model]

    gradient = (bottom_temp_C - top_temp_C) / (bottom_depth - top_depth)

    t_surface_C = top_temp_C - (gradient * top_depth)
    intercept_K = t_surface_C + 273.15

    for i, layer in enumerate(filtered_layers):
        layer_num = i+1
        set_name = f'L{layer_num}-I'
        z_top = layer['Top']

        t_top_K = (gradient * z_top) + intercept_K

        expressionf = f"({gradient:.16f}*pow(-Y,1))/{t_top_K:.1f} + ({intercept_K:.15f}*pow(-Y,0))/{t_top_K:.1f}"

        name_field = f'NT_{set_name}'

        if name_field in m.analyticalFields.keys():
            del m.analyticalFields[name_field]

        m.ExpressionField(
            name=name_field,
            localCsys=None,
            description=f'Normalized Temperature for the layer base {set_name}',
            expression=expressionf
        )
        print(f"ExpressionField '{name_field}' created with denominator {t_top_K:.1f} K")

    print("All the thermal ExpressionFields of the rocks were created!")

    
def CreateFluidExpressionFields(name_model, mud_weight_ppg=8.5):
    """
    Create fluid expresion fields.
    """ 

    m = mdb.models[name_model]

    factor_conversion = 119.826 * 9.81
    gradient_fluid = mud_weight_ppg * factor_conversion 

    expression_clean = f'{gradient_fluid} * pow(-Y,1)'

    names_fields = [
        'P_FASEI_COMPLETED_WELL',
        'P_FASEI_FLUID',
        'P_FASEI_OPEN_WELL'
    ]

    for name_field in names_fields:

        if name_field in m.analyticalFields.keys():
            del m.analyticalFields[name_field]

        m.ExpressionField(
            name=name_field, 
            localCsys=None,
            description=f'Pressure hydrostatic clean ({mud_weight_ppg} ppg)',
            expression=expression_clean
        )
        print(f"ExpressionField '{name_field}' created with success!")


def ApplyInitialTemperatures(name_model, filtered_layers, step_name='Initial', top_depth=2000.0, top_temp_C=4.0, base_depth=4000.0, base_temp_C=75.0):
    """
    Create the condition of application of initial temperature.
    """ 
    m = mdb.models[name_model]
    a = m.rootAssembly
    inst_rock = a.instances['ROCK_INST']

    gradient = (base_temp_C - top_temp_C) / (base_depth - top_depth)
    t_surface_C = top_temp_C - (gradient * top_depth)
    intercept_K = t_surface_C + 273.15

    for i, layer in enumerate(filtered_layers):
        layer_num = i+1
        sulfix = f'L{layer_num}-I'

        z_top = layer['Top']
        t_top_K = (gradient * z_top) + intercept_K

        name_field_analytical = f'NT_{sulfix}'

        sets_aim = [sulfix, f'{sulfix}_OD']

        for name_set in sets_aim:
            region = inst_rock.sets[name_set]
            name_condition = f'NT_{name_set}'

            m.Temperature(
                name=name_condition,
                createStepName=step_name,
                region=region, 
                distributionType=FIELD, 
                crossSectionDistribution=CONSTANT_THROUGH_THICKNESS,
                field=name_field_analytical,
                magnitudes=(t_top_K, )
            )
            print(f"Temperature '{name_condition}' applied in the region {name_set} (Magnitude: {t_top_K:.2f} K)")

    # print("\n>>> All the temperatures of the layers were started successfully!")


def CreateStepsPartThree(name_model,name_step):
    """
    Create a step of pressure in the model, corresponding to the stage of drilling.
    """ 
    
    m = mdb.models[name_model]
    a = m.rootAssembly

    # name_step = 'Perf_10_375'

    m.StaticStep(name=name_step, previous='TempDefine')
    print(f">>> Step '{name_step}' created with success!")

    if 'FASEI_OPEN_WELL' in a.surfaces.keys():
        region = a.surfaces['FASEI_OPEN_WELL']
    else:
        region =a.sets['FASEI_OPEN_WELL']

    m.Pressure(
        name='P_FASEI_OPEN_WELL',
        createStepName=name_step,
        region=region,
        distributionType=FIELD,
        field='P_FASEI_OPEN_WELL',
        magnitude=1.0,
        amplitude=UNSET
    )

    print("Hydrostatic pressure of the mud applied in the open well region.")
    
    m.boundaryConditions['FIX_FASEI_WELL'].deactivate(
        name_step)
    
def CreateCreepStep(name_model, step_name, previous_step, time_period_days, max_inc_days=None, cetol_value=1e-4, initial_inc_sec=1e-6):
    """
    Create a step of creep in the model.
    """ 
    m = mdb.models[name_model]
    
    time_period_sec = time_period_days * 24.0 * 3600.0

    if max_inc_days is None:
        max_inc_sec = time_period_sec
    else:
        max_inc_sec = max_inc_days * 24.0 * 3600.0

    max_inc_sec = min(max_inc_sec, time_period_sec)

    m.ViscoStep(
        name=step_name,
        previous=previous_step,
        timePeriod=time_period_sec,
        maxNumInc=1000000,
        initialInc=initial_inc_sec,
        minInc=1e-15,
        maxInc=max_inc_sec,
        cetol=cetol_value
    )

    print(f">>> ViscoStep '{step_name}' created: Total duration of {time_period_days} days.")

    if max_inc_days:
        print(f"    - Increment locked in maximum of {max_inc_days} days per step.")


def CreateStepsPartFour(name_model,name_step,name_step_prev):
    """
    Create a step corresponding to the stage of casing installation.
    """     
    
    m = mdb.models[name_model]

    # name_step = 'Rev_9_875'

    m.StaticStep(name=name_step, previous=name_step_prev, minInc=1e-15)
    print(f">>> Step '{name_step}' created with success!") 

def CreateContactCondition(name_model, contact_name, step_name, main_surface_name, secondary_set_name, friction_coeff=0.5, secondary_instance='ROCK_INST'):
    """
    Create a contact condition, corresponding to the stage of casing installation.
    """ 
    m = mdb.models[name_model]
    a = m.rootAssembly

    if contact_name not in m.interactionProperties.keys():
        m.ContactProperty(contact_name)

        # Tangential behavior (friction/penalty)
        m.interactionProperties[contact_name].TangentialBehavior(
            formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
            pressureDependency=OFF, temperatureDependency=OFF, dependencies=0,
            table=((friction_coeff, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION,
            fraction=0.005, elasticSlipStiffness=None
        )

        # Normal behavior (hard contact)
        m.interactionProperties[contact_name].NormalBehavior(
            pressureOverclosure=HARD, allowSeparation=ON, constraintEnforcementMethod=DEFAULT
        )

        print(f"Contact property '{contact_name}' created (Friction: {friction_coeff}).")
    else:
        print(f"Contact property '{contact_name}' already exists. Skipping creation.")

    region_main = a.surfaces[main_surface_name]
    region_secondary = a.instances[secondary_instance].sets[secondary_set_name]


    if contact_name in m.interactions.keys():
        del m.interactions[contact_name]

    m.SurfaceToSurfaceContactStd(
        name=contact_name,
        createStepName=step_name,
        main=region_main,
        secondary=region_secondary,
        sliding=FINITE,
        thickness=ON,
        interactionProperty=contact_name,
        adjustMethod=NONE,
        initialClearance=OMIT,
        datumAxis=None,
        clearanceRegion=None
    )

    print(f"Interaction '{contact_name}' activated in Step '{step_name}'.")

def ConfigurePhaseRev(name_model, step_name):
    """
    Create conditions of pressure in the phase of casing installation.
    """ 
    m = mdb.models[name_model]
    a = m.rootAssembly

    if 'FASEI_COMPLETED_WELL' in a.surfaces.keys():
        region_completed = a.surfaces['FASEI_COMPLETED_WELL']
        m.Pressure(
            name='P_FASEI_COMPLETED_WELL',
            createStepName=step_name,  
            region=region_completed,
            distributionType=FIELD,
            field='P_FASEI_COMPLETED_WELL',
            magnitude=1.0,
            amplitude=UNSET
        )
        print("- Pressure P_FASEI_COMPLETED_WELL activated.")

    if 'FASEI_FLUIDO' in a.surfaces.keys():
        region_fluid = a.surfaces['FASEI_FLUIDO']
        m.Pressure(
            name='P_FASEI_FLUID',
            createStepName=step_name,  
            region=region_fluid,
            distributionType=FIELD,
            field='P_FASEI_FLUID',
            magnitude=1.0,
            amplitude=UNSET
        )
        print("- Pressure P_FASEI_FLUID activated.")

    if 'P_FASEI_OPEN_WELL' in m.loads.keys():
        m.loads['P_FASEI_OPEN_WELL'].deactivate(step_name)
        print(" - Load P_FASEI_OPEN_WELL deactivated.")

    if 'MC_FASEI_REV' in m.interactions.keys():
        m.interactions['MC_FASEI_REV'].setValuesInStep(
            stepName=step_name, 
            activeInStep=True)
        print("- Interaction of casing (Model Change) activated.")

    if 'PIN_FASEI' in m.boundaryConditions.keys():
        m.boundaryConditions['PIN_FASEI'].deactivate(step_name)
        print(" - Boundary condition PIN_FASEI (temporary lock) deactivated.")

    # print("Phase of casing successfully configured!")

