import pygame
from cube import Cube
from os import environ
from sys import exit

FPS = 90
SIZE_X = 800
SIZE_Y = 600
IMG_NAME = "cube.png"
FONT_COLOR = (255,255,255)
BACK_COLOR = (0,0,0)

#init
environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()
pygame.display.set_caption("Rubik Cube")
cube = Cube(120)
#setting the GUI
screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
cube.get_image().save(IMG_NAME)
img = pygame.image.load(IMG_NAME)
screen.blit(img,((SIZE_X - img.get_width()) / 2,\
                    (SIZE_Y - img.get_height()) / 4))
#buttons
font = pygame.font.SysFont("Papyrus", 48)
#left
left = font.render("L", True, FONT_COLOR, BACK_COLOR)
padd = (SIZE_X - left.get_width() * 6) / 7
rect_left = screen.blit(left, (padd, SIZE_Y * 8/10))
left_ = font.render("L'", True, FONT_COLOR, BACK_COLOR)
rect_left_ = screen.blit(left_, (padd, SIZE_Y * 9/10))
#right
right = font.render("R", True, FONT_COLOR, BACK_COLOR)
rect_right = screen.blit(right, (padd * 2, SIZE_Y * 8/10))
right_ = font.render("R'", True, FONT_COLOR, BACK_COLOR)
rect_right_ = screen.blit(right_, (padd * 2, SIZE_Y * 9/10))
#up
up = font.render("U", True, FONT_COLOR, BACK_COLOR)
rect_up = screen.blit(up, (padd * 3, SIZE_Y * 8/10))
up_ = font.render("U'", True, FONT_COLOR, BACK_COLOR)
rect_up_ = screen.blit(up_, (padd * 3, SIZE_Y * 9/10))
#down
down = font.render("D", True, FONT_COLOR, BACK_COLOR)
rect_down = screen.blit(down, (padd * 4, SIZE_Y * 8/10))
down_ = font.render("D'", True, FONT_COLOR, BACK_COLOR)
rect_down_ = screen.blit(down_, (padd * 4, SIZE_Y * 9/10))
#front
front = font.render("F", True, FONT_COLOR, BACK_COLOR)
rect_front = screen.blit(front, (padd * 5, SIZE_Y * 8/10))
front_ = font.render("F'", True, FONT_COLOR, BACK_COLOR)
rect_front_ = screen.blit(front_, (padd * 5, SIZE_Y * 9/10))
#back
back = font.render("B", True, FONT_COLOR, BACK_COLOR)
rect_back = screen.blit(back, (padd * 6, SIZE_Y * 8/10))
back_ = font.render("B'", True, FONT_COLOR, BACK_COLOR)
rect_back_ = screen.blit(back_, (padd * 6, SIZE_Y * 9/10))

pygame.display.flip()


clock = pygame.time.Clock()
while True:
    clock.tick(FPS)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#LEFT BUTTON
        if rect_left.collidepoint(event.pos):
            cube.l()
        elif rect_left_.collidepoint(event.pos):
            cube.l_()
        elif rect_right.collidepoint(event.pos):
            cube.r()
        elif rect_right_.collidepoint(event.pos):
            cube.r_()
        elif rect_up.collidepoint(event.pos):
            cube.u()
        elif rect_up_.collidepoint(event.pos):
            cube.u_()
        elif rect_down.collidepoint(event.pos):
            cube.d()
        elif rect_down_.collidepoint(event.pos):
            cube.d_()
        elif rect_front.collidepoint(event.pos):
            cube.f()
        elif rect_front_.collidepoint(event.pos):
            cube.f_()
        elif rect_back.collidepoint(event.pos):
            cube.b()
        elif rect_back_.collidepoint(event.pos):
            cube.b_()


    cube.get_image().save(IMG_NAME)
    img = pygame.image.load(IMG_NAME)
    screen.blit(img,((SIZE_X - img.get_width()) / 2,\
                        (SIZE_Y - img.get_height()) / 4))
    pygame.display.flip()
