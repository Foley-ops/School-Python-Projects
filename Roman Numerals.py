from turtle import*

speed(0)
#
#
# def I():
#     forward(20)
#     pendown()
#     begin_fill()
#     color('black', 'black')
#
#     forward(90)
#     right(90)
#     forward(15)
#     right(90)
#     forward(35)
#     left(90)
#     forward(110) ## height
#     left(90)
#     forward(35)
#     right(90)
#     forward(15)
#     right(90)
#     forward(90)
#     right(90)
#     forward(15)
#     right(90)
#     forward(35)
#     left(90)
#     forward(110) ## height
#     left(90)
#     forward(35)
#     right(90)
#     forward(15)
#
#     end_fill()
#     penup()
#
#     right(90)
#     forward(100)
#
# def V():
#     forward(20)
#     pendown()
#     begin_fill()
#     color('black', 'black')
#
#     forward(20)
#     right(70)
#     forward(130)
#     left(70)
#     left(70)
#     forward(130)
#     right(70)
#     forward(20)
#     right(110)
#     forward(150)
#     right(70)
#     forward(26)
#     right(70)
#     forward(150)
#
#     end_fill()
#     penup()
#
#     right(110)
#     forward(160)
#
# def X():
#     penup()
#     forward(20)
#     pendown()
#     begin_fill()
#
#     color('black', 'black')
#     forward(20)
#     right(60)
#     forward(60)
#     left(120)
#     forward(60)
#     right(60)
#     forward(20)
#     right(120)
#     forward(80)
#     left(60)
#     forward(80)
#     right(120)
#     forward(20)
#     right(60)
#     forward(60)
#     left(120)
#     forward(60)
#     right(60)
#     forward(20)
#     right(120)
#     forward(80)
#     left(60)
#     forward(80)
#
#     end_fill()
#     penup()
#
#     right(120)
#     forward(120)
#
# def M():
#     penup()
#     forward(20)
#     pendown()
#     begin_fill()
#     color('black', 'black')
#
#     forward(25)
#     right(70)
#     forward(60)
#     left(140)
#     forward(60)
#     right(70)
#     forward(25)
#     right(90)
#     forward(140)  # height
#     right(90)
#     forward(18.75)
#     right(90)
#     forward(100)
#     left(160)
#     forward(60)
#     right(70)
#     forward(12.5)
#     right(70)
#     forward(60)
#     left(160)
#     forward(100)
#     right(90)
#     forward(18.75)
#     right(90)
#     forward(140)   # height
#
#     end_fill()
#     penup()
#
#     right(90)
#     forward(120)
#
# def L():
#     pendown()
#     begin_fill()
#     color('black', 'black')
#
#     forward(20)
#     right(90)
#     forward(120)
#     left(90)
#     forward(60)
#     right(90)
#     forward(20)
#     right(90)
#     forward(80)
#     right(90)
#     forward(140)
#
#     end_fill()
#     penup()
#
#     right(90)
#     forward(100)
#
# def C():
#     penup()
#     forward(75)
#     pendown()
#     begin_fill()
#
#     color('black', 'black')
#
#     right(180)
#     circle(70, 180)
#     forward(21)
#     left(90)
#     forward(14)
#     left(90)
#     forward(14)
#     circle(-56, 180)
#     forward(14)
#     left(90)
#     forward(14)
#     left(90)
#     forward(21)
#     penup()
#     end_fill()
#
#     right(180)
#     forward(60)
#
#
# def D():
#     penup()
#     forward(40)
#     right(90)
#     forward(140)
#     left(90)
#
#     pendown()
#     begin_fill()
#     color('black', 'black')
#     circle(70, 180)
#     forward(26.25)
#     left(90)
#     forward(140)
#     left(90)
#     forward(26.25)
#
#     end_fill()
#     penup()
#     backward(13.125)
#     left(90)
#     forward(26.25)
#     right(90)
#     forward(17.5)
#
#     pendown()
#     begin_fill()
#     color('black', 'white')
#
#     circle(43.75, 180)
#     forward(13.125)
#     left(90)
#     forward(87.5)
#     left(90)
#     forward(13.125)
#
#     penup()
#     end_fill()
#
#
#     forward(90)
#     left(90)
#     forward(115)
#     right(90)
#
# changes input to value
def exchange(x):
    values = [1000,500,100,50,10,5,1]
    letters = ['M','D','C','L','X','V','I']

    print_statement = ''
    count = 0
    while x > 0:
        for i in range(x // values[count]):
            print_statement += letters[count]
            x -= values[count]
        count += 1
    return print_statement


task = int(input("Enter number to see it in roman numerals: "))
roman_numeral = exchange(task)
window_width()
penup()
setposition(-450, 80)
pendown()


write(roman_numeral ,font=("Arial",32,"normal"))
exitonclick()


# for stat in roman_numeral:
#     if stat == 'M':
#         M()
#     elif stat == 'C':
#         C()
#     elif stat == 'I':
#         I()
#     elif stat == 'D':
#         D()
#     elif stat == 'L':
#         L()
#     elif stat == "X":
#         X()
#     elif stat == 'V':
#         V()

exitonclick()