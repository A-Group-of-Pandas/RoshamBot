import pygame
import sys
pygame.init()
pygame.font.init() 
display_width = 800
display_height = 600

title = "RoshamBot!"
instr_title = "Instructions"

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(title)

#colors
black = (0,0,0)
coral = (204,229,255)
light_pink = (255, 204, 255)
hot_pink = (255, 102, 255)
light_green = (204, 255, 209)
mint_green = (51, 255, 153)
light_red = (255, 204, 204)
warm_red = (255, 102, 102)

clock = pygame.time.Clock()

#text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
                
        gameDisplay.fill(coral)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects(title, largeText)
        TextRect.center = ((display_width/2),(display_height-400))
        gameDisplay.blit(TextSurf, TextRect)

        button('Help', 350, 400, 100, 50, hot_pink, light_pink,action=instructions)
        button('Quit', 150, 300, 100, 50, warm_red, light_red, action=quit_game)
        button('Start!', 550, 300, 100, 50, mint_green, light_green, action=game_loop)

        pygame.display.update()
        clock.tick(60)

def game_loop():
    main_game = True
    while main_game:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(light_green)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        smallText = pygame.font.SysFont("freesansbold.ttf",26)
        TextSurf, TextRect = text_objects("Get ready!", largeText)
        TextRect.center = ((display_width/2),(display_height-550))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Hold up your choice in front of the webcam, which will come on this screen.", smallText)
        TextRect.center = ((display_width/2),(display_height-150))
        gameDisplay.blit(TextSurf, TextRect)
        button('Quit', 450, 525, 100, 50, warm_red, light_red, action=quit_game)
        button("Go Back", 600, 525, 100, 50, hot_pink, light_pink, action=game_intro)
        pygame.display.update()


def quit_game():
    pygame.quit()

def instructions():    
    #displays the color and text.
    main_game = True
    while main_game:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(light_pink)
        mouse = pygame.mouse.get_pos()      
        
        smallText = pygame.font.SysFont("freesansbold.ttf",26)
        largeText = pygame.font.Font('freesansbold.ttf', 50)

        TextSurf, TextRect = text_objects("Instructions:", largeText)
        TextRect.center = ((display_width/2),(display_height-525))
        gameDisplay.blit(TextSurf, TextRect)
        # pygame.display.update()

        TextSurf, TextRect = text_objects("To play, make either a rock, paper, or scissors out of your fist.", smallText)
        TextRect.center = ((display_width/2),(display_height-350))
        gameDisplay.blit(TextSurf, TextRect)
        #pygame.display.update()
        
        TextSurf, TextRect = text_objects("To make a rock, clench your fist into a ball.", smallText)
        TextRect.center = ((display_width/2),(display_height-310))
        gameDisplay.blit(TextSurf, TextRect)
        #pygame.display.update()

        TextSurf, TextRect = text_objects("To make paper, flatten your hand and hold it vertically.", smallText)
        TextRect.center = ((display_width/2),(display_height-270))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("To make scissors, hold up two fingers.", smallText)
        TextRect.center = ((display_width/2),(display_height-230))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Hold this up in front of the camera.", smallText)
        TextRect.center = ((display_width/2),(display_height-190))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("The CPU will also hold out either rock/paper/scissors", smallText)
        TextRect.center = ((display_width/2),(display_height-150))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Scissors beats Paper, Rock beats Scissors, Paper beats Rock.", smallText)
        TextRect.center = ((display_width/2),(display_height-110))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Your score will be displayed at the bottom of the screen. Good luck!", smallText)
        TextRect.center = ((display_width/2),(display_height-70))
        gameDisplay.blit(TextSurf, TextRect)

        button("Go Back", 600, 550, 100, 50, warm_red, light_red, action=game_intro)
        pygame.display.update()


        # text_list = ["Choose either rock, paper, or scissors.", "Make a rock by clenching your fist",
        #     "You can make paper by flattening your palm.", "Finally, hold up two fingers to make scissors."]
        # for x in text_list:
        #     for i in [500, 450, 400, 350]:
        #         mediumText = pygame.font.Font('freesansbold.ttf', 20)
        #         TextSurf, TextRect = text_objects(text_list[x], mediumText)
        #         TextRect.center = ((display_width/2),(display_height-i))
        #         gameDisplay.blit(TextSurf, TextRect)
        #         pygame.display.update()
        

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