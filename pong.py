import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800

WHITE = (255,255,255)

welcomeFontSize = 50
# Must download this file for text.
font = pygame.font.Font('./publicPixel.ttf', welcomeFontSize)
# Welcome text
welcomeText = font.render("Welcome to Pong!", 1, pygame.Color('black'))
welcomeTextW = welcomeText.get_width()
welcomeTextH = welcomeText.get_height()
welcomeTextX = WIDTH//2 - welcomeTextW//2
welcomeTextY = HEIGHT/2 - welcomeTextH*4

startButton = pygame.image.load("./startButton.png")
startButtonW = startButton.get_width()
startButtonH = startButton.get_height()
buttonX = WIDTH//2 - startButtonW//2
buttonY = HEIGHT/2 - startButtonH//2


gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    gameWindow.fill(WHITE)

    # Welcome text
    gameWindow.blit(welcomeText, (welcomeTextX, welcomeTextY))

    # Start button
    gameWindow.blit(startButton, (buttonX,buttonY))
    

    pygame.display.update()
    pygame.event.clear()
