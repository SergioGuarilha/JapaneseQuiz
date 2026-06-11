import pygame
import random
from quizbuilder import all_rect_numbers
from hiragana import hiradict
from katakana import katadict

pygame.init()

#General Configurations
screen = pygame.display.set_mode((1000, 600))
font = pygame.font.Font('fonts/ipaexg.ttf', 36)
config_cog = pygame.image.load('./assets/ConfigCog.png')

quiz_options = ["Hiragana", "Hiragana\n Combos", "Katakana", "Katakana\n Combos"]

dist_from_top = 410
rect_width = 180
rect_height = 140
border_width = 10

main_rect = pygame.Rect(300, 50, 400, 200)
config_rect = pygame.Rect(890, 10, 70, 70)
menu_rects = [
    pygame.Rect(80, dist_from_top, rect_width, rect_height),
    pygame.Rect(300, dist_from_top, rect_width, rect_height),
    pygame.Rect(520, dist_from_top, rect_width, rect_height),
    pygame.Rect(740, dist_from_top, rect_width, rect_height)
]

def draw_menu():
    screen.fill("white")

    #draws menu background decoration
    for i in range(10):
        screen_width = pygame.display.get_window_size()[0]
        screen_height = pygame.display.get_window_size()[1]
        line_pattern = ((i * 10) + 5) / 100
        line_placement = screen_height * line_pattern
        pygame.draw.line(screen, pygame.Color("white"),[0, line_placement],[1000, line_placement], 5)
        for j in range(25):
            if j % 2 == 0:
                hira_or_kata = hiradict
            else:
                hira_or_kata = katadict
            deco_symbol = font.render(hira_or_kata['symbols'].__getitem__(random.randrange(len(hira_or_kata['symbols']))), True, pygame.Color("black"))
            symbol_x = (j / 24) * screen_width
            symbol_y = line_placement - (deco_symbol.get_height() // 2)
            screen.blit(deco_symbol, (symbol_x, symbol_y))

    pygame.draw.rect(screen, "black", main_rect)
    pygame.draw.rect(screen, "grey", main_rect, border_width)
    title = font.render("Japanese Quiz", True, "white")
    title_rect = title.get_rect(center=main_rect.center)
    screen.blit(title, title_rect)

    pygame.draw.rect(screen, "white", config_rect)
    pygame.draw.rect(screen, "grey", config_rect, 4)
    config_cog_rect = config_cog.get_rect(center=config_rect.center)
    screen.blit(config_cog, config_cog_rect)

    for i, rect in enumerate(menu_rects):
        pygame.draw.rect(screen, "black", rect)
        pygame.draw.rect(screen, "grey", rect, border_width)
        text = font.render(quiz_options[i], True, (255, 255, 255))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    for i in range(len(all_rect_numbers)):
        all_rect_numbers.pop(0)