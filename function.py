import matplotlib as plt
import numpy as np

def density_from_height(h, scale_height):
    return (1.225 * np.exp(1)**(-h/scale_height))
