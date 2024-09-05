# Initialize The Arkhight Blade
# todo debugger

import pygame
from sys import exit

import Player
import game_map
import swords
import shop_items
from Buttons import Buttons
from dubug import debugger  # debugger file

pygame.init()  # initialization
pygame.mixer.init()  # music initialization

# display settings
screen_width = 1280
screen_height = 640
game_screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption('The Arkhight Blade')  # window settings
game_icon = pygame.image.load("pictures/random assets/arkhight_icon.png")  # icon image
pygame.display.set_icon(game_icon)  # setting icon

pygame.mouse.set_pos((500, 360))  # for rare cases of bugs it will automatically set the mouse to the center

# elements
clock = pygame.time.Clock()  # for clock

events = []

# fonts
freesansbold_font = 'freesansbold.ttf'
Rackis_bold_font = "fonts/rackis/Rackis Bold.ttf"
Rackis_font = "fonts/rackis/Rackis.ttf"
hermes_font = "fonts/hermes/Hermes-Regular.otf"

# images
game_tittle = pygame.image.load("pictures/random assets/arkhight blade(game).jpg").convert_alpha()  # image making
menu_icon_32 = pygame.image.load("pictures/random assets/pause.png").convert_alpha()  # changing to pause icon

main_cha_down0 = pygame.image.load("pictures/main_cha/main_cha_down_0.png").convert_alpha()  # main cgarecter images
main_cha_up0 = pygame.image.load("pictures/main_cha/main_cha_up_0.png").convert_alpha()
main_cha_left0 = pygame.image.load("pictures/main_cha/main_cha_left_0.png").convert_alpha()
main_cha_right0 = pygame.image.load("pictures/main_cha/main_cha_right_0.png").convert_alpha()

main_cha_down1 = pygame.image.load("pictures/main_cha/main_cha_down_1.png").convert_alpha()  # main cgarecter images
main_cha_up1 = pygame.image.load("pictures/main_cha/main_cha_up_1.png").convert_alpha()
main_cha_left1 = pygame.image.load("pictures/main_cha/main_cha_left_1.png").convert_alpha()
main_cha_right1 = pygame.image.load("pictures/main_cha/main_cha_right_1.png").convert_alpha()

main_cha_down2 = pygame.image.load("pictures/main_cha/main_cha_down_0.png").convert_alpha()  # main cgarecter images
main_cha_up2 = pygame.image.load("pictures/main_cha/main_cha_up_0.png").convert_alpha()
main_cha_left2 = pygame.image.load("pictures/main_cha/main_cha_left_0.png").convert_alpha()
main_cha_right2 = pygame.image.load("pictures/main_cha/main_cha_right_0.png").convert_alpha()

main_cha_down3 = pygame.image.load("pictures/main_cha/main_cha_down_2.png").convert_alpha()  # main cgarecter images
main_cha_up3 = pygame.image.load("pictures/main_cha/main_cha_up_2.png").convert_alpha()
main_cha_left3 = pygame.image.load("pictures/main_cha/main_cha_left_2.png").convert_alpha()
main_cha_right3 = pygame.image.load("pictures/main_cha/main_cha_right_2.png").convert_alpha()

main_cha_up = [main_cha_up0, main_cha_up1, main_cha_up2, main_cha_up3]  # lists for animations
main_cha_left = [main_cha_left0, main_cha_left1, main_cha_left2, main_cha_left3]
main_cha_right = [main_cha_right0, main_cha_right1, main_cha_right2, main_cha_right3]
main_cha_down = [main_cha_down0, main_cha_down1, main_cha_down2, main_cha_down3]

radio_button_on = pygame.image.load("pictures/random assets/switch.png").convert_alpha()
radio_button_off = pygame.image.load("pictures/random assets/switch (1).png").convert_alpha()
grass_tile = pygame.image.load("pictures/grass/grass_tile.png").convert_alpha()
radio_choice = radio_button_on.convert_alpha()

shop_left_aroow = pygame.image.load("pictures/random assets/left.png").convert_alpha()
shop_right_aroow = pygame.image.load("pictures/random assets/right.png").convert_alpha()

game_coin = pygame.image.load("pictures/random assets/binance.png")

sword_icon_test1 = pygame.image.load("pictures/swords/weapons/jacweapons18.png")
sword1 = pygame.image.load("pictures/swords/weapons/weapon18v2.png")
sword_icon_test2 = pygame.image.load("pictures/swords/weapons/jacweapons17.png")
sword2 = pygame.image.load("pictures/swords/weapons/weapon17v2.png")
sword_icon_test3 = pygame.image.load("pictures/swords/weapons/jacweapons12.png")
sword3 = pygame.image.load("pictures/swords/weapons/weapon12v2.png")
sword_icon_test4 = pygame.image.load("pictures/swords/weapons/jacweapons21.png")
sword4 = pygame.image.load("pictures/swords/weapons/weapon21v2.png")
sword_icon_test5 = pygame.image.load("pictures/swords/weapons/jacweapons6.png")
sword5 = pygame.image.load("pictures/swords/weapons/weapon6v2.png")

list_of_swords = [sword1, sword2, sword3, sword4, sword5]

custom_cursor_point = pygame.image.load("pictures/random assets/mouse_curson1.png")  # custom cursor
custom_cursor_point = pygame.transform.scale(custom_cursor_point, (32, 32))

custom_cursor = custom_cursor_point

custom_cursor_rect = custom_cursor.get_rect()

# variables
game_loop = True  # variable initialization
in_button_check = False  # for rand color modification

# colors
white = (255, 255, 255)  # colors
green = (0, 255, 0)  # pure green
blue = (0, 0, 128)
red = (255, 0, 0)
black = (0, 0, 0)
mid_grey = (120, 120, 120)
light_grey = (180, 180, 180)
rand_color = (100, 250, 0)  # only used when rand color selection is broken else only rand color as seen in button class

# music
button_press = pygame.mixer.Sound('music/Button_press.wav')
# button_press.play()  #syntax

music_choice1 = "music/BoxCat-Games-Battle-Boss.mp3"  # default
music_choice2 = "music/Neverland.mp3"

neverland = "music/Neverland.mp3"  # defining music
intense_music = "music/BoxCat-Games-Battle-Boss.mp3"


def music_change(sound_choice):  # music switcher class
    global music_choice1
    global music_choice2
    if music_choice2 != music_choice1:  # only change when new song is being requested
        if music_choice2 == "none":  # to play no background music
            pygame.mixer.music.pause()
            music_choice1 = music_choice2
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()  # remving old song
            pygame.mixer.music.load(sound_choice)  # adding new song
            pygame.mixer.music.play(-1)
            music_choice1 = music_choice2


# external objects
# player class
player_obj = Player.Player(main_cha_down, main_cha_left, main_cha_right, main_cha_up,
                           (595, 285), 0)  # import player object

sword_obj = swords.swords()

game_tile_obj = game_map.tilemap()

game_shop_sword = shop_items.shop(events, sword_icon_test1, "purpleeboi", "FREE", 0, "hello", 45)
game_shop_sword1 = shop_items.shop(events, sword_icon_test2, "greenboii", 20, 1, "bye bye", 54)
game_shop_sword2 = shop_items.shop(events, sword_icon_test3, "redtrident", 35, 43, "ring ring",
                                   "*number*")
game_shop_sword3 = shop_items.shop(events, sword_icon_test4, "Demon_thing(red)", 47, 32, "money",
                                   "mcqueen")
game_shop_sword4 = shop_items.shop(events, sword_icon_test5, "THOR Hammer", 63, 10000, "titanic",
                                   "Lol")

game_swords = [game_shop_sword, game_shop_sword1, game_shop_sword2, game_shop_sword3, game_shop_sword4]

sword_equippedlist = [game_swords[0]]  # list of equipped swords
current_sword = pygame.transform.scale(list_of_swords[0], (96, 96))


def gameobjectshop(obj):
    obj.sword_data(events)


# button classs
play_button = Buttons("PLAY", True, white)  # object creation for Button class
help_button = Buttons("HELP", True, white)
help_back_button = Buttons("BACK", True, white)  # back button in help
menu_icon_image = Buttons("menu_icon", True, white)
in_game_menu_main = Buttons("MAIN MENU", True, black)
in_game_menu_shop = Buttons("SHOP", True, black)
in_game_menu_shop_back = Buttons("BACK", True, black)  # back button in shop
in_game_shop_info = Buttons("SHOP", True, black)  # info for the player
quit_option_button = Buttons("QUIT", True, white)
press_space_info = Buttons("PRESS SPACE TO PLAY!", True, white)  # info for the player
press_tab_info = Buttons("(TAB)", True, black)
in_pause_menu_info = Buttons("PAUSED", True, black)
in_game_pause_resume = Buttons("RESUME", True, black)
in_game_pause_sound = Buttons("SOUND", True, black)
radio_button_on_obj = Buttons("radio_on", True, black)
radio_button_off_obj = Buttons("radio_off", True, black)
shop_left_aroow_obj = Buttons("left_arrow", True, black)
shop_right_aroow_obj = Buttons("right_arrow", True, black)


class State_Manager:  # state/game scene
    def __init__(self):
        self.game_state = "main_menu"  # starter zone
        self.music_state = "on"  # for music on and offing
        self.music = "none"
        self.sword_number = 0
        self.money = 200

    def main_menu(self):  # main menu modded code
        game_screen.fill(black)
        game_screen.blit(game_tittle, (290, 50))  # tittle pic #aka tittle art

        if self.music_state == "on":
            self.music = neverland

        press_space_info.text_Blit(520, 600, Rackis_font, 30)

        play_button.text_Blit(570, 500, Rackis_font, 80)  # object play
        play_button.press_check(rand_color, white, 570, 500, 715, 560, events)  # play button
        play_button.key_press_check("space")
        if play_button.button_status == "positive":  # if click in area change game state
            print("pressed play")
            self.game_state = "in_game"
            button_press.play()
            play_button.button_status = "negitive"

        help_button.text_Blit(270, 500, Rackis_font, 80)  # object help
        help_button.press_check(rand_color, white, 270, 500, 410, 560, events)  # help button
        if help_button.button_status == "positive":  # if click in area change game state
            print("pressed help")
            self.game_state = "help_screen"
            button_press.play()
            help_button.button_status = "negitive"

        quit_option_button.text_Blit(880, 500, Rackis_font, 80)  # object quit
        quit_option_button.press_check(rand_color, white, 880, 500, 1000, 560, events)  # quit button
        if quit_option_button.button_status == "positive":
            quit_option_button.button_status = "negitive"
            print("pressed quit")
            pygame.quit()  # quitting pygame
            exit()  # quitting the program

    def in_game(self):  # main game code goes here
        global current_sword

        if self.music_state == "on":
            self.music = intense_music  # changing music

        game_tile_obj.update()  # blitting the tiles
        player_obj.update()  # calling player class in in_game
        for i in range(0, len(game_swords)):
            if game_swords[i].Buy_status == "equipped":
                current_sword = list_of_swords[i]
                current_sword = pygame.transform.scale(current_sword, (96, 96))
                break

        sword_obj.sword_update(events, current_sword)  # sword update

        pygame.draw.rect(game_screen, light_grey,
                         pygame.Rect(0, 580, 1280, 60))  # player shop bar/health bar/other stuff
        pygame.draw.rect(game_screen, light_grey, pygame.Rect(120, 0, 1000, 60))

        font = pygame.font.Font(Rackis_font, 50)  # money on game_screen
        play_text = font.render(str(self.money), True, (0, 0, 0))
        game_screen.blit(play_text, (200, 20))

        pygame.draw.rect(game_screen, light_grey, pygame.Rect(1224, 16, 40, 40))  # rectangle aroung menu button
        menu_icon_image.img_blit(menu_icon_32, 1228, 20)  # pic blit
        menu_icon_image.pic_press(1224, 16, 1264, 60, events)  # pic press check
        if menu_icon_image.pic_status == "positive":
            self.game_state = "in_game_menu"
            menu_icon_image.pic_status = "negitive"  # butoon press = False
            button_press.play()  # play button music
            print("pressed in game menu")

        press_tab_info.text_Blit(1130, 580, Rackis_font, 20)
        in_game_menu_shop.text_Blit(1100, 590, Rackis_font, 60)  # shop button in in game
        in_game_menu_shop.press_check(rand_color, black, 1100, 590, 1200, 635, events)
        in_game_menu_shop.key_press_check("tab")  # checking press with tab key
        if in_game_menu_shop.button_status == "positive":
            self.game_state = "in_shop"
            in_game_menu_shop.right_click = False
            in_game_menu_shop.button_status = "negitive"  # butoon press = False
            button_press.play()  # play button music
            print("pressed shop in in game")

    # player_obj.update()

    def help_screen(self):  # help screen code here
        game_screen.fill(black)
        help_back_button.text_Blit(1100, 20, Rackis_font, 60)  # object play
        help_back_button.press_check(rand_color, white, 1100, 20, 1210, 65, events)  # play button
        help_back_button.key_press_check("esc")
        if help_back_button.button_status == "positive":  # sending in to main menu
            self.game_state = "main_menu"
            help_back_button.button_status = "negitive"  # butoon press = False
            button_press.play()  # play button music
            print("pressed help back")

    def in_game_pause(self):
        # making there be no music
        if self.music_state == "on":
            self.music = "none"
        global radio_choice
        global menu_icon_32

        game_screen.fill(black)
        pygame.draw.rect(game_screen, light_grey, pygame.Rect(100, 50, 1080, 500))
        menu_icon_image.img_blit(menu_icon_32, 1120, 70)  # pic blit
        menu_icon_image.pic_press(1120, 70, 1150, 100, events)  # pic press check
        in_pause_menu_info.text_Blit(560, 50, Rackis_font, 50)
        if menu_icon_image.pic_status == "positive":
            self.game_state = "in_game"
            menu_icon_image.right_click = False
            menu_icon_image.pic_status = "negitive"  # butoon press = False
            button_press.play()  # play button music
            print("pressed in game menu back")

        in_game_menu_main.text_Blit(520, 420, Rackis_font, 60)  # main menu button in in game menu#235
        in_game_menu_main.press_check(rand_color, black, 520, 420, 750, 465, events)
        if in_game_menu_main.button_status == "positive":
            self.game_state = "main_menu"
            in_game_menu_main.right_click = False
            in_game_menu_main.button_status = "negitive"  # butoon press = False
            button_press.play()  # play button music
            print("pressed main menu in in game menu")

        in_game_pause_resume.text_Blit(550, 350, Rackis_font, 60)  # main menu button in in game menu#235
        in_game_pause_resume.press_check(rand_color, black, 550, 350, 720, 395, events)
        if in_game_pause_resume.button_status == "positive":
            self.game_state = "in_game"
            in_game_pause_resume.right_click = False
            in_game_pause_resume.button_status = "negitive"  # butoon press = False
            button_press.play()  # play button music
            print("pressed resume in in game pause")

        in_game_pause_sound.text_Blit(500, 150, Rackis_font, 60)
        radio_button_on_obj.img_blit(radio_choice, 650, 150)  # pic blit
        radio_button_on_obj.pic_press(650, 150, 715, 200, events)  # pic press check
        if radio_button_on_obj.pic_status == "positive":
            radio_button_on_obj.pic_status = "negitive"
            if radio_choice == radio_button_off:
                radio_choice = radio_button_on
                self.music_state = "on"
            else:
                radio_choice = radio_button_off
                self.music_state = "off"
            button_press.play()  # play button music
            print("pressed in game menu sound")

    def in_shop(self):
        # making to music choice
        if self.music_state == "on":
            self.music = neverland

        game_screen.fill(light_grey)
        in_game_menu_shop_back.text_Blit(1100, 20, Rackis_font, 60)
        in_game_menu_shop_back.press_check(rand_color, black, 1100, 20, 1210, 65, events)
        in_game_menu_shop_back.key_press_check("esc")
        in_game_shop_info.text_Blit(600, 10, Rackis_font, 50)  # shows the player they are in shop
        if in_game_menu_shop_back.button_status == "positive":  # sending in to in_game
            self.game_state = "in_game"
            in_game_menu_shop_back.button_status = "negitive"  # butoon press = False
            button_press.play()  # play button music
            print("pressed back in shop")

        gameobjectshop(game_swords[self.sword_number])
        self.money = game_swords[self.sword_number].player_money

        for i in game_swords:
            if i.equip:
                sword_equippedlist.append(i)

        for j in game_swords:

            if j.Buy_status == "buy":
                j.Buy_status = "buy"
            elif j.Buy_status == "equip":
                j.Buy_status = "equip"
                j.equip = False
            elif j.Buy_status == "equipped":
                j.Buy_status = "equip"
                j.equip = False

            sword_equippedlist[len(sword_equippedlist) - 1].Buy_status = "equipped"

        debugger(game_swords[0].Buy_status, 10, 130, "red")
        debugger(game_swords[1].Buy_status, 10, 160, "red")
        debugger(game_swords[2].Buy_status, 10, 190, "red")
        debugger(game_swords[3].Buy_status, 10, 220, "red")
        debugger(game_swords[4].Buy_status, 10, 250, "red")

        shop_left_aroow_obj.img_blit(shop_left_aroow, 200, 450)
        shop_right_aroow_obj.img_blit(shop_right_aroow, 300, 450)

        shop_left_aroow_obj.pic_press(200, 450, 264, 514, events)
        shop_right_aroow_obj.pic_press(300, 450, 364, 514, events)

        if shop_left_aroow_obj.pic_status == "positive":  # switching between swords in shop arrows
            if self.sword_number > 0:
                self.sword_number -= 1
            else:
                self.sword_number = 0
            print("pressed left in shop")
        if shop_right_aroow_obj.pic_status == "positive":
            if len(game_swords) - 1 > self.sword_number:
                self.sword_number += 1
            print("pressed right in shop")

    def state_manager(self):  # manages which state to work in
        global music_choice2

        if self.game_state == "main_menu":
            self.main_menu()
        if self.game_state == "in_game":
            self.in_game()
        if self.game_state == "help_screen":
            self.help_screen()
        if self.game_state == "in_game_menu":
            self.in_game_pause()
        if self.game_state == "in_shop":
            self.in_shop()

        if self.music_state == "on":
            music_choice2 = self.music  # changing global music from the class
        else:
            music_choice2 = "none"


state_manager_obj = State_Manager()  # object that runs everything

while game_loop:  # forever game loop
    events = pygame.event.get()
    for event in events:  # event loop
        if event.type == pygame.QUIT:  # Quit function
            pygame.quit()  # quitting pygame
            exit()  # quitting the program
        elif event.type == pygame.MOUSEBUTTONDOWN:  # testing feature on mouse position #test
            print(pygame.mouse.get_pos())
            mouse_press = True
        else:
            mouse_press = False

    state_manager_obj.state_manager()  # game class

    music_change(music_choice2)  # calling the music function

    debugger(player_obj.pos, 10, 10, red)  # debugging text
    debugger(round(clock.get_fps(), 2), 10, 40, red)
    debugger(game_tile_obj.offset_x_add, 10, 70, "red")
    debugger(game_tile_obj.offset_y_add, 10, 100, "red")

    pygame.display.update()  # screen updater
    game_screen.fill("white")
    clock.tick(30)  # frame rate cap
