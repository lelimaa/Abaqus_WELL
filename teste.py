import json
import sys 
import numpy as np

# path_project = r'C:\Users\juani\Documents\Github\Abaqus_WELL_' 
path_project = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_'

if path_project not in sys.path:
    sys.path.append(path_project)

from POSTPROCESS.post import *

job_name = 'WellClosureJob'

ExportDisplacementHistory(
        odb_path=job_name + '.odb',
        node_label=3,
        instance_name='ROCK_INST',
        output_file='displacement_no_3.csv'
    )