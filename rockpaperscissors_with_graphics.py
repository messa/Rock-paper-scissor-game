from pathlib import Path
from pyglet import sprite
from pyglet import app
from pyglet import image
from pyglet.window import Window
from pyglet.window import mouse
from pyglet.window import key
from pyglet import graphics
from pyglet import gl
from pyglet import text
import random

image_dir = Path(__file__).parent / "images"

F_SIZE = 30
#transform player's options
o_rock_pos = (950, 350)
o_paper_pos = (950, 250)
o_scissors_pos = (950, 150)
#transform big choice
players_choice_pos = (650, 200)
comps_choice_pos = (150, 200)
questionmark_pos = (50, 250)

options_all = graphics.Batch()
window = Window(1100, 600)
#players options
image_option_player_rock = image.load(image_dir / "small_choice_player-01.png")
option_player_rock = sprite.Sprite(image_option_player_rock, o_rock_pos[0], o_rock_pos[1], batch = options_all)
image_option_player_paper = image.load(image_dir / "small_choice_player-02.png")
option_player_paper = sprite.Sprite(image_option_player_paper, o_paper_pos[0], o_paper_pos[1], batch = options_all)
image_option_player_scissors = image.load(image_dir / "small_choice_player-03.png")
option_player_scissors = sprite.Sprite(image_option_player_scissors, o_scissors_pos[0], o_scissors_pos[1], batch = options_all)
# player choice
image_player_rock = image.load(image_dir / "choice_player-01.png")
image_player_paper = image.load(image_dir / "choice_player-02.png")
image_player_scissors = image.load(image_dir / "choice_player-03.png")
chosen_image = image_player_rock
player_start = sprite.Sprite(chosen_image, players_choice_pos[0], players_choice_pos[1], batch = options_all)
#pc's choice
image_pc_rock = image.load(image_dir / "choice_pc-01.png")
image_pc_paper = image.load(image_dir / "choice_pc-02.png")
image_pc_scissors = image.load(image_dir / "choice_pc-03.png")
image_questionmark = image.load(image_dir / "questionmark.png")
pc_start = sprite.Sprite(image_pc_rock, comps_choice_pos[0], comps_choice_pos[1])

questionmark = sprite.Sprite(image_questionmark, questionmark_pos[0], questionmark_pos[1], batch = options_all)

@window.event
def on_draw():
    global pc_start, player_start, its_a_tie
    window.clear()
    game.draw()
    options_all.draw()
    pc_start.draw()
    #score
    chose_one.draw()
    if its_a_tie == 1:
         tie_label.draw()
    #round
    player_start.draw()



@window.event
def on_mouse_press(x, y, b, mod):
    global click_record, chosen_image, player_start
    click_record[0] = x
    click_record[1] = y
    if game.round_no < 4:
        #options change
        if x in get_bounding_box(choice_image_size[1], o_rock_pos[0]) and y in get_bounding_box(choice_image_size[3], o_rock_pos[1]):
            chosen_image = image_player_rock
            player_start = sprite.Sprite(chosen_image, x = 650, y = 200)
            game.evaluate(image_player_rock, computer_chose())
        elif x in get_bounding_box(choice_image_size[1], o_paper_pos[0]) and y in get_bounding_box(choice_image_size[3], o_paper_pos[1]):
            chosen_image = image_player_paper
            player_start = sprite.Sprite(chosen_image, x = 650, y = 200)
            game.evaluate(image_player_paper, computer_chose())
        elif x in get_bounding_box(choice_image_size[1], o_scissors_pos[0]) and y in get_bounding_box(choice_image_size[3], o_scissors_pos[1]):
            chosen_image = image_player_scissors
            player_start = sprite.Sprite(chosen_image, x = 650, y = 200)
            game.evaluate(image_player_scissors, computer_chose())
        else:
            pass # nothing changes if clicked outside the bounding boxes

@window.event
def on_key_press(symbol, modyfiers):
    if symbol == key.SPACE:
        if game.round_no > 3:
            game.restart()

#create a bounding box area of the image
def get_bounding_box(v2, v_center):
        x_pos_BB = range(v_center, v_center+v2)
        if v_center in x_pos_BB:
            return x_pos_BB

def computer_chose():
    global pc_choice, pc_start
    pc_option = random.choice(pc_options)
    pc_start = sprite.Sprite(pc_option, x = 150, y = 200)
    return pc_option


class Game:
    '''
    Herni logika
    '''

    def __init__(self):
        self.round_no = 1
        self.score = [0, 0]


    def draw(self):
        self.player_score_screen.draw()
        self.pc_score_screen.draw()

        if self.round_no > 3:
            self.round_screen = text.Label(f"round: 3", font_size = 40, x = 550, y = 80, anchor_x="center")
            if self.score[0] > self.score[1]:
                self.gameover_screen = text.Label(f"Computer wins!\nPress space to restart", font_size = 24, x = 550, y = 30, anchor_x = "center").draw()
            elif self.score[1] > self.score[0]:
                self.gameover_screen = text.Label(f"You win!\nPress space to restart", font_size = 24, x = 550, y = 30, anchor_x = "center").draw()
        self.round_screen.draw()

    def restart(self):
        '''
        When spacebar is pressed
        '''
        self.round_no = 1
        self.score = [0, 0]
        self.newgame()

    def start(self):
        self.player_score_screen = text.Label(f"Player's\nscore: {str(self.score[1])}",
                                    font_size = 30, x = 800, y = 520, width = 300,
                                    align="center", anchor_x = "center", anchor_y="center", multiline=True)
        self.pc_score_screen = text.Label(f"Computer's\nscore: {str(self.score[0])}",
                                    font_size = 30, x = 280, y = 520, width = 300,
                                    align="center", anchor_x = "center", anchor_y="center", multiline=True)
        self.round_screen = text.Label(f"round: {game.round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")


    def newgame(self):
        self.player_score_screen = text.Label(f"Player's\nscore: {str(self.score[1])}",
                                    font_size = 30, x = 800, y = 520, width = 300,
                                    align="center", anchor_x = "center", anchor_y="center", multiline=True)
        self.pc_score_screen = text.Label(f"Computer's\nscore: {str(self.score[0])}",
                                    font_size = 30, x = 280, y = 520, width = 300,
                                    align="center", anchor_x = "center", anchor_y="center", multiline=True)
        self.round_screen = text.Label(f"round: {game.round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")


    def evaluate(self, player, computer):
        global its_a_tie
            #player wins
        if player == image_player_rock and computer == image_pc_scissors or player == image_player_scissors and computer == image_pc_paper or player == image_player_paper and computer == image_pc_rock:
            self.score[1] = self.score[1] + 1 #adds score number
            its_a_tie = 0
            self.player_score_screen = text.Label(f"Player's\nscore: {str(self.score[1])}", font_size = 30, x = 800, y = 520, width = 300, align="center", anchor_x = "center", anchor_y="center", multiline=True)
            self.round_no = self.round_no + 1 #adds round number
            self.round_screen = text.Label(f"round: {self.round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")
            #computer wins
        elif player == image_player_scissors and computer == image_pc_rock or player == image_player_paper and computer == image_pc_scissors or player == image_player_rock and computer == image_pc_paper:
            self.score[0] = self.score[0] + 1
            its_a_tie = 0
            self.pc_score_screen = text.Label(f"Computer's\nscore: {str(self.score[0])}", font_size = 30, x = 280, y = 520, width = 300, align="center", anchor_x = "center", anchor_y="center", multiline=True)
            self.round_no = self.round_no + 1
            self.round_screen = text.Label(f"round: {self.round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")
            #its a tie
        elif player == image_player_rock and computer == image_pc_rock or player == image_player_scissors and computer == image_pc_scissors or player == image_player_paper and computer == image_pc_paper:
            its_a_tie = 1


game = Game()

#global existing
play_image_size = (-265//2, 265, 215//2, -215)
choice_image_size = (-95//2, 95, -75//2, 75)
pc_options = [image_pc_rock, image_pc_paper, image_pc_scissors]

game.start()

click_record = [0, 0]
#gameover_screen = text.Label("x win!", font_size = 24)
its_a_tie = 0
tie_label = text.Label(f"It's a tie!", font_size = 20, x = 550, y = 250, anchor_x="center")
chose_one = text.Label(f"click \non one:", font_size = 20, x = 1050, y = 470, width = 100,
                                align="center", anchor_x = "right", anchor_y="center", multiline=True)

app.run()
