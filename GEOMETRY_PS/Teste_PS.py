from abaqusConstants import *
from abaqus import *

# import os
import json
import sys

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