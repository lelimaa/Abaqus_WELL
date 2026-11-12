from odbAccess import openOdb
from abaqusConstants import INTEGRATION_POINT
import sys

def ExportRockStressesAllFrames(odb_path, output_file):
    try:
        odb = openOdb(path=odb_path)
    except Exception as e:
        print("Erro ao abrir o ODB: {}".format(e))
        return

    a = odb.rootAssembly
    set_name = 'FASEI_OPEN_WELL' 

    if set_name not in a.elementSets.keys():
        print("Erro: O Element Set '{}' nao foi encontrado.".format(set_name))
        odb.close()
        return

    target_set = a.elementSets[set_name]

    with open(output_file, 'w') as f:
        f.write("Time_s,Element_Label,p_PRESS_MPa,q_MISES_MPa\n")

        for step in odb.steps.values():
            for frame in step.frames:
                time = frame.frameValue

                # Extrai tensoes nos pontos de integracao
                press_field = frame.fieldOutputs['PRESSONLY'].getSubset(region=target_set, position=INTEGRATION_POINT)
                mises_field = frame.fieldOutputs['S'].getSubset(region=target_set, position=INTEGRATION_POINT)

                for press_val, s_val in zip(press_field.values, mises_field.values):
                    e_label = press_val.elementLabel
                    p_val = press_val.data
                    q_val = s_val.mises

                    # Usa .format() para garantir compatibilidade com Abaqus/Python 2.7 ou 3
                    f.write("{},{},{},{}\n".format(time, e_label, p_val, q_val))

    odb.close()
    print(">>> Sucesso! Curvas p-q exportadas para: " + output_file)

# Ponto de entrada quando executado pelo terminal do Abaqus
if __name__ == "__main__":
    # Substitua pelo caminho real do seu modelo no notebook
    odb_file = "WellClosureJob.odb" 
    csv_file = "dados_pq_sal.csv"
    ExportRockStressesAllFrames(odb_file, csv_file)
