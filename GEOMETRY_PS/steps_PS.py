from abaqus import mdb
from abaqusConstants import *
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import numpy as np

STEPS = {
    'init': 'Initial',
    'geo': 'Geostatic',
    'trans': 'Transition',
    'tempdefine': 'TempDefine',
    'perf': 'Perf_10_375',
    'perf_creep': 'Perf_10_375_Creep',
    'rev': 'Rev_9_875',
    'rev_creep': 'Rev_9_875_Creep'
}


def CreateSteps(modelName, STEPS, NIgeom=ON):  
    m = mdb.models[modelName]
    
    #### GEOSTATIC STEP #####################################################
    m.GeostaticStep(name=STEPS['geo'], previous=STEPS['init'], nlgeom=NIgeom)
    
    #### TRANSITION STEP ##################################################### 
    m.StaticStep(name=STEPS['trans'], previous=STEPS['geo'], nlgeom=NIgeom, 
                 timePeriod=2.0, maxNumInc=100, initialInc=1.0, 
                 minInc=2e-05, maxInc=2.0)
                     
    #### TEMPDEFINE STEP #####################################################
    m.StaticStep(name=STEPS['tempdefine'], previous=STEPS['trans'], nlgeom=NIgeom,
                 timePeriod=3.0, maxNumInc=100, initialInc=1.0, 
                 minInc=3e-05, maxInc=3.0)
    
    #### PERF_10_375 STEP ####################################################
    m.StaticStep(name=STEPS['perf'], previous=STEPS['tempdefine'], nlgeom=NIgeom,
                 timePeriod=1.0, maxNumInc=100, initialInc=1.0, 
                 minInc=1e-15, maxInc=1.0)
    
    #### PERF_10_375_CREEP STEP ##############################################
    m.ViscoStep(name=STEPS['perf_creep'], previous=STEPS['perf'], nlgeom=NIgeom, 
                timePeriod=172800.0, maxNumInc=1000000, initialInc=1.0, 
                minInc=1e-15, maxInc=172800.0, cetol=0.01)
                    
    #### REV_9_875 STEP ######################################################
    m.StaticStep(name=STEPS['rev'], previous=STEPS['perf_creep'], nlgeom=NIgeom, 
                 maxNumInc=100, initialInc=1.0, minInc=1e-15, maxInc=1.0)
    
    #### REV_9_875_CREEP STEP ################################################
    m.ViscoStep(name=STEPS['rev_creep'], previous=STEPS['rev'], nlgeom=NIgeom,
                timePeriod=945907000.0, maxNumInc=1000000, initialInc=1.0, 
                minInc=1e-15, maxInc=15552000.0, cetol=0.01)

def CreateBoundaryConditionSteps(modelName, STEPS, stepName):
    m = mdb.models[modelName]
    a = m.rootAssembly
    name_instances = a.instances.keys()
    name_sets = a.sets.keys()
    
    # ========================================================
    # BOUNDARY CONDITIONS em X                             ###
    # ======================================================== 
    if stepName == STEPS['init']:
        if 'ROCK' in name_instances:
            inst_rock = a.instances['ROCK']
            if 'FASEI_WELL' in inst_rock.sets.keys():
                region_well = inst_rock.sets['FASEI_WELL']
                m.EncastreBC(name='FIX_FASEI_WELL', createStepName=stepName, 
                        region=region_well, localCsys=None)
            if 'ROCK_BC' in inst_rock.sets.keys():
                region_rock = inst_rock.sets['ROCK_BC']
                m.EncastreBC(name='FIX_ROCK_BC', createStepName=stepName, 
                        region=region_rock, localCsys=None)

        if 'PIPE' in name_instances:
            inst_pipe = a.instances['PIPE']    
            if  'FASEI_PIPE' in inst_pipe.sets.keys():
                region_rev = inst_pipe.sets['FASEI_PIPE']
                m.PinnedBC(name='PIN_FASEI', createStepName=stepName, 
                        region=region_rev, localCsys=None)
                            
        if  'YSYM' in name_sets:
            region_base = a.sets['YSYM']
            m.YsymmBC(name='YSYM_BASE', createStepName=stepName, 
                    region=region_base, localCsys=None)
            
        if 'REFPT' in name_sets:
            region_rp = a.sets['REFPT']
            m.EncastreBC(name='REFPT', createStepName=stepName, 
                region=region_rp, localCsys=None)

    # ========================================================
    # DESATIVAÇÃO EM OUTROS STEPS                          ###
    # ======================================================== 
    elif stepName == STEPS['perf']:
        # Boa prática: Verificar se a BC existe antes de desativar
        if 'FIX_FASEI_WELL' in m.boundaryConditions.keys():
            m.boundaryConditions['FIX_FASEI_WELL'].deactivate(stepName)
            
    elif stepName == STEPS['rev']:
        if 'PIN_FASEI' in m.boundaryConditions.keys():
            m.boundaryConditions['PIN_FASEI'].deactivate(stepName)



def CreateFieldHistoryOutput(modelName, STEPS, stepName):
    m = mdb.models[modelName]
    a = m.rootAssembly
    name_instances = a.instances.keys()
    
    ####### COMENTEI OS TIMEPOINT - para podermos saber o momento exato em que a rocha encostou no Casing
    # if 'timePoint' not in m.timePoints.keys():
    #     m.TimePoint(name='timePoint', points=((1.0, ), (3600.0, ), 
    #         (7200.0, ), (14400.0, ), (28800.0, ), (57600.0, ), (86400.0, ), (
    #         172800.0, ), (345600.0, ), (691200.0, ), (1382400.0, ), (2764800.0, ), 
    #         (5529600.0, ), (11059200.0, ), (22118400.0, ), (31536000.0, ), (
    #         63072000.0, ), (126144000.0, ), (252288000.0, ), (504576000.0, ), (
    #         946080000.0, )))
    
    # ========================================================
    # FIELD OUTPUTS                                        ###
    # ======================================================== 
    if stepName == STEPS['geo']:
        if 'PIPE' in name_instances:
            inst_pipe = a.instances['PIPE']    
            if  'FASEI_PIPE' in inst_pipe.sets.keys():
                region_rev = inst_pipe.sets['FASEI_PIPE']
                m.FieldOutputRequest(name='FASEI_PIPE', 
                    createStepName=stepName, variables=('S', 'MISES', 'E', 'PE', 'U', 'NT'), 
                    region=region_rev, sectionPoints=DEFAULT, rebar=EXCLUDE, 
                    frequency=1, position=INTEGRATION_POINTS)
        
        if 'ROCK' in name_instances:
            inst_rock = a.instances['ROCK']
            if  'ROCK_OUTPUT' in inst_rock.sets.keys():
                region_rock = a.allInstances['ROCK'].sets['ROCK_OUTPUT']
                m.FieldOutputRequest(name='ROCK_OUTPUT', 
                    createStepName=stepName, variables=('U', 'TEMP'), 
                    region=region_rock, sectionPoints=DEFAULT, rebar=EXCLUDE, 
                    frequency=1, position=INTEGRATION_POINTS)
        
                if 'F-Output-1' in m.fieldOutputRequests.keys():
                    del m.fieldOutputRequests['F-Output-1']
                if 'H-Output-1' in m.historyOutputRequests.keys():
                    del m.historyOutputRequests['H-Output-1']

    if stepName == STEPS['trans']:
        if 'FASEI_PIPE' in m.fieldOutputRequests.keys():  
            m.fieldOutputRequests['FASEI_PIPE'].setValuesInStep(
                stepName=stepName, timeMarks=ON, timePoint='timePoint')
            
        if 'ROCK_OUTPUT' in m.fieldOutputRequests.keys():
            m.fieldOutputRequests['ROCK_OUTPUT'].setValuesInStep(
                stepName=stepName, timeMarks=ON, timePoint='timePoint')
                

def CreatePredefinedFieldSteps(modelName, STEPS):
    m = mdb.models[modelName]
    a = m.rootAssembly
    name_instances = a.instances.keys()
    
    # ========================================================
    # PREDEFINED FIELD no INITIAL STEP                     ###
    # ======================================================== 
    if STEPS['init'] in m.steps.keys():
        if 'PIPE' in name_instances:
            inst_pipe = a.instances['PIPE']
            fase_name = 'FASEI_PIPE'

            if fase_name in inst_pipe.sets.keys():
                region = inst_pipe.sets[fase_name]
                m.Stress(name=f'S_{fase_name}', region=region, 
                    distributionType=UNIFORM, sigma11=0.0, sigma22=0.0, 
                    sigma33=-16570100.0, sigma12=0.0, sigma13=None, sigma23=None)
                
        if 'ROCK' in name_instances:
            inst_rock = a.instances['ROCK']
            fase_name = 'FASEI_ROCK'

            if fase_name in inst_rock.sets.keys():
                region = inst_rock.sets[fase_name]
                m.Stress(name=f'S_{fase_name}', region=region, 
                distributionType=UNIFORM, sigma11=-54536500.0, sigma22=-54536500.0, 
                sigma33=-54536500.0, sigma12=0.0, sigma13=None, sigma23=None)
                
    # ========================================================
    # PREDEFINED FIELD em TEMPERATURE                      ###
    # ======================================================== 
    if STEPS['tempdefine'] in m.steps.keys():
        temperature_value = 337.5  # Kelvin

        # Mapeamento: Instância -> Lista de Sets que receberão a temperatura
        alvos_temperatura = {
            'PIPE': ['FASEI', 'FASEI_COMPLETED_WELL'],
            'ROCK': ['FASEI_ROCK', 'ROCK_BC']}

        for nome_instancia, lista_sets in alvos_temperatura.items():
            if nome_instancia in name_instances:
                instancia = a.instances[nome_instancia]

                for fase_name in lista_sets:
                    region = None
                    origem = ""

                    # 1. Busca primeiro no Assembly
                    if fase_name in a.sets.keys():
                        region = a.sets[fase_name]
                        origem = "Assembly"
                    # 2. Se não achar, busca na Instância
                    elif fase_name in instancia.sets.keys():
                        region = instancia.sets[fase_name]
                        origem = f"Instância '{nome_instancia}'"

                    # 3. Se encontrou em qualquer um dos dois, aplica a temperatura
                    if region is not None:
                        m.Temperature(
                            name=f'NT_{fase_name}', 
                            createStepName=STEPS['tempdefine'], 
                            region=region, 
                            distributionType=UNIFORM, 
                            crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
                            magnitudes=(temperature_value, )
                        )
                        print(f"[OK] Temperatura aplicada no set '{fase_name}' (Origem: {origem}).")
                    else:
                        print(f"[AVISO] Set '{fase_name}' não foi encontrado nem no Assembly nem na instância '{nome_instancia}'.")
               
                
def CreateLoads(modelName, STEPS):
    m = mdb.models[modelName]
    a = m.rootAssembly
    name_instances = a.instances.keys()
    name_steps = m.steps.keys()
    
    # ========================================================
    # LOADS em PRESSURE                                    ###
    # ======================================================== 
    if STEPS['perf'] in name_steps:
        if 'ROCK' in name_instances:
            inst_rock = a.instances['ROCK']
            fase_name = 'FASEI_OPEN_WELL'
            region_rock = None

            # Busca híbrida por superfícies (Assembly -> Instância ROCK)
            if fase_name in a.surfaces.keys():
                region_rock = a.surfaces[fase_name]
            elif fase_name in inst_rock.surfaces.keys():
                region_rock = inst_rock.surfaces[fase_name]

            if region_rock is not None:
                m.Pressure(
                    name=f'P_{fase_name}', createStepName=STEPS['perf'], 
                    region=region_rock, distributionType=UNIFORM, field='', 
                    magnitude=36969400.0, amplitude=UNSET)
                print(f"[OK] Carga 'P_{fase_name}' criada no step '{STEPS['perf']}'.")
            else:
                print(f"[AVISO] Superfície '{fase_name}' não encontrada para criar a carga.")

    # ========================================================
    # LOADS em PRESSURE (STEP REV)                         ###
    # ======================================================== 
    if STEPS['rev'] in name_steps:
        # 1. Carga no FLUIDO (Busca segura em todas as instâncias se não achar no Assembly)
        fase_name_fluid = 'FASEI_FLUID_ALT'
        region_fluid = None
        surf = a.surfaces.keys()

        if fase_name_fluid in surf:
            region_fluid = a.surfaces[fase_name_fluid]
        else:
            # Se não estiver no rootAssembly, busca dentro de cada instância do Assembly
            for inst_name, inst_obj in a.instances.items():
                if fase_name_fluid in inst_obj.surfaces:
                    region_fluid = inst_obj.surfaces[fase_name_fluid]
                    print(f"[INFO] Superfície '{fase_name_fluid}' encontrada dentro da instância '{inst_name}'.")
                    break
        # Cria a carga caso a superfície tenha sido localizada em qualquer um dos níveis
        if region_fluid is not None:
            m.Pressure(
                name=f'P_{fase_name_fluid}', createStepName=STEPS['rev'], 
                region=region_fluid, distributionType=UNIFORM, 
                field='', magnitude=36969400.0, amplitude=UNSET
            )
            print(f"[OK] Carga 'P_{fase_name_fluid}' criada no step '{STEPS['rev']}'.")
        else:
            print(f"[AVISO] Superfície '{fase_name_fluid}' não encontrada no modelo.")
        
        # 2. Carga no FLUIDO (Busca segura em todas as instâncias se não achar no Assembly)    
        if 'PIPE' in name_instances:
            inst_pipe = a.instances['PIPE']
            fase_name = 'FASEI_COMPLETED_WELL'
            region_pipe = None

            if fase_name in a.surfaces.keys():
                region_pipe = a.surfaces[fase_name]
            elif fase_name in inst_pipe.surfaces.keys():
                region_pipe = inst_pipe.surfaces[fase_name]

            if region_pipe is not None:
                m.Pressure(
                    name=f'P_{fase_name}', createStepName=STEPS['rev'], 
                    region=region_pipe, distributionType=UNIFORM, 
                    field='', magnitude=36969400.0, amplitude=UNSET
                )
                print(f"[OK] Carga 'P_{fase_name}' criada no step '{STEPS['rev']}'.")
            else:
                print(f"[AVISO] Superfície '{fase_name}' não encontrada em PIPE/Assembly.")
        
            
        # 3. Desativar a Carga na ROCHA
        if 'ROCK' in name_instances:
            set_desactive = ['FASEI_OPEN_WELL']
            
            for nome_set in set_desactive:                
                nome_carga = f'P_{nome_set}'  # Corrigido: Montamos o nome 'P_...' antes de checar!
                
                if nome_carga in m.loads.keys():
                    m.loads[nome_carga].deactivate(STEPS['rev'])
                    print(f"[OK] Carga '{nome_carga}' desativada com sucesso no step '{STEPS['rev']}'.")
                else:
                    print(f"[AVISO] Tentativa de desativar '{nome_carga}', mas ela não existe em m.loads.")
        
def CreateInteractionProperties(modelName):     
    m = mdb.models[modelName]    
    a = m.rootAssembly
    
    m.ContactProperty('C_FASEI')
    m.interactionProperties['C_FASEI'].TangentialBehavior(formulation=PENALTY, 
                directionality=ISOTROPIC, slipRateDependency=OFF, pressureDependency=OFF, 
                temperatureDependency=OFF, dependencies=0, table=((0.5, ), ), 
                shearStressLimit=None, maximumElasticSlip=FRACTION, fraction=0.005, 
                elasticSlipStiffness=None)
    m.interactionProperties['C_FASEI'].NormalBehavior(pressureOverclosure=HARD, 
                allowSeparation=ON, constraintEnforcementMethod=DEFAULT)

def CreateInteraction(modelName, STEPS):
    m = mdb.models[modelName]
    a = m.rootAssembly
    name_instances = a.instances.keys()
    c_fasei = m.interactionProperties['C_FASEI']

    # ========================================================
    # INTERECTION: STEP GEOSTATIC                          ###
    # ======================================================== 
    if STEPS['geo'] in m.steps.keys():
        name_modchange = {
            'PIPE': ['FASEI_PIPE'],
            'FLUID': ['FASEI_FLUID']
            }
        for name_inst, fasei_names in name_modchange.items():
            if name_inst in name_instances:
                inst = a.instances[name_inst]

                for f_name in fasei_names:
                    region = None
                    if f_name in a.sets.keys():
                        region = a.sets[f_name]
                    elif f_name in inst.sets.keys():
                        region = inst.sets[f_name]
                    
                    if region is not None:
                        m.ModelChange(name=f'MC_{f_name}', createStepName=STEPS['geo'], 
                            region=region, activeInStep=False, 
                            includeStrain=False)
                        print(f"[OK] Model Change criado com sucesso e aplicado ao Set '{f_name}'.")
                    else:
                        print(f"[AVISO] Set '{f_name}' não foi encontrado nem no Assembly nem na instância '{name_inst}'.")
    
    # ========================================================
    # INTERECTION: STEP REV_9_875                          ###
    # ======================================================== 
    if STEPS['rev'] in m.steps.keys():
        region_master = None
        region_slave = None
        
        # 1. Busca a superfície MASTER (Geralmente no PIPE ou Assembly)
        if 'PIPE' in name_instances and 'FASEI_MASTER' in a.instances['PIPE'].surfaces.keys():
            region_master = a.instances['PIPE'].surfaces['FASEI_MASTER']
        elif 'FASEI_MASTER' in a.surfaces.keys():
            region_master = a.surfaces['FASEI_MASTER']

        # 2. Busca a superfície SLAVE (Geralmente na ROCK ou Assembly)
        if 'ROCK' in name_instances and 'FASEI_SLAVE' in a.instances['ROCK'].sets.keys():
            region_slave = a.instances['ROCK'].sets['FASEI_SLAVE']
        elif 'FASEI_SLAVE' in a.sets.keys():
            region_slave = a.sets['FASEI_SLAVE']

        if region_master is not None and region_slave is not None:
            m.SurfaceToSurfaceContactStd(name=c_fasei.name, 
                createStepName=STEPS['rev'], main=region_master, secondary=region_slave, 
                sliding=FINITE, thickness=ON, interactionProperty=c_fasei.name, 
                adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
                clearanceRegion=None)
                    
            print(f"[OK] Interaction '{c_fasei.name}' criada com sucesso entre superfícies MASTER e SLAVE.")
        else:
            print("[ERRO] Superfícies 'FASEI_MASTER' ou 'FASEI_SLAVE' não foram encontradas no modelo.")
                            
        # ========================================================
        # REATIVANDO MODEL CHANGE NO STEP REV (Opcional)       ###
        # ========================================================
        if 'PIPE' in name_instances:
            sets_reativar = ['FASEI_PIPE']
            for nome_set in sets_reativar:
                nome_interacao = f'MC_{nome_set}'  # Sem o '+' aqui!
                
                if nome_interacao in m.interactions.keys():
                    m.interactions[nome_interacao].setValuesInStep(
                        stepName=STEPS['rev'], 
                        activeInStep=True)
                    print(f"[OK] Model Change '{nome_interacao}' reativado com sucesso no step REV.")
                else:
                    print(f"[AVISO] Interação '{nome_interacao}' não foi encontrada em m.interactions.")