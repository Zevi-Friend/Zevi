import turtle as t

t.Screen()
t.setup(600,500,100,100)
t.bgcolor('springgreen')
t.title('my_game')
t.shape('turtle')
tracer(False)
t.forward(200)
t.right(90)
t.up()
t.forward(100)
t.dot(100,'red')
t.hideturtle()
print('exit turtle')
t.done()
input()
try:
    t.bye()
except Terminator:
    print('exit turtle')
