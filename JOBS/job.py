from abaqus import *
from abaqusConstants import *

def CreateJob(name_model, name_job, num_cpus, run_now=True):
    mdb.Job(
        name=name_job,
        model=name_model,
        description='Well Geomechanical Simulation',
        type=ANALYSIS,
        atTime=None,
        waitMinutes=0,
        waitHours=0,
        queue=None,
        memory=90,
        memoryUnits=PERCENTAGE,
        getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE,
        nodalOutputPrecision=SINGLE,
        echoPrint=OFF,
        modelPrint=OFF,
        contactPrint=OFF,
        historyPrint=OFF,
        userSubroutine='',
        scratch='',
        resultsFormat=ODB,
        multiprocessingMode=DEFAULT,
        numCpus=num_cpus,
        numDomains=num_cpus,
        numGPUs=0
    )

    print(f">>> Job '{name_job}' created for model '{name_model}' with {num_cpus} CPUs!")

    if run_now:

        print(f">>> Submiting job '{name_job}' for analysis... Wait for it to finish!")

        mdb.jobs[name_job].submit(consistencyChecking=OFF)

        mdb.jobs[name_job].waitForCompletion()

        print(f">>> Job '{name_job}' completed!")

    else: 
        print(f">>> Job was only created. To run, submitt manually!")