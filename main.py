from geometry import Body, Fins
import foguete

class Rocket():

    def __init__(self, data):
        """This are the general variables that is going to be used by any of the methods

        Args:
            rho (float): air density (kg / m³)
            Mach (float): Mach ratio (-)
            free_stream_velocity (float): free stream velocity (m/s)
            angle (float): angle of attack (rad)
            sound_velocity (float): sound velocity (m/s)
        """
        self.rho = data["rho"]
        self.Mach = data["Mach"]
        self.free_stream_velocity = data["free_stream_velocity"]
        self.angle = data["angle"]
        self.sound_velocity = data["sound_velocity"]

        nose_cone = Body(foguete.nose).cone()
        fuselage = Body(foguete.fuselage).cylinder()
        boattail = Body(foguete.boattail).cone()
        fins = Fins(foguete.fins).fin()
        canards = Fins(foguete.canards).fin()

        print(type(nose_cone))

        self.components = [
            nose_cone,
            fuselage,
            boattail,
            fins,
            canards
        ] # temporario so pra rodar

    def center_of_gravity_pos(self):

        total_weight = 0
        cg_pos = 0

        for component in self.components:
            total_weight += component["weight"]

        # for component in weight_pos_components: ### componentes de peso
        #     total_weight += component[0]
        # for component in weight_pos_components:
        #     cg_pos += (component[0] * component[1]) / total_weight

        for component in self.components:
            cg_pos += component["weight"] * component["center_of_gravity_pos"] / total_weight

        return cg_pos


    def center_of_pressure_pos(self):

        Cna_sum = 0
        cp_pos = 0

        for component in self.components:
            Cna_sum += component["normal_force_angular_coefficient"]


        for component in self.components:
            cp_pos += component["normal_force_angular_coefficient"] * component["center_of_pressure_pos"] / Cna_sum

        return cp_pos

    def static_margin(self):

        cg_pos = center_of_gravity_pos()
        cp_pos = center_of_pressure_pos()

        return cp_pos - cg_pos #colocar em calibres

    def normal_force_angular_coefficient(self):

        normal_force_of_the_rocket = 0

        for component in components:
            normal_force_of_the_rocket += component['normal_force_coefficient_value']

        return normal_force_of_the_rocket

    def normal_force_coefficient(self):
        #plotar cn x alpha
        pass


Foguete = Rocket(foguete.dados)
teste = Foguete.center_of_gravity_pos()
print(teste)
