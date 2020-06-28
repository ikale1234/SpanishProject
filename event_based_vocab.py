
import os
import random
import verborganizer
import sys
import pyglet
from event_client import Game
win = pyglet.window.Window(width=800, height=600)
game = True


class Label:
    def __init__(self, text, size, x, y, width, height):
        self.font = 'Times New Roman'
        self.x = x
        self.y = y
        self.size = size
        self.height = height
        self.width = width
        self.text = text
        self.label = pyglet.text.Label(self.text,
                                       font_name=self.font,
                                       font_size=self.size,
                                       x=self.x, y=self.y,
                                       anchor_x='center', anchor_y='center')
        self.pattern = pyglet.image.SolidColorImagePattern(color=(0, 0, 0, 0))
        self.image = self.pattern.create_image(self.width, self.height)

    def draw_rect(self, color):
        self.pattern = pyglet.image.SolidColorImagePattern(color=color)
        self.image = self.pattern.create_image(self.width, self.height)

    def change_color(self, color, bold):
        self.label = pyglet.text.Label(self.text,
                                       font_name=self.font,
                                       font_size=self.size,
                                       x=self.x, y=self.y,
                                       anchor_x='center', anchor_y='center', color=color, bold=bold)

    def change_background_color(self, color, bold):
        self.label = pyglet.text.Label(self.text,
                                       font_name=self.font,
                                       font_size=self.size,
                                       x=self.x, y=self.y,
                                       anchor_x='center', anchor_y='center', background_color=color, bold=bold)

    def in_hitbox(self, curx, cury):
        if curx > self.x - self.width/2 and curx < self.x + self.width/2:
            if cury > self.y - self.height/2 and cury < self.y + self.height/2:
                return True
            else:
                return False
        else:
            return False

    def draw(self):
        self.image.blit(self.x-self.width/2, self.y-self.height/2)
        self.label.draw()


vocab_game = Game()
mouse_pressed = False
level = 0
gotLevel = False
mouse_released = True
stage = 0
points = 0
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
rightlist = ["Good Job! You got it right!", "Nice! That's right!",
             "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
wronglist = ["You suck! That was the wrong answer!",
             "How did you miss that! That was easy!",
             "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
count = 0
gameOver = False
gotAnswer = False
numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
gotLevel = False
prompt = Label("What is the difficulty of words you want? Press 1 for easiest, 10 for hardest.",
               18, win.width//2, win.height-200, 1, 1)
difflist = []
for i in range(10):
    difflist.append(Label(numlist[i], 40,
                          150+50*i, win.height-400, 40, 60))
print(len(difflist))
thelist = []
letcomb = ''
entername = Label("Enter your username in the terminal. Press enter when done",
                  18, win.width//2, win.height-200, 1, 1)

userinp = Label("Username: "+letcomb, 15,
                win.width//2, 300,
                100, 100)


def stage2():
    english, samplelist = vocab_game.getChoices()

    answers = []

    question = Label("What is the spanish word for " +
                     english+"?", 15, win.width//2, win.height-100, 200, 50)
    question = Label(english, 15, win.width//2, win.height-100, 200, 50)

    data = Label("# Correct: " + str(points) + "    # Wrong: "+str(count-points) + "     # Remaining:   " + str(needed-count), 15, win.width//2, win.height-50,
                 150, 50)
    for i in range(len(samplelist)):
        if i > 3:
            x = 3
            a = 200
        else:
            x = 1
            a = 0
        answers.append(Label(alphabet[i] + ": " + samplelist[i], 15,
                             win.width*(x/4), win.height-225-50*(i)+a, 200, 30))
    return question, data, answers, samplelist


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
    saypoints = Label(state1, 20,
                      win.width//2, win.height-200,
                      100, 100)
    suggest = Label(state2, 20, win.width//2, win.height-400,
                    100, 100)
    playbutton = Label("Play Again", 15,
                       win.width*(3/4), win.height-500,
                       140, 80)
    quitbutton = Label("Quit", 15,
                       win.width*(1/4), win.height-500,
                       140, 80)
    return saypoints, suggest, playbutton, quitbutton


def display_result(guess):
    global points, answers, count
    for i in range(len(samplelist)):
        if guess == i:
            idx = i
    vallist = vocab_game.check_answer(guess)
    print(vallist)
    correct = vallist[0]
    gameover = vallist[1]
    points = vallist[2]
    count = vallist[3]
    word = vallist[4]
    for j in range(len(samplelist)):
        if word == samplelist[j]:
            idx2 = j
    if correct == 1:
        answers[idx].change_color((0, 255, 0, 255), False)
        sentence = random.choice(rightlist)
    else:
        sentence = random.choice(wronglist)
        answers[idx2].change_color((0, 255, 0, 255), False)
        answers[idx].change_color((255, 0, 0, 255), False)
    saying = Label(sentence, 15,
                   win.width//2, 150,
                   100, 100)
    tell_enter = Label("Click Anywhere to Continue.", 15,
                       win.width//2, 50,
                       100, 100)
    return saying, tell_enter, gameover


@win.event
def on_mouse_motion(x, y, dx, dy):
    global playbutton, stage, question, data, answers, samplelist, needed, points, count
    # if stage == 0:
    #     needed = vocab_game.stage0()
    #     points, count = vocab_game.get_score()
    #     question, data, answers, samplelist = stage2()
    #     stage = 2
    if stage == 1:
        for i in range(10):
            if difflist[i].in_hitbox(x, y):
                difflist[i].draw_rect((0, 0, 255, 255))
            else:
                difflist[i].draw_rect((0, 0, 0, 0))
    if stage == 2:
        for i in range(len(answers)):
            if answers[i].in_hitbox(x, y):
                answers[i].draw_rect((0, 0, 255, 255))
            else:
                answers[i].draw_rect((0, 0, 0, 0))
    if gameOver:
        if playbutton.in_hitbox(x, y):
            playbutton.draw_rect((0, 0, 255, 255))
        else:
            playbutton.draw_rect((0, 0, 0, 0))
        if quitbutton.in_hitbox(x, y):
            quitbutton.draw_rect((0, 0, 255, 255))
        else:
            quitbutton.draw_rect((0, 0, 0, 0))


@win.event
def on_mouse_press(x, y, LEFT, none):
    global mouse_pressed, mouse_released
    if mouse_released:
        mouse_pressed = True
        mouse_released = False


@win.event
def on_mouse_release(x, y, LEFT, none):
    global gameover, quitbutton, mouse_released, level, mouse_pressed, stage, question, data, answers, guess, samplelist, let, count, gameOver, saypoints, suggest, playbutton, saying, tell_enter, points
    if stage == 1:
        if mouse_pressed:
            mouse_pressed = False
            mouse_released = True
            for i in range(10):
                if difflist[i].in_hitbox(x, y):
                    level = int(numlist[i])
                    vocab_game.get_difficulty(level)
                    question, data, answers, samplelist = stage2()
                    stage = 2
    if stage == 2:
        if mouse_pressed:
            mouse_pressed = False
            mouse_released = True
            for i in range(len(answers)):
                if answers[i].in_hitbox(x, y):
                    guess = i
                    saying, tell_enter, gameover = display_result(guess)
                    stage = 3
    if stage == 3:
        if mouse_pressed:
            mouse_pressed = False
            mouse_released = True

            if gameover == 1:
                saypoints, suggest, playbutton, quitbutton = whengameOver(
                    points)
                gameOver = True

            else:
                stage = 2
                question, data, answers, samplelist = stage2()
    if gameOver:
        mouse_pressed = False
        mouse_released = True
        if playbutton.in_hitbox(x, y):
            gameOver = False
            vocab_game.play_again()
            stage = 0
            points = 0
            count = 0
        if quitbutton.in_hitbox(x, y):
            vocab_game.play_again()
            pyglet.app.exit()
            exit()


hidden = ''
passwordlabel = Label("Password: "+hidden, 15,
                      win.width//2, 200,
                      100, 100)

passcomb = ''
@win.event
def on_key_release(symbol, none):
    global passwordlabel, passcomb, userinp, stage, entername, letcomb, username, password, needed, ifgood, question, data, answers, samplelist, points, count
    if symbol == pyglet.window.key.A:
        let = 'a'
    if symbol == pyglet.window.key.B:
        let = 'b'
    if symbol == pyglet.window.key.C:
        let = 'c'
    if symbol == pyglet.window.key.D:
        let = 'd'
    if symbol == pyglet.window.key.E:
        let = 'e'
    if symbol == pyglet.window.key.F:
        let = 'f'
    if symbol == pyglet.window.key.G:
        let = 'g'
    if symbol == pyglet.window.key.H:
        let = 'h'
    if symbol == pyglet.window.key.I:
        let = 'i'
    if symbol == pyglet.window.key.J:
        let = 'j'
    if symbol == pyglet.window.key.K:
        let = 'k'
    if symbol == pyglet.window.key.L:
        let = 'l'
    if symbol == pyglet.window.key.M:
        let = 'm'
    if symbol == pyglet.window.key.N:
        let = 'n'
    if symbol == pyglet.window.key.O:
        let = 'o'
    if symbol == pyglet.window.key.P:
        let = 'p'
    if symbol == pyglet.window.key.Q:
        let = 'q'
    if symbol == pyglet.window.key.R:
        let = 'r'
    if symbol == pyglet.window.key.S:
        let = 's'
    if symbol == pyglet.window.key.T:
        let = 't'
    if symbol == pyglet.window.key.U:
        let = 'u'
    if symbol == pyglet.window.key.V:
        let = 'v'
    if symbol == pyglet.window.key.W:
        let = 'w'
    if symbol == pyglet.window.key.X:
        let = 'x'
    if symbol == pyglet.window.key.Y:
        let = 'y'
    if symbol == pyglet.window.key.Z:
        let = 'z'
    if symbol == pyglet.window.key.ENTER:
        let = 'no'
    if symbol == pyglet.window.key._1:
        let = '1'
    if symbol == pyglet.window.key._2:
        let = '2'
    if symbol == pyglet.window.key._3:
        let = '3'
    if symbol == pyglet.window.key._4:
        let = '4'
    if symbol == pyglet.window.key._5:
        let = '5'
    if symbol == pyglet.window.key._6:
        let = '6'
    if symbol == pyglet.window.key._7:
        let = '7'
    if symbol == pyglet.window.key._8:
        let = '8'
    if symbol == pyglet.window.key._9:
        let = '9'
    if symbol == pyglet.window.key._0:
        let = '0'
    if symbol == pyglet.window.key.BACKSPACE:
        let = "back"

    if let == "no":
        if stage == 0:
            entername = Label("Enter your password in the terminal. Press enter when done.",
                              18, win.width//2, win.height-200, 1, 1)
            username = letcomb
            stage = -1

        elif stage == -1:

            password = passcomb
            print(username, password)
            needed, ifgood = vocab_game.stage0(username, password)
            passcomb = ''
            letcomb = ''
            if ifgood == 1:
                points, count = vocab_game.get_score()
                question, data, answers, samplelist = stage2()
                stage = 2
            if ifgood == 0:
                stage = 0
                letcomb = ''
                userinp = Label(letcomb, 15,
                                win.width//2, 300,
                                100, 100)
                entername = Label("The information you entered was invalid. Try your username again.",
                                  18, win.width//2, win.height-200, 1, 1)
    elif let == "back":
        if stage == 0:
            letcomb = letcomb[:-1]
            userinp = Label("Username: "+letcomb, 15,
                            win.width//2, 300,
                            100, 100)
        if stage == -1:
            passcomb = passcomb[:-1]
            hidden = ""
            for i in range(len(passcomb)):
                hidden += "*"
            passwordlabel = Label("Password: "+hidden, 15,
                                  win.width//2, 200,
                                  100, 100)
    else:
        if stage == 0:
            letcomb += let
            userinp = Label("Username: "+letcomb, 15,
                            win.width//2, 300,
                            100, 100)
        if stage == - 1:
            passcomb += let
            hidden = ""
            for i in range(len(passcomb)):
                hidden += "*"
            passwordlabel = Label("Password: "+hidden, 15,
                                  win.width//2, 200,
                                  100, 100)


@win.event
def on_draw():
    global stage
    win.clear()
    if gameOver == False:
        if stage == 0 or stage == -1:
            entername.draw()
            userinp.draw()
            passwordlabel.draw()

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
        quitbutton.draw()


@win.event
def on_window_close(window):
    exit()


pyglet.app.run()
