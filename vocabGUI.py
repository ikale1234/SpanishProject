import pyglet
import random
win = pyglet.window.Window(width=800, height=800)
question = pyglet.text.Label('Hello,\n world',
                             font_name='Times New Roman',
                             font_size=18,
                             x=win.width//2, y=win.height-200,
                             anchor_x='center', anchor_y='center')


class consoleView:
    def __init__(self):
        self.rightlist = ["Good Job! You got it right!", "Nice! That's right!",
                          "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
        self.wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!",
                          "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
        self.answers = []
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.turns = 0
        self.gameover = False

    def askDifficulty(self):
        self.prompt = pyglet.text.Label("What is the difficulty of words you want? Press 1 for easiest, 10 for hardest.",
                                        font_name='Times New Roman',
                                        font_size=10,
                                        x=win.width//2, y=win.height-200,
                                        anchor_x='center', anchor_y='center')

        @win.event
        def on_key_press(_1, none):
            self.level = "1"
            pyglet.app.exit()

        @win.event
        def on_key_press(_2, none):
            self.level = "2"
            pyglet.app.exit()

        @win.event
        def on_key_press(_3, none):
            self.level = "3"
            pyglet.app.exit()

        @win.event
        def on_key_press(_4, none):
            self.level = "4"
            pyglet.app.exit()

        @win.event
        def on_key_press(_5, none):
            self.level = "5"
            pyglet.app.exit()

        @win.event
        def on_key_press(_6, none):
            self.level = "6"
            pyglet.app.exit()

        @win.event
        def on_key_press(_7, none):
            self.level = "7"
            pyglet.app.exit()

        @win.event
        def on_key_press(_8, none):
            self.level = "8"
            pyglet.app.exit()

        @win.event
        def on_key_press(_9, none):
            self.level = "9"
            pyglet.app.exit()

        @win.event
        def on_key_press(_10, none):
            self.level = "10"
            pyglet.app.exit()

        @win.event
        def on_draw():
            self.prompt.draw()

        @win.event
        def on_window_close(window):
            exit()

        pyglet.app.run()

    def betweenStatements(self, statement):
        self.saying = pyglet.text.Label(statement,
                                        font_name='Times New Roman',
                                        font_size=30,
                                        x=win.width//2, y=win.height-100,
                                        anchor_x='center', anchor_y='center')
        self.tellenter = pyglet.text.Label("Press Enter to Continue.",
                                           font_name='Times New Roman',
                                           font_size=30,
                                           x=win.width//2, y=win.height-500,
                                           anchor_x='center', anchor_y='center')

        @win.event
        def on_key_press(Enter, none):
            pyglet.app.exit()

        @win.event
        def on_draw():
            win.clear()
            self.saying.draw()
            self.tellenter.draw()

        @win.event
        def on_window_close(window):
            exit()

        pyglet.app.run()

    def getInput(self, english, samplelist, word):
        self.answers = []
        self.turns += 1
        self.question = pyglet.text.Label("What is the spanish word for " + english+"?",
                                          font_name='Times New Roman',
                                          font_size=10,
                                          x=win.width//2, y=win.height-100,
                                          anchor_x='center', anchor_y='center')
        for i in range(len(samplelist)):
            self.answers.append(pyglet.text.Label(self.alphabet[i] + ": " + samplelist[i],
                                                  font_name='Times New Roman',
                                                  font_size=15,
                                                  x=win.width//2, y=win.height-200-75*i,
                                                  anchor_x='center', anchor_y='center'))

        @win.event
        def on_mouse_press(x, y, LEFT, none):
            for i in range(len(self.answers)):
                if x > win.width//2-100 and x < win.width//2+100:
                    if y > (win.height-200-75*i) - 30 and y < (win.height-200-75*i) + 30:
                        self.guess = self.alphabet[i]
                        pyglet.app.exit()
        for i in range(len(samplelist)):
            if word == samplelist[i]:
                self.let = self.alphabet[i]

        @win.event
        def on_draw():
            win.clear()
            self.question.draw()
            for i in range(len(self.answers)):
                self.answers[i].draw()

        @win.event
        def on_window_close(window):
            exit()

        pyglet.app.run()

    def displayResult(self, correct):
        if correct:
            self.betweenStatements(random.choice(self.rightlist))
        else:
            self.betweenStatements(random.choice(self.wronglist))

    def checkGameOver(self):
        if self.turns >= 10:
            self.gameover == True

    def whenGameOver(self, points):
        self.endline = pyglet.text.Label("You got " + str(points) + " / 10 right.",
                                         font_name='Times New Roman',
                                         font_size=30,
                                         x=win.width//2, y=win.height-100,
                                         anchor_x='center', anchor_y='center')
        if points == 10:
            self.endline2 = pyglet.text.Label("Good Job! You are great at this.",
                                              font_name='Times New Roman',
                                              font_size=15,
                                              x=win.width//2, y=win.height-500,
                                              anchor_x='center', anchor_y='center')
        elif points > 7:
            self.endline2 = pyglet.text.Label("You did good but it could be better.",
                                              font_name='Times New Roman',
                                              font_size=15,
                                              x=win.width//2, y=win.height-500,
                                              anchor_x='center', anchor_y='center')
        elif points > 3:
            self.endline2 = pyglet.text.Label("You suck, and should study more.",
                                              font_name='Times New Roman',
                                              font_size=15,
                                              x=win.width//2, y=win.height-500,
                                              anchor_x='center', anchor_y='center')
        else:
            self.endline2 = pyglet.text.Label("Call your local doctor to check you for a mental disability.",
                                              font_name='Times New Roman',
                                              font_size=15,
                                              x=win.width//2, y=win.height-500,
                                              anchor_x='center', anchor_y='center')

        @win.event
        def on_draw():
            win.clear()
            self.endline.draw()
            self.endline2.draw()

        @win.event
        def on_window_close(window):
            exit()
        pyglet.app.run()
