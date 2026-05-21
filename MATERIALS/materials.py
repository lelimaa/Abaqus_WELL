from abaqus import mdb
from abaqusConstants import *

from part import *


def ElasticMaterial(modelName, name, data, sectionLength=1.):
    m = mdb.models[modelName]
    mat = m.Material(name=name)
    sect_name = name + '_Section'
    sect = m.HomogeneousSolidSection(name=sect_name,
                                     material=name,
                                     thickness=sectionLength)
    if data.get('density') is not None:
        mat.Density(table=((data.get('density'),),))

    if data.get('elastic') is not None:
        mat.Elastic(table=(data.get('elastic'),))

    if data.get('conductivity') is not None:
        mat.Conductivity(table=((data.get('conductivity'),),))

    if data.get('specific_heat') is not None:
        # raw_value = data.get('specific_heat')
        # corrected_spec_heat = raw_value * 4184.0 
        # mat.SpecificHeat(table=((corrected_spec_heat,),))
        mat.SpecificHeat(table=((data.get('specific_heat'),),))

    if data.get('expansion') is not None:
        mat.Expansion(table=((data.get('expansion'),),))
    subroutine = None
    return mat, sect, subroutine


def vonMisesMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    if data.get("stress_strain_curve") is not None:
        mat.Plastic(table=data["stress_strain_curve"])
    return mat, sect, subroutine


def MohrCoulombMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    phi = data.get("friction_angle")
    dilat = data.get("dilatancy_angle")
    c = data.get("cohesion")
    c = c * 1e6  # Convert from MPa to Pa
    ut = data.get("ultimate_traction")
    ut = ut * 1e6  # Convert from MPa to Pa
    labData = data.get("lab_data")
    if None in (phi, c, ut, labData):
        raise ValueError(
            "friction_angle, dilatancy_angle,  cohesion, ultimate traction, and lab_data must be provided for Mohr-Coulomb material.")
        return
    if dilat is None:
        dilat = 0.0
    mat.MohrCoulombPlasticity(table=((phi, dilat), ))
    # mat.mohrCoulombPlasticity.MohrCoulombHardening(table=labData)
    mat.mohrCoulombPlasticity.MohrCoulombHardening(table=((c, 0.0), ))
    mat.mohrCoulombPlasticity.TensionCutOff(temperatureDependency=OFF, dependencies=0,
                                            table=((ut, 0.0), ))

    return mat, sect, subroutine

    # mat.Creep(law=USER, table=())

def DoublePowerCreepMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    
    print(f"O nome que chegou na função foi: {name}")
    try:
        dp_data = data.get("DoublePowerParameters", {})
        A1 = dp_data["a1"] 
        A2 = dp_data["a2"] 
        B1 = dp_data["b1"]
        B2 = dp_data["b2"]
        C1 = dp_data["c1"]
        C2 = dp_data["c2"]
        ref_stress = dp_data["s0"]*1e6  # Converting from MPa to Pa
        mat.Creep(law=DOUBLE_POWER,
                  table=((A1, B1, C1, A2, B2, C2, ref_stress),))
    except:
        raise ValueError(
            "double_power_creep_data with A1, A2, B1, B2, C1, C2, and reference_stress must be provided for Double Power Creep material.")
    return mat, sect, subroutine


def DoubleMechanismCreepMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    mat.Creep(law=USER, table=())
    subroutine = {"CREEP": " my fortran subroutine "}
    return mat, sect, subroutine

def CreateMaterial(modelName, name, data, sectionLength=1.):
    behavior = data.get("behavior")
    mapping = {
        "ELASTIC": ElasticMaterial,
        "VON_MISES_PLASTIC": vonMisesMaterial,
        "MOHR_COULOMB": MohrCoulombMaterial,
        "DOUBLE_POWER_CREEP": DoublePowerCreepMaterial,
        "DOUBLE_MECHANISM_CREEP": DoubleMechanismCreepMaterial,
    }
    create_func = mapping.get(behavior)
    if create_func is not None:
        return create_func(modelName, name, data, sectionLength)
    else:
        raise ValueError("Behavior '%s' not recognized." % behavior)


def Assign_Section(modelName, partName, sectionName, setName=None, isSolid=True):
    model = mdb.models[modelName]
    # Only work with PIPE and FLUID from material_examples
    allowed_parts = ("PIPE", "FLUID")
    if partName not in allowed_parts:
        print("Skipping section assignment for '%s' (use AssignRockByDepth for rock materials)" % partName)
        return
    if partName not in model.parts:
        raise ValueError("Part '%s' not found in model '%s'." %
                         (partName, modelName))

    part = model.parts[partName]

    default_sets = {
        "FLUID": "FASEI_FLUIDO",
        "PIPE": "FASEI_REV"
    }

    if setName is None:
        setName = default_sets.get(partName, partName)

    if setName in part.sets:
        region = part.sets[setName]
    else:
        if part.space in (TWO_D_PLANAR, AXISYMMETRIC):
            region = part.Set(name=setName, faces=part.faces[:])
        elif part.space == THREE_D:
            region = part.Set(name=setName, cells=part.cells[:])
        else:
            raise ValueError("No valid entities to assign section in %s" % partName)

    part.SectionAssignment(region=region,
                           sectionName=sectionName,
                           offset=0.0,
                           offsetType=MIDDLE_SURFACE,
                           offsetField='',
                           thicknessAssignment=FROM_SECTION)


def AssignRockByDepth(modelName, partName, rock_layers):
    model = mdb.models[modelName]
    part = model.parts[partName]


    for i, layer in enumerate(rock_layers, start=1):
        sec_name = layer["sectionName"]

        auto_set_name = "L%d-I" % i 
        set_name = layer.get("set_index", auto_set_name)

        if set_name in part.sets:
            region = part.sets[set_name]

            part.SectionAssignment(
                region=region,
                sectionName=sec_name,
                offset=0.0,
                offsetType=MIDDLE_SURFACE,
                offsetField='',
                thicknessAssignment=FROM_SECTION
            )

            print("Assigned section '%s' to existing set '%s'." % (sec_name, set_name))

        else:

            print("Warning: Set '%s' not found in part '%s'. Skipping assignment." % (set_name, partName))



def AddplasticityToSteel(name_model, material_name='STEEL'):
    m = mdb.models[name_model]

    mat = m.materials[material_name]

    plastic_table = (
        (7.58424e+08, 0.0,  273.15),
        (7.58424e+08, 0.25, 273.15),
        (7.56376e+08, 0.0,  298.15),
        (7.56376e+08, 0.25, 298.15),
        (7.25660e+08, 0.0,  373.15),
        (7.25660e+08, 0.25, 373.15),
        (7.05182e+08, 0.0,  423.15),
        (7.05182e+08, 0.25, 423.15),
        (6.84705e+08, 0.0,  473.15),
        (6.84705e+08, 0.25, 473.15),
        (6.64227e+08, 0.0,  523.15),
        (6.64227e+08, 0.25, 523.15)
    )

    mat.Plastic(table=plastic_table, temperatureDependency=ON)

    print(f">>> Plasticity dependent of temperature added to material '{material_name}'!")



        
