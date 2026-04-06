import json
# with open(r'C:\Users\juani\Documents\Github\Abaqus_WELL_\wellClosure_axi.json') as f:
with open(r'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_\wellClosure_axi.json') as f:
    data = json.load(f)

def process_lithology(data, global_top, global_bottom):
    # 1. Pega os limites globais do modelo (Ex: 3200 e 4250)
    # global_top = data["AnalysisData"]["Top"]
    # global_bottom = data["AnalysisData"]["Bottom"]
    
    # 2. Inicia o set de profundidades já com os limites globais
    # t_depths = set([global_top, global_bottom])
    t_depths = set()
    
    filtered_layers = []
    filtered_rocks = {}
    
    lithology = data["Lithology"]
    json_rocks = data["Rocks"]
    
    # Usamos um contador manual para nomear as camadas sequencialmente (LAYER_01, LAYER_02...)
    layer_counter = 1 
    
    for layer in lithology:
        l_top = layer["Top"]
        l_bottom = layer["Bottom"]
        
        # Ignora as rochas que estão completamente fora do domínio do poço
        if l_bottom <= global_top or l_top >= global_bottom:
            continue
            
        # Se o topo da rocha for menor que o topo do poço, ele corta no topo do poço.
        # Se a base da rocha for maior que a base do poço, ele corta na base do poço.
        clipped_top = max(l_top, global_top)
        clipped_bottom = min(l_bottom, global_bottom)
        
        # Formata o nome da camada (ex: LAYER_01)
        lname = "LAYER_%02d" % layer_counter
        layer_counter += 1
        
        # Prepara o material da rocha
        rock_name = layer["Rock"]
        rock_mat = json_rocks[rock_name].copy()
        mat_name = lname + "_" + rock_name # Ex: LAYER_01_SANDSTONE
        print(rock_mat.keys())
        rock_mat["Name"] = mat_name
        # rock_mat["ElasticParameters"]["Density"] = getFromOverburden(data["overburden"])
        filtered_rocks[mat_name] = rock_mat
        
        # Cria a nova camada com os valores CORTADOS e substitui/adiciona as chaves necessárias
        new_layer = layer.copy()
        new_layer["Name"] = lname
        new_layer["Material"] = mat_name
        new_layer["Top"] = clipped_top
        new_layer["Bottom"] = clipped_bottom
        
        filtered_layers.append(new_layer)
        
        # Adiciona as profundidades cortadas ao set (para particionar a geometria no Abaqus depois)
        t_depths.add(clipped_top)
        t_depths.add(clipped_bottom)
        
    # Remove as fronteiras globais do set, deixando apenas os cortes intermediários
    t_depths.discard(global_top)
    t_depths.discard(global_bottom)

    return filtered_layers, t_depths, filtered_rocks


# filtered_layers, t_depths, filtered_rocks = process_lithology(data) 
# pprint(filtered_layers)
# pprint(filtered_rocks)

# t_depths = set([x for x in depths if A_depths[0]<= x <= A_depths[1]])
# t_depths.add(A_depths[0])
# t_depths.add(A_depths[1])

# print(sorted(t_depths))