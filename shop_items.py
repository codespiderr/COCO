import pygame
from Buttons import Buttons

pygame.init()

Rackis_font = "fonts/rackis/Rackis.ttf"

rand_color = (100, 250, 0)

button_press = pygame.mixer.Sound('music/Button_press.wav')

game_coin = pygame.image.load("pictures/random assets/binance.png")
game_coin = pygame.transform.scale(game_coin, (48, 48))

player_money = 200


class shop:
    def __init__(self, events, picture, name, sword_cost, stat_1="empty", stat_2="empty", stat_3="empty"):
        self.game_screen = pygame.display.get_surface()

        self.sword = picture
        self.sword_rect = self.sword.get_rect()

        self.stat_1 = stat_1
        self.stat_1s = str(stat_1)
        self.stat_2 = stat_2
        self.stat_2s = str(stat_2)
        self.stat_3 = stat_3
        self.stat_3s = str(stat_3)

        self.name = str(name)

        self.sword_cost = sword_cost
        self.sword_costs = str(sword_cost)

        self.rotateNumber = 0

        self.purchase = False
        self.equip = False
        self.equipped = False

        self.Buy_button_obj = Buttons("Buy", True, (0, 0, 0))
        self.Equip_button = Buttons("Equip", True, (0, 0, 0))
        self.Equipped_button = Buttons("Equipped", True, (0, 0, 0))
        self.Buy_status = "buy"

    def sword_data(self, events):
        global game_coin
        global player_money
        self.player_money = player_money
        self.player_moneys = str(self.player_money)

        self.events = events

        self.sword = pygame.transform.scale(self.sword, (200, 200))

        self.sword_rect = self.sword.get_rect(topleft=(200, 220))
        self.game_screen.blit(self.sword, self.sword_rect)

        font = pygame.font.Font(Rackis_font, 80)  # fonts
        self.play_text = font.render(self.stat_1s, True, (0, 0, 0))
        self.game_screen.blit(self.play_text, (800, 200))

        font = pygame.font.Font(Rackis_font, 80)  # fonts
        self.play_text = font.render(self.stat_2s, True, (0, 0, 0))
        self.game_screen.blit(self.play_text, (800, 350))

        font = pygame.font.Font(Rackis_font, 80)  # fonts
        self.play_text = font.render(self.stat_3s, True, (0, 0, 0))
        self.game_screen.blit(self.play_text, (800, 500))

        font = pygame.font.Font(Rackis_font, 60)  # fonts
        self.play_text = font.render(self.name, True, (0, 0, 0))
        self.game_screen.blit(self.play_text, (200, 100))

        if self.rotateNumber >= 360:
            self.rotateNumber = 0
        else:
            self.rotateNumber += 2
        roti_game_coin = pygame.transform.rotate(game_coin, self.rotateNumber)
        rect = roti_game_coin.get_rect(center=(600, 85))
        self.game_screen.blit(roti_game_coin, rect)

        font = pygame.font.Font(Rackis_font, 40)  # fonts
        self.play_text = font.render(self.player_moneys, True, (0, 0, 0))
        self.game_screen.blit(self.play_text, (640, 65))

        rect = roti_game_coin.get_rect(center=(280, 185))
        self.game_screen.blit(roti_game_coin, rect)
        font = pygame.font.Font(Rackis_font, 40)  # fonts
        self.play_text = font.render(self.sword_costs, True, (0, 0, 0))
        self.game_screen.blit(self.play_text, (310, 165))

        if self.Buy_status == "buy":
            self.Buy_button_obj.text_Blit(240, 550, Rackis_font, 60)
            self.Buy_button_obj.press_check(rand_color, (0, 0, 0), 240, 550, 320, 595, self.events)

            if self.Buy_button_obj.button_status == "positive" and self.player_money >= self.sword_cost:
                self.Buy_button_obj.right_click = False
                self.Buy_button_obj.button_status = "negitive"  # butoon press = False
                button_press.play()  # play button music
                print("pressed Buy in shop")
                self.purchase = True
                self.Buy_status = "equip"
                player_money = player_money - self.sword_cost
                self.sword_costs = "OWNED"
        elif self.Buy_status == "equip":
            self.Equip_button.text_Blit(225, 550, Rackis_font, 60)
            self.Equip_button.press_check(rand_color, (0, 0, 0), 225, 550, 340, 600, self.events)

            if self.Equip_button.button_status == "positive":
                self.Equip_button.right_click = False
                self.Equip_button.button_status = "negitive"  # button press = False
                button_press.play()  # play button music
                print("pressed Equip in shop")
                self.purchase = True
                self.equip = True
                self.equipped = False
                self.Buy_status = "equipped"

        elif self.Buy_status == "equipped":
            self.Equipped_button.text_Blit(195, 550, Rackis_font, 60)
