import pygame

pygame.init()

surface = pygame.display.get_surface()
font = pygame.font.Font('fonts/ipaexg.ttf', 24)
color_dict = {
    0: "red",
    1: "red",
    2: "green",
}

#Rectangle configurations
config_distfromleft = 35
config_rect_W = 250
config_rect_H = 45
feedback_distfromleft = 110
feedback_rect_W = 45
feedback_rect_H = 45

#Rectangles to be drawn
config_screen_rect = pygame.Rect(250, 175, 500, 255)
left_adjust = config_screen_rect[0]
top_adjust = config_screen_rect[1] + 40

configuration_rects = [
    pygame.Rect(config_distfromleft + left_adjust, top_adjust, config_rect_W, config_rect_H),
    pygame.Rect(config_distfromleft + left_adjust, top_adjust + 65, config_rect_W, config_rect_H),
    pygame.Rect(config_distfromleft + left_adjust, top_adjust + 130, config_rect_W, config_rect_H),
]
left_adjust += config_rect_W
left_adjust += feedback_rect_W
left_adjust += 10

feedback_rects = [
    pygame.Rect(left_adjust, top_adjust, feedback_rect_W, feedback_rect_H),
    pygame.Rect(left_adjust, top_adjust + 65, feedback_rect_W, feedback_rect_H),
    pygame.Rect(left_adjust, top_adjust + 130, feedback_rect_W, feedback_rect_H),
]

def draw_config(update=None):
    global color_dict
    pygame.draw.rect(surface,(40, 40, 40), config_screen_rect)
    pygame.draw.rect(surface,(80, 80, 80), config_screen_rect, 10)

    for i, rect in enumerate(configuration_rects):
        pygame.draw.rect(surface, "white", rect)

    if update is not None:
        if color_dict[update] == "red":
            color_dict[update] = "green"
        else:
            color_dict[update] = "red"

    left_margin = left_adjust + 23
    top_margin = top_adjust + 23
    for i, rect in enumerate(feedback_rects):
        pygame.draw.circle(surface, color_dict[i], (left_margin, top_margin), 25)
        top_margin += 65

    config1 = configuration_rects[0]
    config2 = configuration_rects[1]
    config3 = configuration_rects[2]

    config1_text = font.render("Practice Mode", True, "black")
    config1_text_rect = config1_text.get_rect(center=config1.center)
    surface.blit(config1_text, config1_text_rect)

    config2_text = font.render("Infinite Quiz", True, "black")
    config2_text_rect = config2_text.get_rect(center=config2.center)
    surface.blit(config2_text, config2_text_rect)

    config3_text = font.render("Timed Quiz", True, "black")
    config3_text_rect = config3_text.get_rect(center=config3.center)
    surface.blit(config3_text, config3_text_rect)

    pygame.display.flip()