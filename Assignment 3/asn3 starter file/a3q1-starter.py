#141 assignment 3

# python modules
import turtle as t


def draw_spiral(num_segments,length):
    """
    Uses turtle graphics to draw a spiral with a random color,
    starting at random location.

    :param num_segments: The number of line segments in the spiral
    :param length: The number of pixels in the first segment
    :return: none
    """
    # Here you need to write code to change the pencolor of the turtle to a random color
    # You also need to produce a random starting location for the spiral
    
    t.up()
    t.goto(x, y)
    t.down()

    # Here you need to write a loop to produce the spiral

################################################################
# main program
################################################################
# Set up the turtle to draw fast
t.speed(10)
t.hideturtle()
t.title('Spiral Art')

# decide the length of the first spiral segment
number_of_pixels = 2

# decide how many spirals will be drawn
# This should be between 1 and 7
number_of_spirals = 5

# Here draw the spirals using a loop calling a function draw_spiral()
# The first spiral should have 20 segments, and 2nd should have a random
# number of segments between 20 and 30, and the third should a random
# number of segments between 20 and 40, and so on...


# tell the turtle we are done!
t.done()