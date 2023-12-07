import random
import turtle


class Polygon:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        self.num_sides = random.randint(3, 5)  # triangle, square, or pentagon
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = Polygon.get_new_color()
        self.border_size = random.randint(1, 10)
        Polygon.draw_polygon(self.num_sides, self.size, self.orientation,
                             self.location, self.color, self.border_size)

    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_polygon(num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    def reposition(self, reduction_ratio):
        turtle.penup()
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= reduction_ratio
        Polygon.draw_polygon(self.num_sides, self.size, self.orientation,
                             self.location, self.color, self.border_size)


plgn = Polygon()
reduction_ratio = 0.618
plgn.reposition(reduction_ratio)

turtle.done()
