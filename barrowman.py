from math import pi

class BarrowmanBody():

    def __init__(self, body, dimensions, angle):
        self.volume = body["volume"]
        self.body_type = body["body_type"]
        self.length = dimensions["length"]
        self.reference_area = dimensions["reference_area"]
        self.angle = angle

    def coefficients(self):

        if self.body_type == "cylinder":
            normal_force_coefficient_value = 1.1 * (length * body_diameter) / reference_area * (sin(angle) ** 2)
            normal_force_angular_coefficient = 1.1 * (length * body_diameter) / reference_area * (sin(2 * angle))

            momentum_value = 2 * sin(angle) / (reference_area * body_diameter) * (length * final_area - volume)
            momentum_angular_coefficient = (2 / (reference_area * body_diameter)) * (length * final_area - volume)

        elif self.body_type == "cone": ### ERRADO (se pá)

            if self.angle == 0:
                normal_force_coefficient_value = 2 / reference_area * abs(final_area - initial_area)
            else:
                normal_force_coefficient_value = (2 / reference_area) * abs(final_area - initial_area) * (sin(angle) / angle)

            normal_force_angular_coefficient = (2 / reference_area) * abs(final_area - initial_area)


            momentum_value = 2 * sin(angle) / (reference_area * body_diameter) * (length * final_area - volume)
            momentum_angular_coefficient = (2 / (reference_area * body_diameter)) * (length * final_area - volume)

        elif self.body_type == "von karman":

            self.integral = body["rIntegral"]

            normal_force_angular_coefficient = ((4*np.pi)/reference_area) * (np.sin(angle)/angle) * (0.5*body_diameter) * self.integral
            normal_force_coefficient_value = normal_force_angular_coefficient * angle

            momentum_value = 2 * sin(angle) / (reference_area * body_diameter) * (length * final_area - volume)
            momentum_angular_coefficient = (2 / (reference_area * body_diameter)) * (length * final_area - volume)

        return {
            "normal_force_coefficient_value": normal_force_coefficient_value,
            "normal_force_angular_coefficient": normal_force_angular_coefficient,
            "momentum_value": momentum_value,
            "momentum_angular_coefficient": momentum_angular_coefficient,

        }


class BarrowmanFins():

    def __init__(self, dimensions, body):
        self.spanwise_length = dimensions["spanwise_length"]
        self.max_body_diameter = dimensions["max_body_diameter"]
        self.reference_area = body["reference_area"]
        self.fin_area = body["fin_area"]
        self.beta = body["beta"]
        self.sweep_angle = body["sweep_angle"]

    def coefficients(self):

        Cn_a_one_fin = ((2 * pi * self.spanwise_length ** 2) / self.reference_area)/(1 + sqrt(1 + ((self.beta * self.spanwise_length ** 2) / (self.fin_area * cos(self.sweep_angle))) ** 2))

        # normal force coefficient derivative for N fins [DOUBLE CHECH THE REFERENCE FOR Ntot (total number of parallel fins that have an interference effect)]
        Cn_a = (N / 2) * Cn_a_one_fin

        ktb = 1 + (self.max_body_diameter / 2) / (self.spanwise_length + (self.max_body_diameter / 2)) # Correction term for the normal force on the fins due to the body
        Cn = ktb * Cn_a # final normal force coefficient derivative for the fins

        return {
            "Cn_a_one_fin": Cn_a_one_fin,
            "Cn_a": Cn_a,
            "Cn": Cn
        }
