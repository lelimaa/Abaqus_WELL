# -*- coding: utf-8 -*-
from abaqusConstants import *
from abaqus import mdb
import numpy as np
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import sys
import importlib
# import os

from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

class PlaneStrainPart:

    def __init__(self, name, data, span="half"):
        self.name = name
        self.data = data
        self.span = span
        
    def get_geometry(self, depth):
        center1 = self.data.get("center1", [0.0,-depth])
        center2 = self.data.get("center2", [0.0,-depth])
        Ro1 = self.data.get("outer_radius")
        Ro2 = self.data.get("outer_radius")
        Ri1 = Ro1 - self.data.get("thickness")
        Ri2 = Ro2 - self.data.get("thickness")
        self.geometry = {
            "center1": center1,
            "center2": center2,
            "Ro1": Ro1,
            "Ro2": Ro2,
            "Ri1": Ri1,
            "Ri2": Ri2
        }

    def create_part(self, modelName, depth):
        self.get_geometry(depth)
        m = mdb.models[modelName]
        sketch_name = '__profile__' + self.name
        # Ajuste o sheetSize conforme necessário para acomodar a geometria
        s = m.ConstrainedSketch(name=sketch_name, sheetSize=10000.0)
        s.setPrimaryObject(option=STANDALONE)
        
        # Simplificando o acesso às variáveis de centro
        cx = self.geometry["center1"][0]
        cy = self.geometry["center1"][1]
        Ro = self.geometry["Ro1"]
        Ri = self.geometry["Ri1"]


        if self.span == "half":
            # Arco Externo (Curva superior): do lado direito (+Ro) para o esquerdo (-Ro)
            s.ArcByCenterEnds(center=(cx, cy), point1=(cx + Ro, cy), point2=(cx - Ro, cy), direction=COUNTERCLOCKWISE)
            # Arco Interno (Curva inferior): do lado direito (+Ri) para o esquerdo (-Ri)
            s.ArcByCenterEnds(center=(cx, cy), point1=(cx + Ri, cy), point2=(cx - Ri, cy), direction=COUNTERCLOCKWISE)
            
            # Linhas retas que fecham a base em y = -2600
            s.Line(point1=(cx - Ro, cy), point2=(cx - Ri, cy)) # Fecha o lado esquerdo
            s.Line(point1=(cx + Ro, cy), point2=(cx + Ri, cy)) # Fecha o lado direito
        elif self.span == "quarter":
            # Quadrante superior direito (0 a 90 graus)
            s.ArcByCenterEnds(center=(cx, cy), point1=(cx + Ro, cy), point2=(cx, cy + Ro), direction=COUNTERCLOCKWISE)
            s.ArcByCenterEnds(center=(cx, cy), point1=(cx + Ri, cy), point2=(cx, cy + Ri), direction=COUNTERCLOCKWISE)
            
            s.Line(point1=(cx + Ri, cy), point2=(cx + Ro, cy)) # Base horizontal no eixo X
            s.Line(point1=(cx, cy + Ri), point2=(cx, cy + Ro)) # Base vertical no eixo Y
        
        p = m.Part(name=self.name, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        del m.sketches[sketch_name]
        return p

    def set_Mesh():
        pass
        # self.elemTypes = (CPE4, CPE3)
        # elemType1 = mesh.ElemType(elemCode=self.elemTypes[0], elemLibrary=STANDARD)
        # elemType2 = mesh.ElemType(elemCode=self.elemTypes[1], elemLibrary=STANDARD)

        # p.setMeshControls(regions=p.faces, technique=STRUCTURED)
        # p.setElementType(regions=(p.faces,), elemTypes=(elemType1, elemType2))

        # ec = geomAuxiliar.filterEdges(p.edges, geomAuxiliar.isCircularEdge)
        # eh = geomAuxiliar.filterEdges(p.edges, geomAuxiliar.isHorizontalEdge)

        # p.seedEdgeByNumber(edges=eh, number=self.numElems[0], constraint=FINER)
        # p.seedEdgeByNumber(edges=ec, number=self.numElems[1], constraint=FINER)
        # p.generateMesh()

    def add_to_assembly(self, modelName):
        m = mdb.models[modelName]
        m.rootAssembly.Instance(name=self.name,
                                part=m.parts[self.name],
                                dependent=ON)
        m.rootAssembly.regenerate()

    def create_spec_sets(self, modelName):
        pass

    def create_contact_sets(self):
        pass
             
    def create_sets(self, modelName):
        m = mdb.models[modelName]
        p = m.parts[self.name]
        f = p.faces
        tol = 0.001
    
        # ---------------------------------------------------------------------
        # 1. SETS GERAIS (ALL e FASEI)
        # ---------------------------------------------------------------------
        all_faces = f[0:len(f)]
        p.Set(faces=all_faces, name='FASEI_' + self.name.upper())

        if self.name.upper() == 'FLUID':
            p.Set(faces=all_faces, name='FASEI_' + self.name.upper())
            p.Set(faces=all_faces, name='FASEI_ANNULAR')

        # ---------------------------------------------------------------------
        # 2. IDENTIFICAÇÃO DOS ARCOS (OD e ID) PARA A GEOMETRIA EM "U"
        # ---------------------------------------------------------------------
        if self.span == "half":
            angles = (0.25*np.pi, 0.75*np.pi)
        elif self.span == "quarter":
            angles = (0.25*np.pi,)
        else:
            angles = (0.25*np.pi, 0.75*np.pi, 1.25*np.pi, 1.75*np.pi)
        
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
            
        if self.name.upper() == 'FLUID':
            p.Set(faces=all_faces, name='FASEI_' + self.name.upper() + '_OD')
            p.Set(faces=all_faces, name='FASEI_' + self.name.upper() + '_ID')
            p.Set(faces=all_faces, name='FASEI_ANNULAR_OD')
            p.Set(faces=all_faces, name='FASEI_ANNULAR_ID')
        
        if self.name.upper() == 'PIPE':
            p.Set(faces=all_faces, name='PROD_ANNULAR')
            
        # ---------------------------------------------------------------------
        # 3. IDENTIFICAÇÃO DOS TOPOS HORIONTAIS (MESH_TT e YSYM_TOP)
        # ---------------------------------------------------------------------
        # O "topo" do U são as linhas planas na cota y = -depth
        y_top = self.geometry["center1"][1] 
            
        top_edges = p.edges.getByBoundingBox(
            xMin=-1e20, yMin=y_top - tol, zMin=-tol,
            xMax=1e20,  yMax=y_top + tol, zMax=tol
        )

        vertical_edge = p.edges.getByBoundingBox(
            xMin=-tol, yMin=-1e20, zMin=-tol,
            xMax=tol,  yMax=1e20,  zMax=tol
        )
        
        if top_edges and vertical_edge:
            # CORREÇÃO: Usar apenas 'edges=' para objetos de linha
            p.Set(edges=top_edges + vertical_edge, name='FASEI_' + self.name.upper() + '_TT')
            
            # Se você precisa de outro Set separado com as mesmas linhas:
            if self.name.upper() == 'FLUID':
                p.Set(edges=od_edges, name='FASEI_' + self.name.upper() + '_OD')
                p.Set(edges=id_edges, name='FASEI_' + self.name.upper() + '_ID')
                p.Set(edges=od_edges, name='FASEI_ANNULAR_OD')
                p.Set(edges=id_edges, name='FASEI_ANNULAR_ID')
                p.Set(edges=top_edges + vertical_edge, name='FASEI_ANNULAR_TT')
                
                nome_set_remover = 'FASEI_' + self.name.upper() + '_TT'

                if nome_set_remover in p.sets.keys():
                    del p.sets[nome_set_remover]
        
            # if self.name.upper() == 'PIPE':
                # p.Set(faces=id_edges, name='PROD_ANNULAR')

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
        if top_edges and vertical_edge:
            if self.name.upper() == 'ROCK':
                p.Set(edges=id_edges, name='FASEI_OPEN_WELL')
                p.Set(edges=id_edges, name='FASEI_WELL')
                p.Set(edges=od_edges, name='ROCK_BC')
                # p.Set(edges=top_edges, name='YSYM_BASE_ROCK') # A base da rocha é a curva mais externa
                p.Set(faces=all_faces, name='ROCK_OUTPUT')
                p.Set(faces=all_faces, name='FASEI_SLAVE')
                              
                print(f"Sets específicos da ROCK criados.")

                ROCK_ID_remover = 'FASEI_' + self.name.upper() + '_ID'
                ROCK_OD_remover = 'FASEI_' + self.name.upper() + '_OD'

                if ROCK_ID_remover and ROCK_OD_remover in p.sets.keys():
                    del p.sets[ROCK_OD_remover]
                    del p.sets[ROCK_ID_remover]

            # elif self.name.upper() == 'FLUID':
            #     p.Set(edges=od_edges, name='FASEI_OPEN_WELL')
            #     print(f"Sets específicos do FLUID criados.")

            elif self.name.upper() == 'PIPE':
                p.Set(edges=id_edges, name='FASEI_COMPLETED_WELL')
                print(f"Sets específicos do PIPE criados.")

    def CreateSurfaces(self, modelName):
        m = mdb.models[modelName]
        p = m.parts[self.name]
        
        # Inicializa as sequências de arestas (edges) vazias
        od_edges = p.edges[:0]
        id_edges = p.edges[:0]
        # side_edges = p.edges[:0] # Arestas retas nas extremidades do arco

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
                p.Surface(side1Edges=edges_fluido, name='FASEI_FLUIDO')
                p.Surface(side1Edges=edges_fluido, name='FASEI_ANNULAR')
                print("Surfaces de 'FASEI_FLUIDO' foram criadas")

            # # FASEI_ANNULAR: Contorno fechado completo (ID + OD + Laterais retas)
            # all_edges = od_edges + id_edges + side_edges
            # if len(all_edges) > 0:
            #     p.Surface(side1Edges=all_edges, name='FASEI_ANNULAR')
            #     print("Surface 'FASEI_ANNULAR' criada")
        
        elif self.name.upper() == 'PIPE':
            p.Surface(side1Edges=id_edges, name='FASEI_COMPLETED_WELL')
            p.Surface(side1Edges=id_edges, name='FASEI_' + self.name.upper() + '_ID')
            p.Surface(side1Edges=id_edges, name='FASEI_PROD_ANNULAR')
            p.Surface(side1Edges=od_edges, name='FASEI_MASTER')
            p.Surface(side1Edges=od_edges, name='FASEI_' + self.name.upper() + '_OD')

        elif self.name.upper() == 'ROCK':
            p.Surface(side1Edges=id_edges, name='FASEI_OPEN_WELL')
            p.Surface(side1Edges=id_edges, name='FASEI_WELL')
            p.Surface(side1Edges=od_edges, name='ROCK_BC')
        
                   
    def CreateSetsAssembly(self, modelName):  
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
        # FASEI_OPEN_WELL + FASEI_WELL
        # =========================================================
        nome_fluid = None # Antes estava 'FLUID_INST'
        nome_pipe  = None # Antes estava 'PIPE_INST'
        nome_rock  = None # Antes estava 'ROCK_INST'

        inst_fluid = a.instances[nome_fluid] if nome_fluid in a.instances.keys() else None
        inst_pipe  = a.instances[nome_pipe]  if nome_pipe  in a.instances.keys() else None
        inst_rock  = a.instances[nome_rock]  if nome_rock  in a.instances.keys() else None
        
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

        if inst_fluid in a.instances.values() and od_edges:
            a.Set(edges=od_edges, name='FASEI_OPEN_WELL')
        if inst_rock in a.instances.values() and id_edges:
            a.Set(edges = id_edges, name='FASEI_WELL') # if only from ROCK      

        # =========================================================
        # FASEI_COMPLETED_WELL
        # =========================================================
        if inst_pipe in a.instances.values() and id_edges:
            a.Set(edges = id_edges,name='FASEI_COMPLETED_WELL') # if only from PIPE  
        
        # =========================================================
        # ROCK_BC
        # =========================================================
        if inst_rock in a.instances.values() and od_edges:
            a.Set(edges=od_edges, name='ROCK_BC')
        
        # =========================================================
        # ROCK_OUTPUT
        # ========================================================= 
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

    def SetsAssembly(self, modelName):
        m = mdb.models[modelName]  
        a = m.rootAssembly
        tol =0.001
        print("Instâncias disponíveis no Assembly:", a.instances.keys())
        
        # =========================================================
        # FASEI = FLUIDO + PIPE
        # =========================================================
        # Substitua pelas chaves reais impressas no terminal (geralmente NomeDaPeca-1)
        nome_fluid = None # Antes estava 'FLUID_INST'
        nome_pipe  = None # Antes estava 'PIPE_INST'
        nome_rock  = None # Antes estava 'ROCK_INST'

        inst_fluid = a.instances[nome_fluid] if nome_fluid in a.instances.keys() else None
        inst_pipe  = a.instances[nome_pipe]  if nome_pipe  in a.instances.keys() else None
        inst_rock  = a.instances[nome_rock]  if nome_rock  in a.instances.keys() else None

        # Usando listas para agrupar as faces de forma mais robusta
        faces_combinadas = []
        
        if inst_fluid is not None:
            faces_combinadas.extend(inst_fluid.faces)
            
        if inst_pipe is not None:
            faces_combinadas.extend(inst_pipe.faces)

        # Criar o Set no Assembly APENAS se a lista não estiver vazia
        if faces_combinadas:
            a.Set(faces=faces_combinadas, name='FASEI')
            print("Set 'FASEI' combinado gerado com sucesso no Assembly!")
        else:
            print("Aviso: Nenhuma face encontrada para FLUID e PIPE. Set 'FASEI' ignorado nesta etapa.")

    def add_reference_point(self, modelName, depth):
        # 1. Acessa a parte dentro da classe (assumindo que self.name é o nome da parte)
        part = mdb.models[modelName].parts[self.name]
    
        # 3. Cria o RP
        rp_feature = part.ReferencePoint(point=(0.0, -depth, 0.0))

        # 3. Define os novos nomes baseados no nome da parte
        novo_nome_feature = f'RP_{self.name}'
        
        # 4. Altera o nome do RP na aba 'Features' da árvore
        part.features.changeKey(fromName=rp_feature.name, toName=novo_nome_feature)

        # 5. Acessa o objeto real do RP usando o ID
        rp_object = part.referencePoints[rp_feature.id]

        # 6. Lógica exclusiva para a parte 'ROCK' (Criação de Set)
        if self.name == 'ROCK':
            depth_str = str(-depth).replace('.', '_')
            set_name = f'Set_{novo_nome_feature}_{depth_str}'

            # Remove o Set se já existir para evitar conflitos
            if set_name in part.sets.keys():
                del part.sets[set_name]
                        
            # Cria o Set passando o objeto
            part.Set(name=set_name, referencePoints=(rp_object, ))
            print(f"Feature '{novo_nome_feature}' e Set '{set_name}' criados na parte '{self.name}'.")
            
        else:
            # Se não for ROCK, apenas avisa que a Feature foi criada
            print(f"Feature '{novo_nome_feature}' criada na parte '{self.name}' (Set ignorado).")
        
    def PartitionFacePS(self, modelName):
        """
        Cria uma partição vertical na face de um semicírculo em uma Part 
        usando um plano YZ no eixo X = 0.
        """
        part = mdb.models[modelName].parts[self.name]

        # Cria plano datum vertical diretamente no X = 0.0
        dp = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=0.0)

        # Particiona todas as faces cortadas pelo plano infinito
        part.PartitionFaceByDatumPlane(
            datumPlane=part.datums[dp.id],
            faces=part.faces[:]
        )         
    
    # def CreateSetsAssembly(self, modelName):  
    #     m = mdb.models[modelName]
    #     a = m.rootAssembly
        
    #     # ALL FACES
    #     faces_totais = None
    #     for inst in a.instances.values():
    #         if faces_totais is None:
    #             faces_totais = inst.faces[:]
    #         else:
    #             faces_totais = faces_totais + inst.faces[:]
    #     a.Set(faces=faces_totais, name=self.name + '_ALL')

    #     # FASEI
    #     nomes_instancias = self.name + '_INST'
    #     faces_totais = None
    #     for nome in nomes_instancias:
    #         if nome == 'FLUID_INST' or nome == 'PIPE_INST':
    #             inst = a.instances[nome]
    #             if faces_totais is None:
    #                 faces_totais = inst.faces[:]
    #             else:
    #                 faces_totais = faces_totais + inst.faces[:]

    #     if faces_totais:
    #         a.Set(faces=faces_totais, name='FASEI')
    #         print("Set 'ALL' criado com todas as faces das 2 instancias.")

    #     ######## FASEI_OPEN_WELL #############################
    #     tol =0.001
    #     for nome in nomes_instancias:
    #         if nome == 'FLUID_INST':
    #             inst_f = a.instances[nome]
    #             x_interface = max([v.pointOn[0][0] for v in inst_f.vertices])

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
    #                self.geometry["Ro2"]*np.sin(angle) + self.geometry["center1"][1],
    #                0.0)
    #         xy2 = (self.geometry["Ri1"]*np.cos(angle) + self.geometry["center2"][0],
    #                self.geometry["Ri2"]*np.sin(angle) + self.geometry["center2"][1],
    #                0.0)
    #         od_edges += a.edges.findAt((xy1,))
    #         id_edges += a.edges.findAt((xy2,))
    #     a.Set(edges = id_edges,name='FASEI_OPEN_WELL')

    #     ######## FASEI_COMPLETED_WELL #############################
    #     for nome in nomes_instancias:
    #         if nome == 'PIPE_INST':
    #             inst_f = a.instances[nome]
    #             x_interface = max([v.pointOn[0][0] for v in inst_f.vertices])
    #     a.Set(edges = id_edges,name='FASEI_COMPLETED_WELL') 

    #     edges_f = inst_f.edges.getByBoundingBox(
    #         xMin=x_interface - tol, yMin=y_min - tol, zMin=-tol,
    #         xMax=x_interface + tol, yMax=y_max + tol, zMax=tol
    #     )

    #     inst_r = a.instances['ROCK_INST']
    #     edges_r = inst_r.edges.getByBoundingBox(
    #         xMin=x_interface - tol, yMin=y_min - tol, zMin=-tol,
    #         xMax=x_interface + tol, yMax=y_max + tol, zMax=tol
    #     )

    #     edges_total = edges_f+edges_r

    #     # a.Set(edges=edges_f, name='FASEI_OPEN_WELL') # if only from fluid
    #     a.Set(edges=edges_r, name='FASEI_OPEN_WELL') # if only from rock
    #     # a.Set(edges=edges_total, name='FASEI_OPEN_WELL') # if from fluid and rock
    #     print(f"Set FASEI_OPEN_WELL criado na interface X = {x_interface}")  

    #     a.Set(edges=edges_r, name='FASEI_WELL') # if only from rock
    #     print(f"Set FASEI_WELL criado na interface X = {x_interface}")  

    #     # FASEI_COMPLETED_WELL
    #     inst_p = a.instances['PIPE_INST']
    #     x_int_pipe = min([v.pointOn[0][0] for v in inst_p.vertices])

    #     y_min_p = min([v.pointOn[0][1] for v in inst_p.vertices])
    #     y_max_p = max([v.pointOn[0][1] for v in inst_p.vertices])

    #     edges_completed = inst_p.edges.getByBoundingBox(
    #         xMin=x_int_pipe - tol, yMin=y_min_p - tol, zMin=-tol,
    #         xMax=x_int_pipe + tol, yMax=y_max_p + tol, zMax=tol
    #     )

    #     if edges_completed:
    #         a.Set(edges=edges_completed, name='FASEI_COMPLETED_WELL')
    #         print(f"Set 'FASEI_COMPLETED_WELL' criado na face interna do Pipe (X = {x_int_pipe})")


    #     # MESH_TT_ + PIPES/FLUID/ROCK
    #     inst_p = a.instances[self.name + '_INST']
    #     tol = 0.001
    #     all_coords = [v.pointOn[0][1] for v in inst_p.vertices]
    #     min_y_global = min(all_coords)
    #     base_edges = inst_p.edges.getByBoundingBox(
    #         xMin = -1e20, yMin=min_y_global - tol, zMin=-tol,
    #         xMax = 1e20, yMax=min_y_global + tol, zMax=tol
    #     )
    #     a.Set(edges=base_edges, name='FASEI_' + self.name.upper() + '_TT')
    #     min_x_p = min([v.pointOn[0][0] for v in inst_p.vertices])
    #     max_x_p = max([v.pointOn[0][0] for v in inst_p.vertices])

    #     edges_tt = None

    #     for y in all_coords:
    #         edges_camada = inst_p.edges.getByBoundingBox(
    #             xMin=min_x_p - tol, yMin=y - tol, zMin=-tol,
    #             xMax=max_x_p + tol, yMax=y + tol, zMax=tol
    #         )
    #         if edges_camada:
    #             if edges_tt is None:
    #                 edges_tt = edges_camada
    #             else:
    #                 edges_tt = edges_tt + edges_camada

    #     if edges_tt:
    #         a.Set(edges=edges_tt, name='MESH_TT_PIPES')
    #         print(f"Set 'MESH_TT_PIPES' criado com {len(edges_tt)} arestas horizontais.")

    #     # ROCK_BC
    #     inst_r = a.instances['ROCK_INST']
    #     x_externo_rock = max([v.pointOn[0][0] for v in inst_r.vertices])

    #     y_min = min([v.pointOn[0][1] for v in inst_r.vertices])
    #     y_max = max([v.pointOn[0][1] for v in inst_r.vertices])

    #     edges_bc = inst_r.edges.getByBoundingBox(
    #         xMin=x_externo_rock - tol, yMin=y_min - tol, zMin=-tol,
    #         xMax=x_externo_rock + tol, yMax=y_max + tol, zMax=tol
    #     )

    #     if edges_bc:
    #         a.Set(edges=edges_bc, name='ROCK_BC')
    #         print(f"Set 'ROCK_BC' criado com sucesso na borda X = {x_externo_rock}")

    #     # ROCK_OUTPUT
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

    #     # YSYM_BASE
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

    #     # YSYM_TOP
    #     # 1. Identificar a altura MÁXIMA (Y) global do modelo
    #     y_global_topo = []
    #     for inst in a.instances.values():
    #         y_global_topo.append(max([v.pointOn[0][1] for v in inst.vertices]))
    #     y_topo = max(y_global_topo)

    #     # 2. Criar uma lista para acumular as arestas do topo de cada instância
    #     edges_topo_lista = None

    #     for inst in a.instances.values():
    #         # Buscamos as arestas horizontais desta instância que estão na cota y_topo
    #         x_min_i = min([v.pointOn[0][0] for v in inst.vertices])
    #         x_max_i = max([v.pointOn[0][0] for v in inst.vertices])
            
    #         edges_inst = inst.edges.getByBoundingBox(
    #             xMin=x_min_i - tol, yMin=y_topo - tol, zMin=-tol,
    #             xMax=x_max_i + tol, yMax=y_topo + tol, zMax=tol
    #         )
            
    #         # Se encontrou arestas no topo desta instância, adiciona à sequência
    #         if edges_inst:
    #             if edges_topo_lista is None:
    #                 edges_topo_lista = edges_inst
    #             else:
    #                 edges_topo_lista = edges_topo_lista + edges_inst

    #     # 3. Criar o Set no Assembly
    #     if edges_topo_lista:
    #         a.Set(edges=edges_topo_lista, name='YSYM_TOP')
    #         print(f"Set 'YSYM_TOP' criado com sucesso na altura Y = {y_topo}")
    #     else:
    #         print("Erro: Nenhuma aresta encontrada no topo (Y =", y_topo, ")")

    # def CreateSurfacesAssembly(modelName, data):

    #     m = mdb.models[modelName]
    #     a = m.rootAssembly

    #     top_depth = -data["FLUID"]["top_depth"]
    #     base_depth = -data["FLUID"]["base_depth"]
    #     inner_radius_fluid = data["FLUID"]["inner_radius"]
    #     outer_radius_fluid = data["FLUID"]["inner_radius"] + data["FLUID"]["thickness"]
    #     inner_radius_pipe = data["PIPE"]["inner_radius"]
    #     outer_radius_pipe = data["PIPE"]["inner_radius"] + data["PIPE"]["thickness"]
    #     inner_radius_rock = data["ROCK"]["inner_radius"]
    #     outer_radius_rock = data["ROCK"]["inner_radius"] + data["ROCK"]["thickness"]

    #     # SUPERFICIE DE INTERFACE
    #     tol = 0.001

    #     y_min = min(top_depth, base_depth)
    #     y_max = max(top_depth, base_depth)

    #     # Creating the annular surface using edges from the fluid and rock instances at the interface
    #     # FASEI_ANNULAR
    #     instanceName = 'FLUID_INST'
    #     inst = a.instances[instanceName]

    #     inner_edges_fluid = inst.edges.getByBoundingBox(
    #         xMin = inner_radius_fluid-tol, xMax = inner_radius_fluid+tol,
    #         yMin = y_min-tol, yMax = y_max + tol, zMin = -tol, zMax = tol
    #     )

    #     outer_edges_fluid = inst.edges.getByBoundingBox(
    #         xMin = outer_radius_fluid-tol, xMax = outer_radius_fluid+tol,
    #         yMin = y_min-tol, yMax = y_max + tol, zMin = -tol, zMax = tol
    #     )

    #     top_edges_fluid = inst.edges.getByBoundingBox(
    #         xMin = inner_radius_fluid-tol, xMax = outer_radius_fluid+tol,
    #         yMin = y_max-tol, yMax = y_max+tol, zMin = -tol, zMax = tol
    #     )


    #     bottom_edges_fluid = inst.edges.getByBoundingBox(
    #         xMin = inner_radius_fluid-tol, xMax = outer_radius_fluid+tol,
    #         yMin = y_min-tol, yMax = y_min+tol, zMin = -tol, zMax = tol
    #     )

    #     all_edges_fluid = inner_edges_fluid + outer_edges_fluid + top_edges_fluid + bottom_edges_fluid

    #     surface_name_fluid = 'FASEI_ANNULAR'
    #     a.Surface(side1Edges= all_edges_fluid, name=surface_name_fluid)

    #     print("Surface '%s' created successfully containing %d edges." % (surface_name_fluid, len(all_edges_fluid)))
        
    #     # Creation of inner and outer surfaces in the fluid 
    #     # FASEI_FLUIDO

    #     # edges_fluid_phasei = inner_edges_fluid + outer_edges_fluid 

    #     # surface_name_fluid_phasei = 'FASEI_FLUIDO'
    #     # a.Surface(side1Edges= edges_fluid_phasei, name=surface_name_fluid_phasei)

    #     # print("Surface '%s' created successfully containing %d edges." % (surface_name_fluid_phasei, len(edges_fluid_phasei)))

    #     # It was defined below in the PIPE and ROCK instances ###############################################################

    #     # Creating the casing surface using edges from the pipe instance
    #     # FASEI_COMPLETED_WELL
    #     instanceName = 'PIPE_INST'
    #     inst = a.instances[instanceName]

    #     inner_edges_pipe = inst.edges.getByBoundingBox(
    #         xMin = inner_radius_pipe-tol,
    #         xMax = inner_radius_pipe+tol,
    #         yMin = y_min-tol, 
    #         yMax = y_max + tol, 
    #         zMin = -tol, 
    #         zMax = tol
    #     )

    #     surfaceName_pipe = 'FASEI_COMPLETED_WELL'
    #     a.Surface(side1Edges= inner_edges_pipe, name=surfaceName_pipe)

    #     print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_pipe, len(inner_edges_pipe)))
        
    #     # Creating the casing outer surface using edges from the pipe instance
    #     # FASEI_MASTER

    #     outer_edges_pipe = inst.edges.getByBoundingBox(
    #         xMin = outer_radius_pipe-tol,
    #         xMax = outer_radius_pipe+tol,
    #         yMin = y_min-tol, 
    #         yMax = y_max + tol, 
    #         zMin = -tol, 
    #         zMax = tol
    #     )

    #     surfaceName_pipe_outer = 'FASEI_MASTER'
    #     a.Surface(side1Edges= outer_edges_pipe, name=surfaceName_pipe_outer)

    #     print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_pipe_outer, len(outer_edges_pipe)))

    #     # Creating the casing external surfaces using edges from the pipe instance
    #     # FASEI_REV

    #     top_edges_pipe = inst.edges.getByBoundingBox(
    #         xMin = inner_radius_pipe-tol, xMax = outer_radius_pipe+tol,
    #         yMin = y_max-tol, yMax = y_max+tol, zMin = -tol, zMax = tol
    #     )


    #     bottom_edges_pipe = inst.edges.getByBoundingBox(
    #         xMin = inner_radius_pipe-tol, xMax = outer_radius_pipe+tol,
    #         yMin = y_min-tol, yMax = y_min+tol, zMin = -tol, zMax = tol
    #     )

    #     all_edges_pipe = inner_edges_pipe + outer_edges_pipe + top_edges_pipe + bottom_edges_pipe

    #     surfaceName_pipe = 'FASEI_REV'
    #     a.Surface(side1Edges= all_edges_pipe, name=surfaceName_pipe)

    #     # Creating the rock internal surfaces using edges from the rock instance
    #     # FASEI_OPEN_WELL



    #     instanceName = 'ROCK_INST'
    #     inst = a.instances[instanceName]

    #     inner_edges_rock = inst.edges.getByBoundingBox(
    #         xMin = inner_radius_rock-tol,
    #         xMax = inner_radius_rock+tol,
    #         yMin = y_min-tol, 
    #         yMax = y_max + tol, 
    #         zMin = -tol, 
    #         zMax = tol
    #     )

    #     surfaceName_rock_open = 'FASEI_OPEN_WELL'
    #     a.Surface(side1Edges= inner_edges_rock, name=surfaceName_rock_open)

    #     print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_rock_open, len(inner_edges_rock)))

    #     surfaceName_rock = 'FASEI_WELL'
    #     a.Surface(side1Edges= inner_edges_rock, name=surfaceName_rock)

    #     print("Surface '%s' succesfully created with success containing %d edges." % (surfaceName_rock, len(inner_edges_rock)))

    #     # return a.surfaces[surface_name_fluid], a.surfaces[surface_name_fluid_phasei], a.surfaces[surfaceName_pipe], a.surfaces[surfaceName_pipe_outer], a.surfaces[surfaceName_pipe], a.surfaces[surfaceName_rock], a.surfaces[surfaceName_rock_open]

    #     # Defining the FASEI_FLUID via pipe and rock surfaces 

    #     edges_fluid_phasei = outer_edges_pipe + inner_edges_rock

    #     surface_name_fluid_phasei = 'FASEI_FLUIDO'
    #     a.Surface(side1Edges= edges_fluid_phasei, name=surface_name_fluid_phasei)

    #     # print("Surface '%s' created successfully containing %d edges." % (surface_name_fluid_phasei, len(edges_fluid_phasei)))
            