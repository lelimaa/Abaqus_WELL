from abaqus import mdb
from abaqusConstants import *

def CreateSetsPipe(name_model):
    """
    Creates all the sets corresponding to the pipe.
    """
    m = mdb.models[name_model]
    p = m.parts['PIPE']
    f = p.faces
    e = p.edges

    # FASEI_REV, FASEI_REV_ABOVE_TOC
    all_faces = f[0:len(f)]
    p.Set(faces=all_faces, name='FASEI_REV')
    p.Set(faces=all_faces, name='FASEI_REV_ABOVE_TOC')


    # FASEI_REV_BASE    
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
    """
    Creates all the sets present in the fluid (annular space).
    """
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
    """
    Creates all the sets corresponding to the rock layers, including individually 
    for all the lithologies.
    """
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
    all_heights = sorted(list(set([vert.pointOn[0][1] for vert in v])))
    inverted_heights = sorted(all_heights, reverse=True)
    descendant_interfaces = inverted_heights[1:]

    for i, height_y in enumerate(descendant_interfaces):
        name_set = 'L' + str(i+1) + '-I_BASE'

        edges_interface = e.getByBoundingBox(
            xMin=-1e20, yMin=height_y - tol, zMin=-tol,
            xMax=1e20, yMax=height_y + tol, zMax=tol
        )

        if edges_interface:
            p.Set(edges=edges_interface, name=name_set)
            print(f"Set '{name_set}' automatically created in Y = {height_y}")


    # L1-I_ID, L2-I_ID, L3-I_ID, ... , LN-I_ID
    heights = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)
    min_x = min([vert.pointOn[0][0] for vert in v])

    for i in range(len(heights) - 1):
        y_top = heights[i]
        y_base = heights[i+1]

        y_middle = (y_top + y_base) / 2.0

        name_set = 'L' + str(i+1) + '-I_ID'

        edge_found = e.findAt(((min_x, y_middle, 0.0), ))

        if edge_found:
            p.Set(edges=edge_found, name=name_set)
            print(f"Set '{name_set}' created with sucess in the medium point Y={y_middle}")


    # L1-I_OD, L2-I_OD, L3-I_OD, ... , LN-I_OD
    heights = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)
    max_x = max([vert.pointOn[0][0] for vert in v])

    for i in range(len(heights)-1):
        y_top = heights[i]
        y_base = heights[i+1]

        y_middle = (y_top+y_base) / 2.0

        name_set = 'L' + str(i+1) + '-I_OD'

        edge_found = e.findAt(((max_x, y_middle, 0.0), ))

        if edge_found:
            p.Set(edges=edge_found, name=name_set)
            print(f"Set '{name_set}' created with success in X={max_x}, Y={y_middle}")

    # L1-I_TOP, L2-I_TOP, L3-I_TOP, ... , LN-I_TOP
    heights = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)

    for i in range(len(heights) - 1):
        height_top_layer = heights[i]
        name_set = 'L' +str(i+1)+ '-I_TOP'

        edges_top = e.getByBoundingBox(
            xMin=-1e20, yMin=height_top_layer - tol, zMin=-tol,
            xMax=1e20, yMax=height_top_layer + tol, zMax=tol
        )

        if edges_top:
            p.Set(edges=edges_top, name=name_set)
            print(f"Set '{name_set}' created in the height Y = {height_top_layer}")

    # L1-I, L2-I, L3-I, ... , LN-I
    heights = sorted(list(set([vert.pointOn[0][1] for vert in v])), reverse=True)

    min_x = min([vert.pointOn[0][0] for vert in v])
    max_x = max([vert.pointOn[0][0] for vert in v])
    x_middle_face = (min_x + max_x) / 2.0

    for i in range(len(heights)-1):
        y_top = heights[i]
        y_base = heights[i+1]

        y_middle_layer = (y_top + y_base) / 2.0

        name_set = 'L' + str(i+1) + '-I'

        point_search = ((x_middle_face, y_middle_layer, 0.0), )

        face_found = f.findAt(point_search)

        if face_found:
            p.Set(faces=face_found, name=name_set)
            print(f"Set of Face '{name_set}' created in X={x_middle_face}, Y={y_middle_layer}")

def CreateSetsAssembly(name_model): 
    """
    Creates all the sets corresponding to the assembly.
    """ 
    m = mdb.models[name_model]  
    a = m.rootAssembly
    
    # ALL    
    faces_total = None

    for inst in a.instances.values():
        if faces_total is None:
            faces_total = inst.faces[:]
        else:
            faces_total = faces_total + inst.faces[:]

    a.Set(faces=faces_total, name='ALL')

    # FASEI
    names_instances = ['FLUID_INST', 'PIPE_INST']
    faces_total = None

    for name in names_instances:
        if name in a.instances.keys():
            inst = a.instances[name]
            if faces_total is None:
                faces_total = inst.faces[:]
            else:
                faces_total = faces_total + inst.faces[:]

    if faces_total:
        a.Set(faces=faces_total, name='FASEI')
        print("Set 'ALL' created with all faces from the 2 instances.")

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
    print(f"Set FASEI_OPEN_WELL created at the interface X = {x_interface}")  

    a.Set(edges=edges_r, name='FASEI_WELL') # if only from rock
    print(f"Set FASEI_WELL created at the interface X = {x_interface}")  


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
        print(f"Set 'FASEI_COMPLETED_WELL' created at the internal face of the Pipe (X = {x_int_pipe})")


    # MESH_TT_PIPES
    inst_p = a.instances['PIPE_INST']
    heights_pipe = sorted(list(set([v.pointOn[0][1] for v in inst_p.vertices])))

    min_x_p = min([v.pointOn[0][0] for v in inst_p.vertices])
    max_x_p = max([v.pointOn[0][0] for v in inst_p.vertices])

    edges_tt = None

    for y in heights_pipe:
        edges_layer = inst_p.edges.getByBoundingBox(
            xMin=min_x_p - tol, yMin=y - tol, zMin=-tol,
            xMax=max_x_p + tol, yMax=y + tol, zMax=tol
        )

        if edges_layer:
            if edges_tt is None:
                edges_tt = edges_layer
            else:
                edges_tt = edges_tt + edges_layer

    if edges_tt:
        a.Set(edges=edges_tt, name='MESH_TT_PIPES')
        print(f"Set 'MESH_TT_PIPES' created with {len(edges_tt)} horizontal edges.")

    # MESH_TT_PIPES
    inst_f = a.instances['FLUID_INST']
    heights_annular = sorted(list(set([v.pointOn[0][1] for v in inst_f.vertices])))

    min_x_a = min([v.pointOn[0][0] for v in inst_f.vertices])
    max_x_a = max([v.pointOn[0][0] for v in inst_f.vertices])

    edges_tt = None

    for y in heights_annular:
        edges_layer = inst_f.edges.getByBoundingBox(
            xMin=min_x_a - tol, yMin=y - tol, zMin=-tol,
            xMax=max_x_a + tol, yMax=y + tol, zMax=tol
        )

        if edges_layer:
            if edges_tt is None:
                edges_tt = edges_layer
            else:
                edges_tt = edges_tt + edges_layer

    if edges_tt:
        a.Set(edges=edges_tt, name='MESH_TT_ANNULARS')
        print(f"Set 'MESH_TT_ANNULARS' created with {len(edges_tt)} horizontal edges.")  


    # MESH_TT_ROCK
    inst_r = a.instances['ROCK_INST']
    heights_rock = sorted(list(set([v.pointOn[0][1] for v in inst_r.vertices])))

    min_x_r = min([v.pointOn[0][0] for v in inst_r.vertices])
    max_x_r = max([v.pointOn[0][0] for v in inst_r.vertices])

    edges_tt = None

    for y in heights_rock:
        edges_layer = inst_r.edges.getByBoundingBox(
            xMin=min_x_r - tol, yMin=y - tol, zMin=-tol,
            xMax=max_x_r + tol, yMax=y + tol, zMax=tol
        )

        if edges_layer:
            if edges_tt is None:
                edges_tt = edges_layer
            else:
                edges_tt = edges_tt + edges_layer

    if edges_tt:
        a.Set(edges=edges_tt, name='MESH_TT_ROCK')
        print(f"Set 'MESH_TT_ROCK' created with {len(edges_tt)} horizontal edges.")           


    # MESH_VERTICAL
    instances = ['FLUID_INST', 'PIPE_INST', 'ROCK_INST']
    edges_verticals_total = None

    for name in instances:
        if name in a.instances.keys():
            inst = a.instances[name]
            edges_of_instance = inst.edges

            indexes_verticals = []

            for i, edge in enumerate(edges_of_instance):
                v1 = inst.vertices[edge.getVertices()[0]]
                v2 = inst.vertices[edge.getVertices()[1]]

                if abs(v1.pointOn[0][0] - v2.pointOn[0][0]) < tol:
                    indexes_verticals.append(edge)

            if indexes_verticals:
                temp_seq = inst.edges[0:0]
                for ed in indexes_verticals:
                    temp_seq = temp_seq + inst.edges[ed.index:ed.index+1]

                if edges_verticals_total is None:
                    edges_verticals_total = temp_seq
                else:
                    edges_verticals_total = edges_verticals_total + temp_seq

    if edges_verticals_total:
        a.Set(edges=edges_verticals_total, name='MESH_VERTICAL')
        print("Set 'MESH_VERTICAL' created with success (all vertical edges).")

    # ROCK_BC
    inst_r = a.instances['ROCK_INST']
    x_external_rock = max([v.pointOn[0][0] for v in inst_r.vertices])

    y_min = min([v.pointOn[0][1] for v in inst_r.vertices])
    y_max = max([v.pointOn[0][1] for v in inst_r.vertices])

    edges_bc = inst_r.edges.getByBoundingBox(
        xMin=x_external_rock - tol, yMin=y_min - tol, zMin=-tol,
        xMax=x_external_rock + tol, yMax=y_max + tol, zMax=tol
    )

    if edges_bc:
        a.Set(edges=edges_bc, name='ROCK_BC')
        print(f"Set 'ROCK_BC' created with success at the border X = {x_external_rock}")

    # ROCK_OUTPUT
    name_instance = ['ROCK_INST']
    faces_total = None

    for name in name_instance:
        if name in a.instances.keys():
            inst = a.instances[name]
            if faces_total is None:
                faces_total = inst.faces[:]
            else:
                faces_total = faces_total + inst.faces[:]

    if faces_total:
        a.Set(faces=faces_total, name='ROCK_OUTPUT')
        print("Set 'ROCK_OUTPUT' created with all faces from this instance.")


    # YSYM_BASE
    # 1. Identify the minimum height (Y) globally in the model
    # We search all instances to find the "floor"
    y_global = []
    for inst in a.instances.values():
        y_global.append(min([v.pointOn[0][1] for v in inst.vertices]))
    y_base = min(y_global)

    # 2. Create a list to accumulate the edges of the base of each instance
    edges_base_list = None

    for inst in a.instances.values():
        # Search for the horizontal edges of this specific instance that are at the y_base level
        # We limit the X to the bounds of the instance itself for precision
        x_min_i = min([v.pointOn[0][0] for v in inst.vertices])
        x_max_i = max([v.pointOn[0][0] for v in inst.vertices])
        
        edges_inst = inst.edges.getByBoundingBox(
            xMin=x_min_i - tol, yMin=y_base - tol, zMin=-tol,
            xMax=x_max_i + tol, yMax=y_base + tol, zMax=tol
        )
        
        # If we found edges at the base of this instance, add them to the "bag"
        if edges_inst:
            if edges_base_list is None:
                edges_base_list = edges_inst
            else:
                edges_base_list = edges_base_list + edges_inst

    # 3. Create the Set in the Assembly with the accumulated edges
    if edges_base_list:
        a.Set(edges=edges_base_list, name='YSYM_BASE')
        print("Set 'YSYM_BASE' created with success uniting all instances.")
    else:
        print("Error: No edges found at Y coordinate =", y_base)


    # YSYM_TOP
    # 1. Identify the maximum height (Y) globally in the model
    y_global_topo = []
    for inst in a.instances.values():
        y_global_topo.append(max([v.pointOn[0][1] for v in inst.vertices]))
    y_top = max(y_global_topo)

    # 2. Create a list to accumulate the edges of the top of each instance
    edges_top_list = None

    for inst in a.instances.values():
        # Search for the horizontal edges of this specific instance that are at the y_top level
        x_min_i = min([v.pointOn[0][0] for v in inst.vertices])
        x_max_i = max([v.pointOn[0][0] for v in inst.vertices])
        
        edges_inst = inst.edges.getByBoundingBox(
            xMin=x_min_i - tol, yMin=y_top - tol, zMin=-tol,
            xMax=x_max_i + tol, yMax=y_top + tol, zMax=tol
        )
        
        # If we found edges at the top of this instance, add them to the sequence
        if edges_inst:
            if edges_top_list is None:
                edges_top_list = edges_inst
            else:
                edges_top_list = edges_top_list + edges_inst

    # 3. Create the Set in the Assembly
    if edges_top_list:
        a.Set(edges=edges_top_list, name='YSYM_TOP')
        print(f"Set 'YSYM_TOP' created with success at Y coordinate = {y_top}")
    else:
        print("Error: No edges found at Y coordinate =", y_top)

def CreateSurfacesAssembly(modelName, data):
    """
    Creates all the surfaces corresponding to the assembly.
    """

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

    # INTERFACE SURFACE 
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

    # Creating the rock internal surfaces using edges from the rock instance FASEI_OPEN_WELL

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


##### These functions were created in order to display the results in the post processing phase at specific points of the model, such as the outer face of the pipe (bottom) and at the rock wall (bottom).
    
def CreateSetPointRock(model_name, r_coord, z_coord):
    """
    Creates the set corresponding to a point located at the bottom and the internal 
    surface of the well formation.
    """

    m = mdb.models[model_name]
    a = m.rootAssembly

    a.regenerate()
    
    # Change in the instance
    inst_rock = a.instances['ROCK_INST']
    
    # Remember the order (R, 0, -Z) that we corrected before
    target_coords = (r_coord, z_coord, 0.0)
    
    closest_nodes = inst_rock.nodes.getClosest(coordinates=(target_coords,))
    
    if closest_nodes:
        node_label = closest_nodes[0].label
        # Use a different name to avoid overwriting the PIPE set
        set_name = 'SET_ROCK_STRESS_MONITOR'
        
        if set_name in a.sets.keys():
            del a.sets[set_name]
            
        target_node_seq = inst_rock.nodes.sequenceFromLabels((node_label,))
        a.Set(name=set_name, nodes=target_node_seq)
        
        print("SUCESSO: Set of rock '%s' created (No: %d)" % (set_name, node_label))
        return a.sets[set_name]
    return None    
    
def CreateSetPointCasing(model_name, r_coord, z_coord):
    """
    Creates the set corresponding to a point located at the bottom and the internal 
    surface of the well formation.
    """
    
    m = mdb.models[model_name]
    a = m.rootAssembly
    
    # 1. Guarantee that the Assembly is updated with the new mesh
    a.regenerate()
    
    inst_pipe = a.instances['PIPE_INST']
    target_coords = (r_coord, z_coord, 0.0)
    
    # 2. Search for the closest node to capture its LABEL
    closest_nodes = inst_pipe.nodes.getClosest(coordinates=(target_coords,))
    
    if closest_nodes:
        node_label = closest_nodes[0].label # We get the identity number of the node
        set_name = 'SET_STRESS_MONITOR'
        
        # 3. Rigorous cleanup of the old Set
        if set_name in a.sets.keys():
            del a.sets[set_name]
            
        try:
            # 4. Create the Set by asking Abaqus to search for the node by its label
            # This is the most stable way to link instance nodes to the Assembly
            target_node_seq = inst_pipe.nodes.sequenceFromLabels((node_label,))
            a.Set(name=set_name, nodes=target_node_seq)
            
            print("SUCCESS: Set '%s' created (Node Label: %d)" % (set_name, node_label))
            return a.sets[set_name]
            
        except Exception as e:
            print(">>> Fatal Error in Set creation: %s" % str(e))
            return None
    else:
        print(">>> AVISO: No node found at coordinates (%.2f, %.2f)" % (r_coord, z_coord))
        return None    
    
