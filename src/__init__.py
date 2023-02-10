import pygame
from pygame.locals import *

from src.deck import Deck
from src.tools import button


class TextInput(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, bg_color, font_size):
        self.text_value = ""
        self.color = color
        self.bg_color = bg_color
        self.font = pygame.font.SysFont("Corbel", font_size)
        self.text = self.font.render(self.text_value, True, self.color)
        self.bg = pygame.Rect(x, y, width, height)


game_balance = 0.0
current_points = 0.0
has_the_game_begun = False

background_colour = (234, 212, 252)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
bright_green = (0, 121, 44)

display_width = 1024
display_height = 800
screen_bounds = (display_width, display_height)

window = pygame.display.set_mode(screen_bounds)
pygame.display.set_caption("CardGame")
window.fill(background_colour)
pygame.display.flip()

pygame.init()

huge_font = pygame.font.SysFont('Corbel', 80)
large_font = pygame.font.SysFont('Corbel', 60)
small_font = pygame.font.SysFont('Corbel', 25)
the_smallest_font = pygame.font.SysFont('Corbel', 12)

running = True

# cardBack = pygame.image.load('../resources/cards/BACK.png')
# cardBack = pygame.transform.scale(cardBack, (100, 160))

# window.blit(cardBack, (0, 0))
# pygame.display.flip()


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def begin_easy_game():
    global has_the_game_begun
    has_the_game_begun = True


def create_label(message, font, center_width, center_height):
    text_surf, text_rect = text_objects(message, font)
    text_rect.center = (center_width, center_height)
    window.blit(text_surf, text_rect)


def create_input_box(start_x, start_y, width, height, color_font, bg_color, text):
    input_rect = pygame.Rect(start_x, start_y, width, height)
    pygame.draw.rect(window, bg_color, input_rect)
    text_input_box_surface = small_font.render(text, True, color_font)

    window.blit(text_input_box_surface, (input_rect.x + 5, input_rect.y + 5))


def home_screen(user_input):
    global game_balance
    game_balance = 100.0

    # start message
    create_label("Enter balance, then choose a level", large_font, (display_width / 2), (display_height / 3))

    # start input box
    create_input_box(440, 340, 140, 40, white, black, user_input)

    # buttons for levels - Easy, Hard

    button("Easy", 240, 440, 140, 80, 80, green, bright_green, begin_easy_game)
    button("Hard", 640, 440, 140, 80, 80, green, bright_green, None)


def game_screen(user_input):
    create_label("Balance", small_font, 50, 15)
    create_label(str(game_balance), small_font, 50, 40)

    create_label("Points", small_font, display_width - 50, 15)
    create_label(str(current_points), small_font, display_width - 50, 40)

    create_label("Input your bet", small_font, (display_width / 2), 480)
    create_input_box((display_width / 2) - 50, 490, 100, 40, black, white, user_input)
    # create_input_box(20, 30, 70, 40, black, background_colour, str(game_balance))
    # create_input_box(970, 30, 70, 40, black, background_colour, str(current_points))

    button("LOWER", 250, 550, 150, 50, 40, green, bright_green, None)
    button("HIGHER", (display_width / 2) + 112, 550, 150, 50, 40, green, bright_green, None)

    chance_higher = 60
    chance_lower = 40

    # because it's easy game
    create_label("Chance: ", small_font, 300, 620)
    create_label(str(chance_lower) + '%', small_font, 355, 620)

    create_label("Chance: ", small_font, 680, 620)
    create_label(str(chance_higher) + '%', small_font, 735, 620)

    # shuffle & finish button

    button("Shuffle", 30, 720, 150, 40, 40, green, bright_green, None)
    button("Finish", 850, 720, 150, 40, 40, green, bright_green, None)

    card = pygame.image.load('../resources/cards/CLUB-1.svg')
    card = pygame.transform.scale(card, (200, 320))

    window.blit(card, (50, 100))
    pygame.display.flip()




def game_intro():
    user_text = ''
    while running:
        # filling here because we want to remove buttons after click
        window.fill(background_colour)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        if not has_the_game_begun:
            home_screen(user_text)
        else:
            game_screen(user_text)
        pygame.display.update()


game_intro()

