# from abaqus import mdb
# from abaqusConstants import *

from odbAccess import openOdb
# import visualization
import numpy as np
import os
from abaqusConstants import ELEMENT_NODAL


def ExportRockDisplacementAllFrames(odb_path, output_file):

    odb = openOdb(path=odb_path)
    a = odb.rootAssembly
    set_name = 'FASEI_OPEN_WELL'

    if set_name not in a.nodeSets.keys():
        print("Error: The set was not found.")
        odb.close()
        return

    target_set = a.nodeSets[set_name]

    # instance_name = 'ROCK_INST' 

    node_coords = {}
    # nodes = a.instances[instance_name].nodes

    for node in target_set.nodes[0]:

        node_coords[node.label] = node.coordinates[2]
    

    with open(output_file, 'w') as f:

        f.write("Time (s), Node Label, Z Position (m), U1 Displacement (m)\n")

        for step in odb.steps.values():
            for frame in step.frames:
                time = frame.frameValue
                u_field = frame.fieldOutputs['U'].getSubset(region=target_set)

                for val in u_field.values:
                    n_label = val.nodeLabel
                    z_pos = float(odb.rootAssembly.instances['ROCK_INST'].nodes[n_label-1].coordinates[1])
                    # z_pos = node_coords[n_label]
                    u1 = float(val.data[0])

                    f.write(f"{time},{n_label},{z_pos},{u1}\n")

    odb.close()
    print(f">>> Success! complete curves exported to: {output_file}")


def ExportRockStressAllFrames(odb_path, output_file):

    odb = openOdb(path=odb_path)
    a = odb.rootAssembly
    set_name = 'FASEI_OPEN_WELL'

    if set_name not in a.nodeSets.keys():
        print("Error: The set was not found.")
        odb.close()
        return

    target_set = a.nodeSets[set_name]

    # instance_name = 'ROCK_INST' 

    node_coords = {}
    # nodes = a.instances[instance_name].nodes

    for node in target_set.nodes[0]:

        node_coords[node.label] = node.coordinates[1]
    

    with open(output_file, 'w') as f:

        f.write("Time (s), Node Label, Z Position (m), Mises (Pa), S11_Radial (Pa)\n")

        for step in odb.steps.values():
            # step = odb.steps[step]
            for frame in step.frames:
                time = frame.frameValue
                
                if 'S' not in frame.fieldOutputs.keys():
                    print(">>> Aviso: Tensão 'S' não encontrada no Step {} - Frame {}. (Disponíveis: {})".format(
                            step, frame.frameId, frame.fieldOutputs.keys()
                        ))
                    continue
                
                stress_field = frame.fieldOutputs['S'].getSubset(region=target_set, position=ELEMENT_NODAL)

                for val in stress_field.values:
                    n_label = val.nodeLabel
                    z_pos = node_coords[n_label]
                    mises = val.mises
                    s11 = float(val.data[0])

                    f.write("{},{},{},{},{}\n".format(time, n_label, z_pos, mises, s11))

    odb.close()
    print(f">>> Success! complete curves exported to: {output_file}")


def ExportCasingStressAllFrames(odb_path, output_file):

    odb = openOdb(path=odb_path)
    a = odb.rootAssembly

    instance_name = 'PIPE_INST'
    set_name = 'FASEI_REV_OD'

    try:
        inst = a.instances[instance_name]
        if set_name in inst.nodeSets.keys():
            target_set = inst.nodeSets[set_name]
            print(f">>> Success: Set '{set_name}' found at instance '{instance_name}'!")
            print(">>> Mapeando coordenadas da malha...")
            node_coords = {node.label: node.coordinates[1] for node in inst.nodes}
        else:
            print(f">>> Success: Set '{set_name}' don't exist at instance '{instance_name}'!")
            odb.close()
            return
    except:
        print(f">>> Error: Instance '{instance_name}' not found at ODB.")
        odb.close()
        return

    with open(output_file, 'w') as f:

        f.write("Time (s), Node Label, Z Position (m), Mises (Pa), S11_Radial (Pa)\n")

        print(">>> Extracting data from frames...")

        for step in odb.steps.keys():
            step = odb.steps[step]
            for frame in step.frames:
                time = frame.frameValue

                if 'S' not in frame.fieldOutputs.keys():
                    print(">>> Aviso: Tensão 'S' não encontrada no Step {} - Frame {}. (Disponíveis: {})".format(
                            step, frame.frameId, frame.fieldOutputs.keys()
                        ))
                    continue

                stress_field = frame.fieldOutputs['S'].getSubset(region=target_set, position=ELEMENT_NODAL)

                for val in stress_field.values:
                    n_label = val.nodeLabel
                    z_pos = node_coords[n_label]
                    mises = val.mises
                    s11 = float(val.data[0])

                    f.write("{},{},{},{},{}\n".format(time, n_label, z_pos, mises, s11))

    print(f">>> Success! complete curves exported to: {output_file}")

    odb.close()

def ExportCasingTemperatureAllFrames(odb_path, output_file):

    print("\n" + "="*50)
    print(">>> INICIANDO DIAGNOSTICO DE TEMPERATURA")
    
    if not os.path.exists(odb_path):
        print(">>> ERRO: Arquivo ODB nao encontrado em: %s" % odb_path)
        return

    odb = openOdb(path=odb_path)
    a = odb.rootAssembly
    instance_name = 'PIPE_INST'
    set_name = 'FASEI_REV_OD'

    # 1. Verificar Instancia e Set
    if instance_name not in a.instances.keys():
        print(">>> ERRO: Instancia %s nao existe. Disponiveis: %s" % (instance_name, a.instances.keys()))
        odb.close()
        return
    
    inst = a.instances[instance_name]
    
    if set_name not in inst.nodeSets.keys():
        print(">>> ERRO: Set %s nao existe na instancia. Disponiveis: %s" % (set_name, inst.nodeSets.keys()))
        odb.close()
        return
    
    target_set = inst.nodeSets[set_name]
    node_coords = {node.label: node.coordinates[1] for node in inst.nodes}

    # 2. Abrir arquivo e processar
    try:
        with open(output_file, 'w') as f:
            f.write("Time (s), Node Label, Z Position (m), NT (K)\n")
            
            # Pegar o primeiro frame para testar as chaves
            first_step = odb.steps.values()[0]
            first_frame = first_step.frames[0]
            print(">>> Variaveis disponiveis no ODB: %s" % first_frame.fieldOutputs.keys())

            # Definir a chave correta (tentando NT, TEMP ou PRESS)
            var_key = None
            for k in ['NT', 'NT11', 'TEMP']:
                if k in first_frame.fieldOutputs.keys():
                    var_key = k
                    break
            
            if not var_key:
                print(">>> ERRO: Nenhuma variavel de temperatura (NT, NT11, TEMP) encontrada!")
                odb.close()
                return
            
            print(">>> Extraindo variavel: %s" % var_key)

            for step in odb.steps.values():
                for frame in step.frames:
                    time = frame.frameValue
                    
                    # Subset da temperatura
                    temp_data = frame.fieldOutputs[var_key].getSubset(region=target_set)
                    
                    # Se o subset vier vazio, avisar
                    if not temp_data.values:
                        print(">>> Aviso: Subset vazio no Frame %d" % frame.frameId)
                        continue

                    for val in temp_data.values:
                        # Para NT (nodal), o dado pode estar em val.data ou val.data[0]
                        # Vamos garantir a leitura correta
                        t_val = val.data
                        if isinstance(t_val, (list, tuple)):
                            t_val = t_val[0]
                            
                        f.write("{},{},{},{}\n".format(time, val.nodeLabel, node_coords[val.nodeLabel], t_val))
        
        print(">>> SUCESSO! Arquivo gerado: %s" % output_file)
        
    except Exception as e:
        print(">>> ERRO DURANTE EXECUCAO: %s" % str(e))
    finally:
        odb.close()
    print("="*50 + "\n")


def ExportRockTemperatureAllFrames(odb_path, output_file):

    print("\n" + "="*50)
    print(">>> INICIANDO DIAGNOSTICO DE TEMPERATURA")
    
    if not os.path.exists(odb_path):
        print(">>> ERRO: Arquivo ODB nao encontrado em: %s" % odb_path)
        return

    odb = openOdb(path=odb_path)
    a = odb.rootAssembly
    # instance_name = 'PIPE_INST'
    set_name = 'FASEI_OPEN_WELL'
    
    target_set = a.nodeSets[set_name]

    node_coords = {}

    for node in target_set.nodes[0]:

        node_coords[node.label] = node.coordinates[1]

    # 2. Abrir arquivo e processar
    try:
        with open(output_file, 'w') as f:
            f.write("Time (s), Node Label, Z Position (m), NT (K)\n")
            
            # Pegar o primeiro frame para testar as chaves
            first_step = odb.steps.values()[0]
            first_frame = first_step.frames[0]
            print(">>> Variaveis disponiveis no ODB: %s" % first_frame.fieldOutputs.keys())

            # Definir a chave correta (tentando NT, TEMP ou PRESS)
            var_key = None
            for k in ['NT', 'NT11', 'TEMP']:
                if k in first_frame.fieldOutputs.keys():
                    var_key = k
                    break
            
            if not var_key:
                print(">>> ERRO: Nenhuma variavel de temperatura (NT, NT11, TEMP) encontrada!")
                odb.close()
                return
            
            print(">>> Extraindo variavel: %s" % var_key)

            for step in odb.steps.values():
                for frame in step.frames:
                    time = frame.frameValue
                    
                    # Subset da temperatura
                    temp_data = frame.fieldOutputs[var_key].getSubset(region=target_set)
                    
                    # Se o subset vier vazio, avisar
                    if not temp_data.values:
                        print(">>> Aviso: Subset vazio no Frame %d" % frame.frameId)
                        continue

                    for val in temp_data.values:
                        # Para NT (nodal), o dado pode estar em val.data ou val.data[0]
                        # Vamos garantir a leitura correta
                        t_val = val.data
                        if isinstance(t_val, (list, tuple)):
                            t_val = t_val[0]
                            
                        f.write("{},{},{},{}\n".format(time, val.nodeLabel, node_coords[val.nodeLabel], t_val))
        
        print(">>> SUCESSO! Arquivo gerado: %s" % output_file)
        
    except Exception as e:
        print(">>> ERRO DURANTE EXECUCAO: %s" % str(e))
    finally:
        odb.close()
    print("="*50 + "\n")


# Can be useful in the plane strain codes   
# def ExportDisplacementHistory(odb_path, node_label, instance_name, output_file):
#     odb = openOdb(path=odb_path)

#     data_list = []

#     for step_name in odb.steps.keys():
#         step = odb.steps[step_name]

#         for frame in step.frames:
#             time_value = frame.frameValue

#             u_field = frame.fieldOutputs['U']

#             sub_field = u_field.getSubset(
#                 region=odb.rootAssembly.instances[instance_name],           
#             )

#             for val in sub_field.values:
#                 if val.nodeLabel == node_label:
#                     u1_val = val.data[0]
#                     data_list.append((time_value, u1_val))
#                     break

#             # if sub_field.values:
#             #     u1_val = sub_field.values[0].data[0]
#             #     data_list.append((time_value, u1_val))

#     with open(output_file, 'w') as f:
#         f.write("Time (s), Displacement U1 (m)\n")
#         for time, u1 in data_list:
#             f.write(f"{time}, {u1}\n")

#     odb.close()
#     print(f">>> Exported data successfully to: {output_file}")


# Can be useful in the plane strain codes     
# def ExportPipeStressAtFixedPoint(odb_path, output_file):
    
#     odb = openOdb(path=odb_path)

#     target_set = odb.rootAssembly.nodeSets['SET_STRESS_MONITOR']

#     results = []  

#     for step in odb.steps.values():
#         for frame in step.frames:
#             time = frame.frameValue

#             stress_field = frame.fieldOutputs['S'].getSubset(
#                 region=target_set,
#                 position=ELEMENT_NODAL
#             )       
            
#             if stress_field.values:
            
#                 s11 = np.mean([v.data[0] for v in stress_field.values])

#                 mises = np.mean([v.mises for v in stress_field.values])

#                 results.append((time, s11, mises))

#     with open(output_file, 'w') as f:
#         f.write("Time (s), S11_Radial (Pa), Mises (Pa)\n")
#         for t, s, m in results:
#             f.write(f"{t}, {s}, {m}\n")

#     odb.close()
#     print(f">>> Exported data successfully to: {output_file}")