import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipi.spatial.distance import squareform, pdist
from numpy.linalg import norm

width, height = 640, 480

class Boids:
    """ Class that represents Boids simulation """
    def __init__(self, N):
        """ Initialize the Boid simulation """
        # init position & velocities
        self.pos = [width/2.0, height/2.0] + 10*np.random.rand(2*N).reshape(N, 2)
        # normalized random velocities
        angles = 2*math.pi*np.random.rand(N)