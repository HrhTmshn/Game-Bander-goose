import random
import os
import sys
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BROWN = 165,42,42

font = pygame.font.SysFont("Verdana", 20)

main_surface = pygame.display.set_mode(screen)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

IMGS_PATH = resource_path('goose')

# player = pygame.Surface((20, 20))
# player.fill(WHITE)
player_imgs = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in os.listdir(IMGS_PATH)]
player = player_imgs[0]
player_rect = player.get_rect()
player_speed = 5

def create_enemy():
    # enemy = pygame.Surface((20, 20))
    # enemy.fill(RED)
    enemy_size = 100, 20
    enemy = pygame.transform.scale(pygame.image.load(resource_path("enemy.png")).convert_alpha(), enemy_size)
    enemy_rect = pygame.Rect(width, random.randint(50, height-50), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

def create_bonus():
    # bonus = pygame.Surface((20, 20))
    # bonus.fill(GREEN)
    bonus_size = 40, 80
    bonus = pygame.transform.scale(pygame.image.load(resource_path("bonus.png")).convert_alpha(), bonus_size)
    bonus_rect = pygame.Rect(random.randint(40, width-40), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]

bg = pygame.transform.scale(pygame.image.load(resource_path("background.png")).convert(), screen)
bgx = 0
bgx2 = bg.get_width()
bg_speed = 3

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)

img_index = 0

scores = 0

enemies = []
bonuses = []

Is_working = True

while Is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            Is_working = False
            
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index == len(player_imgs):
                img_index = 0
            player = player_imgs[img_index]
    
    pressed_keys = pygame.key.get_pressed()
    
    # main_surface.fill(WHITE)
    
    # main_surface.blit(bg, (0, 0))
    
    bgx -= bg_speed
    bgx2 -= bg_speed
    
    if bgx < -bg.get_width():
        bgx = bg.get_width()
    if bgx2 < -bg.get_width():
        bgx2 = bg.get_width()
    
    main_surface.blit(bg, (bgx, 0))
    main_surface.blit(bg, (bgx2, 0))
    
    main_surface.blit(player, player_rect)
    
    main_surface.blit(font.render(str(scores), True, BROWN), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])
        
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if player_rect.colliderect(enemy[1]):
            Is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])
        
        if bonus[1].bottom > height:
            bonuses.pop(bonuses.index(bonus))
        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1
        

    if pressed_keys[K_DOWN] and player_rect.bottom < height:
        player_rect = player_rect.move(0, player_speed)
    if pressed_keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(0, -player_speed)
    if pressed_keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(-player_speed, 0)
    if pressed_keys[K_RIGHT] and player_rect.right < width:
        player_rect = player_rect.move(player_speed, 0)
    
    
    pygame.display.flip()