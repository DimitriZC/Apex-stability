from Rocket import Rocket
from foguete import dados, _rocket


"""
This file is been used to test the formulas and output all component values.
"""

Foguete = Rocket(dados, _rocket) # rocket been constructed with foguete.py data.
teste = Foguete.center_of_pressure_pos()
Foguete.plot_coefficients()


print(f'''
# NoseCone:
#     => cna = {float(Foguete.components_barrowman[0]["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(Foguete.components_barrowman[0]["normal_force_coefficient_value"]):.4f}
#     => cma = {float(Foguete.components_barrowman[0]["momentum_angular_coefficient"]):.4f}
#     => xcp = {float(Foguete.components_barrowman[0]["center_of_pressure_pos"]):.4f}
#     => xcg = {float(Foguete.components_geometry[0]["center_of_gravity_pos"]):.4f}

# # body:
#     => cna = {float(Foguete.components_barrowman[1]["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(Foguete.components_barrowman[1]["normal_force_coefficient_value"]):.4f}
#     => cma = {float(Foguete.components_barrowman[1]["momentum_angular_coefficient"]):.4f}
#     => xcp = {float(Foguete.components_barrowman[1]["center_of_pressure_pos"]):.4f}
#     => xcg = {float(Foguete.components_geometry[1]["center_of_gravity_pos"]):.4f}

# # Boattail:
#     => cna = {float(Foguete.components_barrowman[2]["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(Foguete.components_barrowman[2]["normal_force_coefficient_value"]):.4f}
#     => cma = {float(Foguete.components_barrowman[2]["momentum_angular_coefficient"]):.4f}
#     => xcp = {float(Foguete.components_barrowman[2]["center_of_pressure_pos"]):.4f}
#     => xcg = {float(Foguete.components_geometry[2]["center_of_gravity_pos"]):.4f}

# # Fins:
#     => cna = {float(Foguete.components_barrowman[3]["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(Foguete.components_barrowman[3]["normal_force_coefficient_value"]):.4f}
# => cna1Fin = {float(Foguete.components_barrowman[3]["normal_force_angular_coefficient_one_fin"]):.4f}
#     => xcp = {float(Foguete.components_geometry[3]["center_of_pressure_pos"]):.4f}
#     => xcg = {float(Foguete.components_geometry[3]["center_of_gravity_pos"]):.4f}

# # Canards:
#     => cna = {float(Foguete.components_barrowman[4]["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(Foguete.components_barrowman[4]["normal_force_coefficient_value"]):.4f}
# => cna1Fin = {float(Foguete.components_barrowman[4]["normal_force_angular_coefficient_one_fin"]):.4f}
#     => xcp = {float(Foguete.components_geometry[4]["center_of_pressure_pos"]):.4f}
#     => xcg = {float(Foguete.components_geometry[4]["center_of_gravity_pos"]):.4f}

''')
'''

# # Canards:
#     => cna = {float(Foguete.components_barrowman[4]["normal_force_angular_coefficient"]):.4f}
#     => cn  = {float(Foguete.components_barrowman[4]["normal_force_coefficient_value"]):.4f}
# => cna1Fin = {float(Foguete.components_barrowman[4]["normal_force_angular_coefficient_one_fin"]):.4f}
#     => xcp = {float(Foguete.components_geometry[4]["center_of_pressure_pos"]):.4f}
#     => xcg = {float(Foguete.components_geometry[4]["center_of_gravity_pos"]):.4f}
# '''

print(f"CG = {Foguete.center_of_gravity_pos()}")
print(f"CP = {Foguete.center_of_pressure_pos()}")
# print(f"Cna = {Foguete.normal_force_angular_coefficient()}")
print(f"SM = {Foguete.static_margin()}")

Foguete.plot_coefficients()
