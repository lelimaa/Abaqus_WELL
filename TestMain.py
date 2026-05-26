from abaqus import *
from abaqusConstants import *

# import os
import json
import sys 
import numpy as np

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL' 
path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL'

if path_project not in sys.path:
    sys.path.append(path_project)

from GEOMETRY.geometries import * 
from GEOMETRY.assembly import *
from GEOMETRY.sets import *
from MATERIALS.materials import *
from JSONS.ImportTools import *
from BCONDITIONS.conditions import *     
from BCONDITIONS.casing import *     
from MESH.mesh import *    
from JOBS.job import *
from POSTPROCESS.post import *

name_of_model = 'MyFirstModel'

mdb.models.changeKey(fromName='Model-1', toName=name_of_model)

if name_of_model not in mdb.models:
    mdb.Model(name=name_of_model)
# mdb.Model(name=name_of_model)

# Reading the json file and filling the input data for the analysis ####################

# with open(r'C:\Users\juani\Documents\Github\Abaqus_WELL\wellClosure_axi.json') as f:
with open(r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL\wellClosure_axi.json') as f:
    data = json.load(f)

# print(f"Data keys: {data.keys()}") # To see the main keys of the json file

# Geometry Variables (read from json) ####################################################

name_phase = '3dda7930-6dbf-4d05-87f2-d2809a3e9fc6'  # The phase from the given json file. It may disappear, because only one phase will be considered soon.
name_tubular = 'LIN_09_875' # The name of the casing in the json file. There refferred to as "Tubulars".

outer_diamenter_pipe = data["Tubulars"][name_tubular]['OD'] # outer diameter of the pipe in inches, as given in the json file. It is converted to meters below.
outer_diamenter_pipe = outer_diamenter_pipe * 0.0254  # Convert from inches to meters
thickness_pipe = data["Tubulars"][name_tubular]['Thickness'] # thickness of the pipe in inches, as given in the json file. It is converted to meters below.
thickness_pipe = thickness_pipe * 0.0254  # Convert from inches to meters
inner_radius_pipe = outer_diamenter_pipe / 2 - thickness_pipe # Inner radius of the pipe, calculated and already in meters.
inner_radius_annular = inner_radius_pipe + thickness_pipe # Inner radius of the annular space, also the outer radius of the pipe, calculated and already in meters.
diameter_wellbore = data["Phases"][name_phase]['HoleDiameter'] # diameter of the wellbore in inches, as given in the json file. It is converted to meters below.
diameter_wellbore = diameter_wellbore * 0.0254  # Convert from inches to meters
inner_radius_wellbore = diameter_wellbore / 2 # Inner radius of the wellbore, calculated and already in meters.
thickness_annular = inner_radius_wellbore - inner_radius_annular # Thickness of the annular space, calculated and already in meters. It is the difference between the inner radius of the wellbore and the inner radius of the annular space (which is the outer radius of the pipe).
thickness_wellbore = 12.0   # Horizontal length of the rock layer ... Check the maximum by testing different lengths. 

top_depth = data["AnalysisData"]["Top"] # The top of the wellbore in meters, as given in json file.
top_depth = int(top_depth) # Convert to integer for easier handling, since the depth is usually given in whole numbers. It is already in meters, so no conversion needed.
base_depth = data["AnalysisData"]["Bottom"] # The bottom of the wellbore in meters, as given in json file. 
base_depth = int(base_depth) # Convert to integer for easier handling, since the depth is usually given in whole numbers. It is already in meters, so no conversion needed.

print(f"The top of the wellbore is at: {-top_depth} meters")
print(f"The bottom of the wellbore is at: {-base_depth} meters")

########################################################################################

if __name__ == "__main__":

    filtered_layers, t_depths, filtered_rocks = process_lithology(data, top_depth, base_depth) 
    layers_depths = sorted(t_depths)

    data_code = {
        "PIPE": {"inner_radius": inner_radius_pipe,
                 "top_depth": top_depth,
                 "base_depth": base_depth,
                 "thickness": thickness_pipe,
                 "layer_depths": layers_depths
                 },
        "FLUID": {"inner_radius": inner_radius_annular,
                  "top_depth": top_depth,
                  "base_depth": base_depth,
                  "thickness": thickness_annular,
                  "layer_depths": layers_depths
                  },
        "ROCK": {"inner_radius": inner_radius_wellbore,
                 "top_depth": top_depth,
                 "base_depth": base_depth,
                 "thickness": thickness_wellbore,
                 "layer_depths": layers_depths
                 }
    }

    for part_name, part_data in data_code.items():
            CreateGeometry(name_of_model, part_name, part_data)
            PartitionLayersByDepth(name_of_model, part_name=part_name, layer_depths=part_data["layer_depths"])

    # Definition of materials ###############################################################

    lithology = data["Lithology"]

    init_search = top_depth
    end_search = base_depth

    filtered_data = [
        item for item in lithology 
        if item["Top"] < end_search and item["Bottom"] > init_search
        ]

    rock_in_region = {item["Rock"] for item in filtered_data}

    examples = {}

    # casing_type = "VM110"
    casing_type = "VM-95"

    examples["STEEL"] = {
        'behavior': data["SteelGrades"][casing_type]["Law"],
        'density': data["SteelGrades"][casing_type]["ElasticParameters"]["Density"],
        'elastic': (data["SteelGrades"][casing_type]["ElasticParameters"]["Young"]*1e9,
                     data["SteelGrades"][casing_type]["ElasticParameters"]["Poisson"]),
        'conductivity': data["SteelGrades"][casing_type]["ThermalParameters"]["Conductivity"],
        'specific_heat': data["SteelGrades"][casing_type]["ThermalParameters"]["SpecificHeat"],
        'expansion': data["SteelGrades"][casing_type]["ThermalParameters"]["ThermalExpansion"],
        # 'plastic': tuple(tuple(item) for item in data["SteelGrades"][casing_type]["MisesPlastic"]["PlasticTable"]),    
        'type': "Casing"
    }

    examples["FLUID"] = {
        'behavior': "ELASTIC",
        'density': 1.0,
        'elastic': (10000, 0),
        'conductivity': 0.702,
        'specific_heat': 2060.0,
        'type': "Fluid"
    }    

    for mat_name, properties in filtered_rocks.items():

        examples[mat_name] = {
            'behavior': properties["Law"],
            'density': properties["ElasticParameters"]["Density"],
            'elastic': (properties["ElasticParameters"]["Young"]*1e9,
                        properties["ElasticParameters"]["Poisson"]),
            'conductivity': properties["ThermalParameters"]["Conductivity"],
            'specific_heat': properties["ThermalParameters"]["SpecificHeat"],
            'expansion': properties["ThermalParameters"]["ThermalExpansion"],
            'type': "Rock"
        }

        if "MohrCoulombParameters" in properties:
            mc = properties["MohrCoulombParameters"]
            examples[mat_name].update({
                'friction_angle': mc["FrictionAngle"],
                'dilatancy_angle': mc["DilatancyAngle"],
                'cohesion': mc["Cohesion"],
                'ultimate_traction': mc["UltimateTraction"]
                # "lab_data": ((20001698.76, 0.0), )
                })

        if "DoublePowerParameters" in properties:
            examples[mat_name]["DoublePowerParameters"] = properties["DoublePowerParameters"]


    material_examples = {
        "PIPE": {
            "partName": 'PIPE',
            "sectionName": 'STEEL_Section',
            "isSolid": True
        },
        "FLUID": {
            "partName": 'FLUID',
            "sectionName": 'FLUID_Section',
            "isSolid": True
        }
    }


    lythology_examples = []

    for i, layer in enumerate(filtered_layers, start=1):

        new_block = {
            "set_name": layer["Rock"],
            "set_index": f"L{i}-I",
            "top_depth": layer["Top"],
            "base_depth": layer["Bottom"],
            "partName": "ROCK",
            "sectionName": f"{layer['Material']}_Section"
        }

        lythology_examples.append(new_block)


    for mat_name, mat_data in examples.items():
        CreateMaterial(name_of_model, mat_name, mat_data, sectionLength=1.)

    mdb.models[name_of_model].setValues(absoluteZero=0.0, stefanBoltzmann=5.670374e-8)

    # plastic_list = data["SteelGrades"][casing_type]["MisesPlastic"]["PlasticTable"]
    # plastic_table_formatted = tuple(tuple(item) for item in plastic_list)

    plastic_table = tuple([tuple(item) for item in data["SteelGrades"][casing_type]["MisesPlastic"]["PlasticTable"]])
    
    AddPlasticityToSteel(name_of_model, 'STEEL', plastic_table)

    CreateSetsPipe(name_of_model)
    CreateSetsFluid(name_of_model)
    CreateSetsRock(name_of_model)

    for section_name in material_examples.values():
        AssignSection(name_of_model,
                        partName=section_name["partName"],
                        sectionName=section_name["sectionName"],
                        isSolid=section_name["isSolid"])
 
    # Assign rock materials by depth layers
    AssignRockByDepth(name_of_model, 'ROCK', lythology_examples)

    # Create assembly
    Assembly(name_of_model, partsNames=['FLUID', 'PIPE', 'ROCK'],
                top_depth=top_depth, base_depth=base_depth)  
        
    # Defining sets for boundary conditions and interactions
    CreateSetsAssembly(name_of_model)   
    CreateSurfacesAssembly(name_of_model, data_code)

    # Steps creation and boundary conditions application  ##############################################

    # Four main steps are required to be created, corresponding to drilling and casing stages

    diameter_wellbore_inch = diameter_wellbore / 0.0254
    diameter_wellbore_str = str(diameter_wellbore_inch).replace('.','_')

    diameter_casing_inch = outer_diamenter_pipe / 0.0254
    diameter_casing_str = str(diameter_casing_inch).replace('.','_')

    name_step1 = 'Drill_' + diameter_wellbore_str
    name_step2 = name_step1 + '_Creep'
    name_step3 = 'Cas_' + diameter_casing_str
    name_step4 = name_step3 + '_Creep'
    
    CreateSteps(name_of_model)

    # Calculation of axial stresses in the casing due to its own weight (initial stresses)    
    stress_top, stress_bottom = CasingStresses(data, name_phase, examples["STEEL"]["density"], top_depth, base_depth)
    ApplyCasingInitialStresses(name_of_model, top_depth, base_depth, stress_top, stress_bottom)

    # Another part of creation of steps
    CreateStepsPartOne(name_of_model)

    stresses_table = ConvertStressesJSON(data["InSituStresses"])

    # Required update in densities in function of vertical loads of each layer
    UpdateMaterialDensities(name_of_model, filtered_layers, stresses_table)

    # Application of geostatic stresses
    ApplyGeostaticStresses(name_of_model, filtered_layers, stresses_table)

    CreateNormalizedGeothermalGrid(
        name_model=name_of_model,
        top_depth=data["ThermalGradient"]["Geothermal_cold"][0]["Depth"], top_temp_C=data["ThermalGradient"]["Geothermal_cold"][0]["Temperature"],
        bottom_depth=data["ThermalGradient"]["Geothermal_cold"][-1]["Depth"], bottom_temp_C=data["ThermalGradient"]["Geothermal_cold"][-1]["Temperature"],
        start_mesh_depth=top_depth,
        end_mesh_depth=base_depth 
    )

    # Another part of creation of steps
    CreateStepsPartTwo(name_of_model)

    ApplyExpressionFieldsGeothermal(
        name_model=name_of_model, filtered_layers=filtered_layers,
        top_depth=data["ThermalGradient"]["Geothermal_cold"][0]["Depth"], top_temp_C=data["ThermalGradient"]["Geothermal_cold"][0]["Temperature"],
        bottom_depth=data["ThermalGradient"]["Geothermal_cold"][-1]["Depth"], bottom_temp_C=data["ThermalGradient"]["Geothermal_cold"][-1]["Temperature"]
        )

    CreateFluidExpressionFields(name_model=name_of_model, mud_weight_ppg=8.5)

    ApplyInitialTemperatures(
        name_model=name_of_model, filtered_layers=filtered_layers,
        top_depth=data["ThermalGradient"]["Geothermal_cold"][0]["Depth"], top_temp_C=data["ThermalGradient"]["Geothermal_cold"][0]["Temperature"],
        base_depth=data["ThermalGradient"]["Geothermal_cold"][-1]["Depth"], base_temp_C=data["ThermalGradient"]["Geothermal_cold"][-1]["Temperature"] 
    )

    # Another part of creation of steps
    CreateStepsPartThree(name_of_model,name_step1)
    

    CreateCreepStep(
        name_model=name_of_model, 
        step_name=name_step2,
        previous_step=name_step1,
        time_period_days=2.0 
        # max_inc_days=None,
        # cetol_value=0.01
    )

    # Another part of creation of steps
    CreateStepsPartFour(
        name_model=name_of_model,
        name_step=name_step3,
        name_step_prev=name_step2
    )

    CreateContactCondition(
        name_model=name_of_model, 
        contact_name='C_FASEI', 
        step_name=name_step3,
        main_surface_name='FASEI_MASTER', 
        secondary_set_name='FASEI_SLAVE', 
        friction_coeff=0.5, 
        secondary_instance='ROCK_INST'
    )

    ConfigurePhaseRev(
        name_model=name_of_model,
        step_name=name_step3
    )

    CreateCreepStep(
        name_model=name_of_model, 
        step_name=name_step4,
        previous_step=name_step3,
        time_period_days=10950.0, 
        max_inc_days=180.0
        # cetol_value=0.01
    )

    ###############################################################################################

    # Calling mesh

    radius_search_pipe = (inner_radius_pipe+inner_radius_annular) / 2.0
    radius_search_fluid = (inner_radius_annular + inner_radius_wellbore) / 2.0
    radius_search_rock = (2 * inner_radius_wellbore + thickness_wellbore) / 2.0

    CreateMeshSizeHorizontal(
        name_model=name_of_model,
        name_instance='FLUID_INST',
        filtered_layers=filtered_layers,
        radius_middle=radius_search_fluid,
        elementSize=4e-3,
        deviationFactor=0.1
    )
    CreateMeshSizeHorizontal(
        name_model=name_of_model,
        name_instance='PIPE_INST',
        filtered_layers=filtered_layers,
        radius_middle=radius_search_pipe,
        elementSize=4e-3,
        deviationFactor=0.1
    )
    CreateMeshBiasHorizontal(
        name_model=name_of_model,
        name_instance='ROCK_INST',
        filtered_layers=filtered_layers,
        radius_middle=radius_search_rock,
        minSize=0.5e-3,
        maxSize=3.0
    )

    # CreateMeshVerticalBySet(
    #     name_model=name_of_model,
    #     name_set='MESH_VERTICAL',
    #     element_size=10
    # )

    CreateMeshVerticalWithBias(
        name_model=name_of_model,
        name_set='MESH_VERTICAL',
         min_size=1,
         max_size=10
    )

    AttributeTypeElement(
        name_model=name_of_model,
        name_set='ALL'
    )

    GenerateMesh(
        name_model=name_of_model,
        name_instance='FLUID_INST'
    )
    GenerateMesh(
        name_model=name_of_model,
        name_instance='PIPE_INST'
    )
    GenerateMesh(
        name_model=name_of_model,
        name_instance='ROCK_INST'
    )

    # Creating a set for the target point in the bottom of the casing 

    CreateSetPointRock(model_name=name_of_model, r_coord=inner_radius_wellbore, z_coord=-abs(base_depth))    
    CreateSetPointCasing(model_name=name_of_model, r_coord=inner_radius_annular, z_coord=-abs(base_depth))


    # Creating a job and saving the model #################################################################
    job_name = 'WellClosureJob'

    CreateJob(
        name_model=name_of_model,
        name_job=job_name,
        num_cpus=14,
        num_gpus=1, 
        run_now=False
    )

    run_now=False

    if run_now:
        RunJob(job_name)

    mdb.saveAs(pathName=r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\WellClosureJob.cae')
    print("Model saved as 'WellClosureJob.cae' in the project folder. You can open it with Abaqus/CAE to review the model and submit the job for analysis.")

    # Output exporting 

    # ExportRockdisplacementAllFrames(
    #     odb_path=job_name + '.odb',
    #     output_file='wall_displacement_all_frames.csv'
    # )

    # ExportRockStressAllFrames(
    #     odb_path=job_name + '.odb',
    #     output_file='rock_stress_all_frames.csv'
    # )

    # ExportCasingStressAllFrames(
    #     odb_path=job_name + '.odb',
    #     output_file='casing_stress_all_frames.csv'
    # )

    # ExportCasingTemperatureAllFrames(
    #     odb_path=job_name + '.odb',  
    #     output_file='casing_temperature_all_frames.csv'
    # )     

    # ExportRockTemperatureAllFrames(
    #     odb_path=job_name + '.odb',
    #     output_file='rock_temperature_all_frames.csv'
    # )   


    # End of the script. ############################################


    # Falta:
    # enxugar as defs para os sets
    # enxugar as defs para os steps
    
    # Can be discussed if necessary to be plotted    
    # ExportCasingTemperatureAllFrames(
    #     odb_path=job_name + '.odb',  
    #     output_file='casing_temperature_all_frames.csv'
    # )
    
    # Can be useful in the plane strain codes
    # ExportPipeStressAtFixedPoint(
    #     odb_path=job_name + '.odb',
    #     output_file='pipe_stress_at_fixed_point_bottom.csv'
    # )

    # Can be useful in the plane strain codes
    # ExportDisplacementHistory(
    #     odb_path=job_name + '.odb',
    #     node_label=3,
    #     instance_name='ROCK_INST',
    #     output_file='displacement_no_3.csv'
    # )