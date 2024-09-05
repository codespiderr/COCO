import pygame
import random

rand_color = (100,250,0)

# classes
class Buttons:  # button class

    def __init__(self, text_name, trueFalse, colors):  # Init initialization of basic text info
        self.text_name = text_name
        self.TrueFalse = trueFalse
        self.colors = colors
        self.pic_status = "negitive"
        self.right_click = False
        self.game_screen = pygame.display.get_surface()
        self.in_button_check= False


    def text_Blit(self, x, y, font_name, size):  # blit part   # function for puttin g the text on screen
        font1 = pygame.font.Font(font_name, size)  # fonts
        self.play_text = font1.render(self.text_name, True, self.colors)
        self.game_screen.blit(self.play_text, (x, y))


    def press_check(self, fin_color, ini_color, x1, y1, x2, y2,events):  # function for button color change

        self.right_click = False
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:

                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    self.right_click = True
            else:
                self.right_click = False
        if self.mouse_x > x1 and self.mouse_x < x2 and self.mouse_y > y1 and self.mouse_y < y2:
            if self.in_button_check == True:  # for random color structure
                # it will only allow
                # for picking of a new
                # random color once  it
                # moves off the area
                if fin_color == rand_color:
                    fin_color = (random.randint(0, 255), random.randint(0, 255),
                                 random.randint(0, 255))  # only for rand color generator
                self.colors = fin_color
                self.in_button_check = False

            if self.right_click == True:  # in an object
                self.button_status = "positive"
            else:
                self.button_status = "negitive"

        else:
            self.colors = ini_color
            self.in_button_check = True
            self.button_status = "negitive"


    def key_press_check(self, pygame_parameter):  # for checking press with keys
        keys = pygame.key.get_pressed()
        if pygame_parameter == "tab":  # checking for tab key
            if keys[pygame.K_TAB]:
                self.button_status = "positive"

        if pygame_parameter == "space":  # checking for space key
            if keys[pygame.K_SPACE]:
                self.button_status = "positive"

        if pygame_parameter == "esc":  # checking for escape key
            if keys[pygame.K_ESCAPE]:
                self.button_status = "positive"


    def img_blit(self, picture, x, y):
        self.game_screen.blit(picture, (x, y))


    def pic_press(self, x, y, x1, y1,events):
        self.right_click = False
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    self.right_click = True
                    pygame.time.wait(100)

                else:
                    self.right_click = False
            else:
                self.right_click = False
        if self.mouse_x > x and self.mouse_x < x1 and self.mouse_y > y and self.mouse_y < y1:
            if self.right_click == True:  # in an object
                self.pic_status = "positive"
            else:
                self.pic_status = "negitive"
        else:
            self.pic_status = "negitive"
