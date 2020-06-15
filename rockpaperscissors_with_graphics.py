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

window = Window(1100, 600)
F_SIZE = 30

#rock option
o_rock_pos = (950, 350)
image_option_player_rock = image.load("images\\small_choice_player-01.png")
option_player_rock = sprite.Sprite(image_option_player_rock, o_rock_pos[0], o_rock_pos[1])

#paper option
o_paper_pos = (950, 250)
image_option_player_paper = image.load("images\\small_choice_player-02.png")
option_player_paper = sprite.Sprite(image_option_player_paper, o_paper_pos[0], o_paper_pos[1])

#scissors option
o_scissors_pos = (950, 150)
image_option_player_scissors = image.load("images\\small_choice_player-03.png")
option_player_scissors = sprite.Sprite(image_option_player_scissors, o_scissors_pos[0], o_scissors_pos[1])

# player choice
image_player_rock = image.load("images\\choice_player-01.png")
image_player_paper = image.load("images\\choice_player-02.png")
image_player_scissors = image.load("images\\choice_player-03.png")
chosen_image = image_player_rock
player_start = sprite.Sprite(chosen_image, x = 650, y = 200)

#pc choice
image_pc_rock = image.load("images\\choice_pc-01.png")
image_pc_paper = image.load("images\\choice_pc-02.png")
image_pc_scissors = image.load("images\\choice_pc-03.png")
image_questionmark = image.load("images\\questionmark.png")
pc_start = sprite.Sprite(image_pc_rock, x = 150, y = 200)
questionmark = sprite.Sprite(image_questionmark, x = 50, y = 250)

round_no = 1
score = [0, 0]
play_image_size = (-265//2, 265, 215//2, -215)
choice_image_size = (-95//2, 95, -75//2, 75)
pc_options = [image_pc_rock, image_pc_paper, image_pc_scissors]
player_score_screen = text.Label(f"score: {str(score[1])}", font_size = 30, x = 750, y = 500)
pc_score_screen = text.Label(f"score: {str(score[0])}", font_size = 30, x = 150, y = 500)
round_screen = text.Label(f"round: {round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")
click_record = [0, 0]
gameover_screen = text.Label("x win!\n(Press space to restart)", font_size = 24)
gameover = 0

def newgame():
    global pc_start, option_player_rock, option_player_paper, option_player_scissors, gameover, new
    global player_score_screen, pc_score_screen, round_no, score, questionmark, player_start, round_screen
    round_no = 1
    score = [0, 0]
    play_image_size = (-265//2, 265, 215//2, -215)
    choice_image_size = (-95//2, 95, -75//2, 75)
    pc_options = [image_pc_rock, image_pc_paper, image_pc_scissors]
    player_score_screen = text.Label(f"score: {str(score[1])}", font_size = 30, x = 750, y = 500)
    pc_score_screen = text.Label(f"score: {str(score[0])}", font_size = 30, x = 150, y = 500)
    round_screen = text.Label(f"round: {round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")
    click_record = [0, 0]

@window.event
def on_draw():
    global pc_start, option_player_rock, option_player_paper, option_player_scissors, gameover, new
    global player_score_screen, pc_score_screen, round_no, score, questionmark, player_start, round_screen
    window.clear()
    questionmark.draw()
    player_start.draw()

    pc_start.draw()
    option_player_rock.draw()
    option_player_paper.draw()
    option_player_scissors.draw()
    #score
    player_score_screen.draw()
    pc_score_screen.draw()
    #round
    round_screen.draw()
    player_start.draw()
    if round_no >= 4:
        if score[0] > score[1]:
            gameover_screen = text.Label("Computer wins!\n(Press space to restart)", font_size = 24, x = 550, y = 30, anchor_x = "center").draw()
        elif score[1] > score[0]:
            gameover_screen = text.Label("You win!\n(Press space to restart)", font_size = 24, x = 550, y = 30, anchor_x = "center").draw()

@window.event
def on_mouse_press(x, y, b, mod):
    global click_record, chosen_image, player_start, round_no, gameover, score
    click_record[0] = x
    click_record[1] = y

    if round_no < 4:
    #options change
        if x in get_bounding_box(choice_image_size[1], o_rock_pos[0]) and y in get_bounding_box(choice_image_size[3], o_rock_pos[1]):
            chosen_image = image_player_rock
            player_start = sprite.Sprite(chosen_image, x = 650, y = 200)
            evaluate(image_player_rock, computer_chose())
        elif x in get_bounding_box(choice_image_size[1], o_paper_pos[0]) and y in get_bounding_box(choice_image_size[3], o_paper_pos[1]):
            chosen_image = image_player_paper
            player_start = sprite.Sprite(chosen_image, x = 650, y = 200)
            evaluate(image_player_paper, computer_chose())
        elif x in get_bounding_box(choice_image_size[1], o_scissors_pos[0]) and y in get_bounding_box(choice_image_size[3], o_scissors_pos[1]):
            chosen_image = image_player_scissors
            player_start = sprite.Sprite(chosen_image, x = 650, y = 200)
            evaluate(image_player_scissors, computer_chose())
        else:
            pass # nothing changes if clicked outside the bounding boxes

@window.event
def on_key_press(symbol, modyfiers):
    global gameover, round_no, score
    if round_no >= 4:
        if symbol == key.SPACE:
            round_no = 1
            score = [0, 0]
            newgame()

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

def evaluate(player, computer):
    global player_score_screen, pc_score_screen, round_no, round_screen, score
        #player wins
    if player == image_player_rock and computer == image_pc_scissors or player == image_player_scissors and computer == image_pc_paper or player == image_player_paper and computer == image_pc_rock:
        score[1] = score[1] + 1 #adds score number
        player_score_screen = text.Label(f"score: {str(score[1])}", font_size = 30, x = 750, y = 500)
        player_score_screen.draw()
        round_no = round_no + 1 #adds round number
        round_screen = text.Label(f"round: {round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")
        round_screen.draw()
        #computer wins
    elif player == image_player_scissors and computer == image_pc_rock or player == image_player_paper and computer == image_pc_scissors or player == image_player_rock and computer == image_pc_paper:
        score[0] = score[0] + 1
        pc_score_screen = text.Label(f"score: {str(score[0])}", font_size = 30, x = 150, y = 500)
        pc_score_screen.draw()
        round_no = round_no + 1
        round_screen = text.Label(f"round: {round_no}", font_size = 40, x = 550, y = 80, anchor_x="center")
        round_screen.draw()
        #its a tie
    elif player == image_player_rock and computer == image_pc_rock or player == image_player_scissors and computer == image_pc_scissors or player == image_player_paper and computer == image_pc_paper:
        pass
app.run()
