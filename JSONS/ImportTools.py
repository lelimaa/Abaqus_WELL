import json
# with open(r'C:\Users\juani\Documents\Github\Abaqus_WELL\wellClosure_axi.json') as f:
with open(r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json') as f:
    data = json.load(f)

def process_lithology(data, global_top, global_bottom):

    t_depths = set()
    
    filtered_layers = []
    filtered_rocks = {}
    
    lithology = data["Lithology"]
    json_rocks = data["Rocks"]
    
    # We use a manual counter to name the layers sequentially (LAYER_01, LAYER_02...)
    layer_counter = 1 
    
    for layer in lithology:
        l_top = layer["Top"]
        l_bottom = layer["Bottom"]
        
        # Ignore the rocks that are completely outside the well domain
        if l_bottom <= global_top or l_top >= global_bottom:
            continue
            
        # If the top of the rock is less than the top of the well, it cuts at the well's top.
        # If the bottom of the rock is greater than the bottom of the well, it cuts at the well's bottom.
        clipped_top = max(l_top, global_top)
        clipped_bottom = min(l_bottom, global_bottom)
        
        # Formats the name of the layer (ex: LAYER_01)
        lname = "LAYER_%02d" % layer_counter
        layer_counter += 1
        
        # Prepares the material of the rock
        rock_name = layer["Rock"]
        rock_mat = json_rocks[rock_name].copy()
        mat_name = lname + "_" + rock_name # Ex: LAYER_01_SANDSTONE
        rock_mat["Name"] = mat_name
        filtered_rocks[mat_name] = rock_mat
        
        # Creates the new layer with the clipped values and updates/adds the necessary keys
        new_layer = layer.copy()
        new_layer["Name"] = lname
        new_layer["Material"] = mat_name
        new_layer["Top"] = clipped_top
        new_layer["Bottom"] = clipped_bottom
        
        filtered_layers.append(new_layer)
        
        # Adds the clipped depths to the set (for partitioning the geometry in Abaqus later)
        t_depths.add(clipped_top)
        t_depths.add(clipped_bottom)
        
    # Remove the global boundaries from the set, leaving only the intermediate cuts
    t_depths.discard(global_top)
    t_depths.discard(global_bottom)

    return filtered_layers, t_depths, filtered_rocks

