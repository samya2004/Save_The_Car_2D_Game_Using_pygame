import random
import sys
import pygame
from pygame.locals import *


arr = []
x = []
FPS = 25
SCREENWIDTH = 260
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/car.png'
BACKGROUND1 = 'gallery/sprites/background.png'
BACKGROUND = 'gallery/sprites/road2.jpg'
OPPONENT = 'gallery/sprites/car.png'


def welcomeScreen():

    playerx = int((SCREENWIDTH-GAME_SPRITES['player'].get_width())/2)
    playery = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height()-50)

    while True:
        left, middle, right = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            elif left:
                return
            else:
                SCREEN.blit(GAME_SPRITES['background1'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (-15, 0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def checkCollision(a, b, arr, x):
    width = GAME_SPRITES['player'].get_width()
    height = GAME_SPRITES['player'].get_height()
    for p, q in zip(arr, x):
        if (a <= p <= a+width or a <= p+width <= a+width) and b <= q+height <= b+height:
            GAME_SOUNDS['crash1'].play()
            return True


def mainGame():
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height()-7)
    font = pygame.font.Font(None, 36)
    x1 = -100
    width = GAME_SPRITES['player'].get_width()
    height = GAME_SPRITES['player'].get_height()
    score = 0
    hello = 0
    chu = []
    ku = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_RIGHT):
                if (playerx+width)+30 < 260:
                    playerx += 30
            if event.type == KEYDOWN and (event.key == K_LEFT):
                if playerx-30 > 0:
                    playerx -= 30
            if event.type == KEYDOWN and (event.key == K_UP):
                playery -= 20

        a = random.randint(1, 20)
        a = a*10
        arr.append(a)
        x1 -= 400
        x.append(x1)
        chu.append(hello)

        for p in chu:
            SCREEN.blit(GAME_SPRITES['background'],
                        (0, p))
        i = 0
        for i in range(0, len(chu)):
            chu[i] = chu[i]+15

            i += 1
        hello -= 511

        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        i = 0
        for i in range(0, len(x)):
            x[i] = x[i]+15
            i += 1
        kutta = str(random.randint(0, 3))
        ku.append(kutta)
        for p, q in zip(zip(arr, x), ku):

            SCREEN.blit(GAME_SPRITES['opponent'+q],
                        p)

        abc = False
        abc = checkCollision(playerx, playery, arr, x)
        if abc:

            arr.clear()
            x.clear()
            chu.clear()
            return score
        for i in x:

            if playery+10 < i < playery+30:
                if playery+10 < i:

                    GAME_SOUNDS['point'].play()
                    score += 5

                    break
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        SCREEN.blit(score_text, (10, 10))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gameOver(a):
    font = pygame.font.Font(None, 36)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
            left = pygame.mouse.get_pressed()

            if left:
                return
        playerx = int((SCREENWIDTH-GAME_SPRITES['score'].get_width())/2)
        playery = int((SCREENHEIGHT-GAME_SPRITES['score'].get_height())/2)
        SCREEN.blit(GAME_SPRITES['score'], (playerx, playery+22))
        score_text = font.render(f'{a}', True, (255, 255, 255))

        SCREEN.blit(score_text, (int((SCREENWIDTH-score_text.get_width())/2),
                    int((SCREENHEIGHT-score_text.get_height())/2)))
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()  # Initialize all pygame's modules
    pygame.font.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Save the car -- By Samya')
    GAME_SPRITES['player'] = pygame.image.load(
        'gallery/sprites/car.png').convert_alpha()
    GAME_SPRITES['message'] = pygame.image.load(
        'gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['background'] = pygame.transform.rotate(
        pygame.image.load(BACKGROUND).convert(), 90)
    GAME_SPRITES['background1'] = pygame.image.load(BACKGROUND1).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['score'] = pygame.image.load(
        'gallery/sprites/score.png').convert_alpha()
    GAME_SPRITES['opponent0'] = pygame.image.load(
        'gallery/sprites/car4.png').convert_alpha()
    GAME_SPRITES['opponent1'] = pygame.image.load(
        'gallery/sprites/car1.png').convert_alpha()
    GAME_SPRITES['opponent2'] = pygame.image.load(
        'gallery/sprites/car2.png').convert_alpha()
    GAME_SPRITES['opponent3'] = pygame.image.load(
        'gallery/sprites/car3.png').convert_alpha()

    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.mp3')

    GAME_SOUNDS['crash1'] = pygame.mixer.Sound('gallery/audio/crash1.mp3')

    while True:
        welcomeScreen()  # Shows welcome screen to the user until he presses a button
        a = mainGame()
        gameOver(a)
