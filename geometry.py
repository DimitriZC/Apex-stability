from numpy import pi, sqrt, arccos

class Body():

    def __init__(self, dimensions):
        self.reference_area = dimensions["reference_area"]
        self.initial_radius = dimensions["initial_radius"]
        self.initial_area = (dimensions["initial_radius"] ** 2) * pi
        self.final_radius = dimensions["final_radius"]
        self.final_area = (dimensions["final_radius"] ** 2) * pi
        self.length = dimensions["length"]
        self.body_diameter = dimensions["body_diameter"] # ???????????????
        self.weight = dimensions["weight"]
        self.position = dimensions["position"]


    def cylinder(self):
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

        # Calculate the volume of the body
        volume = 1/3 * pi * ((self.initial_area / pi) * (sqrt((self.initial_area / pi) * (self.final_area / pi))) * (self.final_area / pi)) * self.length

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
        dx = self.length/1000
        _x = np.arange(0, self.length, dx)
        _theta = [np.arccos(1 - 2*x/self.length) for x in _x]
        _r = [(0.5 * self.body_diameter / np.sqrt(np.pi)) * (np.sqrt(theta - 0.5 * np.sin(2 * theta)))  for theta in _theta]
        _r2 = [r**2 for r in _r]
        rIntegral = np.trapz(_r, _x, dx=dx)
        r2Integral = np.trapz(_r2, _x, dx=dx)
        volume = np.pi * r2Integral
        center_of_pressure_pos = volume / self.reference_area
        center_of_gravity_pos = 1/3 * self.length

        return{
            "volume": volume,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": weight,
            "rIntegral": rIntegral,
            "body_type": "von karman"
        }



class Fins():

    def __init__(self, dimensions):

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

        MAC = 0 #botar formula aqui

        # One-sided area of a single fin
        fin_area = (self.root_chord + self.tip_chord) * self.spanwise_length / 2

        # Aspec ratio of the fin
        AR = 2 * (self.spanwise_length ** 2) / fin_area

        ymac = (self.spanwise_length * (self.root_chord - 2 * self.tip_chord)) / (3 * (self.root_chord + self.tip_chord)) # MAC spanwise self.position

        # Beta parameter
        beta = sqrt(1 - self.Mach ** 2) if self.Mach <=1 else sqrt(self.Mach ** 2 - 1)

        reference_area = self.number_of_fins * self.thickness * self.spanwise_length
        if self.Mach <= 0.5 or self.Mach <= 2:

            center_of_pressure_pos = self.position +  0.25 * MAC
            #testar e comparar essas duas equações com o openrocket
            #center_of_pressure_pos =   (self.sweep_length * (self.root_chord + 2 * self.tip_chord)) / (3 * (self.root_chord + self.tip_chord)) + (self.root_chord ** 2 + self.tip_chord ** 2 + self.root_chord * self.tip_chord) / (6 * (self.root_chord + self.tip_chord)) # CP self.position (verificar uso) [CHEK REFERENCE FOR center_of_pressure_pos IF M>0.5 (pg 36)]

        elif self.Mach > 2:

            center_of_pressure_pos = self.position + ((MAC * (AR * beta - 0.67)) / (2 * AR * beta - 1))

        # calculate the sweep angle of the fin [Verificar Uso]
        sweep_angle = arccos(self.spanwise_length / sqrt(self.spanwise_length ** 2 + ((self.tip_chord / 2) + self.sweep_length - self.root_chord / 2)))

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
            "sin_area": fin_area
        }

