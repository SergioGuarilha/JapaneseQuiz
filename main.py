import pygame
from menu import draw_menu, menu_rects, config_rect
from quizbuilder import draw_rand_quiz, draw_result, quiz_rects, return_rect, get_correct_rect_index
from configscreen import draw_config, config_screen_rect, feedback_rects
from audios import menu_click, return_sound, correct_guess, wrong_guess

if __name__ =='__main__':
    #state variables
    on_result_screen = False
    on_menu_screen = True
    on_config_screen = False

    #config variables
    add_deco = True
    current_quiz = None

    #draw initial screen
    draw_menu(add_deco)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and on_menu_screen:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(menu_rects):
                    if rect.collidepoint(mouse_pos) and not on_config_screen:
                        pygame.mixer.Sound.play(menu_click)
                        current_quiz = i
                        draw_rand_quiz(i)
                        on_menu_screen = False
                if config_rect.collidepoint(mouse_pos):
                    pygame.mixer.Sound.play(menu_click)
                    draw_config()
                    on_config_screen = True
                elif not config_screen_rect.collidepoint(mouse_pos) and on_config_screen:
                    draw_menu()
                    on_config_screen = False
                elif on_config_screen:
                    for i, rect in enumerate(feedback_rects):
                        if rect.collidepoint(mouse_pos):
                            draw_config(i)

            elif event.type == pygame.MOUSEBUTTONDOWN and not on_result_screen:
                mouse_pos = pygame.mouse.get_pos()
                if return_rect.collidepoint(mouse_pos):
                    pygame.mixer.Sound.play(return_sound)
                    draw_menu(add_deco)
                    on_menu_screen = True
                for i, rect in enumerate(quiz_rects):
                    if rect.collidepoint(mouse_pos):
                        draw_result()
                        on_result_screen = True
                        if i == get_correct_rect_index():
                            pygame.mixer.Sound.play(correct_guess)
                        else:
                            pygame.mixer.Sound.play(wrong_guess)

            elif event.type == pygame.MOUSEBUTTONDOWN and on_result_screen:
                mouse_pos = pygame.mouse.get_pos()
                draw_rand_quiz(current_quiz)
                on_result_screen = False

    pygame.quit()