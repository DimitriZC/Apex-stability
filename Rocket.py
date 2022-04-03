import numpy as np
from matplotlib import pyplot as plt

from geometry import Body, Fins
from barrowman import BarrowmanBody, BarrowmanFins


class Rocket():
    """
    This class takes all components coefficients and calculate them for the whole rocket
    """

    def __init__(self, data, _rocket, internal_components):
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
            internal_components (list): list of dictionaries with internal components data
        """
        self.rho = data["rho"]
        self.Mach = data["Mach"]
        self.free_stream_velocity = data["free_stream_velocity"]
        self.angle = data["angle"]
        self.sound_velocity = data["sound_velocity"]
        self._rocket = _rocket
        self.internal_components = internal_components

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
        #     fins_geometry = Fins(rocket.fins).coefficiecomponent['final_radius'] * 2ail, boattail_geometry, self.angle).coefficients()
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
        for component in self.internal_components:
            total_weight += component["weight"]

        # for component in weight_pos_components: ### componentes de peso
        #     total_weight += component[0]
        # for component in weight_pos_components:
        #     cg_pos += (component[0] * component[1]) / total_weight

        for component in self.components_geometry:
            cg_pos += component["weight"] * component["center_of_gravity_pos"] / total_weight

        for component in self.internal_components:
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

    def normal_force_coefficient(self, use_angle = False, angle = 0):
        """This method takes the normal force angular coefficient, and plot the normal force value
        for a range of AoA
        """

        if use_angle:
            aoa = angle
        else:
            aoa = self.angle

        rocket_normal_force_coefficient = self.normal_force_angular_coefficient() * aoa

        return rocket_normal_force_coefficient

    def angular_momentum_coefficient(self):
        """This methos calculates the resulting momentum angular coefficient for te whole rocket

        Returns:
            (float): Normal force angular coefficient of the rocket
        """

        # angular_momentum_coefficient_rocket = 0

        # for component in self.components_barrowman:
        #     angular_momentum_coefficient_rocket += component["angular_momentum_coefficient"]

        angular_momentum_coefficient_rocket = - (self.static_margin() * self.normal_force_angular_coefficient())

        return angular_momentum_coefficient_rocket

    def momentum_coefficient(self, use_angle = False, angle = 0, barrowman = False):
        """This method takes the momentum coefficient, and plot the normal force value
        for a range of AoA

        Args:
            use_angle (boolean): set to True if you want to set the angle of attack manually;
            angle (float): Value of the Angle of attack to be used if use_angle == True;
            Barrowman (boolean): temporary argument to test barrowman method (results are really bad)
        """

        if barrowman:
            momentum_coefficient_rocket = 0

            for component in self.components_barrowman:
                momentum_coefficient_rocket += component["momentum_value"]

            return momentum_coefficient_rocket



        if use_angle:
            aoa = angle
        else:
            aoa = self.angle


        rocket_angular_momentum_coefficient = self.angular_momentum_coefficient()

        rocket_momentum_coefficient = rocket_angular_momentum_coefficient * aoa

        return rocket_momentum_coefficient

    def damping_ratio(self):

        # Calcular Momento de inercia do foguete
        # Estimar frequencia natural ????
        # Tirar o m'
        # Verificar se o x_nozzle é o cp do bocal do foguete
        # Se o m' está junto da somatoria o Cna (acho q não)

        damping_ratio = 0

        for component in self._rocket:
            if component["name"] == "nose":
                reference_area = np.pi * component['final_radius'] ** 2
                break


        return damping_ratio


    def plot_coefficients(self, plot=True):
        """
        This method will plot the Cn, Cp, Cd and damping coefficient with respect to alpha
        """

        angles = np.arange(0.1, 13, 0.5)
        normal_force_coefficient = list()
        momentum_coefficient = list()
        static_margin = list()

        normal_force_angular_coefficient = self.normal_force_angular_coefficient()

        for aoa in angles:
            # normal_force_coefficient.append(normal_force_angular_coefficient * aoa)
            normal_force_coefficient.append(self.normal_force_coefficient(use_angle = True, angle = aoa))


            for k, component in enumerate(self._rocket):
                #This loop is chanching the aoa to analyse the angular coefficient for the momentun, since he isn't linear

                if component["geometry_method"] == "body":
                    self.components_barrowman[k] = (BarrowmanBody(component, self.components_geometry[k], aoa).coefficients())
                elif component["geometry_method"] == "fin":
                    self.components_barrowman[k] = (BarrowmanFins(component, self.components_geometry[k], aoa).coefficients())

            #calculating the momentum for the new aoa
            momentum_coefficient.append(self.angular_momentum_coefficient() * aoa)
            # print(f'Cma => {self.angular_momentum_coefficient()} aoa => {aoa} ==> {self.angular_momentum_coefficient() * aoa}')
            static_margin.append(self.static_margin())




        if plot:

            plt.style.use(['science', 'notebook', 'grid'])



            fig, axes = plt.subplots(2, 2)

            Cn = axes[0][0]
            Cn.plot(angles, normal_force_coefficient, color="#000")
            # Cn.set_title("Normal Force Coefficient")
            Cn.set_xlabel("aoa")
            Cn.set_ylabel("Cn")

            SM = axes[0][1]
            SM.plot(angles, static_margin, color="#000")
            # SM.set_title("Static Margin")
            SM.set_xlabel("aoa")
            SM.set_ylabel("SM")

            Cm = axes[1][0]
            Cm.plot(angles, momentum_coefficient, color="#000")
            # Cm.set_title("Momentum Coefficient")
            Cm.set_xlabel("aoa")
            Cm.set_ylabel("Cm")

            plt.show()
        return normal_force_coefficient, static_margin

