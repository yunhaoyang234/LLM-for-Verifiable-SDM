class AutonomousVehicle():
	def __init__(self):
        self.pedestrian = False
        self.car = False
        self.stop_sign = False

    @abstractmethod
    def move_forward(self):
    	# vehicle starts moving forward
        pass

    @abstractmethod
    def turn_left(self):
    	# vehicle turns left
        pass

    @abstractmethod
    def turn_right(self):
    	# vehicle turns right
        pass

    @abstractmethod
    def stop(self):
    	# vehicle slows down and stops
        pass

    @abstractmethod
    def approach_stop_sign(self):
        # go straight and approach the observed stop sign
        pass

    @abstractmethod
    def observe(self):
     	# vehicle observe the environment and update the variables
        # self.pedestrian = {True, False}
        # self.car = {True, False}
        # self.stop_sign = {True, False}
        # self.chair = {True, False}
     	pass
    
    def pedestrian_observed(self):
        return self.pedestrian

    def car_observed(self):
        return self.car

    def stop_sign_observed(self):
        return self.stop_sign

