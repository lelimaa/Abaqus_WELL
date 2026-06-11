# from abaqus import mdb
# from abaqusConstants import *
import numpy as np

def CasingStresses(data, name_phase, density_steel, z_top, z_bottom):

    name_phase = "3dda7930-6dbf-4d05-87f2-d2809a3e9fc6"  # The phase from the given json file. It may disappear, because only one phase will be considered soon.
    name_tubular = 'LIN_09_875' # The name of the casing in the json file. There refferred to as "Tubulars".

    density_fluid = 1000  # kg/m³ (density of water)
    density_cement = data["Phases"][name_phase]["CementSheath"][0]["Density"]  # kg/m³ (density of the cement, as given in the json file)
    gravity = 9.81  # m/s² (acceleration due to gravity)

    height_water_above_casing = data["Phases"][name_phase]["Casing"][0]["Top"] 
    # height_water_above_casing = z_top 
    length_casing = data["Phases"][name_phase]["Casing"][0]["Bottom"] - data["Phases"][name_phase]["Casing"][0]["Top"]
    length_cement = data["Phases"][name_phase]["CementSheath"][0]["Bottom"] - data["Phases"][name_phase]["CementSheath"][0]["Top"]
    
    height_base_casing = length_casing + height_water_above_casing
    # height_base_casing = z_bottom
    height_top_of_cement = height_water_above_casing + length_casing - length_cement

    outer_diamenter_pipe = data["Tubulars"][name_tubular]['OD'] # outer diameter of the pipe in inches, as given in the json file. It is converted to meters below.
    outer_diamenter_pipe = outer_diamenter_pipe * 0.0254  # Convert from inches to meters
    thickness_pipe = data["Tubulars"][name_tubular]['Thickness'] # thickness of the pipe in inches, as given in the json file. It is converted to meters below.
    thickness_pipe = thickness_pipe * 0.0254  # Convert from inches to meters
    inner_radius_pipe = outer_diamenter_pipe / 2 - thickness_pipe # Inner radius of the pipe, calculated and already in meters.

    area_outer = (np.pi * (outer_diamenter_pipe / 2) ** 2)  # Cross-sectional area of the outer diameter of the pipe
    area_inner = (np.pi * inner_radius_pipe ** 2)  # Cross-sectional area of the inner diameter of the pipe

    area_s = area_outer - area_inner  # Cross-sectional area of the steel material in the pipe wall

    pressure_inner_casing = density_fluid * gravity * height_water_above_casing + density_fluid * gravity * (height_base_casing - height_water_above_casing)  # Pressure at the inner surface of the casing due to the fluid column above it
    pressure_outer_casing = density_fluid * gravity * height_water_above_casing + density_fluid * gravity * (height_top_of_cement - height_water_above_casing) + density_cement * gravity * length_cement  # Pressure at the outer surface of the casing due to the fluid column above it

    force_real_base = pressure_inner_casing * area_inner - pressure_outer_casing * area_outer  # Net force at the base of the casing due to the fluid pressures

    stress_real_base = force_real_base / area_s

    force_real_top = force_real_base + density_steel * gravity * area_s * (height_base_casing - height_water_above_casing)  # Net force at the top of the casing considering the weight of the steel material

    stress_real_top = force_real_top / area_s

    a = (stress_real_top-stress_real_base)/(height_water_above_casing-height_base_casing)
    b = stress_real_top - a * height_water_above_casing

    stress_top = a * z_top + b
    stress_bottom = a * z_bottom + b

    return stress_top, stress_bottom

    # # stress_base = density_fluid * gravity * height_base_casing
    # stress_base = density_fluid * gravity * height_base_casing

    # stress_top = -stress_base + density_steel * gravity * (height_base_casing - z_top)
    # stress_bottom = -stress_base + density_steel * gravity * (height_base_casing - z_bottom)