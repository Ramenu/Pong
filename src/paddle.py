# Paddle
import pygame

class Paddle:
    # Creates a x by y rectangle which represents the paddle
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Draws the paddle
    def drawPaddle(self):
        from screen import SCR_SURFACE
        pygame.draw.rect(SCR_SURFACE, (255, 255, 255), pygame.Rect((self.x, self.y), (50, 395)))
    
    # Moves the paddle left or right
    def movePaddle(self, direction):
        self.erasePaddle() # Erase the current paddle located at (x,y) before drawing the next one so multiple paddles aren't drawn

        if direction:
            self.x += 5 # Moves the paddle to the right if direction == true
        else:
            self.x -= 5 # Moves the paddle to the left otherwise

    # Erases the paddles at the current position
    def erasePaddle(self):
        from screen import SCR_SURFACE
        pygame.draw.rect(SCR_SURFACE, (0, 0, 0), pygame.Rect((self.x, self.y), (50, 395)))

    # Returns the x-pos of the paddle
    def xPos(self):
        return self.x
    
    # Returns the y-pos of the paddle (always a fixed constant)
    def yPos(self):
        return self.y
    
    
    # Checks if the ball collides with the paddle, returns true if so
    def collides(self, ballX):
        if ballX >= self.x and ballX <= self.x + 50:
            return True
        return False
        
        


        


    
        

    
