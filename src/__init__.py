import pygame
from pygame.locals import *

#from src.deck import Deck
from src.tools import button


class TextInput(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, bg_color, font_size):
        self.text_value = ""
        self.color = color
        self.bg_color = bg_color
        self.font = pygame.font.SysFont("Corbel", font_size)
        self.text = self.font.render(self.text_value, True, self.color)
        self.bg = pygame.Rect(x, y, width, height)


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

running = True

# cardBack = pygame.image.load('../resources/cards/BACK.png')
# cardBack = pygame.transform.scale(cardBack, (100, 160))

# window.blit(cardBack, (0, 0))
# pygame.display.flip()


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def game_intro():
    user_text = ''
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # start message
        text_surf, text_rect = text_objects("Enter balance, then choose a level", large_font)
        text_rect.center = ((display_width / 2), (display_height / 3))
        window.blit(text_surf, text_rect)

        # start input box

        # input_box = TextInput(0, 0, 0, 0, black, (130, 12, 22), 30)

        input_rect = pygame.Rect(440, 340, 140, 40)
        pygame.draw.rect(window, black, input_rect)
        text_input_box_surface = small_font.render(user_text, True, white)

        window.blit(text_input_box_surface, (input_rect.x + 5, input_rect.y + 5))

        # buttons for levels - Easy, Hard

        button("Easy", 240, 440, 140, 80, 80, green, bright_green, None)
        button("Hard", 640, 440, 140, 80, 80, green, bright_green, None)

        pygame.display.update()


game_intro()
