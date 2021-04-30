import functions
from math import pi, radians

reference_area = ((0.0792 / 2) ** 2) * pi
boattail_initial_area = ((0.0832 / 2) ** 2) * pi
boattail_final_area = ((0.065 / 2) ** 2) * pi

thickness = 0.0023 # (m)

rho = 1.225
Mach = 0.3
v0 = 20
a = 340
angle = radians(0)

Cna_sum = 0
cp_pos = 0


nose = functions.body(rho, Mach, v0, reference_area, 0, reference_area, 0.228, 0.0792, 100, angle, 0, "cone")
body = functions.body(rho, Mach, v0, reference_area, reference_area, reference_area, 1.7, 0.0792, 1072.58, angle, 0.228, "cylinder")
boattail = functions.body(rho, Mach, v0, reference_area, boattail_initial_area, boattail_final_area, 0.06, 0.0832, 50.8, angle, 1.88, "cone")
fins = functions.fins(v0, a, 1.94, 0.0832, thickness, Mach, 0.18, 0.05, 0.16, 0.161, 0.17, 1.69, 179 , 3, "rounded")
canards = functions.fins(v0, a, 1.94, 0.0832, thickness, Mach, 0.07, 0.02, 0.10, 0.0496, 0.09, 0.410, 37 , 3, "rounded")

components = [
    nose,
    body,
    boattail,
    fins,
    canards
]

weight_pos_components = [
    ( 311, 0.2705), # (weight, center_position)
    ( 300, 0.383),
    ( 134, 0.462),
    ( 316, 0.533),
    (  50, 0.613),
    ( 223, 0.793),
    ( 100, 0.673),
    ( 100, 0.865),
    (  75, 0.794),
    ( 316, 1.043),
    (  50, 0.962),
    ( 329, 1.325),
    (  10, 1.285),
    (4000, 1.175),
    ( 719, 1.875),
    # pegar peso do motor:
    (1134, 1.662),
    (1000, 1.880)

]

total_weight = 0 # nose["weight"] + body["weight"] + fins["weight"] + canards["weight"]
cg_pos = 0 # (nose["weight"]*nose["center_of_gravity_pos"] + body["weight"]*body["center_of_gravity_pos"] + fins["weight"]*fins["center_of_gravity_pos"] + canards["weight"]*canards["center_of_gravity_pos"]) / total_weight


#=====================================================================================
# CG

for component in components:
    total_weight += component["weight"]

for component in weight_pos_components:
    total_weight += component[0]

for component in components:
    cg_pos += component["weight"] * component["center_of_gravity_pos"] / total_weight


print(total_weight)

for component in weight_pos_components:
    cg_pos += (component[0] * component[1]) / total_weight

# cg_pos = 1.26
#================================================================================
# CP

for component in components:
    Cna_sum += component["normal_force_angular_coefficient"]


for component in components:
    cp_pos += component["normal_force_angular_coefficient"] * component["center_of_pressure_pos"] / Cna_sum

#==================================================================================
# Cn

normal_force_of_the_rocket = 0

for component in components:
    normal_force_of_the_rocket += component['normal_force_coefficient_value']


print(f'''
# NoseCone:
#     => cna = {float(nose["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(nose["normal_force_coefficient_value"]):.4f}
#     => cma = {float(nose["momentum_angular_coefficient"]):.4f}
#     => xcp = {float(nose["center_of_pressure_pos"]):.4f}

# # body:
#     => cna = {float(body["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(body["normal_force_coefficient_value"]):.4f}
#     => cma = {float(body["momentum_angular_coefficient"]):.4f}
#     => xcp = {float(body["center_of_pressure_pos"]):.4f}

# # Boattail:
#     => cna = {float(boattail["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(boattail["normal_force_coefficient_value"]):.4f}
#     => cma = {float(boattail["momentum_angular_coefficient"]):.4f}
#     => xcp = {float(boattail["center_of_pressure_pos"]):.4f}

# # Fins:
#     => cna = {float(fins["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(fins["normal_force_coefficient_value"]):.4f}
# => cna1Fin = {float(fins["normal_force_angular_coefficient_one_fin"]):.4f}
#     => xcp = {float(fins["center_of_pressure_pos"]):.4f}
#     => xcg = {float(fins["center_of_gravity_pos"]):.4f}

# # Canards:
#     => cna = {float(canards["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(canards["normal_force_coefficient_value"]):.4f}
# => cna1Fin = {float(canards["normal_force_angular_coefficient_one_fin"]):.4f}
#     => xcp = {float(canards["center_of_pressure_pos"]):.4f}
''')

print(f"CG = {cg_pos}")
print(f"CP = {cp_pos}")
print(f"Cn = {normal_force_of_the_rocket}")
print(f"SM = {(cp_pos - cg_pos) / 0.0792}")

