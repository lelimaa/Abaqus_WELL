from abaqus import mdb
from abaqusConstants import *
import numpy as np
from GEOMETRY_PS.geometry_PS import *

# def Create_Sets(self, modelName):
#     m = mdb.models[modelName]
#     p = m.parts[self.name]
#     f = p.faces
#     tol = 0.001
    
#     # ---------------------------------------------------------------------
#     # 1. SETS GERAIS (ALL e FASEI)
#     # ---------------------------------------------------------------------
#     all_faces = f[0:len(f)]
#     p.Set(faces=all_faces, name='FASEI_' + self.name.upper())

#     if self.name.upper() == 'FLUID':
#         p.Set(faces=all_faces, name='FASEI_' + self.name.upper())
#         p.Set(faces=all_faces, name='FASEI_ANNULAR')

#     # ---------------------------------------------------------------------
#     # 2. IDENTIFICAÇÃO DOS ARCOS (OD e ID) PARA A GEOMETRIA EM "U"
#     # ---------------------------------------------------------------------
#     if self.span == "half":
#         # Ângulos apontando para baixo (225º e 315º)
#         angles = (1.25*np.pi, 1.75*np.pi)
#     elif self.span == "quarter":
#         # Quarto de círculo inferior direito (270º a 360º)
#         angles = (1.75*np.pi,)
#     else:
#         angles = (1.25*np.pi, 1.75*np.pi)
        
#     od_edges = p.edges[:0]
#     id_edges = p.edges[:0]
        
#     for angle in angles:
#         xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
#                 self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
#                 0.0)
#         xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
#                 self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
#                 0.0)
#         od_edges += p.edges.findAt((xy1,))
#         id_edges += p.edges.findAt((xy2,))
        
#     p.Set(edges=od_edges, name='FASEI_' + self.name.upper() + '_OD')
#     p.Set(edges=id_edges, name='FASEI_' + self.name.upper() + '_ID')
        
#     if self.name.upper() == 'FLUID':
#         p.Set(faces=all_faces, name='FASEI_' + self.name.upper() + '_OD')
#         p.Set(faces=all_faces, name='FASEI_' + self.name.upper() + '_ID')
#         p.Set(faces=all_faces, name='FASEI_ANNULAR_OD')
#         p.Set(faces=all_faces, name='FASEI_ANNULAR_ID')

#     # ---------------------------------------------------------------------
#     # 3. IDENTIFICAÇÃO DOS TOPOS HORIONTAIS (MESH_TT e YSYM_TOP)
#     # ---------------------------------------------------------------------
#     # O "topo" do U são as linhas planas na cota y = -depth
#     y_top = self.geometry["center1"][1] 
        
#     top_edges = p.edges.getByBoundingBox(
#         xMin=-1e20, yMin=y_top - tol, zMin=-tol,
#         xMax=1e20,  yMax=y_top + tol, zMax=tol
#     )
#     if top_edges:
#         p.Set(edges=top_edges, name='FASEI_' + self.name.upper() + '_TT')

#     if self.name.upper() == 'FLUID':
#         p.Set(edges=od_edges, name='FASEI_' + self.name.upper() + '_OD')
#         p.Set(edges=id_edges, name='FASEI_' + self.name.upper() + '_ID')
#         p.Set(edges=od_edges, name='FASEI_ANNULAR_OD')
#         p.Set(edges=id_edges, name='FASEI_ANNULAR_ID')
#         p.Set(faces=all_faces, name='FASEI_ANNULAR_TT')

#     # ---------------------------------------------------------------------
#     # 4. IDENTIFICAÇÃO DE ARESTAS VERTICAIS (Apenas no modelo Quarter)
#     # ---------------------------------------------------------------------
#     if self.span == "quarter":
#         vertical_edges = p.edges[:0]
#         for edge in p.edges:
#             v1 = p.vertices[edge.getVertices()[0]]
#             v2 = p.vertices[edge.getVertices()[1]]
#             # Se X for igual, é uma linha perfeitamente vertical
#             if abs(v1.pointOn[0][0] - v2.pointOn[0][0]) < tol:
#                 vertical_edges += p.edges[edge.index:edge.index+1]
            
#         if vertical_edges:
#             p.Set(edges=vertical_edges, name='FASEI_VERTICAL_' + self.name.upper())

#     # ---------------------------------------------------------------------
#     # 5. SETS CONTEXTUAIS POR TIPO DE PEÇA (ROCK, FLUID, PIPE)
#     # ---------------------------------------------------------------------
#     if self.name.upper() == 'ROCK':
#         p.Set(edges=id_edges, name='FASEI_OPEN_WELL')
#         p.Set(edges=id_edges, name='FASEI_WELL')
#         p.Set(edges=od_edges, name='ROCK_BC')
#         p.Set(edges=od_edges, name='YSYM_BASE_ROCK') # A base da rocha é a curva mais externa
#         p.Set(faces=all_faces, name='ROCK_OUTPUT')
#         print(f"Sets específicos da ROCHA criados.")

#     elif self.name.upper() == 'FLUID':
#         p.Set(edges=od_edges, name='FASEI_OPEN_WELL')
#         print(f"Sets específicos do FLUIDO criados.")

#     elif self.name.upper() == 'PIPE':
#         p.Set(edges=id_edges, name='FASEI_COMPLETED_WELL')
#         print(f"Sets específicos do PIPE criados.")

#     # if self.name == 'FLUID':
#     #     m = mdb.models[modelName]
#     #     p = m.parts[self.name]
#     #     f = p.faces
#     #     e = p.edges

#     #     # FASEI_ANNULAR
#     #     all_faces = f
#     #     p.Set(faces=all_faces, name='FASEI_ANNULAR')
        
#     #     ########## FASEI_ANNULAR_OD e FASEI_ANNULAR_ID ###########################
#     #     if self.span == "half":
#     #         angles = (0.25*np.pi, 0.75*np.pi)
#     #     elif self.span == "quarter":
#     #         angles = (0.25*np.pi,)
#     #     else:
#     #         angles = (0.25*np.pi, 0.75*np.pi, 1.25*np.pi, 1.75*np.pi)
#     #     od_edges = p.edges[:0]
#     #     id_edges = p.edges[:0]
#     #     for angle in angles:
#     #         xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
#     #                self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
#     #                0.0)
#     #         xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
#     #                self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
#     #                0.0)
#     #         od_edges += p.edges.findAt((xy1,))
#     #         id_edges += p.edges.findAt((xy2,))
#     #     p.Set(edges = od_edges,name='FASEI_ANNULAR_OD')
#     #     p.Set(edges = id_edges,name='FASEI_ANNULAR_ID')

#     #     ##### FASEI_ANNULAR_TT ##################
#     #     tol = 0.001
#     #     all_coords = [v.pointOn[0][1] for v in p.vertices]
#     #     min_y_global = min(all_coords)
#     #     base_edges = p.edges.getByBoundingBox(
#     #         xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
#     #         xMax = 1e20, yMax=min_y_global + tol, zMax=tol
#     #     )
#     #     p.Set(edges=base_edges, name='FASEI_ANNULAR_TT')

def CreateSetsAssembly(self, modelName, span='half'):  
    m = mdb.models[modelName]    
    a = m.rootAssembly
    tol =0.001
    print("Instâncias disponíveis no Assembly:", a.instances.keys())
        
    # =========================================================
    # Set ALL    
    # =========================================================
    faces_totais = None
    for inst in a.instances.values():
        if faces_totais is None:
            faces_totais = inst.faces[:]
        else:
            faces_totais = faces_totais + inst.faces[:]
    if faces_totais:
        a.Set(faces=faces_totais, name='ALL')

    # =========================================================
    # FASEI = FLUIDO + PIPE
    # =========================================================
    # Substitua pelas chaves reais impressas no terminal (geralmente NomeDaPeca-1)
    nome_fluid = 'FLUID'
    nome_pipe  = 'PIPE'  
    nome_rock  = 'ROCK'
      
    inst_fluid = a.instances.get(nome_fluid)
    inst_pipe  = a.instances.get(nome_pipe)
    inst_rock  = a.instances.get(nome_rock)

    # Usando listas para agrupar as faces de forma mais robusta
    faces_combinadas = None # []
    
    if inst_fluid is not None:
        faces_combinadas.extend(inst_fluid.faces[:])
        
    if inst_pipe is not None:
        faces_combinadas.extend(inst_pipe.faces[:])

    # Criar o Set no Assembly APENAS se a lista não estiver vazia
    if faces_combinadas:
        a.Set(faces=faces_combinadas, name='FASEI')
        print("Set 'FASEI' combinado gerado com sucesso no Assembly!")
    else:
        print("Aviso: Nenhuma face encontrada para FLUID e PIPE. Set 'FASEI' ignorado nesta etapa.")

    # =========================================================
    # FASEI_OPEN_WELL + FASEI_WELL
    # =========================================================
    if self.span == "half":
        angles = (0.25*np.pi, 0.75*np.pi)
    elif self.span == "quarter":
        angles = (0.25*np.pi,)
    else:
        angles = (0.25*np.pi, 0.75*np.pi, 1.25*np.pi, 1.75*np.pi)
        
    od_edges = None # a.edges[:0]
    id_edges = None # a.edges[:0]
    
    for angle in angles:
        xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
                self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
                0.0)
        xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
                self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
                0.0)
        
        # Bloco de proteção para evitar os Warnings do findAt
        try:
            encontrado_od = a.edges.findAt((xy1,))
            if encontrado_od: od_edges += encontrado_od
        except:
            pass # Silencia o erro se não achar nada
            
        try:
            encontrado_id = a.edges.findAt((xy2,))
            if encontrado_id: id_edges += encontrado_id
        except:
            pass # Silencia o erro se não achar nada

    if inst_fluid in a.instances.values() and od_edges is not None:
        a.Set(edges=od_edges, name='FASEI_OPEN_WELL')
    if inst_rock in a.instances.values() and id_edges is not None:
        a.Set(edges = id_edges, name='FASEI_WELL') # if only from ROCK      

    # =========================================================
    # FASEI_COMPLETED_WELL
    # =========================================================
    if inst_pipe in a.instances.values() and id_edges is not None:
        a.Set(edges = id_edges,name='FASEI_COMPLETED_WELL') # if only from PIPE  
    
    # =========================================================
    # ROCK_BC
    # =========================================================
    if inst_rock in a.instances.values() and od_edges is not None:
        a.Set(edges=od_edges, name='ROCK_BC')
    
    # =========================================================
    # ROCK_OUTPUT
    # ========================================================= 
    faces_totais_rock = None

    if inst_rock is not None:
        faces_totais_rock = inst_rock.faces[:]
            
    if faces_totais_rock:
        a.Set(faces=faces_totais_rock, name='ROCK_OUTPUT')
        print("Set 'ROCK_OUTPUT' criado com todas as faces dessa instancia.")

    # =========================================================
    # YSYM_BASE
    # =========================================================
    # 1. Identificar a altura mínima (Y) global do modelo
    y_global = []
    for inst in a.instances.values():
        # ESTA É A LINHA QUE EVITA O CRASH (ValueError)
        if len(inst.vertices) > 0: 
            y_global.append(min([v.pointOn[0][1] for v in inst.vertices]))
    
    # Só prossegue com o cálculo da base se a lista y_global não estiver vazia
    if y_global:
        y_base = min(y_global)

        # 2. Criar uma lista para acumular as arestas da base de cada instância
        edges_base_lista = None

        for inst in a.instances.values():
            if len(inst.vertices) > 0:
                x_min_i = min([v.pointOn[0][0] for v in inst.vertices])
                x_max_i = max([v.pointOn[0][0] for v in inst.vertices])
                
                edges_inst = inst.edges.getByBoundingBox(
                    xMin=x_min_i - tol, yMin=y_base - tol, zMin=-tol,
                    xMax=x_max_i + tol, yMax=y_base + tol, zMax=tol
                )
                
                if edges_inst:
                    if edges_base_lista is None:
                        edges_base_lista = edges_inst
                    else:
                        edges_base_lista = edges_base_lista + edges_inst

        # 3. Criar o Set no Assembly com o acumulado
        if edges_base_lista:
            a.Set(edges=edges_base_lista, name='YSYM_BASE')
            print("Set 'YSYM_BASE' criado com sucesso unindo todas as instâncias.")
        else:
            print("Aviso: Nenhuma aresta encontrada na cota Y =", y_base)
            
    else:
        print("Aviso: Não foi possível determinar a base (y_base). O Assembly está vazio ou as instâncias não possuem vértices.")

# def CreateSetsAssembly(self, modelName):  
#     m = mdb.models[modelName]  
#     a = m.rootAssembly
#     nome_peca = self.name.upper()
#     tol =0.001
    
#     # =========================================================
#     # SET ALL
#     # =========================================================    
#     faces_totais = None
#     for inst in a.instances.values():
#         if faces_totais is None:
#             faces_totais = inst.faces[:]
#         else:
#             faces_totais = faces_totais + inst.faces[:]
#         a.Set(faces=faces_totais, name='ALL')

#     # =========================================================
#     # FASEI = FLUIDO + PIPE
#     # =========================================================
#     if nomes_instancias is not a.instances[nome_peca + '_INST']:
#         nomes_instancias = nome_peca + '_INST'
#         print(nomes_instancias)
#     faces_totais = None

#     # 1. Certifique-se de usar o nome exato das instâncias.
#     for nome in nomes_instancias:
#         if nome == 'FLUID_INST' or nome == 'PIPE_INST':
#             inst = a.instances[nome]
#             if faces_totais is None:
#                 faces_totais = inst.faces[:]
#             else:
#                 faces_totais = faces_totais + inst.faces[:]

#     # 2. Pegue todas as faces de cada instância
#     ######### O [:] garante que estamos pegando a sequência de faces (Array de geometria)
#     # faces_fluid = inst_fluid.faces[:]
#     # faces_pipe  = inst_pipe.faces[:]
#     # faces_rock = inst_rock.faces[:]
    
#     # # 3. Some as sequências (O Abaqus entende isso como uma união de geometrias)
#     # faces_combinadas = faces_fluid + faces_pipe
#     # 4. Crie o Set no nível da Montagem (Assembly)
#     if faces_totais:
#         a.Set(faces=faces_totais, name='FASEI')
#         print("Set 'FASEI' combinado gerado com sucesso no Assembly!")
#     else:
#         print("Aviso: Nenhuma face encontrada para FLUID e PIPE. Set 'FASEI' ignorado nesta etapa.")

    
#     # =========================================================
#     # FASEI_OPEN_WELL + FASEI_WELL
#     # =========================================================
#     if self.span == "half":
#         angles = (0.25*np.pi, 0.75*np.pi)
#     elif self.span == "quarter":
#         angles = (0.25*np.pi,)
#     else:
#         angles = (0.25*np.pi, 0.75*np.pi, 1.25*np.pi, 1.75*np.pi)
    
#     od_edges = a.edges[:0]
#     id_edges = a.edges[:0]
    
#     for angle in angles:
#         xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
#                 self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
#                 0.0)
#         xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
#                 self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
#                 0.0)
#         od_edges += a.edges.findAt((xy1,))
#         id_edges += a.edges.findAt((xy2,))
    
#     if nome_peca == 'FLUID_INST':
#         a.Set(edges=od_edges, name='FASEI_OPEN_WELL')
#     if nome_peca == 'ROCK_INST':
#         a.Set(edges = id_edges,name='FASEI_WELL') # if only from ROCK      
    
#     # ========================================================
#     # FASEI_COMPLETED_WELL
#     # ======================================================== 
#     if nome_peca == 'PIPE_INST':
#         a.Set(edges = id_edges,name='FASEI_WELL') # if only from ROCK
#         a.Set(edges = id_edges,name='FASEI_COMPLETED_WELL') # if only from PIPE  

#     # ========================================================
#     # ROCK_BC
#     # ========================================================
#     if nome_peca == 'ROCK_INST' and od_edges:
#         a.Set(edges=od_edges, name='ROCK_BC')
    
#     # ========================================================
#     # ROCK_OUTPUT
#     # ========================================================
#     nome_instancia = ['ROCK_INST']
#     faces_totais = None

#     for nome in nome_instancia:
#         if nome in a.instances.keys():
#             inst = a.instances[nome]
#             if faces_totais is None:
#                 faces_totais = inst.faces[:]
#             else:
#                 faces_totais = faces_totais + inst.faces[:]

#     if faces_totais:
#         a.Set(faces=faces_totais, name='ROCK_OUTPUT')
#         print("Set 'ROCK_OUTPUT' criado com todas as faces dessa instancia.")

#     # ========================================================
#     # YSYM_BASE
#     # ========================================================
#     # 1. Identificar a altura mínima (Y) global do modelo
#     # Procuramos em todas as instâncias para achar o "chão"
#     y_global = []
#     for inst in a.instances.values():
#         y_global.append(min([v.pointOn[0][1] for v in inst.vertices]))
#     y_base = min(y_global)

#     # 2. Criar uma lista para acumular as arestas da base de cada instância
#     edges_base_lista = None

#     for inst in a.instances.values():
#         # Buscamos as arestas horizontais desta instância específica que estão na cota y_base
#         # Limitamos o X aos limites da própria instância para ser preciso
#         x_min_i = min([v.pointOn[0][0] for v in inst.vertices])
#         x_max_i = max([v.pointOn[0][0] for v in inst.vertices])
        
#         edges_inst = inst.edges.getByBoundingBox(
#             xMin=x_min_i - tol, yMin=y_base - tol, zMin=-tol,
#             xMax=x_max_i + tol, yMax=y_base + tol, zMax=tol
#         )
        
#         # Se encontrou arestas na base desta instância, adiciona à "bolsa"
#         if edges_inst:
#             if edges_base_lista is None:
#                 edges_base_lista = edges_inst
#             else:
#                 edges_base_lista = edges_base_lista + edges_inst

#     # 3. Criar o Set no Assembly com o acumulado
#     if edges_base_lista:
#         a.Set(edges=edges_base_lista, name='YSYM_BASE')
#         print("Set 'YSYM_BASE' criado com sucesso unindo todas as instâncias.")
#     else:
#         print("Erro: Nenhuma aresta encontrada na cota Y =", y_base)
    
def CreateSurfacesAssembly(self, modelName, data):
    m = mdb.models[modelName]
    p = m.parts[self.name]
    
    # Inicializa as sequências de arestas (edges) vazias
    od_edges = p.edges[:0]
    id_edges = p.edges[:0]
    side_edges = p.edges[:0] # Arestas retas nas extremidades do arco

    # Define os ângulos para buscar as arestas curvas e retas
    if self.span == "half":
        angles = (0.25 * np.pi, 0.75 * np.pi) # 45º e 135º para garantir o clique nas curvas
        side_angles = (0.0, np.pi)            # 0º e 180º para as faces retas conectando os arcos
    elif self.span == "quarter":
        angles = (0.25 * np.pi,)
        side_angles = (0.0, 0.5 * np.pi)
    else: # Geometria completa (full)
        angles = (0.25 * np.pi, 0.75 * np.pi, 1.25 * np.pi, 1.75 * np.pi)
        side_angles = () # Círculo completo não tem arestas retas laterais
        
    # 1. Encontrar arestas Curvas: Diâmetro Externo (OD) e Interno (ID)
    for angle in angles:
        xy_od = (self.geometry["Ro1"] * np.cos(angle) + self.geometry["center1"][0],
                 self.geometry["Ro1"] * np.sin(angle) + self.geometry["center1"][1],
                 0.0)
                 
        xy_id = (self.geometry["Ri1"] * np.cos(angle) + self.geometry["center2"][0],
                 self.geometry["Ri1"] * np.sin(angle) + self.geometry["center2"][1],
                 0.0)
        
        try:
            encontrado_od = p.edges.findAt((xy_od,))
            if encontrado_od: od_edges += encontrado_od
        except:
            pass # Silencia erro se a coordenada cair fora da aresta
            
        try:
            encontrado_id = p.edges.findAt((xy_id,))
            if encontrado_id: id_edges += encontrado_id
        except:
            pass

    # 2. Encontrar arestas Retas (laterais conectando o ID ao OD)
    for s_angle in side_angles:
        r_mid = (self.geometry["Ro1"] + self.geometry["Ri1"]) / 2.0 # Raio médio
        xy_side = (r_mid * np.cos(s_angle) + self.geometry["center1"][0],
                   r_mid * np.sin(s_angle) + self.geometry["center1"][1],
                   0.0)
        try:
            encontrado_side = p.edges.findAt((xy_side,))
            if encontrado_side: side_edges += encontrado_side
        except:
            pass

    # 3. Criação das Surfaces baseada no nome da Part (Ex: FLUID)
    if self.name.upper() == 'FLUID':
        
        # FASEI_FLUIDO: Geralmente representa apenas as interfaces de contato (ID e OD)
        edges_fluido = od_edges + id_edges
        if len(edges_fluido) > 0:
            p.Surface(edges=edges_fluido, name='FASEI_FLUIDO')
            print("Surface 'FASEI_FLUIDO' criada em %s com %d arestas." % (self.name, len(edges_fluido)))

        # FASEI_ANNULAR: Contorno fechado completo (ID + OD + Laterais retas)
        all_edges = od_edges + id_edges + side_edges
        if len(all_edges) > 0:
            p.Surface(edges=all_edges, name='FASEI_ANNULAR')
            print("Surface 'FASEI_ANNULAR' criada em %s com %d arestas." % (self.name, len(all_edges)))

    # Você pode adicionar blocos `elif self.name.upper() == 'PIPE':` 
    # e `elif self.name.upper() == 'ROCK':` para criar as respectivas
    # surfaces para as outras parts usando a mesma lógica do findAt.
    