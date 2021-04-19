class BarrowmanBody():

    def __init__(self, body, dimensions, angle):
        self.volume = body["volume"]
        self.body_type = body["body_type"]
        self.length = dimensions["length"]
        self.reference_area = dimensions["reference_area"]
        self.angle = angle

    def coefficients():

        if self.type == "cylinder":
            normal_force_coefficient_value = 1.1 * (length * body_diameter) / reference_area * (sin(angle) ** 2)
            normal_force_angular_coefficient = 1.1 * (length * body_diameter) / reference_area * (sin(2 * angle))

            momentum_value = 2 * sin(angle) / (reference_area * body_diameter) * (length * final_area - volume)
            momentum_angular_coefficient = (2 / (reference_area * body_diameter)) * (length * final_area - volume)

        elif self.type == "cone":


            momentum_value = 2 * sin(angle) / (reference_area * body_diameter) * (length * final_area - volume)
            momentum_angular_coefficient = (2 / (reference_area * body_diameter)) * (length * final_area - volume)

        elif self.type == "von karman":

            self.integral = body["rIntegral"]

            normal_force_angular_coefficient = ((4*np.pi)/reference_area) * (np.sin(angle)/angle) * (0.5*body_diameter) * self.integral
            normal_force_coefficient_value = normal_force_angular_coefficient * angle

            momentum_value = 2 * sin(angle) / (reference_area * body_diameter) * (length * final_area - volume)
            momentum_angular_coefficient = (2 / (reference_area * body_diameter)) * (length * final_area - volume)

