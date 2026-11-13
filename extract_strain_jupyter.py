from odbAccess import openOdb
from abaqusConstants import INTEGRATION_POINT
import sys

def ExportRockStrainsAllFrames(odb_path, output_file):
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

    # Focando diretamente no passo de fluência
    target_step_name = 'Cas_9_875_Creep'

    with open(output_file, 'w') as f:
        # Cabeçalho do CSV
        f.write("Time_s,Element_Label,LE11,LE22,LE33,PEEQ\n")

        if target_step_name in odb.steps.keys():
            step = odb.steps[target_step_name]

            for frame in step.frames:
                time = frame.frameValue

                # Verifica se as variáveis existem no frame para evitar erros
                if 'LE' not in frame.fieldOutputs or 'PEEQ' not in frame.fieldOutputs:
                    continue

                le_field = frame.fieldOutputs['LE'].getSubset(region=target_set, position=INTEGRATION_POINT)
                peeq_field = frame.fieldOutputs['PEEQ'].getSubset(region=target_set, position=INTEGRATION_POINT)

                for le_val, peeq_val in zip(le_field.values, peeq_field.values):
                    e_label = le_val.elementLabel

                    # No Abaqus, os índices do tensor de deformação são: 0->11(X), 1->22(Y), 2->33(Z)
                    le11 = le_val.data[0]
                    le22 = le_val.data[1]
                    le33 = le_val.data[2]
                    peeq = peeq_val.data

                    f.write("{},{},{},{},{},{}\n".format(time, e_label, le11, le22, le33, peeq))
        else:
            print("Aviso: Step '{}' nao encontrado.".format(target_step_name))

    odb.close()
    print(">>> Sucesso! Dados de deformacao exportados para: " + output_file)

if __name__ == "__main__":
    odb_file = "WellClosureJob.odb" 
    csv_file = "dados_strain_sal.csv"
    ExportRockStrainsAllFrames(odb_file, csv_file)
