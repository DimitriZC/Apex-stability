from geometry import Body, Fins
from barrowman import BarrowmanBody, BarrowmanFins
import foguete

class Rocket():

    def __init__(self, data):
        """
        data is an object that contains the basic informations.
        Theose are the general variables that are going to be used by any of the methods

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

        # temporary way to call the geometry method

        nose_cone_geometry = Body(foguete.nose).cone()
        fuselage_geometry = Body(foguete.fuselage).cylinder()
        boattail_geometry = Body(foguete.boattail).cone()
        fins_geometry = Fins(foguete.fins).fin()
        canards_geometry = Fins(foguete.canards).fin()

        # temporary way to call barrowman method

        nose_cone_barrowman = BarrowmanBody(foguete.nose, nose_cone_geometry, self.angle).coefficients()
        fuselage_barrowman = BarrowmanBody(foguete.fuselage, fuselage_geometry, self.angle).coefficients()
        boattail_barrowman = BarrowmanBody(foguete.boattail, boattail_geometry, self.angle).coefficients()
        fins_barrowman = BarrowmanFins(foguete.fins, fins_geometry).coefficients()
        canards_barrowman = BarrowmanFins(foguete.canards, canards_geometry).coefficients()

        self.components_geometry = [
            nose_cone_geometry,
            fuselage_geometry,
            boattail_geometry,
            fins_geometry,
            canards_geometry
        ] # temporario so pra rodar

        self.components_barrowman = [
            nose_cone_barrowman,
            fuselage_barrowman,
            boattail_barrowman,
            fins_barrowman,
            canards_barrowman
        ] # temporario so pra rodar

    def center_of_gravity_pos(self):
        """this method is responsable to take all components weight and position, and then calculate
        the center of gravity of the rocket

        Returns:
            (float): center of gravity posittion of the rocket
        """

        total_weight = 0
        cg_pos = 0

        for component in self.components_geometry:
            total_weight += component["weight"]

        # for component in weight_pos_components: ### componentes de peso
        #     total_weight += component[0]
        # for component in weight_pos_components:
        #     cg_pos += (component[0] * component[1]) / total_weight

        for component in self.components_geometry:
            cg_pos += component["weight"] * component["center_of_gravity_pos"] / total_weight

        return cg_pos


    def center_of_pressure_pos(self):
        """this method is responsable to take all components centers of pressure, and then calculate
        the resulting center of pressure of the rocket

        Returns:
            float: center of pressure of the whole rocket
        """

        Cna_sum = 0
        cp_pos = 0

        for component in self.components_barrowman:
            Cna_sum += component["normal_force_angular_coefficient"]


        for component in self.components_barrowman:
            cp_pos += component["normal_force_angular_coefficient"] * component["center_of_pressure_pos"] / Cna_sum

        return cp_pos

    def static_margin(self):
        """This method takes the CG and CP of the rocket and returns the static margins of the rocket

        Returns:
            float: static margin
        """

        cg_pos = self.center_of_gravity_pos()
        cp_pos = self.center_of_pressure_pos()

        return (cp_pos - cg_pos) / (foguete.nose["final_radius"] * 2) #colocar em calibres

    def normal_force_angular_coefficient(self):
        """This methos calculates the resulting normal force angular coefficient for te whole rocket

        Returns:
            (float): Normal force angular coefficient of the rocket
        """

        normal_force_of_the_rocket = 0

        for component in self.components_barrowman:
            normal_force_of_the_rocket += component['normal_force_coefficient_value']

        return normal_force_of_the_rocket

    def normal_force_coefficient(self):
        """This method takes the normal force angular coefficient, and plot the normal force value
        for a range of AoA
        """

        #plotar cn x alpha
        pass
