import pygame
from pygame.locals import *
import csv
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
pink = (255,105,180)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 1250
Y = 700

questionFile = open('C:\/Users\jklew\OneDrive\Documents\/newlywedquestions.txt', encoding="utf8")
#questions = csv.reader(open('C:\/Users\jklew\OneDrive\Documents\/newlywedquestions.txt'))

questions = []
with open('C:\/Users\jklew\OneDrive\Documents\/newlywedquestions.txt', encoding="utf8") as my_file:
    questions = (my_file.read().split('\n'))

random.shuffle(questions)


display_surface = pygame.display.set_mode((X, Y), FULLSCREEN)

# create a font object.
font = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.TTF', 128)
fontthe = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.TTF', 112)

# create a text suface object,
# on which text is drawn.
text1 = fontthe.render('The', True, pink)
text2 = font.render('Newlydate', True, pink)
text3 = font.render('Game', True, pink)

# create a rectangular object for the
# text surface object
textRect2 = text1.get_rect()

# set the center of the rectangular object.
myRect = Rect((100, 190), (1050, 400))
center_textX = 400
center_textY = 250

display_surface.fill(white)

display_surface.blit(text1, (center_textX, center_textY-80))
display_surface.blit(text2, (center_textX, center_textY))
display_surface.blit(text3, (center_textX+80, center_textY+95))

pygame.display.update()

name1points = 0
name2points = 0
fontthe1 = fontthe
qfont = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 36)
name1score = fontthe1.render(str(name1points), True, white)
name2score = fontthe1.render(str(name2points), True, white)

while True:
    event = pygame.event.wait()
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        key = pygame.key.name(event.key)

        if event.key == K_ESCAPE:
            # deactivates the pygame library
            break;
        else:
            center_textX = 510
            center_textY = 52

            font = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.TTF', 70)
            fontthe = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.TTF', 61)

            text1 = fontthe.render('The', True, black)
            text2 = font.render('Newlydate', True, black)
            text3 = font.render('Game', True, black)

            display_surface.fill(pink)
            pygame.draw.rect(display_surface, white, myRect)
            display_surface.blit((qfont.render("Name 2", True, black)), (20, 12))
            display_surface.blit((qfont.render("Name 1", True, black)), (1115, 12))
            display_surface.blit(name2score, (30, 18))
            display_surface.blit(name1score, (1124, 18))
            display_surface.blit(text1, (center_textX, center_textY - 45))
            display_surface.blit(text2, (center_textX, center_textY))
            display_surface.blit(text3, (center_textX + 42, center_textY + 55))
            pygame.display.update()
            break


pygame.display.update()

counter = 0


while counter < len(questions):

    pygame.display.update()
    event = pygame.event.wait()
    if event.type == (pygame.KEYDOWN):
        display_surface.fill(pink)
        pygame.draw.rect(display_surface, white, myRect)
        key = pygame.key.name(event.key)
        #escape via escape key
        if (event.key == K_ESCAPE):
            pygame.quit()
            quit()
        # add points to name1
        elif key == 'a':
            name1points+= 1
        # add points to name2
        elif key == 'j':
            name2points+= 1

        #draw the question onto the center of the screen
        questText = qfont.render(questions[counter], True, black, white)
        questrect = questText.get_rect()
        questrect.center = (X // 2, Y // 2)

        counter += 1
        display_surface.blit(questText, questrect)


        display_surface.blit((qfont.render("Name 2", True, black)), (20, 12))
        display_surface.blit((qfont.render("Name 1", True, black)), (1115, 12))

        name1score = fontthe1.render(str(name1points), True, white)
        name2score = fontthe1.render(str(name2points), True, white)

        display_surface.blit(name2score, (30, 18))
        display_surface.blit(name1score, (1124, 18))
        display_surface.blit(text1, (center_textX, center_textY - 45))
        display_surface.blit(text2, (center_textX, center_textY))
        display_surface.blit(text3, (center_textX + 42, center_textY + 55))

        # Draw the surface object to the screen.

        pygame.display.update()


