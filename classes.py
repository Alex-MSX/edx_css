class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def modulus(self):
        return pow(pow(self.x,2) + pow(self.y,2),0.5)

p = Point(3,4)
print(p.x)
print(p.y)

print(p.modulus())
