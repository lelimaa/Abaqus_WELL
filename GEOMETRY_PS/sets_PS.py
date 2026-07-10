from abaqus import mdb
from abaqusConstants import *
import numpy as np

def CreateSetsAssembly(modelName):  
    m = mdb.models[modelName]    
    a = m.rootAssembly
    tol = 0.0001
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

    # Verifica se a chave existe no Repository antes de acessar para não gerar erro
    inst_fluid = a.instances[nome_fluid] if nome_fluid in a.instances.keys() else None
    inst_pipe  = a.instances[nome_pipe]  if nome_pipe  in a.instances.keys() else None
    inst_rock  = a.instances[nome_rock]  if nome_rock  in a.instances.keys() else None

    # Usando listas para agrupar as faces de forma mais robusta
    faces_combinadas = None # []
    
    if inst_fluid is not None:
        faces_combinadas = inst_fluid.faces[:]
        
    if inst_pipe is not None:
        if faces_combinadas is None:
            faces_combinadas = inst_pipe.faces[:]
        else:
            # O Abaqus une as faces perfeitamente com o sinal de mais
            faces_combinadas = faces_combinadas + inst_pipe.faces[:]

    # Criar o Set no Assembly APENAS se a lista não estiver vazia
    if faces_combinadas:
        a.Set(faces=faces_combinadas, name='FASEI')
        print("Set 'FASEI' combinado gerado com sucesso no Assembly!")
    else:
        print("Aviso: Nenhuma face encontrada para FLUID e PIPE. Set 'FASEI' ignorado nesta etapa.")

    # =========================================================
    # FASEI_SPRING 1 + FASEI_SPRING 2
    # =========================================================
   
    y_eixo_x0 = []
    # 1. Varredura para descobrir a coordenada Y do ponto vermelho
    for inst in a.instances.values():
        if len(inst.vertices) > 0:
            for v in inst.vertices:
                coords = v.pointOn[0]
                # Verifica se o ponto está sobre o eixo Y (X = 0)
                if abs(coords[0]) < tol: 
                    y_eixo_x0.append(coords[1])
    
    # 2. FILTRAR E ORDENAR AS COORDENADAS Y
    y_unicos = []
    for y in y_eixo_x0:
        # Remove duplicatas caso instâncias diferentes compartilhem o mesmo ponto (evita erro de tolerância)
        if not any(abs(y - y_ext) < tol for y_ext in y_unicos):
            y_unicos.append(y)
    
    # Ordena a lista do menor raio para o maior raio
    y_unicos.sort() 

    # Verifica se o modelo tem pelo menos dois pontos nesse eixo
    if len(y_unicos) >= 2:
        # O primeiro item da lista é o SPRING1, o segundo é o SPRING2
        y_spring1 = y_unicos[0] 
        y_spring2 = y_unicos[1] 
        
        ponto1_geom = None
        ponto2_geom = None

        # 2. Varredura para criar o Bounding Box exatamente ao redor desse único ponto
        for inst in a.instances.values():
            if len(inst.vertices) > 0:
            # Captura para FASEI_SPRING1
                verts1 = inst.vertices.getByBoundingBox(
                    xMin=-tol, yMin=y_spring1 - tol, zMin=-tol,
                    xMax=tol,  yMax=y_spring1 + tol, zMax=tol
                )
                if verts1:
                    ponto1_geom = verts1 if ponto1_geom is None else ponto1_geom + verts1
                
            # Captura para FASEI_SPRING2
            verts2 = inst.vertices.getByBoundingBox(
                xMin=-tol, yMin=y_spring2 - tol, zMin=-tol,
                xMax=tol,  yMax=y_spring2 + tol, zMax=tol
            )
            if verts2:
                ponto2_geom = verts2 if ponto2_geom is None else ponto2_geom + verts2
        # 3. Criação do Set no Assembly
        if ponto1_geom:
            a.Set(vertices=ponto1_geom, name='FASEI_SPRING1')
            print("Set 'FASEI_SPRING1' criado.")
        
        if ponto2_geom:
            a.Set(vertices=ponto2_geom, name='FASEI_SPRING2')
            print("Set 'FASEI_SPRING2' criado.")
    else:
        print("Aviso: O modelo não possui pontos suficientes no eixo X=0 para criar os dois Sets.")
    
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
            a.Set(edges=edges_base_lista, name='YSYM')
            print("Set 'YSYM' criado com sucesso unindo todas as instâncias.")
        else:
            print("Aviso: Nenhuma aresta encontrada na cota Y =", y_base)
            
    else:
        print("Aviso: Não foi possível determinar a base (y_base). O Assembly está vazio ou as instâncias não possuem vértices.")
    
    
def CreateFeaturesAssembly(modelName, depth):
    m = mdb.models[modelName]    
    a = m.rootAssembly

    # CRIA UM DATUM CSYS CARTESIANO NO ASSEMBLY
    a.DatumCsysByThreePoints(
    name='Datum csys-1',                # Nome do seu CSYS (facilita referenciar depois)
    coordSysType=CARTESIAN, 
    origin=(0.0, -depth, 0.0),       # Sua coordenada de origem desejada
    point1=(1.0, -depth, 0.0),       # Um ponto para definir a direção do eixo X
    point2=(0.0, -depth + 1.0, 0.0))

    # CRIA UM REFERENCE POINT (RP) NO ASSEMBLY:
    rp_feature = a.ReferencePoint(point=(0.0, -depth, 0.0))
    # 2. Define os novos nomes baseados no nome da parte
    nome_feature = f'REFPT'
    
    # 3. Altera o nome do RP na aba 'Features' da árvore
    # a.features.changeKey(fromName=rp_feature.name, toName=nome_feature)

    # 4. Acessa o objeto real do RP usando o ID
    rp_object = a.referencePoints[rp_feature.id]
                    
    # 5. Cria o Set passando o objeto
    a.Set(name=nome_feature, referencePoints=(rp_object, ))
    
    # insti_rock = 'ROCK'
    # if insti_rock in a.instances.keys():
    #     rp_set = f'{insti_rock}.Set_RP_{insti_rock}_-{depth}_0'
    # # Limpeza geral antes de rodar a automação
    # sets_para_limpar = [rp_set]

    # for set_name in sets_para_limpar:
    #     if set_name in a.sets:
    #         del a.sets[set_name]
