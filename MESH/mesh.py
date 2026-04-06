from abaqus import mdb
from abaqusConstants import *

def CreateMeshBiasHorizontal(name_model, name_part, filtered_layers, radius_middle):
    # Get the model and part
    m = mdb.models[name_model]
    p = m.parts[name_part]
    e = p.edges

    depths = []

    for layer in filtered_layers:
        depths.append(layer['Top'])

    depths.append(filtered_layers[-1]['Bottom'])  

    points_search = []

    for z in depths:
        points_search.append( ((radius_middle, -z, 0.0), ) )

    horizontal_lines = e.findAt(*points_search)

    p.seedEdgeByBias(
        biasMethod=SINGLE, 
        end1Edges=horizontal_lines,
        ratio=5.0,
        number=100,
        constraint=FINER
    )

    print(f">>> Bias Mesh applyed in {len(depths)} horizontal lines!")
    