import pygame

pygame.mixer.init()
menu_click = pygame.mixer.Sound("./sounds/menuclick.mp3")
correct_guess = pygame.mixer.Sound("./sounds/correctsound.mp3")
return_sound = pygame.mixer.Sound("./sounds/returnsound.mp3")
wrong_guess = pygame.mixer.Sound("./sounds/wrongsound.mp3")