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
        # 1. Cabeçalho atualizado para incluir SP1 e SP3
        f.write("Time_s,Element_Label,p_PRESS_MPa,q_MISES_MPa,SP1_MPa,SP3_MPa\n")

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

                    # 2. Extração direta das tensões principais do tensor 'S' do Abaqus
                    sp1_val = s_val.maxPrincipal
                    sp3_val = s_val.minPrincipal

                    # 3. Escrita com os 6 parâmetros
                    f.write("{},{},{},{},{},{}\n".format(time, e_label, p_val, q_val, sp1_val, sp3_val))

    odb.close()
    print(">>> Sucesso! Curvas completas exportadas para: " + output_file)

# Ponto de entrada quando executado pelo terminal do Abaqus
if __name__ == "__main__":
    odb_file = "WellClosureJob.odb" 
    csv_file = "dados_principais_sal.csv" # Nome atualizado para evitar sobrescrever o anterior
    ExportRockStressesAllFrames(odb_file, csv_file)
