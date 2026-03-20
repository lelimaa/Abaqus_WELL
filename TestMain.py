from abaqus import *
from abaqusConstants import *

# import os
import json
import sys 

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_' 
path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

from GEOMETRY.geometries import * 
from GEOMETRY.assembly import *
from GEOMETRY.sets import *
from MATERIALS.materials import *
from JSONS.ImportTools import process_lithology             

mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')

if 'MyFirstModel' not in mdb.models:
    mdb.Model(name='MyFirstModel')

# Reading the json file and filling the input data for the analysis ####################

# with open(r'C:\Users\juani\Documents\Github\Abaqus_WELL_\wellClosure_axi.json') as f:
with open(r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json') as f:
    data = json.load(f)

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

    filtered_layers, t_depths, filtered_rocks = process_lithology(data) 
    layers_depths = sorted(t_depths)
    print(layers_depths)

    # layers_depths = [3550, 3900]
    # layers_depths = [3600.0, 4000, 4150.0]

    data = {
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

for part_name, part_data in data.items():
        CreateGeometry('MyFirstModel', part_name, part_data)
        PartitionLayersByDepth("MyFirstModel", part_name=part_name, layer_depths=part_data["layer_depths"])

# Definition of materials ###############################################################

if __name__ == "__main__":
    examples = {
        "STEEL": {
            "behavior": "Elastic",
            'density': 7950,
            'elastic': (206842800000, 0.3),
            'conductivity': 45.3452,
            'specific_heat': 342.2186813,
            "type": "Casing"
        }, 
        "FLUID": {
            "behavior": "Elastic",
            'density': 1.0,
            'elastic': (10000, 0),
            'conductivity': 0.702,
            'specific_heat': 2060.0,
            "type": "Fluid"
        }, 
        "SHALE": {
            "behavior": "MohrCoulomb",
            'density': 2332.73533930301,
            'elastic': (20001698760, 0.29),
            'conductivity': 1.592,
            'specific_heat': 0.209946,
            'expansion': 1.2e-5,
            'friction_angle': 30.0,
            'dilatancy_angle': 10.0,
            'cohesion': 5e6,
            'lab_data': ((10e6, 0.0), (20e6, 0.01), (30e6, 0.03), (40e6, 0.06)),
            "type": "Rock"
        },
        "SANDSTONE": {
            "behavior": "MohrCoulomb",
            'density': 1780.08814332222,
            'elastic': (24062022924.0, 0.25),
            'conductivity': 1.869,
            'specific_heat': 0.209946,
            'expansion': 1.2e-5,
            'friction_angle': 30.0,
            'dilatancy_angle': 10.0,
            'cohesion': 5e6,
            'lab_data': ((10e6, 0.0), (20e6, 0.01), (30e6, 0.03), (40e6, 0.06)),    
            "type": "Rock"
        },
        "HALITE": {
            "behavior": "DoublePowerCreep",
            'density': 1780.08814332222,
            'elastic': (20400009045.2, 0.36),
            'conductivity': 5.55,
            'specific_heat': 0.209946,
            'expansion': 1.2e-5,
            "creep_parameters": {
                "A1": 1.0,
                "A2": 2.0,
                "B1": 3.0,
                "B2": 4.0,
                "C1": 5.0,
                "C2": 6.0,
                "reference_stress": 100.0
            },
            "type": "Rock"
        },
        "CARNALLITE": {
            "behavior": "DoublePowerCreep",
            'density': 1600.0,
            'elastic': (4020040000, 0.36),
            'conductivity': 0.75,
            'specific_heat': 0.209946,
            'expansion': 1.0e-5,
            "creep_parameters": {
                "A1": 1.0,
                "A2": 2.0,
                "B1": 3.0,
                "B2": 4.0,
                "C1": 5.0,
                "C2": 6.0,
                "reference_stress": 100.0
            },
            "type": "Rock"
        }
    }
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

    lythology_examples = [
        {
            "set_name": 'SHALE',
            "set_index": 'L1-I',
            "top_depth": 3200.0,
            "base_depth": 3600.0,
            "partName": 'ROCK',
            "sectionName": 'SHALE_Section',
        },
        {
            "set_name": 'SANDSTONE',
            "set_index": 'L2-I',
            "top_depth": 3600.0,
            "base_depth": 4150.0,
            "partName": 'ROCK',
            "sectionName": 'SANDSTONE_Section',
        },
        # {
        #     "set_name": 'HALITE',
        #     "set_index": 'L3-I',
        #     "top_depth": 4000.0,
        #     "base_depth": 4150.0,
        #     "partName": 'ROCK',
        #     "sectionName": 'HALITE_Section',
        # },
        {
            "set_name": 'HALITE',
            "set_index": 'L3-I',
            "top_depth": 4150.0,
            "base_depth": 4250.0,
            "partName": 'ROCK',
            "sectionName": 'HALITE_Section',
        }
    ]

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

