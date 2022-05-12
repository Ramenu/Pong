# Handles the ball direction and the movement of the ball
import pygame


class Ball:

    # Creates a ball with the given length and width
    def __init__(self, width, height): 
        self.x = width
        self.y = height
        self.hitTop = True
        self.hitBottom = False
        self.direction = True # True for going right, false for going left 

    # Moves the ball in a given direction, TRUE if going right, FALSE if going left
    def moveBall(self):
      self.eraseBall() # Erase the current ball located at (x,y) before drawing the next one so multiple balls aren't drawn

      if self.hitsWall(): # Check to see if a wall is a hit and change the direction if so
        self.direction = not self.direction 
    
      # Adjusts the x-coordinate of the ball, +3 if going right, otherwise -3
      if self.direction:
        self.x += 3
      else:
        self.x -= 3

      # Adjusts the y-coordinate of the ball, if it hits the top it goes down, otherwise it goes up
      if self.hitTop:
        self.y += 3
      else:
        self.y -= 3

      if self.y < 0: # If it hits the top, bounce back to the bottom
        self.hitBottom = False
        self.hitTop = True 
      elif self.y >= 400:
        self.hitTop = False
        self.hitBottom = True

    # Returns true if the ball hits a wall
    def hitsWall(self):
      if self.x >= 400 or self.x <= 0: 
        return True
      return False


    # Draws the ball onto the screen
    def drawBall(self):
      from screen import SCR_SURFACE
      pygame.draw.circle(SCR_SURFACE, (255, 255, 255), (self.x, self.y), 5, 0)
      pygame.time.wait(20)

    # Erases the current ball drawn
    def eraseBall(self):
      from screen import SCR_SURFACE
      pygame.draw.circle(SCR_SURFACE, (0, 0, 0), (self.x, self.y), 5, 0)

    # Bounces the ball in the given direction (should be called iff the ball collides with the wall or paddle)
    def bounce(self, fromPaddle):
      from screen import SCR_WIDTH
      if SCR_WIDTH / 2 <= self.x:
        self.direction = True
      else:
        self.direction = False

      if fromPaddle: # If the collision was with the paddle
        self.hitBottom = True
        self.hitTop = False
        self.direction = not self.direction



    # Returns the x-pos of the ball
    def xPos(self):
      return self.x
    # Returns the y-pos of the ball
    def yPos(self):
      return self.y
    

    

