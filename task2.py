import matplotlib.pyplot as plt
import matplotlib.patches as patches

import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.color("green")
    t.pensize(2)
    t.speed(250)
    t.penup()
    t.goto(-size / 10, 20)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    try:
        user_order = int(
            input("Enter the order for the Koch snowflake: "))
        if user_order < 0:
            print("Order must be a non-negative integer. Using default order 3.")
            user_order = 3
        draw_koch_curve(user_order)
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
