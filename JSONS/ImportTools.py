import json
with open(r'C:\Users\juani\Documents\Github\Abaqus_WELL_\wellClosure_axi.json') as f:
# with open(r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json') as f:
    data = json.load(f)

# pprint(data["Lithology"])
# print("\n\n")
# data["AnalysisData"]["Top"] = 4000
# data["AnalysisData"]["Bottom"] = 5000

materials = dict()

def process_lithology(data):
    top = data["AnalysisData"]["Top"]
    bottom = data["AnalysisData"]["Bottom"]
    t_depths = set((top, bottom))
    filtered_layers = []
    filtered_rocks = {}
    lithology = data["Lithology"]
    json_rocks = data["Rocks"]
    for i, layer in enumerate(lithology):
        lname = "LAYER_%.2d" % (i+1)
        if layer["Bottom"] <= top or layer["Top"] >= bottom:
            continue
        if layer["Top"] < top and layer["Bottom"] > top:
            rock_mat = json_rocks[layer["Rock"]].copy()
            rock_mat["Name"] = lname + "_Material"
            filtered_rocks[rock_mat["Name"]] = rock_mat
            filtered_layers.append({**layer, "Name": lname, "Top": top, "Material": rock_mat["Name"]})
        elif layer["Top"] < bottom and layer["Bottom"] > bottom:
            rock_mat = json_rocks[layer["Rock"]].copy()
            rock_mat["Name"] = lname + "_Material"
            filtered_rocks[rock_mat["Name"]] = rock_mat
            filtered_layers.append({**layer, "Name": lname, "Bottom": bottom, "Material": rock_mat["Name"]})
        else:
            rock_mat = json_rocks[layer["Rock"]].copy()
            rock_mat["Name"] = lname + "_Material"
            filtered_rocks[rock_mat["Name"]] = rock_mat
            filtered_layers.append({**layer, "Name": lname, "Material": rock_mat["Name"]})
        t_depths.add(layer["Top"])
        t_depths.add(layer["Bottom"])

    return filtered_layers, t_depths, filtered_rocks


# filtered_layers, t_depths, filtered_rocks = process_lithology(data) 
# pprint(filtered_layers)
# pprint(filtered_rocks)

# t_depths = set([x for x in depths if A_depths[0]<= x <= A_depths[1]])
# t_depths.add(A_depths[0])
# t_depths.add(A_depths[1])

# print(sorted(t_depths))