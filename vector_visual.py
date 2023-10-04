import turtle
import math

# no loop
# no size scaling for large vectors
# further bug testing might be needed

turtle.title("Drawing vector lines")

s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor('#fcfbe3')
t.ht()

def cartesian_plane():
    t.speed(6)
    t.pensize(4)
    t.forward(200)
    t.stamp()
    t.right(180)
    t.forward(400)
    t.stamp()
    t.backward(200)
    t.right(90)
    t.forward(200)
    t.stamp()
    t.backward(400)
    t.right(180)
    t.stamp()


def magnitude_direction():
    magnitude = turtle.numinput('Magnitude', 'Enter the magnitude of the vector.')
    direction = turtle.numinput('Direction', 'Enter the direction of your vector in degrees.')

    t.speed(4)
    t.pensize(2)
    t.color('red')

    if magnitude > 0:
        t.penup()
        t.home()
        t.pendown()
        t.setheading(direction)
        t.forward(magnitude)
    else:
        t.penup()
        t.home()
        t.left(180)
        t.pendown()
        t.setheading(direction)
        t.forward(magnitude)

    Fx = magnitude * math.cos(math.radians(direction))
    Fy = magnitude * math.sin(math.radians(direction))

    t.penup()
    t.goto(150, 175)
    t.pendown()
    t.write(f'Fx = {Fx: .2f}' +'\n'+
        f'Fy = {Fy: .2f}', 
        font = ("Corbel", 13, "normal"))


def x_y():
    x_component = turtle.numinput('x-component (Fx)', 'Enter the x-component of the vector.')
    y_component = turtle.numinput('y-component (Fy)', 'Enter the y-component of your vector.')

    t.speed(4)
    t.pensize(2)
    t.color('red')
    
    magnitude = math.sqrt((x_component**2) + (y_component**2))
    direction = math.degrees(math.atan((y_component / x_component)))

    if magnitude > 0:
        t.penup()
        t.home()
        t.pendown()
        t.setheading(direction)
        t.forward(magnitude)
    else:
        t.penup()
        t.home()
        t.left(180)
        t.pendown()
        t.setheading(direction)
        t.forward(magnitude)

    t.penup()
    t.goto(150, 175)
    t.pendown()
    t.write(f'Magnitude = {magnitude: .2f}' +'\n'+
        f'Direction = {direction: .2f}', 
        font = ("Corbel", 13, "normal"))


def resultant(direction, magnitude):
    t.speed(4)
    t.pensize(2)
    t.color('red')

    if magnitude > 0:
        t.penup()
        t.home()
        t.pendown()
        t.setheading(direction)
        t.forward(magnitude)
    else:
        t.penup()
        t.home()
        t.left(180)
        t.pendown()
        t.setheading(direction)
        t.forward(magnitude)
    
    t.penup()
    t.goto(150, 175)
    t.pendown()
    t.write(f'Magnitude = {magnitude: .2f}' +'\n'+
        f'Direction = {direction: .2f}', 
        font = ("Corbel", 13, "normal"))


def change_to_positive(num):
        if num < 0:
            num *= -1


cartesian_plane()

# Main menu
menu_option = turtle.textinput('Main menu',
                 'What would you like to do?' + '\n' +
                 '(Type the number of the option you want.)' + '\n' + '\n' +
                 '1) Draw vector' + '\n' +
                 '2) Calculate resultant between two vectors' + '\n' +
                 '3) Quit')

# Drawing vectors (option 1)
if menu_option == '1':
    while True:
        option_1 = turtle.textinput('Draw vector',
                                    'What parameters would you like to use?' + '\n' +
                                    '(Type the number of the option you want.)' + '\n' + '\n' +
                                    '1) Magnitude and direction.' + '\n' +
                                    '2) X and Y components (Fx and Fy).')
        if option_1 == '1':
            magnitude_direction()
            break
        elif option_1 == '2':
            x_y()
            break
        else:
            continue

# Calculate resultant (option 2)
elif menu_option == '2':
    while True:
        option_2_v1 = turtle.textinput('Resultant between two vectors (1)',
                                    'What parameters would you like to use for the first vector?' + '\n' +
                                    '(Type the number of the option you want.)' + '\n' + '\n' +
                                    '1) Magnitude and direction.' + '\n' +
                                    '2) X and Y components (Fx and Fy).')
        if option_2_v1 == '1':
            # Magnitude and direction
            magnitude = turtle.numinput('Magnitude', 'Enter the magnitude of the vector.')
            direction = turtle.numinput('Direction', 'Enter the direction of your vector in degrees.')

            Fx_1 = magnitude * math.cos(math.radians(direction))
            Fy_1 = magnitude * math.sin(math.radians(direction))
            
            break

        elif option_2_v1 == '2':
            # X and Y components
            Fx_1 = turtle.numinput('x-component (Fx)', 'Enter the x-component of the vector.')
            Fy_1 = turtle.numinput('y-component (Fy)', 'Enter the y-component of your vector.')

            break

        else:
            continue

    while True:
        option_2_v2 = turtle.textinput('Resultant between two vectors (2)',
                                    'What parameters would you like to use for the second vector?' + '\n' +
                                    '(Type the number of the option you want.)' + '\n' + '\n' +
                                    '1) Magnitude and direction.' + '\n' +
                                    '2) X and Y components (Fx and Fy).')
        if option_2_v2  == '1':
            magnitude = turtle.numinput('Magnitude', 'Enter the magnitude of the vector.')
            direction = turtle.numinput('Direction', 'Enter the direction of your vector in degrees.')

            Fx_2 = magnitude * math.cos(math.radians(direction))
            Fy_2 = magnitude * math.sin(math.radians(direction))

            break
        
        elif option_2_v2 == '2':
            Fx_2 = turtle.numinput('x-component (Fx)', 'Enter the x-component of the vector.')
            Fy_2 = turtle.numinput('y-component (Fy)', 'Enter the y-component of your vector.')

            break

        else:
            continue
    
    # Calculating resultant
    magnitude = math.sqrt(((Fx_1 + Fx_2)**2 + (Fy_1 + Fy_2)**2))

    change_to_positive(Fx_1)
    change_to_positive(Fx_2)
    change_to_positive(Fy_1)
    change_to_positive(Fy_2)

    direction = math.degrees(math.atan((Fy_1 + Fy_2) / (Fx_1 + Fx_2)))

    resultant(direction, magnitude)

else:
    turtle.bye()


turtle.done()