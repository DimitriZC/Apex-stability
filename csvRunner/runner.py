import os
from time import sleep

import pandas as pd

file_name = "GVT-A33"


if os.path.exists(f"csvRunner/{file_name}") == False:
    os.system(f"mkdir csvRunner/{file_name}")
    print(f"Creating folder {file_name} ⏳️")
else:
    print(f"The folder {file_name} already exists 🚀")

data = pd.read_csv(f"Rockets/{file_name}.csv")

df = pd.DataFrame(data)

teste = df["name"][0]
# breakpoint()


with open(f"{file_name}.txt", "w"):
    pass
with open("csvRunner/values/outputs.txt", "w") as file:
    pass


num_of_rockets = df.shape[0] // 3

for i in range(0, num_of_rockets * 3, 3):

    if df["geometry_method.1"][i + 1] == "0":
        foguete = f"""_rocket = [
    (
        "name": "{df['name'][i]}",
        "geometry_method": "{df['geometry_method'][i]}",
        "reference_area": {df['reference_area'][i].replace(',', '.')},
        "initial_radius": {df['initial_radius'][i].replace(',', '.')},
        "thickness": {df['thickness'][i].replace(',', '.')},
        "final_radius": {df['final_radius'][i].replace(',', '.')},
        "length": {df['length'][i].replace(',', '.')},
        "body_diameter": {df['body_diameter'][i].replace(',', '.')},
        "weight": {df['weight'][i].replace(',', '.')},
        "position": {df['position'][i].replace(',', '.')},
        "material": material_density["{df['material'][i].replace(',', '.')}"],
        "body_type": "{df['body_type'][i].replace(',', '.')}",
    ),

    (
        "name": "{df['name'][i + 1]}",
        "geometry_method": "{df['geometry_method'][i + 1]}",
        "reference_area": {df['reference_area'][i + 1].replace(',', '.')},
        "initial_radius": {df['initial_radius'][i + 1].replace(',', '.')},
        "thickness": {df['thickness'][i + 1].replace(',', '.')},
        "final_radius": {df['final_radius'][i + 1].replace(',', '.')},
        "length": {df['length'][i + 1].replace(',', '.')},
        "body_diameter": {df['body_diameter'][i + 1].replace(',', '.')},
        "weight": {df['weight'][i + 1].replace(',', '.')},
        "position": {df['position'][i + 1].replace(',', '.')},
        "material": material_density["{df['material'][i + 1]}"],
        "body_type": "{df['body_type'][i + 1]}",
    ),

    (
        "name": "{df['name'][i + 2]}",
        "geometry_method": "{df['geometry_method'][i + 2]}",
        "reference_area": {df['reference_area'][i + 2].replace(',', '.')},
        "initial_radius": {df['initial_radius'][i + 2].replace(',', '.')},
        "thickness": {df['thickness'][i + 2].replace(',', '.')},
        "final_radius": {df['final_radius'][i + 2].replace(',', '.')},
        "length": {df['length'][i + 2].replace(',', '.')},
        "body_diameter": {df['body_diameter'][i + 2].replace(',', '.')},
        "weight": {df['weight'][i + 2].replace(',', '.')},
        "position": {df['position'][i + 2].replace(',', '.')},
        "material": material_density["{df['material'][i + 2].replace(',', '.')}"],
        "body_type": "{df['body_type'][i + 2]}",
    ),

    (
        "name": "{df['name.1'][i]}",
        "geometry_method": "{df['geometry_method.1'][i].replace(',', '.')}",
        "thickness":{df['thickness.1'][i].replace(',', '.')},
        "root_chord": {df['root_chord'][i].replace(',', '.')},
        "tip_chord": {df['tip_chord'][i].replace(',', '.')},
        "spanwise_length": {df['spanwise_length'][i].replace(',', '.')},
        "sweep_length": {df['sweep_length'][i].replace(',', '.')},
        "max_body_diameter": {df['max_body_diameter'][i].replace(',', '.')},
        "position": {df['position.1'][i].replace(',', '.')},
        "material": material_density["{df['material.1'][i]}"],
        "weight": {df['weight.1'][i].replace(',', '.')},
        "body_type": "{df['body_type.1'][i]}",
        "number_of_fins":{df['number_of_fins'][i]},
        "Mach": {df['Mach'][i].replace(',', '.')},
        "reference_area": {df['reference_area.1'][i].replace(',', '.')},

    )
]
"""
    else:

        foguete = f"""_rocket = [
    (
        "name": "{df['name'][i]}",
        "geometry_method": "{df['geometry_method'][i]}",
        "reference_area": {df['reference_area'][i].replace(',', '.')},
        "initial_radius": {df['initial_radius'][i].replace(',', '.')},
        "thickness": {df['thickness'][i].replace(',', '.')},
        "final_radius": {df['final_radius'][i].replace(',', '.')},
        "length": {df['length'][i].replace(',', '.')},
        "body_diameter": {df['body_diameter'][i].replace(',', '.')},
        "weight": {df['weight'][i].replace(',', '.')},
        "position": {df['position'][i].replace(',', '.')},
        "material": material_density["{df['material'][i]}"],
        "body_type": "{df['body_type'][i].replace(',', '.')}",
    ),

    (
        "name": "{df['name'][i + 1]}",
        "geometry_method": "{df['geometry_method'][i + 1]}",
        "reference_area": {df['reference_area'][i + 1].replace(',', '.')},
        "initial_radius": {df['initial_radius'][i + 1].replace(',', '.')},
        "thickness": {df['thickness'][i + 1].replace(',', '.')},
        "final_radius": {df['final_radius'][i + 1].replace(',', '.')},
        "length": {df['length'][i + 1].replace(',', '.')},
        "body_diameter": {df['body_diameter'][i + 1].replace(',', '.')},
        "weight": {df['weight'][i + 1].replace(',', '.')},
        "position": {df['position'][i + 1].replace(',', '.')},
        "material": material_density["{df['material'][i + 1]}"],
        "body_type": "{df['body_type'][i + 1]}",
    ),

    (
        "name": "{df['name'][i + 2]}",
        "geometry_method": "{df['geometry_method'][i + 2]}",
        "reference_area": {df['reference_area'][i + 2].replace(',', '.')},
        "initial_radius": {df['initial_radius'][i + 2].replace(',', '.')},
        "thickness": {df['thickness'][i + 2].replace(',', '.')},
        "final_radius": {df['final_radius'][i + 2].replace(',', '.')},
        "length": {df['length'][i + 2].replace(',', '.')},
        "body_diameter": {df['body_diameter'][i + 2].replace(',', '.')},
        "weight": {df['weight'][i + 2].replace(',', '.')},
        "position": {df['position'][i + 2].replace(',', '.')},
        "material": material_density["{df['material'][i + 2]}"],
        "body_type": "{df['body_type'][i + 2]}",
    ),

    (
        "name": "{df['name.1'][i]}",
        "geometry_method": "{df['geometry_method.1'][i]}",
        "thickness":{df['thickness.1'][i].replace(',', '.')},
        "root_chord": {df['root_chord'][i].replace(',', '.')},
        "tip_chord": {df['tip_chord'][i].replace(',', '.')},
        "spanwise_length": {df['spanwise_length'][i].replace(',', '.')},
        "sweep_length": {df['sweep_length'][i].replace(',', '.')},
        "max_body_diameter": {df['max_body_diameter'][i].replace(',', '.')},
        "position": {df['position.1'][i].replace(',', '.')},
        "material": material_density["{df['material.1'][i]}"],
        "weight": {df['weight.1'][i].replace(',', '.')},
        "body_type": "{df['body_type.1'][i]}",
        "number_of_fins":{df['number_of_fins'][i]},
        "Mach": {df['Mach'][i].replace(',', '.')},
        "reference_area": {df['reference_area.1'][i]},

    ),

    (
        "name": "{df['name.1'][i + 1]}",
        "geometry_method": "{df['geometry_method.1'][i + 1]}",
        "thickness":{df['thickness.1'][i + 1].replace(',', '.')},
        "root_chord": {df['root_chord'][i + 1].replace(',', '.')},
        "tip_chord": {df['tip_chord'][i + 1].replace(',', '.')},
        "spanwise_length": {df['spanwise_length'][i + 1].replace(',', '.')},
        "sweep_length": {df['sweep_length'][i + 1].replace(',', '.')},
        "max_body_diameter": {df['max_body_diameter'][i + 1].replace(',', '.')},
        "position": {df['position.1'][i + 1].replace(',', '.')},
        "material": material_density["{df['material.1'][i + 1]}"],
        "weight": {df['weight.1'][i + 1].replace(',', '.')},
        "body_type": "{df['body_type.1'][i + 1]}",
        "number_of_fins":{df['number_of_fins'][i + 1]},
        "Mach": {df['Mach'][i + 1].replace(',', '.')},
        "reference_area": {df['reference_area.1'][i + 1]},

    )
]
"""

    txt_foguete = foguete.replace("(", "{")
    txt_foguete = txt_foguete.replace(")", "}")
    with open(f"{file_name}.txt", "a") as f:
        f.write(
            f"csvRunner/T-{df['rocket'][i].replace('/', '___').replace(' ', '_')}\n\n{txt_foguete}\n\n"
        )

    with open("foguete.py", "r") as f:
        file = f.read().splitlines()
        for index, v in enumerate(file):
            if "_rocket" in v:
                limit = index

    with open("foguete.py", "r") as f:
        file = f.read().splitlines()

    with open("foguete.py", "w") as f:

        for line in file[0:limit]:
            f.write(f"{line}\n")
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
    os.system(
        f"python3 mainDebug.py > csvRunner/{file_name}/T-{df['rocket'][i].replace('/', '___').replace(' ', '_')}.txt"
    )
