import pygame
import random
from hiragana import hiradict, hiracombosdict
from katakana import katadict, katacombosdict

pygame.init()

#General configurations
screen = pygame.display.set_mode((1000, 600))
font = pygame.font.Font('fonts/ipaexg.ttf', 36)
return_arrow = pygame.image.load('./assets/ReturnArrow.png')
scaled_arrow = pygame.transform.scale(return_arrow, (90, 50))

#Global variables
correct_rect_index = None
correct_rect_sound = None
chosen_dict = {}
all_rect_numbers = []

#Rectangle configurations
distfromtop = 350
rect_width = 200
rect_height = 150
border_width = 10

#Rectangles to be drawn
main_rect = pygame.Rect(375, 50, 250, 150)
return_rect = pygame.Rect(860, 20, 100, 60)
quiz_rects = [
    pygame.Rect(25, distfromtop, rect_width, rect_height),
    pygame.Rect(275, distfromtop, rect_width, rect_height),
    pygame.Rect(525, distfromtop, rect_width, rect_height),
    pygame.Rect(775, distfromtop, rect_width, rect_height)
]

#Selects a random number within the list's size
def pick_rand_number(symbol_number, param_list_size):
    if param_list_size != 1:
        while True:
            number = random.randrange(param_list_size)
            if number != symbol_number:
                return number
    return 0

#Draws the quiz
def draw_quiz(chosen_quiz):
    global correct_rect_index
    global correct_rect_sound
    global chosen_dict
    match chosen_quiz:
        case 0:
            chosen_dict = hiradict
        case 1:
            chosen_dict = hiracombosdict
        case 2:
            chosen_dict = katadict
        case 3:
            chosen_dict = katacombosdict

    screen.fill([40, 40, 40])
    list_size = len(chosen_dict['symbols'])

    pygame.draw.rect(screen, "black", main_rect)
    pygame.draw.rect(screen, "grey", main_rect, border_width)

    pygame.draw.rect(screen, "white", return_rect)
    pygame.draw.rect(screen, "grey", return_rect, 4)
    arrow_rect = scaled_arrow.get_rect(center=return_rect.center)
    screen.blit(scaled_arrow, arrow_rect)

    chosen_symbol = random.randrange(list_size)
    correct_rect_sound = chosen_symbol

    symbol = font.render(chosen_dict['symbols'].__getitem__(chosen_symbol), True, "white")
    symbol_rect = symbol.get_rect(center=main_rect.center)
    screen.blit(symbol, symbol_rect)

    correct_sound = random.randint(0, 3)
    correct_rect_index = correct_sound

    for i, rect in enumerate(quiz_rects):
        pygame.draw.rect(screen, "black", rect)
        pygame.draw.rect(screen, "grey", rect, border_width)
        if i == correct_sound:
            sound = font.render(chosen_dict['sounds'].__getitem__(chosen_symbol), True, "white")
            all_rect_numbers.append(chosen_symbol)
        else:
            random_sound = pick_rand_number(chosen_symbol, list_size)
            sound = font.render(chosen_dict['sounds'].__getitem__(random_sound), True, "white")
            all_rect_numbers.append(random_sound)

        sound_rect = sound.get_rect(center=rect.center)
        screen.blit(sound, sound_rect)

    pygame.display.flip()

#Draws the result
def draw_result():
    screen.fill([40, 40, 40])

    pygame.draw.rect(screen, "black", main_rect)
    pygame.draw.rect(screen, "grey", main_rect, border_width)

    symbol = font.render(chosen_dict['symbols'].__getitem__(correct_rect_sound), True, "white")
    symbol_rect = symbol.get_rect(center=main_rect.center)
    screen.blit(symbol, symbol_rect)

    for i, rect in enumerate(quiz_rects):
        pygame.draw.rect(screen, "black", rect)
        if i == correct_rect_index:
            sound = font.render(chosen_dict['sounds'].__getitem__(all_rect_numbers[i]), True, "white")
            pygame.draw.rect(screen, "green", rect, border_width)
        else:
            sound = font.render(chosen_dict['sounds'].__getitem__(all_rect_numbers[i]), True, "white")
            pygame.draw.rect(screen, "red", rect, border_width)

        sound_rect = sound.get_rect(center=rect.center)
        screen.blit(sound, sound_rect)

    for i in range(len(all_rect_numbers)):
        all_rect_numbers.pop(0)

    pygame.display.flip()

def get_correct_rect_index():
    return correct_rect_index