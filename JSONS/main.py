import json 
# import os

# Defining the file paths

json_file_path = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json'
target_script_path = r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\TestMain.py'

# Reading the paramater from the JSON file

try:
    with open(json_file_path, 'r') as f:
        config_data = json.load(f)

    # --- Navigate through the nested structure to get the value ---
    # seawater_depth_json = config_data['ThermalGradient']['seawater'][0]['Depth']
    top_depth_wellbore_json = config_data['AnalysisData']['Top'][0]['Depth']

    # Print the result
    print(f"The top depth of the wellbore is: {top_depth_wellbore_json}")
    # print(f"The temperature is: {seawater_depth_json}")

except FileNotFoundError:
    print(f"Error: The file {json_file_path} was not found.")
    exit()  
except json.JSONDecodeError:
    print(f"Error: The file {json_file_path} is not a valid JSON file.")
    exit()

# Reading the content of the target Python script

try:
    with open(target_script_path, 'r') as f:
        # Reading all the lines of the file into a list
        script_lines = f.readlines()
    
except FileNotFoundError:
    print(f"Error: The file {target_script_path} was not found.")
    exit()

# Finding the line to modify and change the parameter value
new_script_lines = []
modified = False
# The string we are looking for to identify the line
target_line_start = "top_depth"

for line in script_lines:
    if line.strip().startswith(target_line_start):
        # Constructing the new line with the updated parameter value
        new_line = f"{target_line_start} {seawater_depth_json}  # Updated by script\n"
        new_script_lines.append(new_line)
        modified = True
        print(f"Found and replaced line: {new_line.strip()}")
        print(f"New line: '{new_line.strip()}'")
    else:
        # If it's not the target line, keep it unchanged
        new_script_lines.append(line)

# Write the modified content back to the target script if modified
if modified:
    with open(target_script_path, 'w') as f:
        f.writelines(new_script_lines)
    print(f"\nSuccessfully updated the '{target_line_start}' variable in {target_script_path}.")
else:
    print(f"\nWarning: Could not find a line starting with '{target_line_start}' in {target_script_path}. No changes were made.")

