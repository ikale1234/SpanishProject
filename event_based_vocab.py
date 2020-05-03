import os
import random
import verborganizer
import sys
import pyglet
win = pyglet.window.Window(width=800, height=600)
game = True

while game:

    listdata = []
    level = 0
    gotLevel = False
    vlist = []
    nlist = []
    stage = 1
    points = 0
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rightlist = ["Good Job! You got it right!", "Nice! That's right!",
                 "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
    wronglist = ["You suck! That was the wrong answer!",
                 "How did you miss that! That was easy!",
                 "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
    count = 0
    gameOver = False

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
                               font_size=18,
                               x=win.width//2, y=win.height-200,
                               anchor_x='center', anchor_y='center')
    difflist = []
    for i in range(10):
        difflist.append(pyglet.text.Label(numlist[i],
                                          font_name='Times New Roman',
                                          font_size=40,
                                          x=100+50*i, y=win.height-400,
                                          anchor_x='center', anchor_y='center'))
    print(len(difflist))

    def getChoices(vlist, nlist):
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

    thelist = []

    def stage2(level):
        global nlist, vlist
        for i in range(level):
            thelist.append(i+1)

            for i in thelist:
                for verb in listdata["Verbs"]:
                    if i == verb["Difficulty"]:
                        vlist.append(verb["Infinitive"])
            for i in thelist:
                for noun in listdata["Nouns"]:
                    if i == noun["Difficulty"]:
                        nlist.append(noun["Spanish"])

        english, word, samplelist = getChoices(vlist, nlist)
        for i in range(len(samplelist)):
            if word == samplelist[i]:
                let = alphabet[i]

        answers = []

        question = pyglet.text.Label("What is the spanish word for " + english+"?",
                                     font_name='Times New Roman',
                                     font_size=15,
                                     x=win.width//2, y=win.height-100,
                                     anchor_x='center', anchor_y='center')

        data = pyglet.text.Label("# Right: " + str(points) + "    # Wrong: "+str(count-points) + "     # Left:   " + str(10-count),
                                 font_name='Times New Roman',
                                 font_size=15,
                                 x=win.width//2, y=win.height-550,
                                 anchor_x='center', anchor_y='center')

        for i in range(len(samplelist)):
            answers.append(pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                             font_name='Times New Roman',
                                             font_size=15,
                                             x=win.width//2, y=win.height-200-75*i,
                                             anchor_x='center', anchor_y='center'))
        return question, data, answers, samplelist, let

    def whengameOver(points):

        state1 = "You got" + str(points) + "/ 10 right."
        if points == 10:
            state2 = "Good Job! You are great at this."
        elif points > 7:
            state2 = "You did good but it could be better."
        elif points > 3:
            state2 = "You suck, and should study more."
        else:
            state2 = "Call your local doctor to check you for a mental disability."
        saypoints = pyglet.text.Label(state1,
                                      font_name='Times New Roman',
                                      font_size=20,
                                      x=win.width//2, y=win.height-200,
                                      anchor_x='center', anchor_y='center')
        suggest = pyglet.text.Label(state2,
                                    font_name='Times New Roman',
                                    font_size=20,
                                    x=win.width//2, y=win.height-400,
                                    anchor_x='center', anchor_y='center')
        playbutton = pyglet.text.Label("Play Again",
                                       font_name='Times New Roman',
                                       font_size=15,
                                       x=win.width//2, y=win.height-500,
                                       anchor_x='center', anchor_y='center')
        return saypoints, suggest, playbutton

    def evaluateAnswer(guess, let):
        global points, answers
        for i in range(len(alphabet)):
            if guess == alphabet[i]:
                idx = i
        for j in range(len(alphabet)):
            if let == alphabet[j]:
                idx2 = j
        print(samplelist)
        print(random.choice(rightlist))
        if guess == let or guess == let.lower():
            answers[idx] = pyglet.text.Label(alphabet[idx] + ": " + samplelist[idx],
                                             font_name='Times New Roman',
                                             font_size=15,
                                             x=win.width//2, y=win.height-200-75*idx,
                                             anchor_x='center', anchor_y='center', color=(0, 255, 0, 255))
            sentence = random.choice(rightlist)
            points += 1
        else:
            sentence = random.choice(wronglist) + \
                " The answer was " + samplelist[idx2]+"."
            answers[idx] = pyglet.text.Label(alphabet[idx] + ": " + samplelist[idx],
                                             font_name='Times New Roman',
                                             font_size=15,
                                             x=win.width//2, y=win.height-200-75*idx,
                                             anchor_x='center', anchor_y='center', color=(255, 0, 0, 255))
        saying = pyglet.text.Label(sentence,
                                   font_name='Times New Roman',
                                   font_size=10,
                                   x=win.width*(3/4), y=win.height//2,
                                   anchor_x='center', anchor_y='center')
        tellenter = pyglet.text.Label("Press Enter to Continue.",
                                      font_name='Times New Roman',
                                      font_size=15,
                                      x=win.width*(3/4), y=win.height//2 - 50,
                                      anchor_x='center', anchor_y='center')
        return saying, tellenter

    @win.event
    def on_mouse_motion(x, y, dx, dy):
        global playbutton
        if stage == 1:
            for i in range(10):
                if x > (100+50*i) - 20 and x < (100+50*i) + 20:
                    if y > 150 and y < 250:
                        difflist[i] = pyglet.text.Label(numlist[i],
                                                        font_name='Times New Roman',
                                                        font_size=40,
                                                        x=100+50*i, y=win.height-400,
                                                        anchor_x='center', anchor_y='center', color=(0, 0, 255, 255))
                    else:
                        difflist[i] = pyglet.text.Label(numlist[i],
                                                        font_name='Times New Roman',
                                                        font_size=40,
                                                        x=100+50*i, y=win.height-400,
                                                        anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
                else:
                    difflist[i] = pyglet.text.Label(numlist[i],
                                                    font_name='Times New Roman',
                                                    font_size=40,
                                                    x=100+50*i, y=win.height-400,
                                                    anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

        if stage == 2:
            for i in range(len(answers)):
                if x > win.width//2-100 and x < win.width//2+100:
                    if y > (win.height-200-75*i) - 30 and y < (win.height-200-75*i) + 30:
                        answers[i] = pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                                       font_name='Times New Roman',
                                                       font_size=15,
                                                       x=win.width//2, y=win.height-200-75*i,
                                                       anchor_x='center', anchor_y='center', color=(0, 0, 255, 255))
                    else:
                        answers[i] = pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                                       font_name='Times New Roman',
                                                       font_size=15,
                                                       x=win.width//2, y=win.height-200-75*i,
                                                       anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
                else:
                    answers[i] = pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                                   font_name='Times New Roman',
                                                   font_size=15,
                                                   x=win.width//2, y=win.height-200-75*i,
                                                   anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
        if gameOver:
            if x > win.width//2 - 70 and x < win.width//2 + 70:
                if y > 60 and y < 140:
                    playbutton = pyglet.text.Label("Play Again",
                                                   font_name='Times New Roman',
                                                   font_size=15,
                                                   x=win.width//2, y=win.height-500,
                                                   anchor_x='center', anchor_y='center', color=(0, 0, 255, 255))
                else:
                    playbutton = pyglet.text.Label("Play Again",
                                                   font_name='Times New Roman',
                                                   font_size=15,
                                                   x=win.width//2, y=win.height-500,
                                                   anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
            else:
                playbutton = pyglet.text.Label("Play Again",
                                               font_name='Times New Roman',
                                               font_size=15,
                                               x=win.width//2, y=win.height-500,
                                               anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

    @win.event
    def on_mouse_press(x, y, LEFT, none):
        global stage, question, data, answers, guess, samplelist, let, saying, tellenter

        if stage == 1:
            for i in range(10):

                if x > (100+50*i) - 25 and x < (100+50*i) + 25:
                    if y > 150 and y < 250:
                        level = int(numlist[i])
                        print(str(level))
                        question, data, answers, samplelist, let = stage2(
                            level)

                        stage = 2
        if stage == 2:
            for i in range(len(answers)):
                if x > win.width//2-100 and x < win.width//2+100:
                    if y > (win.height-200-75*i) - 30 and y < (win.height-200-75*i) + 30:
                        guess = alphabet[i]
                        saying, tellenter = evaluateAnswer(guess, let)
                        stage = 3
        if gameOver:
            if x > win.width//2 - 70 and x < win.width//2 + 70:
                if y > 60 and y < 140:
                    pyglet.app.exit()

    @win.event
    def on_key_press(Enter, none):
        global stage, question, data, answers, guess, samplelist, let, count, gameOver, saypoints, suggest, playbutton

        if stage == 3:
            count += 1
            if count >= 10:

                saypoints, suggest, playbutton = whengameOver(points)
                gameOver = True
            else:
                stage = 2
                question, data, answers, samplelist, let = stage2(level)

    @win.event
    def on_draw():
        win.clear()
        if gameOver == False:
            if stage == 1:
                prompt.draw()
                for i in difflist:
                    i.draw()
            if stage == 2 or stage == 3:
                question.draw()
                for i in answers:
                    i.draw()
                data.draw()
            if stage == 3:
                saying.draw()
                tellenter.draw()
        if gameOver:
            saypoints.draw()
            suggest.draw()
            playbutton.draw()

    @win.event
    def on_window_close(window):
        exit()

    pyglet.app.run()
