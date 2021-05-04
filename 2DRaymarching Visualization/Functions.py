from math import sqrt
import numpy as np

def SignedDistance( a, b, r):
    distance = sqrt( (a[0] - b.position[0]) ** 2 + (a[1] - b.position[1]) ** 2 )
    return distance - r

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def offScreen(current_vector, max_width, max_height):
    x = int(current_vector[0])
    y = int(current_vector[1])
    if x < 0 or x > max_width or y < 0 or y > max_height:
        return True
    else:
        return False

def rotate( point, degree):
    point.angle += degree
