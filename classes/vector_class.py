import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2))
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range. Use 0 for x or 1 for y.")


v1 = Vector(2, 4)
v2 = Vector(3, 1)

print(v1)              # Output: Vector(2, 4)
print(v1 + v2)         # Output: Vector(5, 5)
print(v1 - v2)         # Output: Vector(-1, 3)
print(v1 * 3)          # Output: Vector(6, 12)
print(v1 == Vector(2, 4)) # Output: True
print(len(v1))         # Output: 4 (magnitude of ~4.47 rounded to 4)
print(v1[0])           # Output: 2 (x component)
print(v1[1])           # Output: 4 (y component)





# NotImplemented is a special singleton value used in operator overloading to signal that an operation is not implemented for the given operands.