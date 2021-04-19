class Body():

    def __init__(self, dimensions):
        self.reference_area = dimensions[reference_area]
        self.initial_area = dimensions[initial_area]
        self.final_area = dimensions[final_area]
        self.weight = dimensions[weight]

    def cylinder():
        # Calculate the volume of the body
        volume = initial_area * length

        # Calculate the center of pressure
        center_of_pressure_pos = self.position + (length / 2)
        center_of_gravity_pos = self.position + (length / 2)

        return {
            "volume": volume,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": weight,
            "body_type": "cylinder"
        }

    def cone():

        # Calculate the volume of the body
        volume = 1/3 * pi * ((initial_area / pi) * (sqrt((initial_area / pi) * (final_area / pi))) * (final_area / pi)) * length

        # Calculate the center of pressure
        center_of_pressure_pos = self.position + ((length * final_area - volume) / abs(final_area - initial_area)) # [VER ESSA FÓRMULA]
        # CG_x_pos: triangle + rectangle cg in respect to area; [PARECE CERTO]
        center_of_gravity_pos = self.position + ((length * (((2 / 3) * (abs(final_radius - initial_radius) / 2)) + (0.5 * min(initial_radius, final_radius)))) / ((initial_radius + final_radius) / 2))

        return{
            "volume": volume,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": weight,
            "body_type": "cone"
        }

    def von_karman():
        dx = length/1000
        _x = np.arange(0, length, dx)
        _theta = [np.arccos(1 - 2*x/length) for x in _x]
        _r = [(0.5 * body_diameter / np.sqrt(np.pi)) * (np.sqrt(theta - 0.5 * np.sin(2 * theta)))  for theta in _theta]
        _r2 = [r**2 for r in _r]
        rIntegral = np.trapz(_r, _x, dx=dx)
        r2Integral = np.trapz(_r2, _x, dx=dx)
        volume = np.pi * r2Integral
        center_of_pressure_pos = volume / reference_area
        center_of_gravity_pos = 1/3 * length

        return{
            "volume": volume,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": weight,
            "rIntegral": rIntegral,
            "body_type": "von karman"
        }



class Fins():

    def __init__(
            self,
            thickness,
            root_chord,
            tip_chord,
            spanwise_length,
            position
        ):

        self.thickness = thickness
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.spanwise_length = spanwise_length
        self.position = position


    def fin():


        # One-sided area of a single fin
        Afin = (self.root_chord + self.tip_chord) * self.spanwise_length / 2

        # Aspec ratio of the fin
        AR = 2 * (self.spanwise_length ** 2) / Afin

        ymac = (self.spanwise_length * (self.root_chord - 2 * self.tip_chord)) / (3 * (self.root_chord + self.tip_chord)) # MAC spanwise self.position

        reference_area = N * self.thickness * self.spanwise_length
        if Mach <= 0.5 or Mach <= 2:

            center_of_pressure_pos = self.position +  0.25 * MAC
            #testar e comparar essas duas equações com o openrocket
            #center_of_pressure_pos =   (Xt * (self.root_chord + 2 * self.tip_chord)) / (3 * (self.root_chord + self.tip_chord)) + (self.root_chord ** 2 + self.tip_chord ** 2 + self.root_chord * self.tip_chord) / (6 * (self.root_chord + self.tip_chord)) # CP self.position (verificar uso) [CHEK REFERENCE FOR center_of_pressure_pos IF M>0.5 (pg 36)]

        elif Mach > 2:

            center_of_pressure_pos = self.position + ((MAC * (AR * beta - 0.67)) / (2 * AR * beta - 1))

        # calculate the sweep angle of the fin
        Tc = np.arccos(self.spanwise_length / sqrt(self.spanwise_length ** 2 + ((self.tip_chord / 2) + Xt - self.root_chord / 2)))

        return {
            "fin_set_weight": fin_set_weight,
            "center_of_pressure_pos": center_of_pressure_pos,
            "center_of_gravity_pos": center_of_gravity_pos,
            "weight": fin_set_weight
        }

