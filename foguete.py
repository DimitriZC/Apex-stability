from math import pi
from materialDensity import material_density

"""
This file contains data for the constructors;
The final goal is to configure the rocket here and then run the code.
"""

#constants

dados = {
    "rho": 1.225,
    "Mach": 0.66,
    "free_stream_velocity": 20,
    "angle": 2,
    "sound_velocity": 342
}


# Armação A22

'''
# Model of the geometry inputs for the body parts
body = {
    "name": ###,
    "reference_area": ###, #m²
    "geometry_method" = "body",
    "initial_radius": ###, #m
    "thickness": ###, #m
    "final_radius": ###, #m
    "length": ###, #m
    "body_diameter": ###, #m
    "weight": ###, #g
    "position": ###, #m
    "material": ###,
    "body_type": ###
},

fin = {
    "name": ###
    "geometry_method": 'fin'
    "thickness": ###
    "root_chord": ###
    "tip_chord": ###
    "spanwise_length": ###
    "sweep_length": ###
    "max_body_diameter": ###
    "position": ###
    "weight": ###
    "body_type": ###
    "number_of_fins": ###
    "Mach": ###
    "reference_area": ###
}

'''

reference_area = ((0.1 / 2) ** 2) * pi

# This object will be exported to the analisys file
_rocket = [
    {
        "name": "nose",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.0,
        "thickness": 0.008,
        "final_radius": 0.10 / 2,
        "length": 0.300,
        "body_diameter": 0.0792, #pra arrasto da pra ver dps
        "weight": 120,
        "position": 0,
        "material": material_density["glass_fiber"],
        "body_type": "von karman",
    },

    {
        "name": "fuselage",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.10 / 2,
        "thickness": 0.008,
        "final_radius": 0.10 / 2,
        "length": 3.0,
        "body_diameter": 0.10, #pra arrasto da pra ver dps
        "weight": 1500,
        "position": 0.300,
        "material": material_density["glass_fiber"],
        "body_type": "cylinder",
    },

    {
        "name": "boattail",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.10 / 2,
        "thickness": 0.008,
        "final_radius": 0.07 / 2,
        "length": 0.12,
        "body_diameter": 0.0792, #pra arrasto da pra ver dps
        "weight": 300,
        "position": 3.3,
        "material": material_density["glass_fiber"],
        "body_type": "cone",
    },

    {
        "name": "fin",
        "geometry_method": "fin",
        "thickness": 0.0023, # (m)
        "root_chord": 0.45, # (m)
        "tip_chord": 0.30,
        "spanwise_length": 0.40,
        "sweep_length": 0.40,
        "max_body_diameter": 0.10,
        "position": 2.85,
        "weight": 100,
        "body_type": "rounded",
        "number_of_fins": 3,
        "Mach": dados["Mach"],
        "material": material_density["glass_fiber"],
        "reference_area": reference_area

    },

    {
        "name": "canard",
        "geometry_method": "fin",
        "thickness": 0.0023, # (m)
        "root_chord": 0.45, # (m)
        "tip_chord": 0.30,
        "spanwise_length": 0.40,
        "sweep_length": 0.40,
        "max_body_diameter": 0.10,
        "position": 0.50,
        "weight": 167,
        "body_type": "rounded",
        "number_of_fins": 3,
        "Mach": dados["Mach"],
        "material": material_density["glass_fiber"],
        "reference_area": reference_area
    }
]
'''
# A-22
_rocket = [
    {
        "name": "nose",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0,
        "final_radius": 0.0792 / 2,
        "length": 0.228,
        "body_diameter": 0.0792, #pra arrasto da pra ver dps
        "weight": 100,
        "position": 0,
        "body_type": "cone",
    },

    {
        "name": "fuselage",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.0792 / 2,
        "final_radius": 0.0792 / 2,
        "length": 1.7,
        "body_diameter": 0.0792, #pra arrasto da pra ver dps
        "weight": 1072.58,
        "position": 0.228,
        "body_type": "cylinder",
    },

    {
        "name": "boattail",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.0832 / 2,
        "final_radius": 0.065 / 2,
        "length": 0.06,
        "body_diameter": 0.0792, #pra arrasto da pra ver dps
        "weight": 50.8,
        "position": 1.88,
        "body_type": "cone",
    },

    {
        "name": "fin",
        "geometry_method": "fin",
        "thickness": 0.0023, # (m)
        "root_chord": 0.18, # (m)
        "tip_chord": 0.05,
        "spanwise_length": 0.17,
        "sweep_length": 0.16,
        "max_body_diameter": 0.0832,
        "position": 1.69,
        "weight": 179,
        "body_type": "rounded",
        "number_of_fins": 3,
        "Mach": dados["Mach"],
        "reference_area": reference_area

    },

    {
        "name": "canard",
        "geometry_method": "fin",
        "thickness": 0.0023, # (m)
        "root_chord": 0.07, # (m)
        "tip_chord": 0.02,
        "spanwise_length": 0.09,
        "sweep_length": 0.10,
        "max_body_diameter": 0.0832,
        "position": 0.410,
        "weight": 37,
        "body_type": "rounded",
        "number_of_fins": 3,
        "Mach": dados["Mach"],
        "reference_area": reference_area
    }
]
'''
