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
