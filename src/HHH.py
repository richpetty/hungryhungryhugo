import random
from random import randint, choice

import pygame

from utils import Image, fetch_sound


#pygame setup
screen = pygame.display.set_mode((1280,720))
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()


hugo = Image("hugo.bmp")
remy = Image("remy.bmp")
dreamies = Image("dreamies.bmp")


meow_sound = fetch_sound("meow.wav")
crunch_sound = fetch_sound("crunch.wav")
fanfare_sound = fetch_sound("fanfare.wav")

white = (255,255,255)

score = 0
score_increment = 10

running = True
dt = 0
rt = 0


hugo.reset_position(screen)
remy.reset_position(screen)
dreamies.reset_position(screen)


while running:
    font = pygame.font.Font(None, 36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    screen.blit(hugo.img, hugo.rect)
    screen.blit(remy.img, remy.rect)
    screen.blit(dreamies.img, dreamies.rect)


    rt = dt
    if score > 1000:
      rt = rt*1.5
    if score > 2000:
        rt = rt*1.5
    if score > 3000:
        rt = rt *1.5
    if score > 4000:
        rt = rt *1.5
    if score > 5000:
        rt = rt *1.5
    if score > 5000:
        font = pygame.font.SysFont("Arial", 72)
        txtsurf = font.render("You Win", True, white)
        screen.blit(txtsurf,(640 - txtsurf.get_width() // 2, 360 - txtsurf.get_height() // 2))
        dt = 0
        rt = 0
        pygame.mixer.Sound.play(fanfare_sound)
        score_increment = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and hugo.rect.centery>0:
        hugo.rect.centery -= 300*dt
    if keys[pygame.K_s] and hugo.rect.centery<720:
        hugo.rect.centery += 300*dt
    if keys[pygame.K_a] and hugo.rect.centerx>0:
        hugo.rect.centerx -= 300*dt
    if keys[pygame.K_d] and hugo.rect.centerx<1280:
        hugo.rect.centerx += 300*dt


    remy.move(rt)
    remy.bound_image()

    dreamies.move(rt)
    dreamies.bound_image()

    if hugo.rect.colliderect(remy.rect):
        score -= score_increment
        pygame.mixer.Sound.play(meow_sound)
    if hugo.rect.colliderect(dreamies.rect):
        score += score_increment
        pygame.mixer.Sound.play(crunch_sound)



    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10,10))
    pygame.display.flip()

    rt = clock.tick(60)/1000
    dt = rt

pygame.quit()
