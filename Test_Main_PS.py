from abaqusConstants import *
from abaqus import *
# import os
import json
import sys

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_'
path_project = r'C:\Users\leticia\Documents\GitHub\Abaqus_WELL'

if path_project not in sys.path:
    sys.path.append(path_project)

# from MESH.meshAlt import *
# from BCONDITIONS.casing import *
# from BCONDITIONS.conditions import *
# from GEOMETRY.geometries import *
# from JOBS.job import *
from JSONS.ImportTools import *
from MATERIALS.materials import *
from GEOMETRY.sets import *
# from GEOMETRY.assembly import *
from GEOMETRY_PS.geometry_PS import *

# Change default model name to avoid conflicts when running the script multiple times in the same Abaqus session
# mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')

if 'MyFirstModel' not in mdb.models:
    mdb.Model(name='MyFirstModel')
# mdb.Model(name='MyFirstModel')

# Reading the json file and filling the input data for the analysis ####################

with open(r'C:\Users\leticia\Documents\GitHub\Abaqus_WELL\wellbore_closure_planestrain.json') as f:
    data = json.load(f)
    print(f"Data keys: {data.keys()}")
# Data keys: dict_keys(['AnalysisData', 'ThermalGradient',
#           'Tubulars', 'Lithology', 'InSituStresses', 'Rocks', 'Cements',
#           'SteelGrades', 'Phases', 'Events', 'Fluids'])

# Variables read from json (geometry) #####################################

# name_phase = '3dda7930-6dbf-4d05-87f2-d2809a3e9fc6'
# name_tubular = 'LIN_09_875'
if "Phases" not in data["AnalysisData"]:
    print("Chave 'Phases' não encontrada")
    print(data["AnalysisData"].keys())
name_phase = data["AnalysisData"]["Phases"]
print(name_phase)
phase_data = data["Phases"][name_phase]
if phase_data:
    name_tubular = phase_data["Casing"][0]["Tubular"]
else:
    print(f"Phase '{name_phase}' not found in data['Phases']")

############ Rock dimensions ############################
diameter_wellbore = phase_data["HoleDiameter"]
outer_radius_wellbore = diameter_wellbore / 2
outer_radius_wellbore = outer_radius_wellbore * 0.0254  # Convert from inches to meters
thickness_wellbore = outer_radius_wellbore * 0.9  # Variavel da espessura da rocha
inner_radius_wellbore = outer_radius_wellbore - thickness_wellbore

########### Casing / Pipe dimensions ####################
outer_diameter_pipe = data["Tubulars"][name_tubular]['OD']
outer_radius_pipe = (outer_diameter_pipe / 2) * 0.1 # 10% do valor do raio externo para criar um espaço entre a parede do tubo e a borda do modelo
outer_radius_pipe = outer_radius_pipe * 0.0254  # Convert from inches to meters
thickness_pipe = data["Tubulars"][name_tubular]['Thickness']
thickness_pipe = thickness_pipe * 0.1 * 0.0254  # 10% do valor da espessira (inches to meters)
inner_radius_pipe = outer_radius_pipe - thickness_pipe
stand_off = data["AnalysisData"]["StandOff"] / 100   # Convert from inches to meters
min_wall_thickness = data["Tubulars"][name_tubular]["MinWallThickness"]/100
min_wall_thickness = (1 - min_wall_thickness)   # Convert from inches to meters
thickness_min = thickness_pipe * min_wall_thickness
ovality = data["Tubulars"][name_tubular]["Ovality"] / 100

########## Annulus dimensions ###########################
outer_radius_annular = inner_radius_wellbore
inner_radius_annular = outer_radius_pipe
thickness_annular = outer_radius_annular - inner_radius_annular

l_depth = data["AnalysisData"]["Depth"]
print(f"The bottom of the wellbore is at: {-l_depth} meters")

################### Script to create the geometry ##########################################

if __name__ == "__main__":
    if 'MyFirstModel' not in mdb.models:
        mdb.Model(name='MyFirstModel')
    
    if PlaneStrainPart.parametrize_geometry is None:
        PlaneStrainPart.parametrize_geometry = {
            "center1": [0,0],
            "center2": [0,0],
            "outer_radius": outer_radius_wellbore,
            "thickness": thickness_wellbore
        }

    AnnulusPart = PlaneStrainPart("AnnulusPart1",
                     data={"center1": [0,0],
                           "center2": [0,0],
                           "outer_radius": outer_radius_annular,
                           "thickness": thickness_annular},)
    AnnulusPart.create_part("MyFirstModel")
    AnnulusPart.create_base_sets("MyFirstModel")
    AnnulusPart.add_to_assembly("MyFirstModel")
    print("Annulus created and added to assembly.")

    RockPart = PlaneStrainPart("RockPart1",
                     data={"center1": [0,0],
                           "center2": [0,0],
                           "outer_radius": outer_radius_wellbore,
                           "thickness": thickness_wellbore},)
    RockPart.create_part("MyFirstModel")
    RockPart.create_base_sets("MyFirstModel")
    RockPart.add_to_assembly("MyFirstModel")
    print("Rock created and added to assembly.")

    CasingPart = PlaneStrainPart("CasingPart1",
                     data={"center1": [0,0],    
                           "center2": [0,0],
                           "outer_radius": outer_radius_pipe,
                           "thickness": thickness_pipe},)
    CasingPart.create_part("MyFirstModel")
    CasingPart.create_base_sets("MyFirstModel")
    CasingPart.add_to_assembly("MyFirstModel")
    print("Casing created and added to assembly.")

    ################### Definition of materials #################################################
    lithology = data["Lithology"]
    
    for layer in lithology:
        if l_depth >= layer["Top"] and l_depth < layer["Bottom"]:
            layer_rock = layer["Rock"]
            print(f"Layer at depth {l_depth} meters: {layer_rock}")
            
    examples = {}

    # casing_type = "VM110"
    casing_type = data["Tubulars"][name_tubular]["Material"] 
    # Seleciona o tipo de aço para o casing definido no json (ex: VM-95) e pega as propriedades do material a partir do json
    steelgrade_info = data["SteelGrades"][casing_type]
    # Seleciona o Gradiente Geotérmico definido no "AnalysisData"
    data_geothermal = data["AnalysisData"]["GeothermalGradient"]
    # Seleciona o Gradiente Térmico presente e definido antes
    thermalGradient = data["ThermalGradient"][data_geothermal]
    # Retorna uma lista de todos os fluidos com "ThermalGradient" = "data_geothermal"
    
    name_fluido = next(
        (name for name, info in data["Fluids"].items() 
         if info.get("ThermalGradient") == data_geothermal), None)
    print(f"Selected Fluid: {name_fluido}")

    examples["STEEL"] = {
        "behavior": data["SteelGrades"][casing_type]["Law"],
        'density': data["SteelGrades"][casing_type]["ElasticParameters"]["Density"],
        'elastic': (data["SteelGrades"][casing_type]["ElasticParameters"]["Young"]*1e9,
                    data["SteelGrades"][casing_type]["ElasticParameters"]["Poisson"]),
        'conductivity': data["SteelGrades"][casing_type]["ThermalParameters"]["Conductivity"],
        'specific_heat': data["SteelGrades"][casing_type]["ThermalParameters"]["SpecificHeat"],
        'expansion': data["SteelGrades"][casing_type]["ThermalParameters"]["ThermalExpansion"],
        "type": "Casing"
    }

    examples["FLUID"] = {
        "behavior": "ELASTIC",
        'density': data["Fluids"][name_fluido]["Density"],
        'compressibility': data["Fluids"][name_fluido]["Compressibility"],
        'ThermalExpansion': data["Fluids"][name_fluido]["ThermalExpansion"],
        "type": "Fluid"
    }
    
    examples[layer_rock] = {
    "behavior": data["Rocks"][layer_rock]["Law"],
    'density': data["Rocks"][layer_rock]["ElasticParameters"]["Density"],
    'elastic': (data["Rocks"][layer_rock]["ElasticParameters"]["Young"]*1e9,
                data["Rocks"][layer_rock]["ElasticParameters"]["Poisson"]),
    'conductivity': data["Rocks"][layer_rock]["ThermalParameters"]["Conductivity"],
    'specific_heat': data["Rocks"][layer_rock]["ThermalParameters"]["SpecificHeat"],
    'expansion': data["Rocks"][layer_rock]["ThermalParameters"]["ThermalExpansion"],
    "type": "Rock"
}

    if "MohrCoulombParameters" in data["Rocks"][layer_rock]:
        mc = data["Rocks"][layer_rock]["MohrCoulombParameters"]
        examples[layer_rock].update({
        'friction_angle': mc["FrictionAngle"],
        'dilatancy_angle': mc["DilatancyAngle"],
        'cohesion': mc["Cohesion"],
        "lab_data": ((20001698.76, 0.0), )
        })
  
    if "DoublePowerParameters" in data["Rocks"][layer_rock]:
            examples[layer_rock]["DoublePowerParameters"] = data["Rocks"][layer_rock]["DoublePowerParameters"]

    material_examples = {
        "PIPE": {
            "partName": CasingPart.name,
            "sectionName": 'STEEL_Section',
            "isSolid": True
        },
        "FLUID": {
            "partName": AnnulusPart.name,
            "sectionName": 'FLUID_Section',
            "isSolid": True
        }
    }

    for mat_name, mat_data in examples.items():
        CreateMaterial('MyFirstModel', mat_name, mat_data, sectionLength=1.)

    mdb.models['MyFirstModel'].setValues(
        absoluteZero=0.0, stefanBoltzmann=5.670374e-8)

    AddplasticityToSteel('MyFirstModel', 'STEEL')

######### Create sets for boundary conditions and interactions ############################
    CreateSetsPipe('MyFirstModel')
    CreateSetsFluid('MyFirstModel')
    CreateSetsRock('MyFirstModel')

    for section_name in material_examples.values():
        Assign_Section('MyFirstModel',
                       partName=section_name["partName"],
                       sectionName=section_name["sectionName"],
                       isSolid=section_name["isSolid"])

    # Assign rock materials by depth layers
    AssignRockByDepth('MyFirstModel', 'ROCK', lythology_examples)

    # Create assembly
    Assembly('MyFirstModel', partsNames=['FLUID', 'PIPE', 'ROCK'],
             top_depth=top_depth, base_depth=base_depth)

    # Defining sets for boundary conditions and interactions
    CreateSetsAssembly('MyFirstModel')

    CreateSurfacesAssembly('MyFirstModel', data_code)

    # Steps creation and boundary conditions application

    CreateSteps('MyFirstModel')