
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


def stage2(level):
    english, word, samplelist = vocab_game.getChoices()

    for i in range(len(samplelist)):
        if word == samplelist[i]:
            let = alphabet[i]

    answers = []

    question = Label("What is the spanish word for " +
                     english+"?", 15, win.width//2, win.height-100, 200, 50)
    question = Label(english, 15, win.width//2, win.height-100, 200, 50)

    data = Label("# Correct: " + str(points) + "    # Wrong: "+str(count-points) + "     # Remaining:   " + str(10-count), 15, win.width//2, win.height-50,
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


def display_result(guess, let):
    global points, answers
    for i in range(len(alphabet)):
        if guess == alphabet[i]:
            idx = i
    for j in range(len(alphabet)):
        if let == alphabet[j]:
            idx2 = j
    if vocab_game.check_answer(guess, let):
        answers[idx].change_color((0, 255, 0, 255), False)
        sentence = random.choice(rightlist)
        points += 1
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
    return saying, tell_enter


@win.event
def on_mouse_motion(x, y, dx, dy):
    global playbutton
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
    global quitbutton, mouse_released, level, mouse_pressed, stage, question, data, answers, guess, samplelist, let, count, gameOver, saypoints, suggest, playbutton, saying, tell_enter, points
    if stage == 1:
        if mouse_pressed:
            mouse_pressed = False
            mouse_released = True
            for i in range(10):
                if difflist[i].in_hitbox(x, y):
                    level = int(numlist[i])
                    vocab_game.get_difficulty(level)
                    question, data, answers, samplelist, let = stage2(
                        level)
                    stage = 2
    if stage == 2:
        if mouse_pressed:
            mouse_pressed = False
            mouse_released = True
            for i in range(len(answers)):
                if answers[i].in_hitbox(x, y):
                    guess = alphabet[i]
                    saying, tell_enter = display_result(guess, let)
                    stage = 3
    if stage == 3:
        if mouse_pressed:
            mouse_pressed = False
            mouse_released = True
            count += 1
            if count >= 10:
                saypoints, suggest, playbutton, quitbutton = whengameOver(
                    points)
                gameOver = True
            else:
                stage = 2
                question, data, answers, samplelist, let = stage2(
                    level)
    if gameOver:
        mouse_pressed = False
        mouse_released = True
        if playbutton.in_hitbox(x, y):
            gameOver = False
            stage = 1
            points = 0
            count = 0
        if quitbutton.in_hitbox(x, y):
            pyglet.app.exit()
            exit()


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
        quitbutton.draw()


@win.event
def on_window_close(window):
    exit()


pyglet.app.run()
