import pygame
from quizbuilder import all_rect_numbers

pygame.init()
screen = pygame.display.set_mode((1000, 600))
font = pygame.font.Font('fonts/ipaexg.ttf', 36)

quiz_options = ["Hiragana", "Hiragana\n Combos", "Katakana", "Katakana\n Combos"]

dist_from_top = 400
rect_width = 180
rect_height = 140
border_width = 10

main_rect = pygame.Rect(300, 50, 400, 200)
menu_rects = [
    pygame.Rect(80, dist_from_top, rect_width, rect_height),
    pygame.Rect(300, dist_from_top, rect_width, rect_height),
    pygame.Rect(520, dist_from_top, rect_width, rect_height),
    pygame.Rect(740, dist_from_top, rect_width, rect_height)
]

def draw_menu():
    screen.fill("white")

    pygame.draw.rect(screen, "black", main_rect)
    pygame.draw.rect(screen, "grey", main_rect, border_width)
    title = font.render("Japanese Quiz", True, "white")
    title_rect = title.get_rect(center=main_rect.center)
    screen.blit(title, title_rect)

    for i, rect in enumerate(menu_rects):
        pygame.draw.rect(screen, "black", rect)
        pygame.draw.rect(screen, "grey", rect, border_width)
        text = font.render(quiz_options[i], True, (255, 255, 255))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    for i in range(len(all_rect_numbers)):
        all_rect_numbers.pop(0)