import numpy as np

class Body():

    def __init__(self, dimensions):
        """This class takes a dictionary with the dimension properties of the component to calculate the geometry values

        Args:
            dimensions (dict): Contain the dimension information of the component
                - reference_area (float): reference area of the rocket body. normaly is the nose base area (m²)
                - initial_radius (float): initial radius of the component (m)
                - final_radius (float): final radius of the component (m)
                - length (float): length of the component (m)
                - body_diameter (float): the diameter of the body, is used for some geometries (m)
                - weight (float) weight of the component (g)
                - position (float): position of the component in relation to the nose tip (m)
        """

        self.reference_area = dimensions["reference_area"]
        self.initial_radius = dimensions["initial_radius"]
        self.initial_area = (dimensions["initial_radius"] ** 2) * np.pi
        self.final_radius = dimensions["final_radius"]
        self.final_area = (dimensions["final_radius"] ** 2) * np.pi
        self.length = dimensions["length"]
        self.body_diameter = dimensions["body_diameter"] # ???????????????
        self.weight = dimensions["weight"]
        self.position = dimensions["position"]


    def cylinder(self):
        """This method calculate the geometry properties of a cylindrical body

        Returns:
            (dict): object with the geometry properties
        """

        # Calculate the volume of the body
        volume = self.initial_area * self.length

        # Calculate the center of pressure
        center_of_pressure_pos = self.position + (self.length / 2)
        center_of_gravity_pos = self.position + (self.length / 2)

        return {
            "volume": volume,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": self.weight,
            "body_type": "cylinder"
        }

    def cone(self):
        """This method calculate the geometry properties of a conical body

        Returns:
            (dict): object with the geometry properties
        """
        # Calculate the volume of the body
        volume = 1/3 * np.pi * ((self.initial_area / np.pi) * (np.sqrt((self.initial_area / np.pi) * (self.final_area / np.pi))) * (self.final_area / np.pi)) * self.length

        # Calculate the center of pressure
        center_of_pressure_pos = self.position + ((self.length * self.final_area - volume) / abs(self.final_area - self.initial_area)) # [VER ESSA FÓRMULA]
        # CG_x_pos: triangle + rectangle cg in respect to area; [PARECE CERTO]
        center_of_gravity_pos = self.position + ((self.length * (((2 / 3) * (abs(self.final_radius - self.initial_radius) / 2)) + (0.5 * min(self.initial_radius, self.final_radius)))) / ((self.initial_radius + self.final_radius) / 2))

        return{
            "volume": volume,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": self.weight,
            "body_type": "cone"
        }

    def von_karman(self):
        """This method calculate the geometry properties of a von karman geometry

        Returns:
            (dict): object with the geometry properties
        """

        dx = self.length/1000
        _x = np.arange(0, self.length, dx)
        _theta = [np.arccos(1 - 2*x/self.length) for x in _x]
        _r = [(0.5 * self.body_diameter / np.sqrt(np.pi)) * (np.sqrt(theta - 0.5 * np.sin(2 * theta)))  for theta in _theta]
        _r2 = [r**2 for r in _r]
        rIntegral = np.trapz(_r, _x, dx=dx)
        r2Integral = np.trapz(_r2, _x, dx=dx)
        volume = np.np.pi * r2Integral
        center_of_pressure_pos = volume / self.reference_area
        center_of_gravity_pos = 1/3 * self.length

        return{
            "volume": volume,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": self.weight,
            "rIntegral": rIntegral,
            "body_type": "von karman"
        }



class Fins():

    def __init__(self, dimensions):
        """This class takes a dictionary with the dimension properties of the component to calculate the geometry values

        Args:
            dimensions (dict): Contain the dimension information of the component
                - thickness (float): thickness of the fin (m)
                - root_chord (float): root chord of the fin (m)
                - tip_chord (float): tip chord of the fin (m)
                - spanwise_length (float): span length of the fin (m)
                - max_body_diameter (float): max body diameter (m)
                - position (float): position of the fin in relation to the nose tip (m)
                - weight (float): weight of one fin (g)
                - body_type (str): indicates the geometry of the fin airfoil
                - number_of_fins (int): number of fins on the finset (-)
                - Mach (float): Mach number (-)
        """
        self.thickness = dimensions["thickness"]
        self.root_chord = dimensions["root_chord"]
        self.tip_chord = dimensions["tip_chord"]
        self.spanwise_length = dimensions["spanwise_length"]
        self.sweep_length = dimensions["sweep_length"]
        self.max_body_diameter = dimensions["max_body_diameter"]
        self.position = dimensions["position"]
        self.weight = dimensions["weight"]
        self.body_type = dimensions["body_type"]
        self.number_of_fins = dimensions["number_of_fins"]
        self.Mach = dimensions["Mach"]



    def fin(self):
        """This method calculate the geometry properties of the fins

        Returns:
            (dict): object with the geometry properties
        """
        MAC = 0 #botar formula aqui

        # One-sided area of a single fin
        fin_area = (self.root_chord + self.tip_chord) * self.spanwise_length / 2

        # Aspec ratio of the fin
        AR = 2 * (self.spanwise_length ** 2) / fin_area

        ymac = (self.spanwise_length * (self.root_chord - 2 * self.tip_chord)) / (3 * (self.root_chord + self.tip_chord)) # MAC spanwise self.position

        # Beta parameter
        beta = np.sqrt(1 - self.Mach ** 2) if self.Mach <=1 else np.sqrt(self.Mach ** 2 - 1)

        reference_area = self.number_of_fins * self.thickness * self.spanwise_length
        if self.Mach <= 0.5 or self.Mach <= 2:

            center_of_pressure_pos = self.position +  0.25 * MAC
            #testar e comparar essas duas equações com o openrocket
            #center_of_pressure_pos =   (self.sweep_length * (self.root_chord + 2 * self.tip_chord)) / (3 * (self.root_chord + self.tip_chord)) + (self.root_chord ** 2 + self.tip_chord ** 2 + self.root_chord * self.tip_chord) / (6 * (self.root_chord + self.tip_chord)) # CP self.position (verificar uso) [CHEK REFERENCE FOR center_of_pressure_pos IF M>0.5 (pg 36)]

        elif self.Mach > 2:

            center_of_pressure_pos = self.position + ((MAC * (AR * beta - 0.67)) / (2 * AR * beta - 1))

        # calculate the sweep angle of the fin [Verificar Uso]
        sweep_angle = np.arctan(self.sweep_length / self.spanwise_length)

        # Calculate fin set weight
        fin_set_weight = self.number_of_fins * self.weight

        # Calculate the CG position in the x axis
        center_of_gravity_pos = self.position + ((2 * self.tip_chord * self.sweep_length * (self.tip_chord ** 2) + self.sweep_length * self.root_chord + (self.root_chord ** 2)) / (3 * (self.tip_chord + self.root_chord)))


        return {
            "weight": fin_set_weight,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "sweep_angle": sweep_angle,
            "reference_area": reference_area,
            "beta": beta,
            "fin_area": fin_area
        }

