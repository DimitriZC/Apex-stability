import os
import pandas as pd
from time import sleep

file_name = "HF"

data = pd.read_csv(f"Rockets/{file_name}.csv")

df = pd.DataFrame(data)

teste = df['name'][0]


with open(f'{file_name}.txt', 'w'): pass
with open("csvRunner/values/outputs.txt", "w") as file: pass


num_of_rockets = df.shape[0] // 3

for i in range(0, num_of_rockets * 3, 3):

    if df['geometry_method.1'][i + 1] == "0":
        foguete = f'''_rocket = [
    (
        "name": "{df['name'][i]}",
        "geometry_method": "{df['geometry_method'][i]}",
        "reference_area": {df['reference_area'][i]},
        "initial_radius": {df['initial_radius'][i]},
        "thickness": {df['thickness'][i]},
        "final_radius": {df['final_radius'][i]},
        "length": {df['length'][i]},
        "body_diameter": {df['body_diameter'][i]},
        "weight": {df['weight'][i]},
        "position": {df['position'][i]},
        "material": material_density["{df['material'][i]}"],
        "body_type": "{df['body_type'][i]}",
    ),

    (
        "name": "{df['name'][i + 1]}",
        "geometry_method": "{df['geometry_method'][i + 1]}",
        "reference_area": {df['reference_area'][i + 1]},
        "initial_radius": {df['initial_radius'][i + 1]},
        "thickness": {df['thickness'][i + 1]},
        "final_radius": {df['final_radius'][i + 1]},
        "length": {df['length'][i + 1]},
        "body_diameter": {df['body_diameter'][i + 1]},
        "weight": {df['weight'][i + 1]},
        "position": {df['position'][i + 1]},
        "material": material_density["{df['material'][i + 1]}"],
        "body_type": "{df['body_type'][i + 1]}",
    ),

    (
        "name": "{df['name'][i + 2]}",
        "geometry_method": "{df['geometry_method'][i + 2]}",
        "reference_area": {df['reference_area'][i + 2]},
        "initial_radius": {df['initial_radius'][i + 2]},
        "thickness": {df['thickness'][i + 2]},
        "final_radius": {df['final_radius'][i + 2]},
        "length": {df['length'][i + 2]},
        "body_diameter": {df['body_diameter'][i + 2]},
        "weight": {df['weight'][i + 2]},
        "position": {df['position'][i + 2]},
        "material": material_density["{df['material'][i + 2]}"],
        "body_type": "{df['body_type'][i + 2]}",
    ),

    (
        "name": "{df['name.1'][i]}",
        "geometry_method": "{df['geometry_method.1'][i]}",
        "thickness":{df['thickness.1'][i]},
        "root_chord": {df['root_chord'][i]},
        "tip_chord": {df['tip_chord'][i]},
        "spanwise_length": {df['spanwise_length'][i]},
        "sweep_length": {df['sweep_length'][i]},
        "max_body_diameter": {df['max_body_diameter'][i]},
        "position": {df['position.1'][i]},
        "material": material_density["{df['material.1'][i]}"],
        "weight": {df['weight.1'][i]},
        "body_type": "{df['body_type.1'][i]}",
        "number_of_fins":{df['number_of_fins'][i]},
        "Mach": {df['Mach'][i]},
        "reference_area": {df['reference_area.1'][i]},

    )
]
'''
    else:

        foguete = f'''_rocket = [
    (
        "name": "{df['name'][i]}",
        "geometry_method": "{df['geometry_method'][i]}",
        "reference_area": {df['reference_area'][i]},
        "initial_radius": {df['initial_radius'][i]},
        "thickness": {df['thickness'][i]},
        "final_radius": {df['final_radius'][i]},
        "length": {df['length'][i]},
        "body_diameter": {df['body_diameter'][i]},
        "weight": {df['weight'][i]},
        "position": {df['position'][i]},
        "material": material_density["{df['material'][i]}"],
        "body_type": "{df['body_type'][i]}",
    ),

    (
        "name": "{df['name'][i + 1]}",
        "geometry_method": "{df['geometry_method'][i + 1]}",
        "reference_area": {df['reference_area'][i + 1]},
        "initial_radius": {df['initial_radius'][i + 1]},
        "thickness": {df['thickness'][i + 1]},
        "final_radius": {df['final_radius'][i + 1]},
        "length": {df['length'][i + 1]},
        "body_diameter": {df['body_diameter'][i + 1]},
        "weight": {df['weight'][i + 1]},
        "position": {df['position'][i + 1]},
        "material": material_density["{df['material'][i + 1]}"],
        "body_type": "{df['body_type'][i + 1]}",
    ),

    (
        "name": "{df['name'][i + 2]}",
        "geometry_method": "{df['geometry_method'][i + 2]}",
        "reference_area": {df['reference_area'][i + 2]},
        "initial_radius": {df['initial_radius'][i + 2]},
        "thickness": {df['thickness'][i + 2]},
        "final_radius": {df['final_radius'][i + 2]},
        "length": {df['length'][i + 2]},
        "body_diameter": {df['body_diameter'][i + 2]},
        "weight": {df['weight'][i + 2]},
        "position": {df['position'][i + 2]},
        "material": material_density["{df['material'][i + 2]}"],
        "body_type": "{df['body_type'][i + 2]}",
    ),

    (
        "name": "{df['name.1'][i]}",
        "geometry_method": "{df['geometry_method.1'][i]}",
        "thickness":{df['thickness.1'][i]},
        "root_chord": {df['root_chord'][i]},
        "tip_chord": {df['tip_chord'][i]},
        "spanwise_length": {df['spanwise_length'][i]},
        "sweep_length": {df['sweep_length'][i]},
        "max_body_diameter": {df['max_body_diameter'][i]},
        "position": {df['position.1'][i]},
        "material": material_density["{df['material.1'][i]}"],
        "weight": {df['weight.1'][i]},
        "body_type": "{df['body_type.1'][i]}",
        "number_of_fins":{df['number_of_fins'][i]},
        "Mach": {df['Mach'][i]},
        "reference_area": {df['reference_area.1'][i]},

    ),

    (
        "name": "{df['name.1'][i + 1]}",
        "geometry_method": "{df['geometry_method.1'][i + 1]}",
        "thickness":{df['thickness.1'][i + 1]},
        "root_chord": {df['root_chord'][i + 1]},
        "tip_chord": {df['tip_chord'][i + 1]},
        "spanwise_length": {df['spanwise_length'][i + 1]},
        "sweep_length": {df['sweep_length'][i + 1]},
        "max_body_diameter": {df['max_body_diameter'][i + 1]},
        "position": {df['position.1'][i + 1]},
        "material": material_density["{df['material.1'][i + 1]}"],
        "weight": {df['weight.1'][i + 1]},
        "body_type": "{df['body_type.1'][i + 1]}",
        "number_of_fins":{df['number_of_fins'][i + 1]},
        "Mach": {df['Mach'][i + 1]},
        "reference_area": {df['reference_area.1'][i + 1]},

    )
]
'''

    txt_foguete = foguete.replace('(', '{')
    txt_foguete = txt_foguete.replace(')', '}')
    with open(f'{file_name}.txt', 'a') as f:
        f.write(f"csvRunner/T-{(i // 3) + 1}\n\n{txt_foguete}\n\n")

    with open('foguete.py', 'r') as f:
        file = f.read().splitlines()


    with open('foguete.py', 'w') as f:
        for i, v in enumerate(file):
            if "_rocket" in v:
                limit = i
        for line in file[0:limit]:
            f.write(f'{line}\n')
        f.write(txt_foguete)

#     with open('foguete.py', 'a') as f:
#         f.write("""
# internal_components = [
# {
#     "name": "engine",
#     "weight": 3704.7, #g
#     "center_of_gravity_pos": (_rocket[1]["position"] + _rocket[1]["length"] - 0.3),
# }
# ]""")
    # sleep(.8)
    os.system(f'python3 mainDebug.py > csvRunner/{file_name}/T-{(i + 1) // 3}.txt')
