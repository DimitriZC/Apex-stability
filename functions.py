from math import sqrt, sin, pi, cos, log
import numpy as np
from time import time

start_time = time()

def body(
    rho,
    Mach,
    free_stream_velocity,
    reference_area,
    initial_area,
    final_area,
    length,
    body_diameter,
    weight,
    angle,
    position,
    body_type = "cylinder" or "cone" or "boattail" or "von karman"
):
    """Barrowman's method for determining
    the total normal force coefficient derivative Cn_alpha,
    the pitch moment coefficient derivative Cm_alpha and the CP location.

    1. The angle of attack is very close to zero;
    2. The flow around the body is steady and non-rotational;
    3. the rocket is rigid body;
    4. The nose tip is a sharp point;
    5. The fins are flat plates;
    6. The rocket body is axially symmetric;

    Args:
        rho (float): density of air (kg/m³)
        Mach (float): Mach value (-)
        free_stream_velocity (float): free stram velocity (m/s)
        reference_area (float): reference area (m²)
        initial_area (float): cross-sectional area at the beggining of body (m²)
        final_area (float): cross-sectional area at the end of body (m²)
        length (float): length of the body (m)
        body_diameter (float): diameter of the body (m)
        weight (float): weight of the body for estimate the CG (g)
        angle (float): angle of attack of the body (rad)
        position(float): position of the body in respect to the tip of the nose cone (m)
        body_type (str, optional): difference of body shape => Defaults to "straight"or"cone".
    """
#====================================================================================================
    #constantes para rodar que serão verificadas, colocadas ou calculadas em seus lugares posteriormente:

    wet_area_body = reference_area * 0.6
    wet_area_fin = 0.0002
    phi = pi / 6
    final_radius = sqrt(final_area / pi)
    initial_radius = sqrt(initial_area / pi)
    Cd_pressure_boattail = 0

#=====================================================================================================

    if body_type == "cylinder":
        # Calculate the volume of the body
        volume = initial_area * length

        # Calculate the center of pressure
        center_of_pressure_pos = position + (length / 2)
        center_of_gravity_pos = position + (length / 2)

    elif body_type == "cone" or body_type == "boattail":
        # Calculate the volume of the body
        volume = 1/3 * pi * ((initial_area / pi) * (sqrt((initial_area / pi) * (final_area / pi))) * (final_area / pi)) * length

        # Calculate the center of pressure
        center_of_pressure_pos = position + ((length * final_area - volume) / abs(final_area - initial_area)) # [VER ESSA FÓRMULA]
        # CG_x_pos: triangle + rectangle cg in respect to area; [PARECE CERTO]
        center_of_gravity_pos = position + ((length * (((2 / 3) * (abs(final_radius - initial_radius) / 2)) + (0.5 * min(initial_radius, final_radius)))) / ((initial_radius + final_radius) / 2))

    elif body_type == "von karman":
        dx = length/1000
        _x = np.arange(0, length, dx)
        _theta = [np.arccos(1 - 2*x/length) for x in _x]
        _r = [(0.5 * body_diameter / np.sqrt(np.pi)) * (np.sqrt(theta - 0.5 * np.sin(2 * theta)))  for theta in _theta]
        _r2 = [r**2 for r in _r]
        rIntegral = np.trapz(_r, _x, dx=dx)
        r2Integral = np.trapz(_r2, _x, dx=dx)
        normal_force_angular_coefficient = ((4*np.pi)/reference_area) * (np.sin(angle)/angle) * (0.5*body_diameter) * rIntegral
        normal_force_coefficient_value = normal_force_angular_coefficient * angle
        volume = np.pi * r2Integral
        center_of_pressure_pos = volume / reference_area

        center_of_gravity_pos = 1/3 * length

    # Calculate the normal force coefficient

    if body_type == "cylinder":
        normal_force_coefficient_value = 1.1 * (length * body_diameter) / reference_area * (sin(angle) ** 2)
        normal_force_angular_coefficient = 1.1 * (length * body_diameter) / reference_area * (sin(2 * angle))
    else:

        if angle == 0:
            normal_force_coefficient_value = 2 / reference_area * abs(final_area - initial_area)
        else:
            normal_force_coefficient_value = (2 / reference_area) * abs(final_area - initial_area) * (sin(angle) / angle)

        normal_force_angular_coefficient = (2 / reference_area) * abs(final_area - initial_area)


# Calculate the momentum coefficient

    momentum_value = 2 * sin(angle) / (reference_area * body_diameter) * (length * final_area - volume)
    momentum_angular_coefficient = (2 / (reference_area * body_diameter)) * (length * final_area - volume)


    return{
        "normal_force_coefficient_value": normal_force_coefficient_value,
        "normal_force_angular_coefficient": normal_force_angular_coefficient,
        "momentum_value": momentum_value,
        "momentum_angular_coefficient": momentum_angular_coefficient,
        "center_of_pressure_pos": center_of_pressure_pos,
        "center_of_gravity_pos": center_of_gravity_pos,
        "weight": weight,
    }



def fins(
    free_stream_velocity,
    sound_velocity,
    rocket_length,
    max_body_diameter,
    thickness,
    Mach,
    root_chord,
    tip_chord,
    Xt,
    MAC,
    spanwise_length,
    fin_position,
    weight, #one fin
    N,
    foil_format = "rounded" or "retangular"
):
    """ fins

    Args:
        free_stream_velocity (float): free stram velocity (m/s)
        sound_velocity (float): velocity of the sound (m/s)
        rocket_length (float): length of the rocket (m)
        max_body_diameter (float): highest diameter of the body (m)
        thickness (float): thickness of the fin (m)
        Mach (float): mach number (-)
        root_chord (float): root chord length (m)
        tip_chord (float): tip chord length (m)
        Xt (float): Sweep length (m)
        MAC (float): mean aerodynamic chord (m)
        spanwise_length (float): span length of the fin (m)
        fin_position (float): fin position in relation to the nose cone tip (m)
        weight (float): weight of one fin (m)
        foil_format (str, optional): format of the foil => Defaults to "rounded"or"retangular".
    """

    ## some of this formulas only work for trapezoidal fins, needs ipgrades for another fin geometries


    # // THE MAXIMUM BODY DIAMETER AND THE BODY DIAMETER AT THE FIN POSITION ARE CONSIDERED TO BE THE SAME (só pra deixar registrado a informação)


    # Constants:
    KINEMATIC_VISCOSITY = 1.5E-5

    # important values:
    # Mach = free_stream_velocity / sound_velocity # Mach number
    R = (free_stream_velocity * rocket_length) / KINEMATIC_VISCOSITY # Reynolds number (verificar uso)
    fb = rocket_length / max_body_diameter # Fineness ratio (verificar uso)

    # One-sided area of a single fin
    Afin = (root_chord + tip_chord) * spanwise_length / 2

    # Aspec ratio of the fin
    AR = 2 * (spanwise_length ** 2) / Afin

    # Beta parameter
    beta = sqrt(1 - Mach ** 2) if Mach <=1 else sqrt(Mach ** 2 - 1)

    # Prandtl factor (verificar uso) {até agr n achei nada}
    P = 1 / beta

    ymac = (spanwise_length * (root_chord - 2 * tip_chord)) / (3 * (root_chord + tip_chord)) # MAC spanwise position

    reference_area = N * thickness * spanwise_length

    #[[[OLHAR PARA EQUAÇÃO DE VF EM 0.5 > MACH > 2, 3.36 ]]] (tem q interpolar mas quero perguntar antes de botar no codigo)
    if Mach <= 0.5 or Mach <= 2:

        center_of_pressure_pos = fin_position +  0.25 * MAC
        #testar e comparar essas duas equações com o openrocket
        #center_of_pressure_pos =   (Xt * (root_chord + 2 * tip_chord)) / (3 * (root_chord + tip_chord)) + (root_chord ** 2 + tip_chord ** 2 + root_chord * tip_chord) / (6 * (root_chord + tip_chord)) # CP position (verificar uso) [CHEK REFERENCE FOR center_of_pressure_pos IF M>0.5 (pg 36)]

    elif Mach > 2:

        center_of_pressure_pos = fin_position + ((MAC * (AR * beta - 0.67)) / (2 * AR * beta - 1))

    # calculate the sweep angle of the fin
    Tc = np.arccos(spanwise_length / sqrt(spanwise_length ** 2 + ((tip_chord / 2) + Xt - root_chord / 2)))

    # normal force coefficient derivatice for one fin [[[[TESTAR ESSA EQUAÇÃO]]]]
    Cn_a_one_fin = ((2 * pi * spanwise_length ** 2) / reference_area)/(1 + sqrt(1 + ((beta * spanwise_length ** 2) / (Afin * cos(Tc))) ** 2))

    # normal force coefficient derivative for N fins [DOUBLE CHECH THE REFERENCE FOR Ntot (total number of parallel fins that have an interference effect)]
    Cn_a = (N / 2) * Cn_a_one_fin

    ktb = 1 + (max_body_diameter / 2) / (spanwise_length + (max_body_diameter / 2)) # Correction term for the normal force on the fins due to the body
    Cn = ktb * Cn_a # final normal force coefficient derivative for the fins

    # Calculate fin set weight
    fin_set_weight = N * weight

    # Calculate the CG position in the x axis
    center_of_gravity_pos = fin_position + ((2 * tip_chord * Xt * (tip_chord ** 2) + Xt * root_chord + (root_chord ** 2)) / (3 * (tip_chord + root_chord)))


    return {
        "normal_force_coefficient_value": Cn,
        "normal_force_angular_coefficient": Cn_a,
        "normal_force_angular_coefficient_one_fin": Cn_a_one_fin,
        "momentum_angular_coefficient": "-",
        "fin_set_weight": fin_set_weight,
        "center_of_pressure_pos": center_of_pressure_pos,
        "center_of_gravity_pos": center_of_gravity_pos,
        "weight": fin_set_weight
    }


# nose = body(1.225, 0.3, 20, pi * 0.01, 0, pi * 0.01, 0.3, 0.2, 200, 0.001, "cone")

# fin = fins(20, 343, 1.9, 0.2, pi * 0.01, 0.3, 0.2, 0.15, 0.05, 0.175, 0.2, 1.5, 75, 3, "rounded")

# print(f"Code time: {time() - start_time}\n\n")
# print(nose, "\n")
# print(fin)

