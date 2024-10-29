import pygame
from sys import exit
from random import randint
pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 40

BLACK = (0,0,0)
GREEN = (0,240,0)
WHITE = (255,255,255)
# 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Quiz pyGame')
screen.fill(BLACK)
clock = pygame.time.Clock()

class TextArea():
    def __init__(self, x=0,y=0,width=10,height=10,color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color

    def set_text(self,text, fsize=18, text_color=WHITE):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
        

    def draw(self,shift_x=0,shift_y=0):
        pygame.draw.rect(screen,self.fill_color,self.rect)
        screen.blit(self.image,(self.rect.x,self.rect.y))

q_card = TextArea(150, 150,300,100,GREEN)
q_card.set_text("Question", 75)

a_card = TextArea(150, 300,300,100,GREEN)
a_card.set_text("Answer", 75)

q_card.draw(10,10)
a_card.draw(10,10)

while True:
    # clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1,3)
                if num == 1:
                    q_card.set_text("Where is China?")
                elif num == 2:
                    q_card.set_text("What language is spoken in Vietnam?")
                elif num == 3:
                    q_card.set_text("Which country holds the tallest mountain?")

                q_card.draw(10,25)
            elif event.key == pygame.K_a:
                num = randint(1,3)
                if num == 1:
                    a_card.set_text("Asia")
                elif num == 2:
                    a_card.set_text("Vietnamese")
                elif num == 3:
                    a_card.set_text("Nepal & China")
                a_card.draw(10,25)
    
    pygame.display.update()
    clock.tick(FPS)
