from abaqus import mdb
from abaqusConstants import *

import mesh

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
    
def CreateMeshVerticalBySet(name_model, name_set, element_size):
    m = mdb.models[name_model]
    a = m.rootAssembly

    vertical_lines = a.sets[name_set].edges

    a.seedEdgeBySize(
        edges=vertical_lines,
        size=element_size,
        deviationFactor=0.1,
        constraint=FINER
    )

    print(f">>> Uniform mesh (Size: {element_size}) applyed with success in set '{name_set}!'")

def CreateMeshVerticalWithBias(name_model, name_set, min_size, max_size):
    m = mdb.models[name_model]
    a = m.rootAssembly

    vertical_lines = a.sets[name_set].edges

    a.seedEdgeByBias(
        DOUBLE,
        vertical_lines,
        constraint=FINER,
        minSize=min_size,
        maxSize=max_size
        # ratio=bias_ratio,
        # numberElements=None,
    )

    print(f">>> Mesh Bias applyed: Interface ({min_size}) | Center ({max_size})")

    
def AttributeTypeElement(name_model, name_set):
    m = mdb.models[name_model]
    a = m.rootAssembly
    elemType1 = mesh.ElemType(elemCode=CAX4, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX3, elemLibrary=STANDARD,
                                secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    region_aim = a.sets[name_set]
    a.setElementType(regions=region_aim, elemTypes=(elemType1, elemType2))

    print(f">>> Element type CAX4 and CAX3 assigned to set '{name_set}'!")

def GenerateMesh(name_model, name_instance):
    m = mdb.models[name_model]
    a = m.rootAssembly

    inst = a.instances[name_instance]

    a.generateMesh(regions=(inst, ))

    print(f">>> Mesh generated with success for instance '{name_instance}'!")