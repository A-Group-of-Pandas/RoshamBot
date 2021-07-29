import pygame

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('RoshamBot!')

black = (0,0,0)
white = (255,255,255)

red = (200, 0, 0)
bright_red = (255, 0, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

green = (0, 200, 0)
bright_green = (0, 255, 0)

title = "RoshamBot!"

clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects(title, largeText)
        TextRect.center = ((display_width/2),(display_height-400))
        gameDisplay.blit(TextSurf, TextRect)

        if 150+100 > mouse[0] > 150 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(gameDisplay, bright_green,(150,300,100,50))
        else:
            pygame.draw.rect(gameDisplay, green,(150,300,100,50))

        if 350+100 > mouse[0] > 350 and 350+50 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, bright_blue, (350, 350,100,50))
        else:
            pygame.draw.rect(gameDisplay, blue, (350, 400,100,50))

        if 550+100 > mouse[0] > 550 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(gameDisplay, bright_red, (550, 300, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (550, 300, 100, 50))
        
        # pygame.draw.rect(gameDisplay, red, (550, 300,100,50))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("START!", smallText)
        textRect.center = ((150+(100/2)), (300+(50/2)))
        gameDisplay.blit(textSurf, textRect)
            
        #pygame.draw.rect(gameDisplay, red,(550,450,100,50))
        
        pygame.display.update()
        clock.tick(60)

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    game_intro()
        
    # pygame.display.update()
    # clock.tick(60)

        
pygame.quit()
quit()