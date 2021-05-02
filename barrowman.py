from math import pi, sin, sqrt, cos

class BarrowmanBody():

    def __init__(self,dimensions, body, angle):
        self.body_diameter = dimensions["body_diameter"]
        self.length = dimensions["length"]
        self.reference_area = dimensions["reference_area"]
        self.initial_radius = dimensions["initial_radius"]
        self.initial_area = (dimensions["initial_radius"] ** 2) * pi
        self.final_radius = dimensions["final_radius"]
        self.final_area = (dimensions["final_radius"] ** 2) * pi
        self.volume = body["volume"]
        self.body_type = body["body_type"]
        self.center_of_pressure_pos = body["center_of_pressure_pos"]
        self.angle = angle

    def coefficients(self):

        if self.body_type == "cylinder":
            normal_force_coefficient_value = 1.1 * (self.length * self.body_diameter) / self.reference_area * (sin(self.angle) ** 2)
            normal_force_angular_coefficient = 1.1 * (self.length * self.body_diameter) / self.reference_area * (sin(2 * self.angle))

            momentum_value = 2 * sin(self.angle) / (self.reference_area * self.body_diameter) * (self.length * self.final_area - self.volume)
            momentum_angular_coefficient = (2 / (self.reference_area * self.body_diameter)) * (self.length * self.final_area - self.volume)

        elif self.body_type == "cone": ### ERRADO (se pá)

            if self.angle == 0:
                normal_force_coefficient_value = 2 / self.reference_area * abs(self.final_area - self.initial_area)
            else:
                normal_force_coefficient_value = (2 / self.reference_area) * abs(self.final_area - self.initial_area) * (sin(angle) / angle)

            normal_force_angular_coefficient = (2 / self.reference_area) * abs(self.final_area - self.initial_area)


            momentum_value = 2 * sin(self.angle) / (self.reference_area * self.body_diameter) * (self.length * self.final_area - self.volume)
            momentum_angular_coefficient = (2 / (self.reference_area * self.body_diameter)) * (self.length * self.final_area - self.volume)

        elif self.body_type == "von karman":

            self.integral = body["rIntegral"]

            normal_force_angular_coefficient = ((4*np.pi)/self.reference_area) * (np.sin(angle)/angle) * (0.5*self.body_diameter) * self.integral
            normal_force_coefficient_value = normal_force_angular_coefficient * angle

            momentum_value = 2 * sin(angle) / (self.reference_area * self.body_diameter) * (self.length * self.final_area - self.volume)
            momentum_angular_coefficient = (2 / (self.reference_area * self.body_diameter)) * (self.length * self.final_area - self.volume)

        return {
            "normal_force_coefficient_value": normal_force_coefficient_value,
            "normal_force_angular_coefficient": normal_force_angular_coefficient,
            "momentum_value": momentum_value,
            "momentum_angular_coefficient": momentum_angular_coefficient,
            "center_of_pressure_pos" : self.center_of_pressure_pos

        }


class BarrowmanFins():

    def __init__(self, dimensions, body):
        self.spanwise_length = dimensions["spanwise_length"]
        self.max_body_diameter = dimensions["max_body_diameter"]
        self.number_of_fins = dimensions["number_of_fins"]
        self.center_of_pressure_pos = body["center_of_pressure_pos"]
        self.reference_area = body["reference_area"]
        self.fin_area = body["fin_area"]
        self.beta = body["beta"]
        self.sweep_angle = body["sweep_angle"]

    def coefficients(self):

        normal_force_angular_coefficient_one_fin = ((2 * pi * self.spanwise_length ** 2) / self.reference_area)/(1 + sqrt(1 + ((self.beta * self.spanwise_length ** 2) / (self.fin_area * cos(self.sweep_angle))) ** 2))

        # normal force coefficient derivative for N fins [DOUBLE CHECH THE REFERENCE FOR Ntot (total number of parallel fins that have an interference effect)]
        normal_force_angular_coefficient = (self.number_of_fins / 2) * normal_force_angular_coefficient_one_fin

        ktb = 1 + (self.max_body_diameter / 2) / (self.spanwise_length + (self.max_body_diameter / 2)) # Correction term for the normal force on the fins due to the body
        normal_force_coefficient = ktb * normal_force_angular_coefficient # final normal force coefficient derivative for the fins

        return {
            "normal_force_angular_coefficient_one_fin": normal_force_angular_coefficient_one_fin,
            "normal_force_angular_coefficient": normal_force_angular_coefficient,
            "normal_force_coefficient_value": normal_force_coefficient,
            "center_of_pressure_pos": self.center_of_pressure_pos
        }
