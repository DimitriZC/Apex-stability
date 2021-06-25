import numpy as np
from math import pi, sin, sqrt, cos, radians

class BarrowmanBody():
    """This class implements the barrowman methos for axial symetric bodys
    """

    def __init__(self,dimensions, body, angle):
        """The class recieve two dictionaries with the variables needed for the method
        and the angle value

        Args:
            dimensions (dict): Contain the dimension information of the component
                - body_diameter (float): the diameter of the body, is used for some geometries (m)
                - length (float): length of the component (m)
                - reference_area (float): reference area of the rocket body. normaly is the nose base area (m²)
                - initial_radius (float): initial radius of the component (m)
                - final_radius (float): final radius of the component (m)
            body (dict): contain the geometry properties of the body
                - volume (float): body volume (m³)
                - body_type (string): indicates the geometry of the body component;
                - center_of_pressure_pos (float): center of pressure position in relation to the nose tip (m)
            angle (float): AoA that is going to be analysed (rad)
        """


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
        # for the von karman geometry
        if self.body_type == "von Karman":
            self.integral = body["rIntegral"]

    def coefficients(self):
        """this method calculates the aerodynamics coefficients of the body components

        Returns:
            (dict): a dictionary that contains the coefficients
        """

        if self.body_type == "cylinder":
            normal_force_coefficient_value = 1.1 * (self.length * self.body_diameter) / self.reference_area * (sin(radians(self.angle)) ** 2)
            normal_force_angular_coefficient = normal_force_coefficient_value / self.angle

            momentum_value = 2 * sin(radians(self.angle)) / (self.reference_area * self.body_diameter) * (self.length * self.initial_area - self.volume)
            momentum_angular_coefficient = momentum_value / self.angle

        elif self.body_type == "cone": ### ERRADO (se pá) [[[NÃO TA USANDO O COMPRIMENTO DO CONE??????????]]]

            normal_force_coefficient_value = (2 * sin(radians(self.angle)) / self.reference_area) * abs(self.final_area - self.initial_area)

            normal_force_angular_coefficient = normal_force_coefficient_value / self.angle


            momentum_value = 2 * sin(radians(self.angle)) / (self.reference_area * self.body_diameter) * (self.length * self.final_area - self.volume)
            momentum_angular_coefficient = momentum_value / self.angle

        elif self.body_type == "von karman":

            # this attribute is only needed with the von karman geometry

            normal_force_angular_coefficient = ((4*np.pi)/self.reference_area) * (np.sin(radians(self.angle))/self.angle) * (0.5*self.body_diameter) * self.integral
            normal_force_coefficient_value = normal_force_angular_coefficient * self.angle

            momentum_value = 2 * sin(radians(self.angle)) / (self.reference_area * self.body_diameter) * (self.length * self.final_area - self.volume)
            momentum_angular_coefficient = (2 / (self.reference_area * self.body_diameter)) * (self.length * self.final_area - self.volume)

        return {
            "normal_force_coefficient_value": normal_force_coefficient_value,
            "normal_force_angular_coefficient": normal_force_angular_coefficient,
            "momentum_value": momentum_value,
            "momentum_angular_coefficient": momentum_angular_coefficient,
            "center_of_pressure_pos" : self.center_of_pressure_pos

        }


class BarrowmanFins():

    def __init__(self, dimensions, body, angle):
        """The class recieve two dictionaries with the variables needed for the method

        Args:
            dimensions (dict): Contain the dimension information of the component
                - spanwise_length (float): span length of the fin (m)
                - max_body_diameter (float): max body diameter (m)
                - number_of_fins (int): number of fins on the finset (-)
            body (dict): contain the geometry properties of the body
                - center_of_pressure_pos: center of pressure possition in relation to nose cone tip (m)
                - refence_area (float): reference area of the fins (m²)
                - fin_area (float): area of one fin (m²)
                - beta (float): beta parameter (-)
                - sweep_angle: sweep angle of the fin (rad)
        """
        self.spanwise_length = dimensions["spanwise_length"]
        self.max_body_diameter = dimensions["max_body_diameter"]
        self.number_of_fins = dimensions["number_of_fins"]
        self.center_of_pressure_pos = body["center_of_pressure_pos"]
        self.reference_area = dimensions["reference_area"]
        self.fin_area = body["fin_area"]
        self.beta = body["beta"]
        self.sweep_angle = body["sweep_angle"]
        self.aspect_ratio = body["aspect_ratio"]
        self.angle = angle

    def coefficients(self):
        """Thos method calculats the aerodynamic coefficients of the finset

        Returns:
            (dict): dictionary with the aerodynamic coefficients
        """
        #==================================================================================================================================================================================================================
        # barrowman equations, [[[NOT WORKING]]]
        # normal_force_angular_coefficient_one_fin = ((2 * pi * self.spanwise_length ** 2) / self.reference_area)/(1 + sqrt(1 + ((self.beta * self.spanwise_length ** 2) / (self.fin_area * cos(self.sweep_angle))) ** 2))

        # # normal force coefficient derivative for N fins [DOUBLE CHECK THE REFERENCE FOR Ntot (total number of parallel fins that have an interference effect)]
        # normal_force_angular_coefficient = (self.number_of_fins / 2) * normal_force_angular_coefficient_one_fin

        # ktb = 1 + (self.max_body_diameter / 2) / (self.spanwise_length + (self.max_body_diameter / 2)) # Correction term for the normal force on the fins due to the body
        # normal_force_coefficient = ktb * normal_force_angular_coefficient # final normal force coefficient derivative for the fins
        #==================================================================================================================================================================================================================

        # Cna of one fin
        normal_force_angular_coefficient_one_fin = ((pi * self.aspect_ratio) / (2 * self.angle) * abs(sin(radians(self.angle)) * cos(radians(self.angle))) + (2 * sin(radians(self.angle)) ** 2) / self.angle) * (self.fin_area / self.reference_area)

        # Cna for the finset
        normal_force_angular_coefficient = (self.number_of_fins / 2) * normal_force_angular_coefficient_one_fin

        #Cn of the fin
        normal_force_coefficient = normal_force_angular_coefficient * self.angle



        return {
            "normal_force_angular_coefficient_one_fin": normal_force_angular_coefficient_one_fin,
            "normal_force_angular_coefficient": normal_force_angular_coefficient,
            "normal_force_coefficient_value": normal_force_coefficient,
            "momentum_value": 0,
            "momentum_angular_coefficient": 0,
            "center_of_pressure_pos": self.center_of_pressure_pos
        }
