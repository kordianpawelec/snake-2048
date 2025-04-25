import pygame
import time
import random


window_x = 720
window_y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


class Snake:
    def __init__(self):
        self.snake_speed = 15
        self.snake_position = [100,50]
        self.snake_body = [ 
                [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
        
        self.direction = 'RIGHT'
        self.change_to = self.direction
        
    
    def set_change_to(self, change_to):
        self.change_to = change_to
        
    def set_direction(self, direction):
        self.direction = direction
        
        
    def directions(self,change_to):
        if change_to == 'UP' and self.direction != 'DOWN':
            self.set_direction('UP')
        if change_to == 'DOWN' and self.direction != 'UP':
            self.set_direction('DOWN')
        if change_to == 'LEFT' and self.direction != 'RIGHT':
            self.set_direction('LEFT')
        if change_to == 'RIGHT' and self.direction != 'LEFT':
            self.set_direction('RIGHT')
            
    def add_segment(self):
            self.snake_body.insert(0, list(self.snake_position))
            
    def check_self_collision(self):
        for block in self.snake_body[1:]:
                if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                    return True
        return False
                   
        
    def moving(self):
        if self.direction == 'UP':
            self.snake_position[1] -= 10
        if self.direction == 'DOWN':
            self.snake_position[1] += 10
        if self.direction == 'LEFT':
            self.snake_position[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_position[0] += 10

        
class Fruit:
    def __init__(self, snake):
        self.fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        self.fruit_spawn = True
        self.snake = snake
        
        
    def fruit_collision_check(self):
        self.snake_position = self.snake.snake_position
        if self.snake_position[0] == self.fruit_position[0] and self.snake_position[1] == self.fruit_position[1]:
            self.fruit_spawn = False
            return True
    
    
    def drop_fruit(self):
            self.fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
            self.fruit_spawn = True


class Score:
    def __init__(self,game_window,colour=white, font='Arial', size=20):
        self.game_window = game_window
        self.colour = colour
        self.score = 0
        self.score_font = pygame.font.SysFont(font, size)
        
        
    def get_surface(self):
        self.score_surface = self.score_font.render('Score : ' + str(self.score), True, self.colour)
        self.score_rect = self.score_surface.get_rect()
        self.game_window.blit(self.score_surface, self.score_rect)
   
    
    def set_score(self):
        self.score += 10
        

class Game_over:
    def __init__(self,game_window,score):
        self.score = score
        self.window = game_window
        self.my_font = pygame.font.SysFont('times new roman', 50)

        
    def update_end(self, score):
        
        self.game_over_surface = self.my_font.render('Your Score is : ' + str(score), True, red)
        self.game_over_rect = self.game_over_surface.get_rect()
        self.game_over_rect.midtop = (window_x/2, window_y/4)
        
        self.window.blit(self.game_over_surface, self.game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()
          

class Play:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake_Game')
        self.game_window = pygame.display.set_mode((window_x,window_y))
        self.fps = pygame.time.Clock()
        self.snake = Snake()
        self.score = Score(self.game_window)
        self.fruit = Fruit(self.snake)
        self.game_over = Game_over(self.game_window, self.score)
        
        
    def start(self): 
        run = True
            
        while run:
            self.game_window.fill(black)
            self.score.get_surface()
            # self.game_window.blit(x, y)
            self.snake.moving()
            
            if self.snake.check_self_collision():
                self.game_over.update_end() 
            
            self.snake.snake_body.insert(0, list(self.snake.snake_position))
            if not self.fruit.fruit_collision_check():  
                self.snake.snake_body.pop()
            else: 
                self.score.set_score()

            if not self.fruit.fruit_spawn:
                self.fruit.drop_fruit()


            if self.snake.snake_body[0][0] > window_x or self.snake.snake_body[0][0] < 0 or self.snake.snake_body[0][1] > window_y or self.snake.snake_body[0][1] < 0:
                self.game_over.update_end(self.score.score)
            
            
            for i, pos in enumerate(self.snake.snake_body):
                if i % 2 == 0:
                    x = red
                else:
                    x = blue
                pygame.draw.rect(self.game_window, x, pygame.Rect(pos[0], pos[1], 10, 10))
                pygame.draw.rect(self.game_window, white, pygame.Rect(self.fruit.fruit_position[0], self.fruit.fruit_position[1], 10, 10))
                
            pos = self.snake.snake_body[0]
            pygame.draw.rect(self.game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.directions('UP')
                    if event.key == pygame.K_DOWN:
                        self.snake.directions("DOWN")

                    if event.key == pygame.K_LEFT:
                        self.snake.directions("LEFT")

                    if event.key == pygame.K_RIGHT:
                        self.snake.directions("RIGHT")

            
            pygame.display.update()
            pygame.time.Clock().tick(15)
            
if __name__ == '__main__':
    
    play = Play()
    play.start()