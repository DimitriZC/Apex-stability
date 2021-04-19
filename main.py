import geometry
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

    components = [
        nose_cone = geometry.Body.cone(foguete.nose),
        fuselage = geometry.Body.cylinder(foguete.fuselage),
        boattail = geometry.Body.cone(foguete.boattail),
        fins = geometry.Fins.fin(foguete.fins),
        canards = geometry.Fins.fin(foguete.canards)
    ]

    def center_of_gravity_pos():
        pass

    def center_of_pressure_pos():
        pass

    def static_margin():
        pass

    def normal_force_angular_coefficient():
        pass

    def normal_force_coefficient():
        #plotar cn x alpha
        pass
