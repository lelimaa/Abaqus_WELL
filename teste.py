
print("\n>>> SCRIPT STARTED SUCCESSFULLY!")

import json
import sys 
import numpy as np
import os

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_' 
path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

from POSTPROCESS.post import *

job_name = 'WellClosureJob'


# ExportRockDisplacementAllFrames(
#     odb_path=job_name + '.odb',
#     output_file='path_data_all_frames.csv'
# )

# ExportRockStressAllFrames(
#     odb_path=job_name + '.odb',
#     output_file='rock_stress_all_frames.csv'
# )


# ExportCasingStressAllFrames(
#         odb_path=job_name + '.odb',
#         output_file='casing_stress_all_frames.csv'
    # )     

# ExportCasingTemperatureAllFrames(
#         odb_path=job_name + '.odb',  
#         output_file='casing_temperature_all_frames.csv'
#     )

ExportRockTemperatureAllFrames(
        odb_path=job_name + '.odb',
        output_file='rock_temperature_all_frames.csv'
    )





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