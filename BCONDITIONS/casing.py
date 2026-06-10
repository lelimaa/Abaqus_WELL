# from abaqus import mdb
# from abaqusConstants import *
# import numpy as np

def CasingStresses(data, name_phase, density_steel, density_cement, z_top, z_bottom):

    density_fluid = 1000  # kg/m³ (density of water)
    gravity = 9.81  # m/s² (acceleration due to gravity)

    height_water_above_casing = data["Phases"][name_phase]["Casing"][0]["Top"] 
    length_casing = data["Phases"][name_phase]["Casing"][0]["Bottom"] - data["Phases"][name_phase]["Casing"][0]["Top"]
    length_cement = data["Phases"][name_phase]["Cement"][0]["Bottom"] - data["Phases"][name_phase]["Cement"][0]["Top"]
    
    height_base_casing = length_casing + height_water_above_casing

    # stress_base = density_fluid * gravity * height_base_casing
    stress_base = density_fluid * gravity * height_base_casing

    stress_top = -stress_base + density_steel * gravity * (height_base_casing - z_top)
    stress_bottom = -stress_base + density_steel * gravity * (height_base_casing - z_bottom)

    return stress_top, stress_bottom
