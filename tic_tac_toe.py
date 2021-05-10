import pygame  
import stats_tick
import pygame.font

pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("tic_tac_toe")
done = False
count=0
temp=[]
class stats():
        def __init__(self):
                self.index_dict={(0,0):(100,100), (0,1):(300,100), (0,2):(500,100),
                                 (1,0):(100,300), (1,1):(300,300), (1,2):(500,300),
                                 (2,0):(100,500), (2,1):(300,500), (2,2):(500,500)}

                self.box_dict={(0,0):(1), (0,1):(2), (0,2):(3),
                               (1,0):(4), (1,1):(5), (1,2):(6),
                               (2,0):(7), (2,1):(8), (2,2):(9)}

        def return_column(self,pos):
                self.pos=pos
                if(self.pos[0]<=200):
                        return(0)
                if(self.pos[0]<=400):
                        return(1)
                if(self.pos[0]<=600):
                        return(2)

        def return_row(self,pos):
                self.pos=pos
                if(self.pos[1]<=200):
                        return(0)
                if(self.pos[1]<=400):
                        return(1)
                if (self.pos[1]<=600):
                        return(2)
        def lines(self):
                pygame.draw.line(screen, (255,255,255), (200,0), (200,600),5)
                pygame.draw.line(screen, (255,255,255), (400,0), (400,600),5)
                pygame.draw.line(screen, (255,255,255), (0,200), (600,200),5)
                pygame.draw.line(screen, (255,255,255), (0,400), (600,400),5)


obj1=stats()
obj2=stats_tick.tik_tak_toe_game()
while not done:
        obj1.lines()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
                        exit()
                        
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                                screen.fill((0,0,0))
                                count=0
                                temp=[]
                                obj2.clear_all()
                                
                if event.type == pygame.MOUSEBUTTONDOWN and (not obj2.check_game_over()):
                        pos =list(pygame.mouse.get_pos())
                        pos1=75
                        column=obj1.return_column(pos)
                        row=obj1.return_row(pos)
                        box=obj1.index_dict[(row,column)]
                        box_num=obj1.box_dict[(row,column)]
                        if (count%2==0) and (box_num not in temp):
                                you_are="o"
                                pygame.draw.circle(screen,(255,255,255),(box[0],box[1]),pos1,5)
                                temp.append(box_num)
                                count+=1
                        if(count%2!=0) and (box_num not in temp):
                                you_are="x"
                                pygame.draw.line(screen,(255,255,255),(box[0]-pos1,box[1]-pos1),(box[0]+pos1,box[1]+pos1),5)
                                pygame.draw.line(screen,(255,255,255),(box[0]-pos1,box[1]+pos1),(box[0]+pos1,box[1]-pos1),5)
                                temp.append(box_num)
                                count+=1
                        obj2.make_move(you_are,box_num)
                        if(obj2.check_game_over()):
                                text = font.render(you_are+" wins", 1, (255, 255, 255))
                                text_box = text.get_rect(centerx=screen.get_width()/2)
                                screen.blit(text, text_box)
        pygame.display.flip()

