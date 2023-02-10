import pygame


black = (0, 0, 0)
display_width = 1024
display_height = 800
screen_bounds = (display_width, display_height)
window = pygame.display.set_mode(screen_bounds)


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(message, start_x, start_y, width, height, font_size, inactive_color, active_color, action):
    mouse_pos = pygame.mouse.get_pos()
    is_clicked = pygame.mouse.get_pressed()

    button_rect = (start_x, start_y, width, height)
    if start_x + width > mouse_pos[0] > start_x and start_y + height > mouse_pos[1] > start_y:
        pygame.draw.rect(window, active_color, button_rect)

        # check if left button of mouse is clicked
        # is_clicked has 3 values (False, False, False) for left, middle, right button of the mouse
        if is_clicked[0] == 1:
            action()
    else:
        pygame.draw.rect(window, inactive_color, button_rect)

    text_font = pygame.font.SysFont('Corbel', font_size)
    text_surface, text_rect = text_objects(message, text_font)
    text_rect.center = ((start_x + width / 2), (start_y + height / 2))

    window.blit(text_surface, text_rect)