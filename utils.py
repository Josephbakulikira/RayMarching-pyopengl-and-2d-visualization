import numpy as np
from math import pi, tan, sin, cos
from Vector import *

def toRadians(degrees):
    return degrees * pi / 180

# def lookAt( eyev, centerv, upv):
#     diff1 = centerv - eyev
#     f = Vector3.normalize( diff1)
#     s = Vector3.normalize(Vector3.cross(f, upv))
#     u = Vector3.cross(s, f)
#     return np.array([ [s.x, s.y, s.z, 0.0],
#                       [u.x, u.y, u.z, 0.0],
#                       [-f.x, -f.y, -f.z, 0.0],
#                       [0.0, 0.0, 0.0, 0.0]])

# def lookAt(camera_position, camera_target, up_vector):
# 	vector = camera_target - camera_position
# 	vector = vector / np.linalg.norm(vector)
#
# 	vector2 = np.cross(up_vector, vector)
# 	vector2 = vector2 / np.linalg.norm(vector2)
#
# 	vector3 = np.cross(vector, vector2)
# 	return np.array([
# 		[vector2[0], vector3[0], vector[0], 0.0],
# 		[vector2[1], vector3[1], vector[1], 0.0],
# 		[vector2[2], vector3[2], vector[2], 0.0],
# 		[-np.dot(vector2, camera_position), -np.dot(vector3, camera_position), np.dot(vector, camera_position), 1.0]
# 	])

# def perspective_fov(fov, aspect_ratio, near_plane, far_plane):
# 	num = 1.0 / np.tan(fov / 2.0)
# 	num9 = num / aspect_ratio
# 	return np.array([
# 		[num9, 0.0, 0.0, 0.0],
# 		[0.0, num, 0.0, 0.0],
# 		[0.0, 0.0, far_plane / (near_plane - far_plane), -1.0],
# 		[0.0, 0.0, (near_plane * far_plane) / (near_plane - far_plane), 1.0]
# 	])
#
# def cameraFrustum(FOV, ASPECT):
#     identity = np.identity(4);
#     fov = toRadians(tan(FOV * 0.5))
#     r_UP = Vector3(0, fov, 0)
#     r_RIGHT = Vector3(fov * ASPECT, 0, 0)
#     r_BOTTOMLEFT = (Vector3(0, 0, -1) - r_RIGHT - r_UP)
#     r_BOTTOMRIGHT = (Vector3(0, 0, -1) + r_RIGHT - r_UP)
#     r_TOPLEFT = (Vector3(0, 0, -1) - r_RIGHT + r_UP);
#     r_TOPRIGHT = (Vector3(0, 0, -1) + r_RIGHT + r_UP);
#
#     return np.array([ r_TOPLEFT.toArray4(),
#                       r_TOPRIGHT.toArray4(),
#                       r_BOTTOMRIGHT.toArray4(),
#                       r_BOTTOMLEFT.toArray4()])
