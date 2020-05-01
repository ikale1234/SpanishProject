import os
import random
import verborganizer
import sys
import pyglet
win = pyglet.window.Window(width=800, height=800)

listdata = []
level = 0
gotLevel = False
vlist = []
nlist = []

points = 0


if len(sys.argv) == 1:
    listdata = verborganizer.build("SpanishWords")
elif len(sys.argv) == 2:
    try:
        listdata = verborganizer.build(sys.argv[1])
    except FileNotFoundError:
        print("That is an invalid directory.")
        quit()
gotAnswer = False
numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

gotLevel = False
prompt = pyglet.text.Label("What is the difficulty of words you want? Press 1 for easiest, 10 for hardest.",
                           font_name='Times New Roman',
                           font_size=10,
                           x=win.width//2, y=win.height-200,
                           anchor_x='center', anchor_y='center')
difflist = []
for i in range(10):
    if i < 6:
        difflist.append(pyglet.text.Label(numlist[i],
                                          font_name='Times New Roman',
                                          font_size=40,
                                          x=100+100*i, y=win.height-400,
                                          anchor_x='center', anchor_y='center'))
    if i > 5:
        difflist.append(pyglet.text.Label(numlist[i],
                                          font_name='Times New Roman',
                                          font_size=40,
                                          x=100+100*(i-5), y=win.height-600,
                                          anchor_x='center', anchor_y='center'))


@win.event
def on_mouse_motion(x, y, dx, dy):
    for i in range(10):
        if i < 6:
            if x > (100+100*i) - 25 and x < (100+100*i) + 25:
                if y > 350 and y < 450:
                    difflist[i] = pyglet.text.Label(numlist[i],
                                                    font_name='Times New Roman',
                                                    font_size=40,
                                                    x=100+100*i, y=win.height-400,
                                                    anchor_x='center', anchor_y='center', color=(0, 0, 255, 255))
                else:
                    difflist[i] = pyglet.text.Label(numlist[i],
                                                    font_name='Times New Roman',
                                                    font_size=40,
                                                    x=100+100*i, y=win.height-400,
                                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
            else:
                difflist[i] = pyglet.text.Label(numlist[i],
                                                font_name='Times New Roman',
                                                font_size=40,
                                                x=100+100*i, y=win.height-400,
                                                anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
        if i > 5:
            if x > (100+100*(i-5)) - 25 and x < (100+100*(i-5)) + 25:
                if y > 150 and y < 250:
                    difflist[i] = pyglet.text.Label(numlist[i],
                                                    font_name='Times New Roman',
                                                    font_size=40,
                                                    x=100+100*(i-5), y=win.height-600,
                                                    anchor_x='center', anchor_y='center', color=(0, 0, 255, 255))
                else:
                    difflist[i] = pyglet.text.Label(numlist[i],
                                                    font_name='Times New Roman',
                                                    font_size=40,
                                                    x=100+100*(i-5), y=win.height-600,
                                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
            else:
                difflist[i] = pyglet.text.Label(numlist[i],
                                                font_name='Times New Roman',
                                                font_size=40,
                                                x=100+100*(i-5), y=win.height-600,
                                                anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))


@win.event
def on_mouse_press(x, y, LEFT, none):

    for i in range(10):
        if i < 6:
            if x > (100+100*i) - 25 and x < (100+100*i) + 25:
                if y > 350 and y < 450:
                    level = int(numlist[i])
                    stage = 2
                    print(str(level))
        if i > 5:
            if x > (100+100*(i-5)) - 25 and x < (100+100*(i-5)) + 25:
                if y > 150 and y < 250:
                    level = int(numlist[i])
                    stage = 2
                    print(str(level))


@win.event
def on_draw():
    win.clear()
    for i in difflist:
        i.draw()


pyglet.app.run()


numlist = []
num = int(level)
for i in range(num):
    numlist.append(i+1)

    for i in numlist:
        for verb in listdata["Verbs"]:
            if i == verb["Difficulty"]:
                vlist.append(verb["Infinitive"])
    for i in numlist:
        for noun in listdata["Nouns"]:
            if i == noun["Difficulty"]:
                nlist.append(noun["Spanish"])


def getChoices():
    # change later      lchoice = random.choice([vlist, nlist])
    # CHANGE BELOW LATER
    lchoice = vlist
    # CHANGE ABOVE LATER
    samplelist = random.sample(lchoice, 5)

    word = random.choice(samplelist)
    if lchoice == vlist:
        for verb in listdata["Verbs"]:
            if word == verb["Infinitive"]:
                english = verb["English"]
    if lchoice == nlist:
        for noun in listdata["Nouns"]:
            if word == noun["Spanish"]:
                english = noun["English"]
    return english, word, samplelist


def askQuestion(english, word, samplelist):
    answers = []

    question = pyglet.text.Label("What is the spanish word for " + english+"?",
                                 font_name='Times New Roman',
                                 font_size=10,
                                 x=win.width//2, y=win.height-100,
                                 anchor_x='center', anchor_y='center')
    for i in range(len(samplelist)):
        answers.append(pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                         font_name='Times New Roman',
                                         font_size=15,
                                         x=win.width//2, y=win.height-200-75*i,
                                         anchor_x='center', anchor_y='center'))

    @win.event
    def on_mouse_press(x, y, LEFT, none):
        for i in range(len(answers)):
            if x > win.width//2-100 and x < win.width//2+100:
                if y > (win.height-200-75*i) - 30 and y < (win.height-200-75*i) + 30:
                    guess = alphabet[i]
                    count += 1
                    gotAnswer = True

    for i in range(len(samplelist)):
        if word == samplelist[i]:
            let = alphabet[i]

    @win.event
    def on_draw():
        win.clear()
        question.draw()
        for i in range(len(answers)):
            answers[i].draw()
    return guess, let


def evaluateAnswer(guess, let):
    global points
    gotResult = False
    if guess == let or guess == let.lower():
        points += 1
        saying = pyglet.text.Label(random.choice(rightlist),
                                   font_name='Times New Roman',
                                   font_size=30,
                                   x=win.width//2, y=win.height-100,
                                   anchor_x='center', anchor_y='center')
        tellenter = pyglet.text.Label("Press Enter to Continue.",
                                      font_name='Times New Roman',
                                      font_size=30,
                                      x=win.width//2, y=win.height-500,
                                      anchor_x='center', anchor_y='center')
    else:
        saying = pyglet.text.Label(random.choice(wronglist),
                                   font_name='Times New Roman',
                                   font_size=30,
                                   x=win.width//2, y=win.height-100,
                                   anchor_x='center', anchor_y='center')
        tellenter = pyglet.text.Label("Press Enter to Continue.",
                                      font_name='Times New Roman',
                                      font_size=30,
                                      x=win.width//2, y=win.height-500,
                                      anchor_x='center', anchor_y='center')

    @win.event
    def on_key_press(Enter, none):
        gotResult = True
    while not gotResult:
        @win.event
        def on_draw():
            saying.draw()
            tellenter.draw()


@win.event
def on_window_close(window):
    exit()


for e in range(10):

    getChoices()

    askQuestion()

    evaluateAnswer()

pyglet.app.run()
