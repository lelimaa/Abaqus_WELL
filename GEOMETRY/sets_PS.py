from abaqus import mdb
from abaqusConstants import *
from GEOMETRY_PS.geometry_PS import *

def Create_Sets(self, modelName):
    m = mdb.models[modelName]
    p = m.parts[self.name]
    tol = 0.001
    
    # ---------------------------------------------------------------------
    # 1. SETS GERAIS (ALL e FASEI)
    # ---------------------------------------------------------------------
    all_faces = p.faces[:]
    if all_faces:
        # p.Set(faces=all_faces, name='ALL')
        p.Set(faces=all_faces, name='FASEI_' + self.name.upper())

    # ---------------------------------------------------------------------
    # 2. IDENTIFICAÇÃO DOS ARCOS (OD e ID) PARA A GEOMETRIA EM "U"
    # ---------------------------------------------------------------------
    if self.span == "half":
        # Ângulos apontando para baixo (225º e 315º)
        angles = (1.25*np.pi, 1.75*np.pi)
    elif self.span == "quarter":
        # Quarto de círculo inferior direito (270º a 360º)
        angles = (1.75*np.pi,)
    else:
        angles = (1.25*np.pi, 1.75*np.pi)
        
    od_edges = p.edges[:0]
    id_edges = p.edges[:0]
        
    for angle in angles:
        xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
                self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
                0.0)
        xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
                self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
                0.0)
        od_edges += p.edges.findAt((xy1,))
        id_edges += p.edges.findAt((xy2,))
        
    p.Set(edges=od_edges, name='FASEI_' + self.name.upper() + '_OD')
    p.Set(edges=id_edges, name='FASEI_' + self.name.upper() + '_ID')

    # ---------------------------------------------------------------------
    # 3. IDENTIFICAÇÃO DOS TOPOS HORIONTAIS (MESH_TT e YSYM_TOP)
    # ---------------------------------------------------------------------
    # O "topo" do U são as linhas planas na cota y = -depth
    y_top = self.geometry["center1"][1] 
        
    top_edges = p.edges.getByBoundingBox(
        xMin=-1e20, yMin=y_top - tol, zMin=-tol,
        xMax=1e20,  yMax=y_top + tol, zMax=tol
    )
    if top_edges:
        p.Set(edges=top_edges, name='FASEI_' + self.name.upper() + '_TT')
        # p.Set(edges=top_edges, name='MESH_TT_' + self.name.upper())
        p.Set(edges=top_edges, name='YSYM_' + self.name.upper())

    # ---------------------------------------------------------------------
    # 4. IDENTIFICAÇÃO DE ARESTAS VERTICAIS (Apenas no modelo Quarter)
    # ---------------------------------------------------------------------
    if self.span == "quarter":
        vertical_edges = p.edges[:0]
        for edge in p.edges:
            v1 = p.vertices[edge.getVertices()[0]]
            v2 = p.vertices[edge.getVertices()[1]]
            # Se X for igual, é uma linha perfeitamente vertical
            if abs(v1.pointOn[0][0] - v2.pointOn[0][0]) < tol:
                vertical_edges += p.edges[edge.index:edge.index+1]
            
        if vertical_edges:
            p.Set(edges=vertical_edges, name='FASEI_VERTICAL_' + self.name.upper())

    # ---------------------------------------------------------------------
    # 5. SETS CONTEXTUAIS POR TIPO DE PEÇA (ROCK, FLUID, PIPE)
    # ---------------------------------------------------------------------
    nome_peca = self.name.upper()
    
    if nome_peca == 'ROCK':
        p.Set(edges=id_edges, name='FASEI_OPEN_WELL')
        p.Set(edges=id_edges, name='FASEI_WELL')
        p.Set(edges=od_edges, name='ROCK_BC')
        p.Set(edges=od_edges, name='YSYM_BASE_ROCK') # A base da rocha é a curva mais externa
        p.Set(faces=all_faces, name='ROCK_OUTPUT')
        print(f"Sets específicos da ROCHA criados.")

    elif nome_peca == 'FLUID':
        p.Set(edges=od_edges, name='FASEI_OPEN_WELL')
        print(f"Sets específicos do FLUIDO criados.")

    elif nome_peca == 'PIPE':
        p.Set(edges=id_edges, name='FASEI_COMPLETED_WELL')
        print(f"Sets específicos do PIPE criados.")


    # if self.name == 'FLUID':
    #     m = mdb.models[modelName]
    #     p = m.parts[self.name]
    #     f = p.faces
    #     e = p.edges

    #     # FASEI_ANNULAR
    #     all_faces = f
    #     p.Set(faces=all_faces, name='FASEI_ANNULAR')
        
    #     ########## FASEI_ANNULAR_OD e FASEI_ANNULAR_ID ###########################
    #     if self.span == "half":
    #         angles = (0.25*np.pi, 0.75*np.pi)
    #     elif self.span == "quarter":
    #         angles = (0.25*np.pi,)
    #     else:
    #         angles = (0.25*np.pi, 0.75*np.pi, 1.25*np.pi, 1.75*np.pi)
    #     od_edges = p.edges[:0]
    #     id_edges = p.edges[:0]
    #     for angle in angles:
    #         xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
    #                self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
    #                0.0)
    #         xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
    #                self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
    #                0.0)
    #         od_edges += p.edges.findAt((xy1,))
    #         id_edges += p.edges.findAt((xy2,))
    #     p.Set(edges = od_edges,name='FASEI_ANNULAR_OD')
    #     p.Set(edges = id_edges,name='FASEI_ANNULAR_ID')

    #     ##### FASEI_ANNULAR_TT ##################
    #     tol = 0.001
    #     all_coords = [v.pointOn[0][1] for v in p.vertices]
    #     min_y_global = min(all_coords)
    #     base_edges = p.edges.getByBoundingBox(
    #         xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
    #         xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    #     )
    #     p.Set(edges=base_edges, name='FASEI_ANNULAR_TT')

def CreateSetsAssembly(self, modelName):  
    m = mdb.models[modelName]  
    a = m.rootAssembly
    tol =0.001
    
    # Set ALL    
    faces_totais = []
    if faces_totais:
        a.Set(faces=faces_totais, name='ALL')

    # FASEI = FLUIDO + PIPE
    nomes_instancias = [self.name + '_INST']
        
        # 1. Certifique-se de usar o nome exato das instâncias.
        ######### No seu código de Assembly, a instância tem o mesmo nome da Part.
    for nome_inst in nomes_instancias:
        if nome_inst == 'FLUID_INST':
            inst_fluid = a.instances['FLUID_INST']
        elif nome_inst == 'PIPE_INST':
            inst_pipe = a.instances['PIPE_INST']
        elif nome_inst == 'ROCK_INST':
            inst_rock = a.instances['ROCK_INST']  

        # 2. Pegue todas as faces de cada instância
        ######### O [:] garante que estamos pegando a sequência de faces (Array de geometria)
    faces_fluid = inst_fluid.faces[:]
    faces_pipe  = inst_pipe.faces[:]
    
        # 3. Some as sequências (O Abaqus entende isso como uma união de geometrias)
    faces_combinadas = faces_fluid + faces_pipe
    
        # 4. Crie o Set no nível da Montagem (Assembly)
    a.Set(faces=faces_combinadas, name='FASEI')
    print("Set combinado gerado com sucesso no Assembly!")
    
    # FASEI_OPEN_WELL + FASEI_WELL
    if self.span == "half":
        angles = (0.25*np.pi, 0.75*np.pi)
    elif self.span == "quarter":
        angles = (0.25*np.pi,)
    else:
        angles = (0.25*np.pi, 0.75*np.pi, 1.25*np.pi, 1.75*np.pi)
    od_edges = a.edges[:0]
    id_edges = a.edges[:0]
    for angle in angles:
        xy1 = (self.geometry["Ro1"]*np.cos(angle) + self.geometry["center1"][0],
                self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
                0.0)
        xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
                self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
                0.0)
        od_edges += a.edges.findAt((xy1,))
        id_edges += a.edges.findAt((xy2,))
    if inst_fluid in a.instances.values() and od_edges:
        a.Set(edges=od_edges, name='FASEI_OPEN_WELL')
    if inst_rock in a.instances.values() and id_edges:
        a.Set(edges = id_edges,name='FASEI_WELL') # if only from ROCK      

    # FASEI_COMPLETED_WELL
    if inst_pipe in a.instances.values() and id_edges:
        a.Set(edges = id_edges,name='FASEI_COMPLETED_WELL') # if only from PIPE  
    
    # ROCK_BC
    if inst_rock in a.instances.values() and od_edges:
        a.Set(edges=od_edges, name='ROCK_BC')
    
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
    