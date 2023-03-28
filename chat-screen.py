import keyboard, threading, time

# CONFIGURATION
screen_height = 23  # x lines of chat
screen_length = 80  # x symbols of line
refresh_rate = 24   # x times per second

screen_background = '□'
player_icon = '■'
player_position_h = 5   # y coordinate start position
player_position_l = 5   # x coordinate start position

# CONTROLLS
up = 'up'
down = 'down'
left = 'left'
right = 'right'

def draw_screen(height, length):
    def draw_line(height):
        line = ''
        n = 0
        while n != length:
            if player_position_h == height and player_position_l == n:
                line += player_icon
                n += 1
            else:
                line += screen_background
                n += 1
        print(line)

    n = 0
    while n != height:
        draw_line(n)
        n += 1

def screen():
    while True:
        print(" ")
        print("--------------")
        print(" ")
        draw_screen(screen_height, screen_length)
        time.sleep(1 / refresh_rate)

def input():
    global player_position_h
    global player_position_l
    while True:
        if keyboard.is_pressed(up):
            if player_position_h - 1 != -1:
                player_position_h -= 1
        if keyboard.is_pressed(down):
            if player_position_h + 1 != screen_height:
                player_position_h += 1
        if keyboard.is_pressed(left):
            if player_position_l - 1 != -1:
                player_position_l -= 1
        if keyboard.is_pressed(right):
            if player_position_l + 1 != screen_length:
                player_position_l += 1
        time.sleep(1 / refresh_rate)

player_position_h -= 1
player_position_l -= 1
t1 = threading.Thread(target=screen)
t2 = threading.Thread(target=input)
t1.start()
t2.start()