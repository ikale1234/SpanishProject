import os
import random
import verborganizer
import sys
import pyglet
from event_class import Game
win = pyglet.window.Window(width=800, height=600)
game = True

vocab_game = Game()
while game:
    mouse_pressed = False
    level = 0
    gotLevel = False
    mouse_released = True
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

    vocab_game.get_list()

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

    thelist = []

    def stage2(level):

        english, word, samplelist = vocab_game.getChoices()
        for i in range(len(samplelist)):
            if word == samplelist[i]:
                let = alphabet[i]

        answers = []

        question = pyglet.text.Label("What is the spanish word for " + english+"?",
                                     font_name='Times New Roman',
                                     font_size=15,
                                     x=win.width//2, y=win.height-100,
                                     anchor_x='center', anchor_y='center')

        data = pyglet.text.Label("# Correct: " + str(points) + "    # Wrong: "+str(count-points) + "     # Remaining:   " + str(10-count),
                                 font_name='Times New Roman',
                                 font_size=15,
                                 x=win.width//2, y=win.height-50,
                                 anchor_x='center', anchor_y='center')

        for i in range(len(samplelist)):
            if i > 3:
                x = 3
                a = 200
            else:
                x = 1
                a = 0
            answers.append(pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                             font_name='Times New Roman',
                                             font_size=15,
                                             x=win.width*(x/4), y=win.height-200-50*(i)+a,
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

    def display_result(guess, let):
        global points, answers
        for i in range(len(alphabet)):
            if guess == alphabet[i]:
                idx = i
        for j in range(len(alphabet)):
            if let == alphabet[j]:
                idx2 = j
        if idx > 3:
            c = 3
            a = 200
        else:
            c = 1
            a = 0
        if idx2 > 3:
            y = 3
            b = 200
        else:
            y = 1
            b = 0
        if vocab_game.check_answer(guess, let):
            answers[idx] = pyglet.text.Label(alphabet[idx] + ": " + samplelist[idx],
                                             font_name='Times New Roman',
                                             font_size=15,
                                             x=win.width*(c/4), y=win.height-200-50*idx + a,
                                             anchor_x='center', anchor_y='center', color=(0, 255, 0, 255))
            sentence = random.choice(rightlist)
            points += 1
        else:
            sentence = random.choice(wronglist)

            answers[idx2] = pyglet.text.Label(alphabet[idx2] + ": " + samplelist[idx2],
                                              font_name='Times New Roman',
                                              font_size=15,
                                              x=win.width*(y/4), y=win.height-200-50*idx2 + b,
                                              anchor_x='center', anchor_y='center', color=(0, 255, 0, 255))
            answers[idx] = pyglet.text.Label(alphabet[idx] + ": " + samplelist[idx],
                                             font_name='Times New Roman',
                                             font_size=15,
                                             x=win.width*(c/4), y=win.height-200-50*idx+a,
                                             anchor_x='center', anchor_y='center', color=(255, 0, 0, 255))
        saying = pyglet.text.Label(sentence,
                                   font_name='Times New Roman',
                                   font_size=15,
                                   x=win.width//2, y=100,
                                   anchor_x='center', anchor_y='center')
        tell_enter = pyglet.text.Label("Click Anywhere to Continue.",
                                       font_name='Times New Roman',
                                       font_size=15,
                                       x=win.width//2, y=50,
                                       anchor_x='center', anchor_y='center')
        return saying, tell_enter

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
                if i > 3:
                    c = 3
                    a = 200
                else:
                    c = 1
                    a = 0
                if x > win.width*(c/4)-100 and x < win.width*(c/4)+100:
                    if y > (win.height-200-50*i+a) - 15 and y < (win.height-200-50*i+a) + 15:
                        answers[i] = pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                                       font_name='Times New Roman',
                                                       font_size=15,
                                                       x=win.width*(c/4), y=win.height-200-50*i+a,
                                                       anchor_x='center', anchor_y='center', color=(0, 0, 255, 255))
                    else:
                        answers[i] = pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                                       font_name='Times New Roman',
                                                       font_size=15,
                                                       x=win.width*(c/4), y=win.height-200-50*i+a,
                                                       anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
                else:
                    answers[i] = pyglet.text.Label(alphabet[i] + ": " + samplelist[i],
                                                   font_name='Times New Roman',
                                                   font_size=15,
                                                   x=win.width*(c/4), y=win.height-200-50*i+a,
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
        global mouse_pressed, mouse_released
        print(mouse_released)
        if mouse_released:

            mouse_pressed = True
            mouse_released = False

    @win.event
    def on_mouse_release(x, y, LEFT, none):
        global mouse_released, level, mouse_pressed, stage, question, data, answers, guess, samplelist, let, count, gameOver, saypoints, suggest, playbutton, saying, tell_enter

        if stage == 1:
            if mouse_pressed:
                mouse_pressed = False
                mouse_released = True

                for i in range(10):

                    if x > (100+50*i) - 25 and x < (100+50*i) + 25:
                        if y > 150 and y < 250:
                            level = int(numlist[i])
                            vocab_game.get_difficulty(level)
                            question, data, answers, samplelist, let = stage2(
                                level)

                            stage = 2
        print(mouse_pressed)
        if stage == 2:
            if mouse_pressed:
                mouse_pressed = False
                mouse_released = True
                for i in range(len(answers)):
                    if i > 3:
                        c = 3
                        a = 200
                    else:
                        c = 1
                        a = 0
                    if x > win.width*(c/4)-100 and x < win.width*(c/4)+100:
                        if y > (win.height-200-50*i+a) - 15 and y < (win.height-200-50*i+a) + 15:
                            guess = alphabet[i]
                            saying, tell_enter = display_result(guess, let)
                            stage = 3
        if stage == 3:
            if mouse_pressed:
                mouse_pressed = False
                mouse_released = True
                count += 1
                if count >= 10:

                    saypoints, suggest, playbutton = whengameOver(points)
                    gameOver = True
                else:
                    stage = 2
                    question, data, answers, samplelist, let = stage2(
                        level)
        if gameOver:
            if mouse_pressed:
                mouse_pressed = False
                mouse_released = True

                if x > win.width//2 - 70 and x < win.width//2 + 70:
                    if y > 60 and y < 140:
                        pyglet.app.exit()

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
                tell_enter.draw()
        if gameOver:
            saypoints.draw()
            suggest.draw()
            playbutton.draw()

    @win.event
    def on_window_close(window):
        exit()

    pyglet.app.run()
