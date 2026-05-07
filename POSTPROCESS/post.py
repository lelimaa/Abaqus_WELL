# from abaqus import mdb
# from abaqusConstants import *

from odbAccess import openOdb
import visualization

def ExportDisplacementHistory(odb_path, node_label, instance_name, output_file):
    odb = openOdb(path=odb_path)

    data_list = []

    for step_name in odb.steps.keys():
        step = odb.steps[step_name]

        for frame in step.frames:
            time_value = frame.frameValue

            u_field = frame.fieldOutputs['U']

            sub_field = u_field.getSubset(
                region=odb.rootAssembly.instances[instance_name],           
            )

            for val in sub_field.values:
                if val.nodeLabel == node_label:
                    u1_val = val.data[0]
                    data_list.append((time_value, u1_val))
                    break

            # if sub_field.values:
            #     u1_val = sub_field.values[0].data[0]
            #     data_list.append((time_value, u1_val))

    with open(output_file, 'w') as f:
        f.write("Time (s), Displacement U1 (m)\n")
        for time, u1 in data_list:
            f.write(f"{time}, {u1}\n")

    odb.close()
    print(f">>> Exported data successfully to: {output_file}")

