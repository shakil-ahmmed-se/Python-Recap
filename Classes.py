class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")
    def addition(self):
        print(self.x + self.y)

# point1 = Point()
# point1.draw()

point = Point(10, 30)
point.addition()
print(point.x)