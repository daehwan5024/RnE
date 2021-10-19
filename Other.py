import numpy as np
import matplotlib.pyplot as plt

class Other:
    def __init__(self, goal, k_p, k_i, k_d):
        self.goal = goal
        self.location = []
        self.error = []
        self.time = []
        self.Integral = 0
        self.k_i = k_i
        self.k_p = k_p
        self.k_d = k_d
        self.length = 0

    def do(self, location, time):
        if location == -1 :
            return 0
        self.location.append(location)
        self.error.append(self.goal - location)
        self.time.append(time)
        if self.length == 1:
            derivative = 0

        else:
            derivative = (self.error[-1]-self.error[-2])/(self.time[-1] - self.time[-2])
            self.Integral += (self.error[-1] + self.error[-2]) * (self.time[-1] - self.time[-2]) / 2


        return self.error[-1]*self.k_p + self.Integral*self.k_i + derivative*self.k_d
