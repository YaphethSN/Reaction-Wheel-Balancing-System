from dataclasses import dataclass

@dataclass
class PendulumParameters:
    mass: float = 0.5   
    rod_length: float = 0.2 
    gravity: float = 9.81   

    @property
    def com_distance(self):
        return self.rod_length / 2

    @property
    def inertia(self):
        return (1/3) * self.mass * self.rod_length**2