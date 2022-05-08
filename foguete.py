from math import pi

from materialDensity import material_density

"""
This file have the data for the constructors of the methods;
The final goal is to configure the rocket here and then run the code.
"""

# constants

dados = {"rho": 1.225, "Mach": 0.66, "free_stream_velocity": 20, "angle": 2, "sound_velocity": 342}

internal_components = [
    {
        "name": "engine",
        "weight": 1583.9,  # g
        "center_of_gravity_pos": 1.1,
    }
]


# Armação A22

"""
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

"""

reference_area = ((0.0792 / 2) ** 2) * pi
# [[[The name of the nosecone component must be "nose" cause its used on some Rocket.py methods]]]
_rocket = [
    {
        "name": "nose",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.0000,
        "thickness": 0.0025,
        "final_radius": 0.02545,
        "length": 0.16,
        "body_diameter": 0.0509,
        "weight": 70,
        "position": 0,
        "material": material_density["glass_fiber"],
        "body_type": "von karman",
    },

    {
        "name": "fuselage",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.02545,
        "thickness": 0.0025,
        "final_radius": 0.02545,
        "length": 1.27,
        "body_diameter": 0.0509,
        "weight": 746.3262541,
        "position": 0.16,
        "material": material_density["glass_fiber"],
        "body_type": "cylinder",
    },

    {
        "name": "boattail",
        "geometry_method": "body",
        "reference_area": reference_area,
        "initial_radius": 0.02545,
        "thickness": 0.0025,
        "final_radius": 0.0204,
        "length": 0.05,
        "body_diameter": 0.0509,
        "weight": 20,
        "position": 1.43,
        "material": material_density["glass_fiber"],
        "body_type": "cone",
    },

    {
        "name": "fin",
        "geometry_method": "fin",
        "thickness":0.0023,
        "root_chord": 0.18,
        "tip_chord": 0.05,
        "spanwise_length": 0.17,
        "sweep_length": 0.16,
        "max_body_diameter": 0.0509,
        "position": 1.25,
        "material": material_density["glass_fiber"],
        "weight": 254.5082,
        "body_type": "rounded",
        "number_of_fins":3.0,
        "Mach": 0.66,
        "reference_area": reference_area,

    },

    {
        "name": "canard",
        "geometry_method": "fin",
        "thickness":0.0023,
        "root_chord": 0.049,
        "tip_chord": 0.014,
        "spanwise_length": 0.063,
        "sweep_length": 0.07,
        "max_body_diameter": 0.0509,
        "position": 0.3,
        "material": material_density["glass_fiber"],
        "weight": 26.3000,
        "body_type": "rounded",
        "number_of_fins":3.0,
        "Mach": 0,
        "reference_area": reference_area,

    }
]
