from abaqus import *
from abaqusConstants import *

# import os
import json
import sys

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_'
# path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'
path_project = r'C:\Users\leticia\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

from JSONS.ImportTools import process_lithology
from GEOMETRY.geometries import *
from MATERIALS.materials import *
from GEOMETRY.sets import *
from GEOMETRY.assembly import *

mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')

if 'MyFirstModel' not in mdb.models:
    mdb.Model(name='MyFirstModel')

# Reading the json file and filling the input data for the analysis ####################

# with open(r'C:\Users\juani\Documents\Github\Abaqus_WELL_\wellClosure_axi.json') as f:
# with open(r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json') as f:
with open(r'C:\Users\leticia\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json') as f:
    data = json.load(f)

print(f"Data keys: {data.keys()}")

# variables read from json (geometry) ####################################################

name_phase = '136fdd5d-6082-4c4f-8f77-7ed08da1932c'
name_tubular = 'VAM_16in_#97_P110'

outer_diamenter_pipe = data["Tubulars"][name_tubular]['OD']
thickness_pipe = data["Tubulars"][name_tubular]['Thickness']
thickness_pipe = thickness_pipe * 0.0254  # Convert from inches to meters
inner_radius_pipe = outer_diamenter_pipe / 2 - thickness_pipe
inner_radius_pipe = inner_radius_pipe * 0.0254  # Convert from inches to meters
inner_radius_annular = inner_radius_pipe + thickness_pipe
diameter_wellbore = data["Phases"][name_phase]['HoleDiameter']
diameter_wellbore = diameter_wellbore * 0.0254  # Convert from inches to meters
inner_radius_wellbore = diameter_wellbore / 2
thickness_annular = inner_radius_wellbore - inner_radius_annular
thickness_wellbore = 12.0   # Verificar o valor máximo com testes

base_depth = data["AnalysisData"]["Bottom"]
base_depth = int(base_depth)
top_depth = data["AnalysisData"]["Top"]
top_depth = int(top_depth)

print(f"The bottom of the wellbore is at: {-base_depth} meters")
print(f"The top of the wellbore is at: {-top_depth} meters")

########################################################################################

if __name__ == "__main__":

    filtered_layers, t_depths, filtered_rocks = process_lithology(
        data, top_depth, base_depth)
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
    CreateGeometry('MyFirstModel', part_name, part_data)
    PartitionLayersByDepth("MyFirstModel", part_name=part_name,
                           layer_depths=part_data["layer_depths"])

# Definition of materials ###############################################################

if __name__ == "__main__":

    lithology = data["Lithology"]

    init_search = top_depth
    end_search = base_depth

    filtered_data = [
        item for item in lithology
        if item["Top"] < end_search and item["Bottom"] > init_search
    ]

    rock_in_region = {item["Rock"] for item in filtered_data}

    examples = {}

    casing_type = "P110"

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
        'density': 1.0,
        'elastic': (10000, 0),
        'conductivity': 0.702,
        'specific_heat': 2060.0,
        "type": "Fluid"
    }

    for mat_name, properties in filtered_rocks.items():

        examples[mat_name] = {
            "behavior": properties["Law"],
            'density': properties["ElasticParameters"]["Density"],
            'elastic': (properties["ElasticParameters"]["Young"]*1e9,
                        properties["ElasticParameters"]["Poisson"]),
            'conductivity': properties["ThermalParameters"]["Conductivity"],
            'specific_heat': properties["ThermalParameters"]["SpecificHeat"],
            'expansion': properties["ThermalParameters"]["ThermalExpansion"],
            "type": "Rock"
        }

        if "MohrCoulombParameters" in properties:
            mc = properties["MohrCoulombParameters"]
            examples[mat_name].update({
                'friction_angle': mc["FrictionAngle"],
                'dilatancy_angle': mc["DilatancyAngle"],
                'cohesion': mc["Cohesion"],
                "lab_data": ((20001698.76, 0.0), )
            })
            # examples[rock_name]['lab_data'] = ((10e6, 0.0), (20e6, 0.01), (30e6, 0.03), (40e6, 0.06))

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

    import pprint
    pprint.pprint(filtered_layers)

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
        CreateMaterial('MyFirstModel', mat_name, mat_data, sectionLength=1.)

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
