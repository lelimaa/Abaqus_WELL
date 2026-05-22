# import os
import json
import sys
from MESH.meshAlt import *
from BCONDITIONS.casing import *
from BCONDITIONS.conditions import *
from GEOMETRY.geometries import *
from JOBS.job import *
from JSONS.ImportTools import *
from MATERIALS.materials import *
from GEOMETRY.sets import *
from GEOMETRY.assembly import *
from abaqusConstants import *
from abaqus import *


# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_'
path_project = r'C:\Users\leticia\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

# Change default model name to avoid conflicts when running the script multiple times in the same Abaqus session
mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')

if 'MyFirstModel' not in mdb.models:
    mdb.Model(name='MyFirstModel')
# mdb.Model(name='MyFirstModel')

# Reading the json file and filling the input data for the analysis ####################

# with open(r'C:\Users\juani\Documents\Github\Abaqus_WELL_\wellClosure_axi.json') as f:
with open(r'C:\Users\leticia\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json') as f:
    data = json.load(f)

print(f"Data keys: {data.keys()}")
# Data keys: dict_keys(['AnalysisData', 'ThermalGradient',
#           'Tubulars', 'Lithology', 'InSituStresses', 'Rocks', 'Cements',
#           'SteelGrades', 'Phases', 'Events', 'Fluids'])

# Variables read from json (geometry) #####################################

# name_phase = '3dda7930-6dbf-4d05-87f2-d2809a3e9fc6'
name_phase = data["AnalysisData"]["Phases"]
# name_tubular = 'LIN_09_875'
fase_data = data["Phases"].get(name_phase)
if fase_data:
    name_tubular = fase_data["Casing"][0]["Tubular"]
else:
    print(f"Phase '{name_phase}' not found in data['Phases']")

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

# Script to create the geometry ##########################################
