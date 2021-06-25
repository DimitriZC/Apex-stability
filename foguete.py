from math import pi, radians

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


# Armação A22

'''
# Model of the geometry inputs for the body parts
body = {
    "name": ###,
    "reference_area": ###,
    "geometry_method" = "body",
    "initial_radius": ###,
    "final_radius": ###,
    "length": ###,
    "body_diameter": ###,
    "weight": ###,
    "position": ###,
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
