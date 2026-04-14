from abaqus import mdb
from abaqusConstants import *

def CreateMeshBiasHorizontal(name_model, name_instance, filtered_layers, radius_middle, minSize, maxSize):
    # Get the model and part
    m = mdb.models[name_model]
    a = m.rootAssembly

    inst = a.instances[name_instance]
    # p = m.parts[name_part]
    # p = a.instances[name_instance]
    # e = p.edges

    depths = []

    for layer in filtered_layers:
        depths.append(layer['Top'])

    depths.append(filtered_layers[-1]['Bottom'])  

    # points_search = []
    found_lines = 0

    for z in depths:

        found_edges = inst.edges.findAt(((radius_middle, -z, 0.0), ))

        if not found_edges:
            continue 
        
        # edge = p.edges.findAt(((radius_middle, -z, 0.0), ))
        edge = found_edges[0]
        found_lines += 1

        v1_id = edge.getVertices()[0]
        v2_id = edge.getVertices()[1]

        x1 = inst.vertices[v1_id].pointOn[0][0]
        x2 = inst.vertices[v2_id].pointOn[0][0]

        if x1 < x2:
            a.seedEdgeByBias(
                biasMethod=SINGLE, 
                end1Edges=found_edges,
                minSize=minSize,
                maxSize=maxSize,
                constraint=FINER
            )
        else:
            a.seedEdgeByBias(
                biasMethod=SINGLE, 
                end2Edges=found_edges,
                minSize=minSize,
                maxSize=maxSize,
                constraint=FINER
            )

    print(f">>> Bias Mesh applyed in {len(depths)} instance lines '{name_instance}'!")



def CreateMeshSizeHorizontal(name_model, name_instance, filtered_layers, radius_middle, elementSize, deviationFactor):
    # Get the model and part
    m = mdb.models[name_model]
    a = m.rootAssembly

    inst = a.instances[name_instance]

    depths = []

    for layer in filtered_layers:
        depths.append(layer['Top'])

    depths.append(filtered_layers[-1]['Bottom'])  

    found_lines = 0

    for z in depths:

        found_edges = inst.edges.findAt(((radius_middle, -z, 0.0), ))

        if found_edges: 
            # edge = p.edges.findAt(((radius_middle, -z, 0.0), ))
            edge = found_edges[0]
            found_lines += 1

            a.seedEdgeBySize(
                edges=(edge, ),
                size=elementSize,
                deviationFactor=deviationFactor,
                constraint=FINER
            )

    print(f">>> Uniform mesh (Size: {elementSize}) applyed in {found_lines} lines of '{name_instance}.'")    
    
