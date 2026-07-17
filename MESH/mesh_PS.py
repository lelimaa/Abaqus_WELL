from abaqus import mdb
from abaqusConstants import *
import mesh

def CreateMeshBiasHorizontal(name_model, name_part, radius_middle):
    # Get the model and part
    m = mdb.models[name_model]
    a = m.rootAssembly
    # p = m.parts[name_part]
    p = a.instances[name_part]
    e = p.edges

    depths = []

    # for layer in filtered_layers:
    #     depths.append(layer['Top'])

    # depths.append(filtered_layers[-1]['Bottom'])  

    points_search = []

    for z in depths:
        edge = p.edges.findAt(((radius_middle, -z, 0.0), ))
        for ie, e in enumerate(edge):
            verts = [p.vertices[x] for x in e.getVertices()]
            if verts[0].pointOn[0][0] < verts[1].pointOn[0][0]:
                a.seedEdgeByBias(
                biasMethod=SINGLE, 
                end1Edges=edge[ie:ie+1],
                ratio=100.0,
                number=100,
                constraint=FINER
                )
            else:
                a.seedEdgeByBias(
                biasMethod=SINGLE, 
                end2Edges=edge[ie:ie+1],
                ratio=100.0,
                number=100,
                constraint=FINER
                )


    print(f">>> Bias Mesh applyed in {len(depths)} horizontal lines!")
    
def AttributeTypeElement(name_model, name_set):
    m = mdb.models[name_model]
    a = m.rootAssembly
    elemType1 = mesh.ElemType(elemCode=CAX4, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX3, elemLibrary=STANDARD,
                                secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    region_aim = a.sets[name_set]
    a.setElementType(regions=region_aim, elemTypes=(elemType1, elemType2))

    print(f">>> Element type CAX4 and CAX3 assigned to set '{name_set}'!")