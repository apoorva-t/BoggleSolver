#!/usr/bin/python
import sys
import pygame
clock = pygame.time.Clock()

def text_wrap(screen, solnList, startCoord):
    GREEN = (0,255,0)
    font_new = pygame.font.SysFont('Comic Sans', 16, True, False)
    text = font_new.render(str(solnList), True, GREEN)
    screen.blit(text, startCoord) 
    
def run_disp(BoggleBoard, solnList):
	#Create screen object
    pygame.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Let's Boggle")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        RED = (255,0,0)
        YELLOW = (255,255,0)
        GREEN = (0,255,0)
        screen.fill(BLACK)
        #pygame.draw.rect(screen, YELLOW, [20,20,40,40])
        #pygame.draw.rect(screen, YELLOW, [65,20,40,40])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        rows = BoggleBoard.BoardSize
        MARGIN = 5
        SIZE = 40
        for r in range(rows):
            for c in range(rows):
                pygame.draw.rect(screen, YELLOW, [(r*(SIZE+MARGIN))+MARGIN, 
                                                  (c*(SIZE+MARGIN))+MARGIN,
                                                  SIZE, SIZE])
                str1 = BoggleBoard.matrix[r][c]
                text = font.render(str1, True, BLACK)
                pos1 = r*(SIZE+MARGIN) + (SIZE/2) - (MARGIN/2)
                pos2 = c*(SIZE+MARGIN) + (SIZE/2) - (MARGIN/2)
                screen.blit(text,[pos1,pos2])
       
        text_wrap(screen, solnList, [MARGIN, (rows+1)*SIZE])
        
        pygame.display.flip()
        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(60)
        #pygame.quit()