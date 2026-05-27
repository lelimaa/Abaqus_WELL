from abaqus import mdb
from abaqusConstants import *


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
    labData = data.get("lab_data")
    if None in (phi, c, labData):
        raise ValueError(
            "friction_angle, dilatancy_angle, cohesion, and lab_data must be provided for Mohr-Coulomb material.")
        return
    if dilat is None:
        dilat = 0.0
    mat.MohrCoulombPlasticity(table=((phi, dilat), ))
    mat.mohrCoulombPlasticity.MohrCoulombHardening(table=labData)
    mat.mohrCoulombPlasticity.TensionCutOff(temperatureDependency=OFF, dependencies=0,
                                            table=((c, 0.0), ))

    return mat, sect, subroutine

    # mat.Creep(law=USER, table=())


def DoublePowerCreepMaterial(modelName, name, data, sectionLength=1.):
    mat, sect, subroutine = ElasticMaterial(
        modelName, name, data, sectionLength)
    try:
        dp_data = data.get("creep_parameters", {})
        A1 = dp_data["A1"]
        A2 = dp_data["A2"]
        B1 = dp_data["B1"]
        B2 = dp_data["B2"]
        C1 = dp_data["C1"]
        C2 = dp_data["C2"]
        ref_stress = dp_data["reference_stress"]
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
        "Elastic": ElasticMaterial,
        "vonMises": vonMisesMaterial,
        "MohrCoulomb": MohrCoulombMaterial,
        "DoublePowerCreep": DoublePowerCreepMaterial,
        "DoubleMechanismCreep": DoubleMechanismCreepMaterial,
    }
    create_func = mapping.get(behavior)
    if create_func is not None:
        return create_func(modelName, name, data, sectionLength)
    else:
        raise ValueError("Behavior '%s' not recognized." % behavior)


def Assign_Section(modelName, partName, sectionName, setName=None, isSolid=True):
    model = mdb.models[modelName]
    if partName not in model.parts:
        raise ValueError("Part '%s' not found in model '%s'." %
                         (partName, modelName))
    part = model.parts[partName]

    if sectionName not in model.sections:
        raise ValueError("Section '%s' not found in model '%s'. Available sections are: %s" % (
            sectionName, modelName, list(model.sections.keys())))

    if setName is None:
        setName = partName + '_Set'
    if setName in part.sets:
        region = part.sets[setName]
    else:
        if part.space in (TWO_D_PLANAR, AXISYMMETRIC):
            region = part.Set(name=setName, faces=part.faces[:])
        elif part.space == THREE_D:
            region = part.Set(name=setName, cells=part.cells[:])
        # if isSolid is True:
        #     region = part.Set(name=setName, cells=part.cells[:])
        # elif isSolid is False:
        else:
            raise ValueError("No valid entities to assign section in %s" % partName)

    part.SectionAssignment(region=region,
                           sectionName=sectionName,
                           offset=0.0,
                           offsetType=MIDDLE_SURFACE,
                           offsetField='',
                           thicknessAssignment=FROM_SECTION)


if __name__ == "__main__":
    examples = {
        "ELASTIC_MAT": {
            "behavior": "Elastic",
            'density': 7800,
            'elastic': (210000, 0.3),
            'conductivity': 45,
            'specific_heat': 500,
            'expansion': 1.2e-5
        },
        "VONMISES_MAT": {
            "behavior": "vonMises",
            'density': 7800,
            'elastic': (210000, 0.3),
            'conductivity': 45,
            'specific_heat': 500,
            'expansion': 1.2e-5,
            'stress_strain_curve': ((250, 0.0), (300, 0.02), (350, 0.05), (400, 0.1))
        },
        "MOHRCOULOMB_MAT": {
            "behavior": "MohrCoulomb",
            'density': 2000,
            'elastic': (15400e6, 0.14),
            'conductivity': 1.1,
            'specific_heat': 2100,
            'expansion': 0.0,
            'friction_angle': 30.0,
            'dilatancy_angle': 10.0,
            'cohesion': 5e6,
            'lab_data': ((10e6, 0.0), (20e6, 0.01), (30e6, 0.03), (40e6, 0.06))
        },
        "DOUBLE_POWER_CREEP_MAT": {
            "behavior": "DoublePowerCreep",
            "density": 2170.23,
            "elastic": (20403e6, 0.36),
            "conductivity": 5.685,
            "specific_heat": 880.25,
            "expansion": 0.0,
            "creep_parameters": {
                "A1": 1.0,
                "A2": 2.0,
                "B1": 3.0,
                "B2": 4.0,
                "C1": 5.0,
                "C2": 6.0,
                "reference_stress": 100.0
            }
        },
        "DOUBLE_MECHANISM_CREEP_MAT": {
            "behavior": "DoubleMechanismCreep",
            "density": 2170.23,
            "elastic": (20403e6, 0.36),
            "conductivity": 5.685,
            "specific_heat": 880.25,
            "expansion": 0.0,
            "creep_parameters": {
                "reference_strain": 1.0,
                "reference_stress": 100.0,
                "reference_temperature": 293.0,
                "N1": 2.0,
                "N2": 4.0,
                "Q": 3.0,
                "R": 5.0,
            },
        }
    }
    material_examples = {
        "PIPE": {
            "partName": 'PIPE',
            "sectionName": 'VONMISES_MAT_Section',
            "isSolid": True
        },
        "FLUID": {
            "partName": 'FLUID',
            "sectionName": 'ELASTIC_MAT_Section',
            "isSolid": True
        },
        "ROCK": {
            "partName": 'ROCK',
            "sectionName": 'DOUBLE_POWER_CREEP_MAT_Section',
            "isSolid": True
        }
    }

    if 'MyFirstModel' not in mdb.models:
        mdb.Model(name='MyFirstModel')

    for mat_name, mat_data in examples.items():
        CreateMaterial('MyFirstModel', mat_name, mat_data, sectionLength=1.)
    for section_name in material_examples.values():
        Assign_Section('MyFirstModel',
                       partName=section_name["partName"],
                       sectionName=section_name["sectionName"],
                       isSolid=section_name["isSolid"])

mdb.saveAs(pathName='FEM_AXYS_WELL_SHIELD.cae')
