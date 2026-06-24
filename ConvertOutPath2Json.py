import csv
import json
from collections import defaultdict

# 1. Variables to store data temporarily
node_for_z = {}
data_for_time = defaultdict(dict)
nodes_order = []  # To ensure nodes and displacements are in the same order

# 2. Reading the CSV file
with open('path_data_all_frames.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header ("Time (s), Node Label, ...")
    
    for row in reader:
        # Skip empty or incomplete rows
        if not row or len(row) < 4: 
            continue
            
        try:
            time_str = row[0].strip()  # Keep as string to use as dictionary key
            node = int(row[1])
            z_pos = float(row[2])
            u1_disp = float(row[3])
            
            # If this is the first time we see this node, register its Z position
            if node not in node_for_z:
                node_for_z[node] = z_pos
                nodes_order.append(node)
            
            # Register the displacement associated with the time instant and node
            data_for_time[time_str][node] = u1_disp
            
        except ValueError:
            # Ignore conversion errors (residual texts)
            continue

# 3. Building the list of Z Coordinates in the same order as the nodes
z_coords = [node_for_z[n] for n in nodes_order]

# 4. Building the dictionary of displacements by time
time_displacements = {}
for t_str, nodes_dict in data_for_time.items():
    # For each time instant, create a list of displacements 
    # ensuring it follows the same order as the "nodes_order" list
    disp_list = [nodes_dict.get(n, 0.0) for n in nodes_order]
    time_displacements[t_str] = disp_list

# 5. Closing everything in the requested JSON structure
json_final = {
    "wellbore_closure": {
        "node_labels": nodes_order,
        "z_coords": z_coords,
        "time_displacements": time_displacements
    }
}

# 6. Saving the file
with open('open_well_closure.json', 'w', encoding='utf-8') as f:
    json.dump(json_final, f, indent=4)

print("Conversion completed successfully!")