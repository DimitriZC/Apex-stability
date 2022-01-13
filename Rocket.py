import numpy as np
from matplotlib import pyplot as plt

from geometry import Body, Fins
from barrowman import BarrowmanBody, BarrowmanFins


class Rocket():
    """
    This class takes all components coefficients and calculate them for the whole rocket
    """

    def __init__(self, data, _rocket):
        """
        data is an object that contains the basic informations.
        Theose are the general variables that are going to be used by any of the methods

        Args:
            rho (float): air density (kg / m³)
            Mach (float): Mach ratio (-)
            free_stream_velocity (float): free stream velocity (m/s)
            angle (float): angle of attack (rad)
            sound_velocity (float): sound velocity (m/s)
            _rocket (list): list of dictionaries with components data
        """
        self.rho = data["rho"]
        self.Mach = data["Mach"]
        self.free_stream_velocity = data["free_stream_velocity"]
        self.angle = data["angle"]
        self.sound_velocity = data["sound_velocity"]
        self._rocket = _rocket

        self.components = []

        self.components_geometry = [] # temporario so pra rodar

        self.components_barrowman = [] # temporario so pra rodar

        for k, component in enumerate(self._rocket):
            self.components.append(component["name"])

            if component["geometry_method"] == "body":
                self.components_geometry.append(Body(component).coefficients())
                self.components_barrowman.append(BarrowmanBody(component, self.components_geometry[k], self.angle).coefficients())
            elif component["geometry_method"] == "fin":
                self.components_geometry.append(Fins(component).coefficients())
                self.components_barrowman.append(BarrowmanFins(component, self.components_geometry[k], self.angle).coefficients())

# Delete after making tests ====================================================================
        #     nose_cone_geometry = Body(rocket.nose).coefficients()
        #     fuselage_geometry = Body(rocket.fuselage).coefficients()
        #     boattail_geometry = Body(rocket.boattail).coefficients()
        #     fins_geometry = Fins(rocket.fins).coefficients()
        #     canards_geometry = Fins(rocket.canards).coefficients()

        # # temporary way to call barrowman method

        # nose_cone_barrowman = BarrowmanBody(rocket.nose, nose_cone_geometry, self.angle).coefficients()
        # fuselage_barrowman = BarrowmanBody(rocket.fuselage, fuselage_geometry, self.angle).coefficients()
        # boattail_barrowman = BarrowmanBody(rocket.boattail, boattail_geometry, self.angle).coefficients()
        # fins_barrowman = BarrowmanFins(rocket.fins, fins_geometry, self.angle).coefficients()
        # canards_barrowman = BarrowmanFins(rocket.canards, canards_geometry, self.angle).coefficients()
# Delete after making tests ====================================================================




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

        for component in self._rocket:
            if component["name"] == "nose":
                reference_diameter = component['final_radius'] * 2
                break


        return (cp_pos - cg_pos) / (reference_diameter) #colocar em calibres

    def normal_force_angular_coefficient(self):
        """This methos calculates the resulting normal force angular coefficient for te whole rocket

        Returns:
            (float): Normal force angular coefficient of the rocket
        """

        normal_force_angular_coefficient_rocket = 0

        for component in self.components_barrowman:
            normal_force_angular_coefficient_rocket += component['normal_force_angular_coefficient']

        return normal_force_angular_coefficient_rocket

    def normal_force_coefficient(self):
        """This method takes the normal force angular coefficient, and plot the normal force value
        for a range of AoA
        """

        #plotar cn x alpha
        pass

    def momentum_angular_coefficient(self):
        """This methos calculates the resulting momentum angular coefficient for te whole rocket

        Returns:
            (float): Normal force angular coefficient of the rocket
        """

        momentum_angular_coefficient_rocket = 0

        for component in self.components_barrowman:
            momentum_angular_coefficient_rocket += component["momentum_angular_coefficient"]

        return momentum_angular_coefficient_rocket

    def momentum_coefficient(self):
        """This method takes the momentum coefficient, and plot the normal force value
        for a range of AoA
        """

        #plotar cn x alpha
        pass

    def plot_coefficients(self, plot=True, save=False):
        """
        This method will plot the Cn, Cp, Cd and damping coefficient with respect to alpha
        """

        angles = np.arange(-20, 20, 1)
        normal_force_coefficient = list()
        momentum_coefficient = list()

        angular_momentum_coefficient = self.momentum_angular_coefficient()
        normal_force_angular_coefficient = self.normal_force_angular_coefficient()

        for aoa in angles:
            normal_force_coefficient.append(normal_force_angular_coefficient * aoa)
            momentum_coefficient.append(angular_momentum_coefficient * aoa)

        if plot:
            fig = plt.figure()

            Cn = fig.add_subplot(121)
            Cn.plot(normal_force_coefficient, angles, color="#000")
            Cn.grid()
            Cn.set_title("Normal Force Coefficient")
            Cn.set_xlabel("aoa")
            Cn.set_ylabel("Cn")

            Cm = fig.add_subplot(122)
            Cm.plot(momentum_coefficient, angles, color="#000")
            Cm.grid()
            Cm.set_title("Momentum Coefficient")
            Cm.set_xlabel("aoa")
            Cm.set_ylabel("Cm")
            
            if save:
                plt.savefig("./img/plot.png")
            else:
                plt.show()
        return normal_force_coefficient, momentum_coefficient

