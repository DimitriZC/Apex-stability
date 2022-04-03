from math import pi
from materialDensity import material_density

"""
This file have the data for the constructors of the methods;
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

internal_components = [
    {
        "name": "engine",
        "weight": 4000, #g
        "center_of_gravity_pos": 1.65,
    }
]


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

reference_area = ((0.0792 / 2) ** 2) * pi
#[[[The name of the nosecone component must be "nose" cause its used on some Rocket.py methods]]]
_rocket = [
    {
        "name": "nose",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0,
        "thickness": 0.008,
        "final_radius": 0.0792 / 2,
        "length": 0.23,
        "body_diameter": 0.0792,
        "weight": 134.0,
        "position": 0.0,
        "material": material_density["glass_fiber"],
        "body_type": "von karman",
    },

    {
        "name": "fuselage",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.0792 / 2,
        "thickness": 0.008,
        "final_radius": 0.0792 / 2,
        "length": 1.61,
        "body_diameter": 0.0792,
        "weight": 1445.0,
        "position": 0.23,
        "material": material_density["glass_fiber"],
        "body_type": "cylinder",
    },

    {
        "name": "boattail",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.0792 / 2,
        "thickness": 0.008,
        "final_radius": 0.05 / 2,
        "length": 0.06,
        "body_diameter": 0.0792,
        "weight": 44.9,
        "position": 2.73,
        "material": material_density["glass_fiber"],
        "body_type": "cone",
    },

    {
        "name": "fin",
        "geometry_method": "fin",
        "thickness":0.0023,
        "root_chord": 0.18,
        "tip_chord": 0.04,
        "spanwise_length": 0.22,
        "sweep_length": 0.25,
        "max_body_diameter": 0.0792,
        "position": 1.69,
        "material": material_density["glass_fiber"],
        "weight": 308.913,
        "body_type": "rounded",
        "number_of_fins":3.0,
        "Mach": 0.66,
        "reference_area": reference_area,

    },

    {
        "name": "canard",
        "geometry_method": "fin",
        "thickness":0.0023,
        "root_chord": 0.06,
        "tip_chord": 0.02,
        "spanwise_length": 0.08,
        "sweep_length": 0.09,
        "max_body_diameter": 0.0792,
        "position": 0.4,
        "material": material_density["glass_fiber"],
        "weight": 40.848,
        "body_type": "rounded",
        "number_of_fins":3.0,
        "Mach": 0.66,
        "reference_area": reference_area,

    }
]
