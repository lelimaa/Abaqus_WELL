# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

# if 'MyFirstModel' not in mdb.models:
#     mdb.Model(name='MyFirstModel')


def ExtractDepthsFromParts(modelName, partsNames):
    """
    Extrai automaticamente top_depth e base_depth das partes existentes.

    Métodos de extração (em ordem de prioridade):
    1. Dos Reference Points da parte ROCK (se existir) - formato RP_TOP_<depth>
    2. Dos vértices das partes (coordenadas Y)
    3. Dos nomes dos sets de camadas (se existirem) - formato SET_<PART>_Layer_<top>_<bottom>
    4. Valores padrão como fallback
    """
    model = mdb.models[modelName]
    top_depth = None
    base_depth = None

    # Método 1: Tentar extrair do Reference Point da parte ROCK
    if 'ROCK' in partsNames and 'ROCK' in model.parts:
        rock_part = model.parts['ROCK']
        try:
            for rp_name in rock_part.sets.keys():
                if rp_name.startswith('RP_TOP_'):
                    try:
                        # Extrai o valor do nome do set: 'RP_TOP_3200' -> 3200
                        top_depth = float(rp_name.split('_')[-1])
                        print("Top depth extraido do Reference Point: %.1f" %
                              top_depth)
                        break
                    except:
                        pass
        except:
            pass

    # Método 2: Extrair das coordenadas dos vértices das partes
    if top_depth is None or base_depth is None:
        all_y_coords = []
        for part_name in partsNames:
            if part_name in model.parts:
                p = model.parts[part_name]
                try:
                    # Coletar coordenadas Y de todos os vértices
                    for vertex in p.vertices:
                        point_on = vertex.pointOn
                        if point_on:
                            y_coord = point_on[0][1]  # Coordenada Y
                            all_y_coords.append(y_coord)
                except:
                    pass

        if all_y_coords:
            # No Abaqus, profundidades são negativas (Y negativo = mais profundo)
            # top_depth é o Y menos negativo (mais próximo de zero)
            # base_depth é o Y mais negativo (mais distante de zero)
            min_y = max(all_y_coords)  # Menos negativo = topo
            max_y = min(all_y_coords)  # Mais negativo = base

            # Converter para profundidades positivas
            if top_depth is None:
                top_depth = -min_y
            if base_depth is None:
                base_depth = -max_y
            print("Profundidades extraidas das geometrias: top=%.1f, base=%.1f" %
                  (top_depth, base_depth))

    # Método 3: Tentar extrair dos nomes dos sets de camadas
    if top_depth is None or base_depth is None:
        all_depths = []
        for part_name in partsNames:
            if part_name in model.parts:
                p = model.parts[part_name]
                try:
                    for set_name in p.sets.keys():
                        if 'Layer' in set_name:
                            # Formato: 'SET_ROCK_Layer_3200_3300'
                            try:
                                parts = set_name.split('_')
                                for i, part_str in enumerate(parts):
                                    if part_str == 'Layer' and i + 2 < len(parts):
                                        top = float(parts[i+1])
                                        bottom = float(parts[i+2])
                                        all_depths.extend([top, bottom])
                            except:
                                pass
                except:
                    pass

        if all_depths:
            if top_depth is None:
                top_depth = min(all_depths)
            if base_depth is None:
                base_depth = max(all_depths)
            print("Profundidades extraidas dos sets de camadas: top=%.1f, base=%.1f" %
                  (top_depth, base_depth))

    # Método 4: Valores padrão como fallback (garantir que sempre retorna valores)
    if top_depth is None:
        top_depth = 3200.0
        print("Aviso: Usando valor padrao para top_depth: %.1f" % top_depth)

    if base_depth is None:
        base_depth = 4000.0
        print("Aviso: Usando valor padrao para base_depth: %.1f" % base_depth)

    return top_depth, base_depth

def Assembly(modelName, partsNames, top_depth=None, base_depth=None):
    """
    Cria o assembly com as partes especificadas.

    Parâmetros:
    -----------
    modelName : str
        Nome do modelo no Abaqus
    partsNames : list
        Lista com os nomes das partes a serem instanciadas
    top_depth : float, optional
        Profundidade do topo. Se None, será extraída automaticamente das partes
    base_depth : float, optional
        Profundidade da base. Se None, será extraída automaticamente das partes
    """
    model = mdb.models[modelName]
    a = model.rootAssembly

    # Extrair profundidades automaticamente se não fornecidas
    if top_depth is None or base_depth is None:
        extracted_top, extracted_base = ExtractDepthsFromParts(
            modelName, partsNames)
        if top_depth is None:
            top_depth = extracted_top
        if base_depth is None:
            base_depth = extracted_base

    # Validar que temos valores válidos antes de continuar
    if top_depth is None or base_depth is None:
        raise ValueError("Nao foi possivel extrair top_depth e/ou base_depth das partes. "
                         "Por favor, forneca esses valores explicitamente.")

    depth = base_depth - top_depth

    # Verificar se GlobalCSYS já existe antes de criar
    if 'GlobalCSYS' not in a.features:
        # Create a global cylindrical coordinate system
        a.DatumCsysByThreePoints(name='GlobalCSYS', coordSysType=CYLINDRICAL,
                                 origin=(0.0, -top_depth-(depth/2), 0.0),
                                 point1=(-1.0, 0.0, 0.0), point2=(0.0, 1.0, 0.0))
        print("Sistema de coordenadas GlobalCSYS criado")
    else:
        print("Sistema de coordenadas GlobalCSYS ja existe")

    instances = {}

    for name in partsNames:
        if name not in model.parts:
            raise ValueError("Part '%s' not found in model '%s'." %
                             (name, modelName))

        p = model.parts[name]
        instName = name + '_INST'

        # Verificar se a instância já existe antes de criar
        if instName not in a.instances:
            a.Instance(name=instName, part=p, dependent=ON)
            print("Instancia criada: %s" % instName)
        else:
            print("Instancia ja existe: %s" % instName)

        inst = a.instances[instName]
        instances[name] = inst

        # Criar set para cada instância (dentro do loop)
        set_name = inst.name + '_Set'
        if set_name not in a.sets:
            if inst.cells:
                a.Set(cells=inst.cells[:], name=set_name)
            elif inst.faces:
                a.Set(faces=inst.faces[:], name=set_name)
            elif inst.edges:
                a.Set(edges=inst.edges[:], name=set_name)
            print("Set criado no assembly: %s" % set_name)
        else:
            print("Set ja existe no assembly: %s" % set_name)

    a.regenerate()
    print("Assembly concluido com profundidades: top=%.1f, base=%.1f" %
          (top_depth, base_depth))
    print("Sets ativos no assembly:", list(a.sets.keys()))
