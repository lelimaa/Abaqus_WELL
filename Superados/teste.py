
print("\n>>> SCRIPT STARTED SUCCESSFULLY!")

import json
import sys 
import numpy as np
import os

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_' 
path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

# from POSTPROCESS.post import *

job_name = 'WellClosureJob'

# ExportRockDisplacementAllFrames(
#     odb_path=job_name + '.odb',
#     output_file='rock_displacement_all_frames.csv'
# )

# ExportRockStressAllFrames(
#     odb_path=job_name + '.odb',
#     output_file='rock_stress_all_frames.csv'
# )

# ExportCasingDisplacementAllFrames(
#     odb_path=job_name + '.odb',
#     output_file='casing_displacement_all_frames.csv'
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

convert_now = True  # Set to True to execute the conversion of CSV to JSON

if convert_now:

### Testing the conversion of CSV to JSON for multiple files
    from JSONS.ConvertTools import convert_csv_abaqus_to_json

    # Converting to csv

    # Dicionário de configuração mapeando cada arquivo e suas respectivas chaves estruturais
    configuration_tasks = [
        {
            "csv": "rock_displacement_all_frames.csv",
            "json": "rock_displacement_all_frames.json",
            "key_root": "wellbore_closure",
            "key_data": "time_rock_displacements"
        },
        {
            "csv": "rock_stress_all_frames.csv",
            "json": "rock_stress_all_frames.json",
            "key_root": "rock_stress",
            "key_data": "time_rock_stresses"
        },
        {
            "csv": "rock_temperature_all_frames.csv",
            "json": "rock_temperature_all_frames.json",
            "key_root": "rock_temperature",
            "key_data": "time_rock_temperatures"
        },
        {
            "csv": "casing_displacement_all_frames.csv",
            "json": "casing_displacement_all_frames.json",
            "key_root": "casing_displacement",
            "key_data": "time_casing_displacements"
        },
        {
            "csv": "casing_stress_all_frames.csv",
            "json": "casing_stress_all_frames.json",
            "key_root": "casing_stress",
            "key_data": "time_casing_stresses"
        },
        {
            "csv": "casing_temperature_all_frames.csv",
            "json": "casing_temperature_all_frames.json",
            "key_root": "casing_temperature",
            "key_data": "time_casing_temperatures"
        }
    ]

    print("Starting the processing of Abaqus files in batch...\n")

    # Sweep the list of configurations executing the funtion for each item
    for task in configuration_tasks:
        convert_csv_abaqus_to_json(
            path_csv=task["csv"],
            path_json=task["json"],
            main_key=task["key_root"],
            name_field_data=task["key_data"]
        )
        
    print("\nAll the available files were processed!")


# Lines for tests with the post-processing functions.

# print("\n" + "="*30)
# print("STARTING POST-PROCESSING...")
# print("="*30)

# try:
#     import post 
#     print(">>> Module 'post' imported successfully.")

#     odb_name ='WellClosureJob.odb'

#     csv_name = 'casing_stress_all_frames.csv'

#     print(f">>> Trying to process: {odb_name}")
#     post.ExportCasingStressAllFrames(odb_name, csv_name)

#     print(">>> Command of export finished.")

# except:
#     print(">>> Error: Could not import the 'post' module or execute the function. Check the file and try again.")

# print("="*30)
# print("END OF SCRIPT")
# print("="*30)

# Can be useful in the plane strain codes 
# ExportDisplacementHistory(
#         odb_path=job_name + '.odb',
#         node_label=3,
#         instance_name='ROCK_INST',
#         output_file='displacement_no_3.csv'
#     )

# Its not necessary, since CasingStressAllFrames has all the points including from the base (pending to work)
# Can be usefull in the plane strain codes
# ExportPipeStressAtFixedPoint(
#         odb_path=job_name + '.odb',
#         output_file='pipe_stress_at_fixed_point_bottom.csv'
#     )