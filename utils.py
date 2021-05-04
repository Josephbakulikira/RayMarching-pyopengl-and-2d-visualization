import numpy as np
from math import pi
from Vector import *

def toRadians(degrees):
    return degrees * pi / 180

def lookAt( eyev, centerv, upv):
    diff1 = centerv - eyev
    f = Vector3.normalize( diff1)
    s = Vector3.normalize(Vector3.cross(f, upv))
    u = Vector3.cross(s, f)
    return np.array([ [s.x, s.y, s.z, 0.0],
                      [u.x, u.y, u.z, 0.0],
                      [-f.x, -f.y, -f.z, 0.0],
                      [0.0, 0.0, 0.0, 0.0]])
