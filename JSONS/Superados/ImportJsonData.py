import json 
# import os
import numpy as np

# Defining the file paths

json_file_path = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json'
target_script_path = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\TestMain.py'

# Reading the paramater from the JSON file

try:
    with open(json_file_path, 'r') as f:
        config_data = json.load(f)

    Config_data_keys = list(config_data.keys())  # to refer the keys as numbers
   
    AnalysisData_keys = list(config_data[Config_data_keys[0]].keys())  # to refer the keys as numbers

    well_top = config_data[Config_data_keys[0]][AnalysisData_keys[2]]
    well_bottom = config_data[Config_data_keys[0]][AnalysisData_keys[3]]

    # Getting Thermal Gradient Data #######################################################################################

    ThermalGradient_keys = list(config_data[Config_data_keys[1]].keys())  # to refer the keys as numbers

    Geothermal_cold_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[0]])  # to refer the keys as numbers

    geothermal_cold_depths = []
    geothermal_cold_temps = []
    
    for i in range(len(Geothermal_cold_keys)):

        geothermal_cold_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[0]][i]['Depth'])
        geothermal_cold_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[0]][i]['Temperature'])

    geothermal_cold_depths = np.array(geothermal_cold_depths)
    geothermal_cold_temps = np.array(geothermal_cold_temps)
    
    Seawater_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[1]])  # to refer the keys as numbers

    seawater_depths = []
    seawater_temps = []

    for i in range(len(Seawater_keys)):
        seawater_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[1]][i]['Depth'])
        seawater_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[1]][i]['Temperature'])

    seawater_depths = np.array(seawater_depths)
    seawater_temps = np.array(seawater_temps)

    temp_drilling_phase_1_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[2]])  # to refer the keys as numbers
    temp_drilling_phase_1_depths = []
    temp_drilling_phase_1_temps = []

    for i in range(len(temp_drilling_phase_1_keys)):
        temp_drilling_phase_1_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[2]][i]['Depth'])
        temp_drilling_phase_1_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[2]][i]['Temperature'])

    temp_drilling_phase_1_depths = np.array(temp_drilling_phase_1_depths)
    temp_drilling_phase_1_temps = np.array(temp_drilling_phase_1_temps)

    temp_drilling_phase_2_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[3]])  # to refer the keys as numbers    
    temp_drilling_phase_2_depths = []
    temp_drilling_phase_2_temps = []

    for i in range(len(temp_drilling_phase_2_keys)):
        temp_drilling_phase_2_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[3]][i]['Depth'])
        temp_drilling_phase_2_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[3]][i]['Temperature'])

    temp_drilling_phase_2_depths = np.array(temp_drilling_phase_2_depths)
    temp_drilling_phase_2_temps = np.array(temp_drilling_phase_2_temps)


    temp_drilling_d1_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[4]])  # to refer the keys as numbers
    temp_drilling_d1_depths = []
    temp_drilling_d1_temps = []

    for i in range(len(temp_drilling_d1_keys)):
        temp_drilling_d1_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[4]][i]['Depth'])
        temp_drilling_d1_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[4]][i]['Temperature'])

    temp_drilling_d1_depths = np.array(temp_drilling_d1_depths)
    temp_drilling_d1_temps = np.array(temp_drilling_d1_temps)

    temp_drilling_d2_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[5]])  # to refer the keys as numbers
    temp_drilling_d2_depths = []
    temp_drilling_d2_temps = []
    
    for i in range(len(temp_drilling_d2_keys)):
        temp_drilling_d2_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[5]][i]['Depth'])
        temp_drilling_d2_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[5]][i]['Temperature'])

    temp_drilling_d2_depths = np.array(temp_drilling_d2_depths)
    temp_drilling_d2_temps = np.array(temp_drilling_d2_temps)

    geothermal_warm_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[6]])  # to refer the keys as numbers
    
    geothermal_warm_depths = []
    geothermal_warm_temps = []

    for i in range(len(geothermal_warm_keys)):
        geothermal_warm_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[6]][i]['Depth'])
        geothermal_warm_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[6]][i]['Temperature'])

    geothermal_warm_depths = np.array(geothermal_warm_depths)
    geothermal_warm_temps = np.array(geothermal_warm_temps)

    production_annulus_keys = list(config_data[Config_data_keys[1]][ThermalGradient_keys[7]])  # to refer the keys as numbers
    production_annulus_depths = []
    production_annulus_temps = []

    for i in range(len(production_annulus_keys)):
        production_annulus_depths.append(config_data[Config_data_keys[1]][ThermalGradient_keys[7]][i]['Depth'])
        production_annulus_temps.append(config_data[Config_data_keys[1]][ThermalGradient_keys[7]][i]['Temperature'])

    production_annulus_depths = np.array(production_annulus_depths)
    production_annulus_temps = np.array(production_annulus_temps)

    # Getting Tubulars Geometric Data #######################################################################################

    tubular_keys = list(config_data[Config_data_keys[2]].keys())  # to refer the keys as numbers
    
    # name_tubular = 'VAM_16in_#97_P110'
    # name_tubular = '22_0IN_251_0NW_X70'
    name_tubular = 'TEN_30_#161.33_X56'
 
    if name_tubular in tubular_keys:
        od_pipe1 = config_data[Config_data_keys[2]][name_tubular]['OD']
        thickness_pipe1 = config_data[Config_data_keys[2]][name_tubular]['Thickness']
        material_pipe1 = config_data[Config_data_keys[2]][name_tubular]['Material']
        inner_radius_pipe1_json = od_pipe1 / 2 - thickness_pipe1
    else:
        od_pipe1 = None
        thickness_pipe1 = None
        material_pipe1 = None
        inner_radius_pipe1_json = None
        print("Tubular not found.")

    # Getting Lithology Data #######################################################################################
    # 
    
    lithology_keys = list(config_data[Config_data_keys[3]])  # to refer the keys as numbers

    rocks_list = [rock['Rock'] for rock in lithology_keys]

    # collecting all 'Top' depths and the last 'Bottom' depth
    depths = [rock['Top'] for rock in lithology_keys] + [lithology_keys[-1]['Bottom']]

    # Getting the unique depths, sort them, and converting to a numpy array
    depths_array = np.array(sorted(set(depths)))

    # Getting InSituStresses Data #######################################################################################

    insitu_keys = list(config_data[Config_data_keys[4]])  # to refer the keys as numbers
    # tubular1_keys = list(config_data[Config_data_keys[2]][tubular_keys[0]].keys())  # to refer the keys as numbers
    
    depths_insitu = [stress['Depth'] for stress in insitu_keys]

    depth_analysis = 4150.0
 
    if depth_analysis in depths_insitu:
        index = depths_insitu.index(depth_analysis)
        overburden_insitu = insitu_keys[index]['Overburden']
        sh_max_insitu = insitu_keys[index]['ShMax']
        sh_min_insitu = insitu_keys[index]['ShMin']
        pore_pressure_insitu = insitu_keys[index]['PorePressure']
    else:
        overburden_insitu = None
        sh_max_insitu = None
        sh_min_insitu = None
        pore_pressure_insitu = None
        print("Depth not found in InSituStresses.")

    # Getting Rocks Material properties Data #######################################################################################

    # This is similar to tubular data in which we have a list of different tubulars 
    rocks_properties_keys = list(config_data[Config_data_keys[5]])  # to refer the keys as numbers

    # name_rock = 'SHALE'
    name_rock = 'HALITE'
    # name_rock = 'TACHYHYDRITE'

    halite_properties_keys = list(config_data[Config_data_keys[5]]['HALITE'].keys())  # to refer the keys as numbers
 
    if name_rock in rocks_properties_keys:
        DPL_s0 = config_data[Config_data_keys[5]][name_rock][halite_properties_keys[0]]['s0']
        DPL_a1 = config_data[Config_data_keys[5]][name_rock][halite_properties_keys[0]]['a1']
        DPL_a2 = config_data[Config_data_keys[5]][name_rock][halite_properties_keys[0]]['a2']
        DPL_b1 = config_data[Config_data_keys[5]][name_rock][halite_properties_keys[0]]['b1']
        DPL_b2 = config_data[Config_data_keys[5]][name_rock][halite_properties_keys[0]]['b2']
        DPL_c1 = config_data[Config_data_keys[5]][name_rock][halite_properties_keys[0]]['c1']
        DPL_c2 = config_data[Config_data_keys[5]][name_rock][halite_properties_keys[0]]['c2']
    else:
        DPL_s0 = None
        DPL_a1 = None
        DPL_a2 = None
        DPL_b1 = None
        DPL_b2 = None
        DPL_c1 = None
        DPL_c2 = None
        print("Rock not found.")

    # Getting SteelGrades Material properties Data #######################################################################################
 
    steelgrades_keys = list(config_data[Config_data_keys[7]])  # to refer the keys as numbers

    name_steelgrade = 'P110'

    steelgrades_properties_keys = list(config_data[Config_data_keys[7]][name_steelgrade].keys())  # to refer the keys as numbers
    
    metal_sy = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[0]]['sy']
    metal_sUlt = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[0]]['sUlt']
    metal_epUlt = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[0]]['epUlt']
    metal_density = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[3]]['Density']
    metal_young_modulus = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[3]]['Young']
    metal_poisson = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[3]]['Poisson']
    metal_conductivity = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[4]]['Conductivity']
    metal_specific_heat = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[4]]['SpecificHeat']
    metal_thermal_expansion = config_data[Config_data_keys[7]][name_steelgrade][steelgrades_properties_keys[4]]['ThermalExpansion']

    # Getting Phases Data #######################################################################################

    phases_keys = list(config_data[Config_data_keys[8]])  # to refer the keys as numbers


    # Getting Fluids Data #######################################################################################

    fluids_keys = list(config_data[Config_data_keys[10]])  # to refer the keys as numbers

    sea_water_density = config_data[Config_data_keys[10]][fluids_keys[0]]['Density']
    drilling_phase_1_density = config_data[Config_data_keys[10]][fluids_keys[1]]['Density']
    drilling_d1_density = config_data[Config_data_keys[10]][fluids_keys[2]]['Density']
    drilling_d2_density = config_data[Config_data_keys[10]][fluids_keys[3]]['Density']
    drilling_d3_density = config_data[Config_data_keys[10]][fluids_keys[4]]['Density']
    drilling_d4_density = config_data[Config_data_keys[10]][fluids_keys[5]]['Density']
    drilling_d5_density = config_data[Config_data_keys[10]][fluids_keys[6]]['Density']
    mud_weight_density = config_data[Config_data_keys[10]][fluids_keys[7]]['Density']
    production_annulusA_density = config_data[Config_data_keys[10]][fluids_keys[8]]['Density']

except FileNotFoundError:
    print(f"Error: The file {json_file_path} was not found.")
    exit()  
except json.JSONDecodeError:
    print(f"Error: The file {json_file_path} is not a valid JSON file.")
    exit()