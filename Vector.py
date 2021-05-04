from math import sqrt, pow

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2) )

    def normalize(vec):
        mag = vec.magnitude()
        if mag != 0:
            return Vector3(vec.x/mag, vec.y/mag, vec.z/mag)
        else:
            return Vector3(0, 0, 0)

    def __add__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x + b.x, self.y + b.y, self.z + b.z)
        elif type(b) is Vector2:
            return Vector3(self.x + b.x, self.y + b.x, self.z)
        else:
            return Vector3(self.x + b, self.y + b, self.z + b)

    def __sub__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x - b.x, self.y - b.y, self.z - b.z)
        elif type(b) is Vector2:
            return Vector3(self.x - b.x, self.y - b.y, self.z)
        else:
            return Vector3(self.x - b, self.y - b, self.z - b)

    def __mul__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x * b.x, self.y * b.y, self.z * b.z)
        return Vector3(self.x * b, self.y * b, self.z * b)

    def __truediv__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x / b.x, self.y / b.y, self.z / b.z)
        return Vector3(self.x / b, self.y / b, self.z / b)

    def cross(a, b):
        return Vector3((a.y * b.z) - (a.z * b.y),
                       (a.z * b.x) - (a.x * b.z),
                       (a.x * b.y) - (a.y * b.x))

    def toMatrix(self):
        return [[self.x], [self.y], [self.z]]


    def __repr__(self):
        return f'{self.x} , {self.y}, {self.z}'
