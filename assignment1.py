import numpy as np
from sim.sim1d import sim_run

# Simulator options.
options = {}
options["FIG_SIZE"] = [8, 8]
options["CONSTANT_SPEED"] = False


class KalmanFilterToy:
    def __init__(self, gain_ratio=0.5):
        self.v = 0
        self.prev_x = 0
        self.prev_t = 0
        self.gain = gain_ratio

    def predict(self, t):
        prediction = self.prev_x + self.v * (t - self.prev_t)
        return prediction

    def measure_and_update(self, x, t):
        measured_v = (x - self.prev_x) / (t - self.prev_t)
        self.v += self.gain * (measured_v - self.v)
        self.prev_x = x
        self.prev_t = t


sim_run(options, KalmanFilterToy, gain_ratio=0.7)
