import turtle

#well well this was super fun
def draw():
    window = turtle.Screen()
    window.bgcolor('white')

    cool = turtle.Turtle()
    cool.shape('turtle')
    cool.color('pink')
    cool.speed(10)

    orientation_init = cool.heading()
    while True:
        for i in range(0,4):
            cool.forward(50)
            cool.right(90)
        cool.right(5)

        orientation_now = cool.heading()
        print(orientation_now)
        if orientation_now == orientation_init:
            cool.right(90)
            cool.color('green')
            cool.forward(200)
            break
    window.exitonclick()


draw()
