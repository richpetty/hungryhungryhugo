import pygame
import random
from random import randint, choice

#pygame setup
screen = pygame.display.set_mode((1280,720))
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

hugo_img = pygame.image.load("hugo.bmp")
hugo_rect = hugo_img.get_rect()

remy_img = pygame.image.load("remy.bmp")
remy_rect = remy_img.get_rect()

dreamies_img = pygame.image.load("dreamies.bmp")
dreamies_rect = dreamies_img.get_rect()


meow_sound = pygame.mixer.Sound("meow.wav")
crunch_sound = pygame.mixer.Sound("crunch.wav")
fanfare_sound = pygame.mixer.Sound("fanfare.wav")


remy_direction_x = 1
remy_direction_y = 1
random_remy_x=1
random_remy_y=1

white = (255,255,255)


dreamies_direction_x = 1
dreamies_direction_y = 1
random_dreamies_x=1
random_dreamies_y=1

score = 0
score_increment = 10

running = True
dt = 0
rt = 0

hugo_rect.centerx = screen.get_width()/2
hugo_rect.centery = screen.get_height()/2

remy_rect.centerx = screen.get_width()/2
remy_rect.centery = screen.get_height()/2

dreamies_rect.centerx = screen.get_width()/2
dreamies_rect.centery = screen.get_height()/2

while running:
    font = pygame.font.Font(None, 36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    screen.blit(hugo_img,hugo_rect)
    screen.blit(remy_img,remy_rect)
    screen.blit(dreamies_img,dreamies_rect)



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
    if keys[pygame.K_w] and hugo_rect.centery>0:
        hugo_rect.centery -= 300*dt
    if keys[pygame.K_s] and hugo_rect.centery<720:
        hugo_rect.centery += 300*dt
    if keys[pygame.K_a] and hugo_rect.centerx>0:
        hugo_rect.centerx -= 300*dt
    if keys[pygame.K_d] and hugo_rect.centerx<1280:
        hugo_rect.centerx += 300*dt


    remy_rect.centery += remy_direction_y*300*rt*random_remy_x
    remy_rect.centerx += remy_direction_x*300*rt*random_remy_y
    if remy_rect.centery <= 100:
        remy_rect.centery = 100
        remy_direction_y *= -1
        random_remy_y = random.choice([-1.25,-1.5,-2,1.25,1.5,2])
    if remy_rect.centery > 620:
        remy_rect.centery = 620
        remy_direction_y *= -1
        random_remy_y = random.choice([-1.25,-1.5,-2,1.25,1.5,2])

    if remy_rect.centerx < 100:
        remy_rect.centerx = 100
        remy_direction_x *= -1
        random_remy_x = random.choice([-1.25,-1.5,-2,1.25,1.5,2])

    if remy_rect.centerx > 1180:
        remy_rect.centerx = 1180
        remy_direction_x *= -1
        random_remy_x = random.choice([-1.25,-1.5,-2,1.25,1.5,2])






    dreamies_rect.centery += dreamies_direction_y*300*dt*random_dreamies_x
    dreamies_rect.centerx += dreamies_direction_x*300*dt*random_dreamies_y
    if dreamies_rect.centery <= 100:
        dreamies_rect.centery = 100
        dreamies_direction_y *= -1
        random_dreamies_y = random.choice([-1.25,-1.5,-2,1.25,1.5,2])
    if dreamies_rect.centery > 620:
        dreamies_rect.centery = 620
        dreamies_direction_y *= -1
        dreamies_dreamies_y = random.choice([-1.25,-1.5,-2,1.25,1.5,2])

    if dreamies_rect.centerx < 100:
        dreamies_rect.centerx = 100
        dreamies_direction_x *= -1
        random_dreamies_x = random.choice([-1.25,-1.5,-2,1.25,1.5,2])

    if dreamies_rect.centerx > 1180:
        dreamies_rect.centerx = 1180
        dreamies_direction_x *= -1
        random_dreamies_x = random.choice([-1.25,-1.5,-2,1.25,1.5,2])

    if hugo_rect.colliderect(remy_rect):
        score -= score_increment
        pygame.mixer.Sound.play(meow_sound)
    if hugo_rect.colliderect(dreamies_rect):
        score += score_increment
        pygame.mixer.Sound.play(crunch_sound)



    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10,10))
    pygame.display.flip()

    rt = clock.tick(60)/1000
    dt = rt

pygame.quit()
