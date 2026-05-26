import os
import json
import sys
# from MESH.meshAlt import *
# from BCONDITIONS.casing import *
# from BCONDITIONS.conditions import *
# from GEOMETRY.geometries import *
# from JOBS.job import *
# from JSONS.ImportTools import *
# from MATERIALS.materials import *
# from GEOMETRY.sets import *
# from GEOMETRY.assembly import *
from abaqusConstants import *
from abaqus import *
from PLANESTRAIN.geometry_plane_strain import *

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_'
path_project = r'C:\Users\leticia\Documents\GitHub\Abaqus_WELL'

if path_project not in sys.path:
    sys.path.append(path_project)

# Change default model name to avoid conflicts when running the script multiple times in the same Abaqus session
mdb.models.changeKey(fromName='Model-1', toName='MyFirstModel')
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

# Rock dimensions
diameter_wellbore = phase_data["HoleDiameter"]
outer_radius_wellbore = diameter_wellbore / 2
outer_radius_wellbore = outer_radius_wellbore * 0.0254  # Convert from inches to meters
thickness_wellbore = diameter_wellbore * 1.5 # Variavel da espessura da rocha
thickness_wellbore = thickness_wellbore * 0.0254 # Convert from inches to meters
inner_radius_wellbore = outer_radius_wellbore + thickness_wellbore
inner_radius_wellbore = inner_radius_wellbore * 0.0254
# Casing / Pipe dimensions
outer_diameter_pipe = data["Tubulars"][name_tubular]['OD']
radius_pipe = outer_diameter_pipe / 2
outer_radius_pipe = radius_pipe * 0.0254  # Convert from inches to meters
thickness_pipe = data["Tubulars"][name_tubular]['Thickness']
thickness_pipe = thickness_pipe * 0.0254  # Convert from inches to meters
inner_radius_pipe = outer_radius_pipe - thickness_pipe
inner_radius_pipe = inner_radius_pipe * 0.0254  # Convert from inches to meters
# Annulus dimensions
outer_radius_annular = inner_radius_wellbore
inner_radius_annular = outer_radius_pipe
thickness_annular = outer_radius_annular - inner_radius_annular
thickness_annular = thickness_annular * 0.0254  # Convert from inches to meters

l_depth = data["AnalysisData"]["Depth"]
print(f"The bottom of the wellbore is at: {-l_depth} meters")

# Script to create the geometry ##########################################

if __name__ == "__main__":
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
                           "outer_radius": outer_radius_annular,
                           "thickness": thickness_annular},)
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