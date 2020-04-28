import pyglet
import random
xvals = []
yvals = []
labels = []
for i in range(5):
    xvals.append(random.randrange(100, 700))
    yvals.append(random.randrange(100, 700))
win = pyglet.window.Window(width=800,  height=800)
questions = ["hi", "hello", "fefef", "dsef", "fat"]
for i in range(len(questions)):
    labels.append(pyglet.text.Label(questions[i],
                                    font_name='Times New Roman',
                                    font_size=18,
                                    x=xvals[i], y=yvals[i],
                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255)))

print(xvals)
print(yvals)
@win.event
def on_draw():
    win.clear()
    for i in labels:
        i.draw()


@win.event
def on_mouse_press(x, y, LEFT, none):
    print(x)
    print(y)
    for i in range(len(questions)):
        if x > xvals[i]-30 and x < xvals[i] + 30:
            if y > yvals[i] - 30 and y < yvals[i] + 30:
                labels[i] = pyglet.text.Label(questions[i],
                                              font_name='Times New Roman',
                                              font_size=18,
                                              x=xvals[i], y=yvals[i],
                                              anchor_x='center', anchor_y='center', color=(255, 0, 0, 255))


pyglet.app.run()
quit()
