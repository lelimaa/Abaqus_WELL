from abaqus import mdb
from abaqusConstants import *

def CreateSetsPipe(name_model):
    m = mdb.models[name_model]
    p = m.parts['PIPE']
    f = p.faces
    e = p.edges

    # FASEI_REV, FASEI_REV_ABOVE_TOC
    all_faces = f[0:len(f)]
    p.Set(faces=all_faces, name='FASEI_REV')
    p.Set(faces=all_faces, name='FASEI_REV_ABOVE_TOC')


    # FASEI_REV_BASE)    
    tol = 0.001
    e = p.edges
    all_coords = [v.pointOn[0][1] for v in p.vertices]
    min_y_global = min(all_coords)
    base_edges = e.getByBoundingBox(
        xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
        xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    )
    p.Set(edges=base_edges, name='FASEI_REV_BASE')

    # FASEI_REV_ID
    all_x_coords = [v.pointOn[0][0] for v in p.vertices]
    min_x_global = min(all_x_coords)
    left_edges = e.getByBoundingBox(
        xMin=min_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=min_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=left_edges, name='FASEI_REV_ID')


    # FASEI_REV_OD
    max_x_global = max([v.pointOn[0][0] for v in p.vertices])
    right_edges = e.getByBoundingBox(
        xMin=max_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=max_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=right_edges, name='FASEI_REV_OD')


    # FASEI_REV_TOP
    all_y = [v.pointOn[0][1] for v in p.vertices]
    max_y_global = max(all_y)

    top_edges = e.getByBoundingBox(
        xMin=-1e20, yMin=max_y_global - tol, zMin=-tol,
        xMax=1e20, yMax=max_y_global + tol, zMax=tol
    )
    p.Set(edges=top_edges, name='FASEI_REV_TOP')

    # FASEI_REV_TT
    horizontal_edges = []
    tol = 0.0001

    for edge in p.edges:
        v1_idx = edge.getVertices()[0]
        v2_idx = edge.getVertices()[1]
        y1 = p.vertices[v1_idx].pointOn[0][1]
        y2 = p.vertices[v2_idx].pointOn[0][1]

        if abs(y1 - y2) < tol:
            horizontal_edges.append(p.edges[edge.index:edge.index + 1])

    if horizontal_edges:
        all_horizontals = horizontal_edges[0]
        for i in range(1, len(horizontal_edges)):
            all_horizontals += horizontal_edges[i]
        p.Set(edges=all_horizontals, name='FASEI_REV_TT')
    
def CreateSetsFluid(name_model):
    m = mdb.models[name_model]
    p = m.parts['FLUID']
    f = p.faces
    e = p.edges

    # ALL FACES
    all_faces = f[0:len(f)]
    p.Set(faces=all_faces, name='FASEI_FLUIDO')

    # FASEI_FLUIDO_BASE
    tol = 0.001
    e = p.edges
    all_coords = [v.pointOn[0][1] for v in p.vertices]
    min_y_global = min(all_coords)
    base_edges = e.getByBoundingBox(
        xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
        xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    )
    p.Set(edges=base_edges, name='FASEI_FLUIDO_BASE')

    # FASEI_FLUIDO_ID
    all_x_coords = [v.pointOn[0][0] for v in p.vertices]
    min_x_global = min(all_x_coords)
    left_edges = e.getByBoundingBox(
        xMin=min_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=min_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=left_edges, name='FASEI_FLUIDO_ID')


    # FASEI_FLUIDO_OD
    max_x_global = max([v.pointOn[0][0] for v in p.vertices])
    right_edges = e.getByBoundingBox(
        xMin=max_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=max_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=right_edges, name='FASEI_FLUIDO_OD')

    # FASEI_FLUIDO_TOP
    all_y = [v.pointOn[0][1] for v in p.vertices]
    max_y_global = max(all_y)

    top_edges = e.getByBoundingBox(
        xMin=-1e20, yMin=max_y_global - tol, zMin=-tol,
        xMax=1e20, yMax=max_y_global + tol, zMax=tol
    )
    p.Set(edges=top_edges, name='FASEI_FLUIDO_TOP')

    # FASEI_ANNULAR
    all_faces = f
    p.Set(faces=all_faces, name='FASEI_ANNULAR')

    # FASEI_ANNULAR_BASE
    tol = 0.001
    e = p.edges
    all_coords = [v.pointOn[0][1] for v in p.vertices]
    min_y_global = min(all_coords)
    base_edges = e.getByBoundingBox(
        xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
        xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    )
    p.Set(edges=base_edges, name='FASEI_ANNULAR_BASE')

    # FASEI_ANNULAR_ID
    all_x_coords = [v.pointOn[0][0] for v in p.vertices]
    min_x_global = min(all_x_coords)
    left_edges = e.getByBoundingBox(
        xMin=min_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=min_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=left_edges, name='FASEI_ANNULAR_ID')

    # FASEI_ANNULAR_OD
    max_x_global = max([v.pointOn[0][0] for v in p.vertices])
    right_edges = e.getByBoundingBox(
        xMin=max_x_global - tol, yMin=-1e20, zMin=-tol,
        xMax=max_x_global + tol, yMax=1e20, zMax=tol
    )
    p.Set(edges=right_edges, name='FASEI_ANNULAR_OD')

    # FASEI_ANNULAR_TOP
    all_y = [v.pointOn[0][1] for v in p.vertices]
    max_y_global = max(all_y)

    top_edges = e.getByBoundingBox(
        xMin=-1e20, yMin=max_y_global - tol, zMin=-tol,
        xMax=1e20, yMax=max_y_global + tol, zMax=tol
    )
    p.Set(edges=top_edges, name='FASEI_ANNULAR_TOP')


    # FASEI_ANNULAR_TT
    horizontal_edges = []
    tol = 0.0001

    for edge in p.edges:
        v1_idx = edge.getVertices()[0]
        v2_idx = edge.getVertices()[1]
        y1 = p.vertices[v1_idx].pointOn[0][1]
        y2 = p.vertices[v2_idx].pointOn[0][1]

        if abs(y1 - y2) < tol:
            horizontal_edges.append(p.edges[edge.index:edge.index + 1])

    if horizontal_edges:
        all_horizontals = horizontal_edges[0]
        for i in range(1, len(horizontal_edges)):
            all_horizontals += horizontal_edges[i]
        p.Set(edges=all_horizontals, name='FASEI_ANNULAR_TT')

def CreateSetsRock(name_model):
    m = mdb.models[name_model]
    p = m.parts['ROCK']
    e = p.edges
    f = p.faces
    v = p.vertices
    tol = 0.001

    # ALLROCK and FASEI_SLAVE (all faces of the rock part, to be used in the contact definition as slave surface)
    all_faces = f[0:len(f)]
    p.Set(faces=all_faces, name='ALLROCK')
    p.Set(faces=all_faces, name='FASEI_SLAVE')

    # L1-I_BASE, L2-I_BASE, L3-I_BASE, ... , LN-I_BASE
    todas_as_alturas = sorted(list(set([vert.pointOn[0][1] for vert in v])))
    alturas_invertidas = sorted(todas_as_alturas, reverse=True)
    interfaces_descendo = alturas_invertidas[1:]

    for i, altura_y in enumerate(interfaces_descendo):
        nome_set = 'L' + str(i+1) + '-I_BASE'

        edges_interface = e.getByBoundingBox(
            xMin=-1e20, yMin=altura_y - tol, zMin=-tol,
            xMax=1e20, yMax=altura_y + tol, zMax=tol
        )

        if edges_interface:
            p.Set(edges=edges_interface, name=nome_set)
            print(f"Set '{nome_set}' gerado automaticamente em Y = {altura_y}")


    # L1-I_ID, L2-I_ID, L3-I_ID, ... , LN-I_ID
    alturas = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)
    min_x = min([vert.pointOn[0][0] for vert in v])

    for i in range(len(alturas) - 1):
        y_topo = alturas[i]
        y_base = alturas[i+1]

        y_meio = (y_topo + y_base) / 2.0

        nome_set = 'L' + str(i+1) + '-I_ID'

        edge_encontrada = e.findAt(((min_x, y_meio, 0.0), ))

        if edge_encontrada:
            p.Set(edges=edge_encontrada, name=nome_set)
            print(f"Set '{nome_set}' created with sucess in the medium point Y={y_meio}")


    # L1-I_OD, L2-I_OD, L3-I_OD, ... , LN-I_OD
    alturas = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)
    max_x = max([vert.pointOn[0][0] for vert in v])

    for i in range(len(alturas)-1):
        y_topo = alturas[i]
        y_base = alturas[i+1]

        y_meio = (y_topo+y_base) / 2.0

        nome_set = 'L' + str(i+1) + '-I_OD'

        edge_encontrada = e.findAt(((max_x, y_meio, 0.0), ))

        if edge_encontrada:
            p.Set(edges=edge_encontrada, name=nome_set)
            print(f"Set '{nome_set}' criado com sucesso em X={max_x}, Y={y_meio}")

    # L1-I_TOP, L2-I_TOP, L3-I_TOP, ... , LN-I_TOP
    alturas = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)

    for i in range(len(alturas) - 1):
        altura_topo_camada = alturas[i]
        nome_set = 'L' +str(i+1)+ '-I_TOP'

        edges_topo = e.getByBoundingBox(
            xMin=-1e20, yMin=altura_topo_camada - tol, zMin=-tol,
            xMax=1e20, yMax=altura_topo_camada + tol, zMax=tol
        )

        if edges_topo:
            p.Set(edges=edges_topo, name=nome_set)
            print(f"Set '{nome_set}' criado na altura Y = {altura_topo_camada}")

    # L1-I, L2-I, L3-I, ... , LN-I
    alturas = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)

    min_x = min([vert.pointOn[0][0] for vert in v])
    max_x = max([vert.pointOn[0][0] for vert in v])
    x_meio_face = (min_x + max_x) / 2.0

    for i in range(len(alturas)-1):
        y_topo = alturas[i]
        y_base = alturas[i+1]

        y_meio_camada = (y_topo + y_base) / 2.0

        nome_set = 'L' + str(i+1) + '-I'

        ponto_busca = ((x_meio_face, y_meio_camada, 0.0), )

        face_encontrada = f.findAt(ponto_busca)

        if face_encontrada:
            p.Set(faces=face_encontrada, name=nome_set)
            print(f"Set de Face '{nome_set}' criado em X={x_meio_face}, Y={y_meio_camada}")

def CreateSetsAssembly(name_model):  

    m = mdb.models[name_model]  
    a = m.rootAssembly
    
    # ALL    
    faces_totais = None

    for inst in a.instances.values():
        if faces_totais is None:
            faces_totais = inst.faces[:]
        else:
            faces_totais = faces_totais + inst.faces[:]

    a.Set(faces=faces_totais, name='ALL')

    # FASEI
    nomes_instancias = ['FLUID_INST', 'PIPE_INST']
    faces_totais = None

    for nome in nomes_instancias:
        if nome in a.instances.keys():
            inst = a.instances[nome]
            if faces_totais is None:
                faces_totais = inst.faces[:]
            else:
                faces_totais = faces_totais + inst.faces[:]

    if faces_totais:
        a.Set(faces=faces_totais, name='FASEI')
        print("Set 'ALL' criado com todas as faces das 2 instancias.")

    # FASEI_OPEN_WELL
    tol =0.001

    inst_f = a.instances['FLUID_INST']
    x_interface = max([v.pointOn[0][0] for v in inst_f.vertices])

    y_min = min([v.pointOn[0][1] for v in inst_f.vertices])
    y_max = max([v.pointOn[0][1] for v in inst_f.vertices])

    edges_f = inst_f.edges.getByBoundingBox(
        xMin=x_interface - tol, yMin=y_min - tol, zMin=-tol,
        xMax=x_interface + tol, yMax=y_max + tol, zMax=tol
    )

    inst_r = a.instances['ROCK_INST']
    edges_r = inst_r.edges.getByBoundingBox(
        xMin=x_interface - tol, yMin=y_min - tol, zMin=-tol,
        xMax=x_interface + tol, yMax=y_max + tol, zMax=tol
    )

    edges_total = edges_f+edges_r

    # a.Set(edges=edges_f, name='FASEI_OPEN_WELL') # if only from fluid
    a.Set(edges=edges_r, name='FASEI_OPEN_WELL') # if only from rock
    # a.Set(edges=edges_total, name='FASEI_OPEN_WELL') # if from fluid and rock
    print(f"Set FASEI_OPEN_WELL criado na interface X = {x_interface}")  

    a.Set(edges=edges_r, name='FASEI_WELL') # if only from rock
    print(f"Set FASEI_WELL criado na interface X = {x_interface}")  


    # FASEI_COMPLETED_WELL
    inst_p = a.instances['PIPE_INST']
    x_int_pipe = min([v.pointOn[0][0] for v in inst_p.vertices])

    y_min_p = min([v.pointOn[0][1] for v in inst_p.vertices])
    y_max_p = max([v.pointOn[0][1] for v in inst_p.vertices])

    edges_completed = inst_p.edges.getByBoundingBox(
        xMin=x_int_pipe - tol, yMin=y_min_p - tol, zMin=-tol,
        xMax=x_int_pipe + tol, yMax=y_max_p + tol, zMax=tol
    )

    if edges_completed:
        a.Set(edges=edges_completed, name='FASEI_COMPLETED_WELL')
        print(f"Set 'FASEI_COMPLETED_WELL' criado na face interna do Pipe (X = {x_int_pipe})")


    # MESH_TT_PIPES
    inst_p = a.instances['PIPE_INST']
    alturas_pipe = sorted(list(set([v.pointOn[0][1] for v in inst_p.vertices])))

    min_x_p = min([v.pointOn[0][0] for v in inst_p.vertices])
    max_x_p = max([v.pointOn[0][0] for v in inst_p.vertices])

    edges_tt = None

    for y in alturas_pipe:
        edges_camada = inst_p.edges.getByBoundingBox(
            xMin=min_x_p - tol, yMin=y - tol, zMin=-tol,
            xMax=max_x_p + tol, yMax=y + tol, zMax=tol
        )

        if edges_camada:
            if edges_tt is None:
                edges_tt = edges_camada
            else:
                edges_tt = edges_tt + edges_camada

    if edges_tt:
        a.Set(edges=edges_tt, name='MESH_TT_PIPES')
        print(f"Set 'MESH_TT_PIPES' criado com {len(edges_tt)} arestas horizontais.")

    # MESH_TT_PIPES
    inst_f = a.instances['FLUID_INST']
    alturas_annular = sorted(list(set([v.pointOn[0][1] for v in inst_f.vertices])))

    min_x_a = min([v.pointOn[0][0] for v in inst_f.vertices])
    max_x_a = max([v.pointOn[0][0] for v in inst_f.vertices])

    edges_tt = None

    for y in alturas_annular:
        edges_camada = inst_f.edges.getByBoundingBox(
            xMin=min_x_a - tol, yMin=y - tol, zMin=-tol,
            xMax=max_x_a + tol, yMax=y + tol, zMax=tol
        )

        if edges_camada:
            if edges_tt is None:
                edges_tt = edges_camada
            else:
                edges_tt = edges_tt + edges_camada

    if edges_tt:
        a.Set(edges=edges_tt, name='MESH_TT_ANNULARS')
        print(f"Set 'MESH_TT_ANNULARS' criado com {len(edges_tt)} arestas horizontais.")  


    # MESH_TT_ROCK
    inst_r = a.instances['ROCK_INST']
    alturas_rock = sorted(list(set([v.pointOn[0][1] for v in inst_r.vertices])))

    min_x_r = min([v.pointOn[0][0] for v in inst_r.vertices])
    max_x_r = max([v.pointOn[0][0] for v in inst_r.vertices])

    edges_tt = None

    for y in alturas_rock:
        edges_camada = inst_r.edges.getByBoundingBox(
            xMin=min_x_r - tol, yMin=y - tol, zMin=-tol,
            xMax=max_x_r + tol, yMax=y + tol, zMax=tol
        )

        if edges_camada:
            if edges_tt is None:
                edges_tt = edges_camada
            else:
                edges_tt = edges_tt + edges_camada

    if edges_tt:
        a.Set(edges=edges_tt, name='MESH_TT_ROCK')
        print(f"Set 'MESH_TT_ROCK' criado com {len(edges_tt)} arestas horizontais.")           


    # MESH_VERTICAL
    instancias = ['FLUID_INST', 'PIPE_INST', 'ROCK_INST']
    edges_verticais_total = None

    for nome in instancias:
        if nome in a.instances.keys():
            inst = a.instances[nome]
            edges_da_instancia = inst.edges

            indices_verticais = []

            for i, edge in enumerate(edges_da_instancia):
                v1 = inst.vertices[edge.getVertices()[0]]
                v2 = inst.vertices[edge.getVertices()[1]]

                if abs(v1.pointOn[0][0] - v2.pointOn[0][0]) < tol:
                    indices_verticais.append(edge)

            if indices_verticais:
                temp_seq = inst.edges[0:0]
                for ed in indices_verticais:
                    temp_seq = temp_seq + inst.edges[ed.index:ed.index+1]

                if edges_verticais_total is None:
                    edges_verticais_total = temp_seq
                else:
                    edges_verticais_total = edges_verticais_total + temp_seq

    if edges_verticais_total:
        a.Set(edges=edges_verticais_total, name='MESH_VERTICAL')
        print("Set 'MESH_VERTICAL' criado com sucesso (todas as verticais).")

    # ROCK_BC
    inst_r = a.instances['ROCK_INST']
    x_externo_rock = max([v.pointOn[0][0] for v in inst_r.vertices])

    y_min = min([v.pointOn[0][1] for v in inst_r.vertices])
    y_max = max([v.pointOn[0][1] for v in inst_r.vertices])

    edges_bc = inst_r.edges.getByBoundingBox(
        xMin=x_externo_rock - tol, yMin=y_min - tol, zMin=-tol,
        xMax=x_externo_rock + tol, yMax=y_max + tol, zMax=tol
    )

    if edges_bc:
        a.Set(edges=edges_bc, name='ROCK_BC')
        print(f"Set 'ROCK_BC' criado com sucesso na borda X = {x_externo_rock}")

    # ROCK_OUTPUT
    nome_instancia = ['ROCK_INST']
    faces_totais = None

    for nome in nome_instancia:
        if nome in a.instances.keys():
            inst = a.instances[nome]
            if faces_totais is None:
                faces_totais = inst.faces[:]
            else:
                faces_totais = faces_totais + inst.faces[:]

    if faces_totais:
        a.Set(faces=faces_totais, name='ROCK_OUTPUT')
        print("Set 'ROCK_OUTPUT' criado com todas as faces dessa instancia.")


    # YSYM_BASE
    # 1. Identificar a altura mínima (Y) global do modelo
    # Procuramos em todas as instâncias para achar o "chão"
    y_global = []
    for inst in a.instances.values():
        y_global.append(min([v.pointOn[0][1] for v in inst.vertices]))
    y_base = min(y_global)

    # 2. Criar uma lista para acumular as arestas da base de cada instância
    edges_base_lista = None

    for inst in a.instances.values():
        # Buscamos as arestas horizontais desta instância específica que estão na cota y_base
        # Limitamos o X aos limites da própria instância para ser preciso
        x_min_i = min([v.pointOn[0][0] for v in inst.vertices])
        x_max_i = max([v.pointOn[0][0] for v in inst.vertices])
        
        edges_inst = inst.edges.getByBoundingBox(
            xMin=x_min_i - tol, yMin=y_base - tol, zMin=-tol,
            xMax=x_max_i + tol, yMax=y_base + tol, zMax=tol
        )
        
        # Se encontrou arestas na base desta instância, adiciona à "bolsa"
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
        print("Erro: Nenhuma aresta encontrada na cota Y =", y_base)



    # YSYM_TOP
    # 1. Identificar a altura MÁXIMA (Y) global do modelo
    y_global_topo = []
    for inst in a.instances.values():
        y_global_topo.append(max([v.pointOn[0][1] for v in inst.vertices]))
    y_topo = max(y_global_topo)

    # 2. Criar uma lista para acumular as arestas do topo de cada instância
    edges_topo_lista = None

    for inst in a.instances.values():
        # Buscamos as arestas horizontais desta instância que estão na cota y_topo
        x_min_i = min([v.pointOn[0][0] for v in inst.vertices])
        x_max_i = max([v.pointOn[0][0] for v in inst.vertices])
        
        edges_inst = inst.edges.getByBoundingBox(
            xMin=x_min_i - tol, yMin=y_topo - tol, zMin=-tol,
            xMax=x_max_i + tol, yMax=y_topo + tol, zMax=tol
        )
        
        # Se encontrou arestas no topo desta instância, adiciona à sequência
        if edges_inst:
            if edges_topo_lista is None:
                edges_topo_lista = edges_inst
            else:
                edges_topo_lista = edges_topo_lista + edges_inst

    # 3. Criar o Set no Assembly
    if edges_topo_lista:
        a.Set(edges=edges_topo_lista, name='YSYM_TOP')
        print(f"Set 'YSYM_TOP' criado com sucesso na altura Y = {y_topo}")
    else:
        print("Erro: Nenhuma aresta encontrada no topo (Y =", y_topo, ")")

def CreateSurfacesAssembly(modelName, data):

    m = mdb.models[modelName]
    a = m.rootAssembly

    top_depth = -data["FLUID"]["top_depth"]
    base_depth = -data["FLUID"]["base_depth"]
    inner_radius_fluid = data["FLUID"]["inner_radius"]
    outer_radius_fluid = data["FLUID"]["inner_radius"] + data["FLUID"]["thickness"]
    inner_radius_pipe = data["PIPE"]["inner_radius"]
    outer_radius_pipe = data["PIPE"]["inner_radius"] + data["PIPE"]["thickness"]
    inner_radius_rock = data["ROCK"]["inner_radius"]
    outer_radius_rock = data["ROCK"]["inner_radius"] + data["ROCK"]["thickness"]

    # SUPERFICIE DE INTERFACE
    tol = 0.001

    y_min = min(top_depth, base_depth)
    y_max = max(top_depth, base_depth)

    # Creating the annular surface using edges from the fluid and rock instances at the interface
    # FASEI_ANNULAR
    instanceName = 'FLUID_INST'
    inst = a.instances[instanceName]

    inner_edges_fluid = inst.edges.getByBoundingBox(
        xMin = inner_radius_fluid-tol, xMax = inner_radius_fluid+tol,
        yMin = y_min-tol, yMax = y_max + tol, zMin = -tol, zMax = tol
    )

    outer_edges_fluid = inst.edges.getByBoundingBox(
        xMin = outer_radius_fluid-tol, xMax = outer_radius_fluid+tol,
        yMin = y_min-tol, yMax = y_max + tol, zMin = -tol, zMax = tol
    )

    top_edges_fluid = inst.edges.getByBoundingBox(
        xMin = inner_radius_fluid-tol, xMax = outer_radius_fluid+tol,
        yMin = y_max-tol, yMax = y_max+tol, zMin = -tol, zMax = tol
    )


    bottom_edges_fluid = inst.edges.getByBoundingBox(
        xMin = inner_radius_fluid-tol, xMax = outer_radius_fluid+tol,
        yMin = y_min-tol, yMax = y_min+tol, zMin = -tol, zMax = tol
    )

    all_edges_fluid = inner_edges_fluid + outer_edges_fluid + top_edges_fluid + bottom_edges_fluid

    surface_name_fluid = 'FASEI_ANNULAR'
    a.Surface(side1Edges= all_edges_fluid, name=surface_name_fluid)

    print("Surface '%s' created successfully containing %d edges." % (surface_name_fluid, len(all_edges_fluid)))
    
    # Creation of inner and outer surfaces in the fluid 
    # FASEI_FLUIDO

    # edges_fluid_phasei = inner_edges_fluid + outer_edges_fluid 

    # surface_name_fluid_phasei = 'FASEI_FLUIDO'
    # a.Surface(side1Edges= edges_fluid_phasei, name=surface_name_fluid_phasei)

    # print("Surface '%s' created successfully containing %d edges." % (surface_name_fluid_phasei, len(edges_fluid_phasei)))

    # It was defined below in the PIPE and ROCK instances ###############################################################

    # Creating the casing surface using edges from the pipe instance
    # FASEI_COMPLETED_WELL
    instanceName = 'PIPE_INST'
    inst = a.instances[instanceName]

    inner_edges_pipe = inst.edges.getByBoundingBox(
        xMin = inner_radius_pipe-tol,
        xMax = inner_radius_pipe+tol,
        yMin = y_min-tol, 
        yMax = y_max + tol, 
        zMin = -tol, 
        zMax = tol
    )

    surfaceName_pipe = 'FASEI_COMPLETED_WELL'
    a.Surface(side1Edges= inner_edges_pipe, name=surfaceName_pipe)

    print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_pipe, len(inner_edges_pipe)))
    
    # Creating the casing outer surface using edges from the pipe instance
    # FASEI_MASTER

    outer_edges_pipe = inst.edges.getByBoundingBox(
        xMin = outer_radius_pipe-tol,
        xMax = outer_radius_pipe+tol,
        yMin = y_min-tol, 
        yMax = y_max + tol, 
        zMin = -tol, 
        zMax = tol
    )

    surfaceName_pipe_outer = 'FASEI_MASTER'
    a.Surface(side1Edges= outer_edges_pipe, name=surfaceName_pipe_outer)

    print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_pipe_outer, len(outer_edges_pipe)))

    # Creating the casing external surfaces using edges from the pipe instance
    # FASEI_REV

    top_edges_pipe = inst.edges.getByBoundingBox(
        xMin = inner_radius_pipe-tol, xMax = outer_radius_pipe+tol,
        yMin = y_max-tol, yMax = y_max+tol, zMin = -tol, zMax = tol
    )


    bottom_edges_pipe = inst.edges.getByBoundingBox(
        xMin = inner_radius_pipe-tol, xMax = outer_radius_pipe+tol,
        yMin = y_min-tol, yMax = y_min+tol, zMin = -tol, zMax = tol
    )

    all_edges_pipe = inner_edges_pipe + outer_edges_pipe + top_edges_pipe + bottom_edges_pipe

    surfaceName_pipe = 'FASEI_REV'
    a.Surface(side1Edges= all_edges_pipe, name=surfaceName_pipe)

    # Creating the rock internal surfaces using edges from the rock instance
    # FASEI_OPEN_WELL



    instanceName = 'ROCK_INST'
    inst = a.instances[instanceName]

    inner_edges_rock = inst.edges.getByBoundingBox(
        xMin = inner_radius_rock-tol,
        xMax = inner_radius_rock+tol,
        yMin = y_min-tol, 
        yMax = y_max + tol, 
        zMin = -tol, 
        zMax = tol
    )

    surfaceName_rock_open = 'FASEI_OPEN_WELL'
    a.Surface(side1Edges= inner_edges_rock, name=surfaceName_rock_open)

    print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_rock_open, len(inner_edges_rock)))

    surfaceName_rock = 'FASEI_WELL'
    a.Surface(side1Edges= inner_edges_rock, name=surfaceName_rock)

    print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_rock, len(inner_edges_rock)))

    # return a.surfaces[surface_name_fluid], a.surfaces[surface_name_fluid_phasei], a.surfaces[surfaceName_pipe], a.surfaces[surfaceName_pipe_outer], a.surfaces[surfaceName_pipe], a.surfaces[surfaceName_rock], a.surfaces[surfaceName_rock_open]

    # Defining the FASEI_FLUID via pipe and rock surfaces 

    edges_fluid_phasei = outer_edges_pipe + inner_edges_rock

    surface_name_fluid_phasei = 'FASEI_FLUIDO'
    a.Surface(side1Edges= edges_fluid_phasei, name=surface_name_fluid_phasei)

    # print("Surface '%s' created successfully containing %d edges." % (surface_name_fluid_phasei, len(edges_fluid_phasei)))
    
def CreateSetPointRock(model_name, r_coord, z_coord):

    m = mdb.models[model_name]
    a = m.rootAssembly

    a.regenerate()
    
    # Mudança da Instância
    inst_rock = a.instances['ROCK_INST']
    
    # Lembre-se da ordem (R, 0, -Z) que corrigimos antes
    target_coords = (r_coord, z_coord, 0.0)
    
    closest_nodes = inst_rock.nodes.getClosest(coordinates=(target_coords,))
    
    if closest_nodes:
        node_label = closest_nodes[0].label
        # Use um nome diferente para não sobrescrever o do PIPE
        set_name = 'SET_ROCK_STRESS_MONITOR'
        
        if set_name in a.sets.keys():
            del a.sets[set_name]
            
        target_node_seq = inst_rock.nodes.sequenceFromLabels((node_label,))
        a.Set(name=set_name, nodes=target_node_seq)
        
        print(">>> SUCESSO: Set da rocha '%s' criado (No: %d)" % (set_name, node_label))
        return a.sets[set_name]
    return None    
    
def CreateSetPointCasing(model_name, r_coord, z_coord):
    
    m = mdb.models[model_name]
    a = m.rootAssembly
    
    # 1. Garante que o Assembly está atualizado com a nova malha
    a.regenerate()
    
    inst_pipe = a.instances['PIPE_INST']
    target_coords = (r_coord, z_coord, 0.0)
    
    # 2. Busca o nó mais próximo para capturar o seu LABEL
    closest_nodes = inst_pipe.nodes.getClosest(coordinates=(target_coords,))
    
    if closest_nodes:
        node_label = closest_nodes[0].label # Pegamos o número de identidade do nó
        set_name = 'SET_STRESS_MONITOR'
        
        # 3. Limpeza rigorosa do Set antigo
        if set_name in a.sets.keys():
            del a.sets[set_name]
            
        try:
            # 4. Criamos o Set pedindo ao Abaqus para buscar o nó pelo seu Label
            # Esta é a forma mais estável de vincular nós de instância ao Assembly
            target_node_seq = inst_pipe.nodes.sequenceFromLabels((node_label,))
            a.Set(name=set_name, nodes=target_node_seq)
            
            print(">>> SUCESSO: Set '%s' criado (No Label: %d)" % (set_name, node_label))
            return a.sets[set_name]
            
        except Exception as e:
            print(">>> Erro fatal na criacao do Set: %s" % str(e))
            return None
    else:
        print(">>> AVISO: Nenhum no encontrado nas coordenadas (%.2f, %.2f)" % (r_coord, z_coord))
        return None    
    
