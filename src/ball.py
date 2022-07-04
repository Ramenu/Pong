# Handles the ball direction and the movement of the ball
import pygame
import direction


class Ball:

    # Creates a ball with the given length and width
    def __init__(self, width, height): 
        self.x = width
        self.y = height
        self.hitTop = True
        self.direction = direction.getRandDirection() # True for going right, false for going left 

    def moveBall(self, score):
      SPEED_MAX = 3
      speedRate = 0.1 * score
      speed = 3 + min(SPEED_MAX, speedRate)

      self.eraseBall() # Erase the current ball located at (x,y) before drawing the next one so multiple balls aren't drawn

      if self.hitsWall(): # Check to see if a wall is a hit and change the direction if so
        self.direction = not self.direction 
    
      # Adjusts the x-coordinate of the ball, +3 if going right, otherwise -3
      if self.direction == direction.RIGHT:
        self.x += speed
      else:
        self.x -= speed

      # Adjusts the y-coordinate of the ball, if it hits the top it goes down, otherwise it goes up
      if self.hitTop:
        self.y += speed
      else:
        self.y -= speed

    # If it hits the top, bounce back to the bottom
      if self.y < 0: 
        self.hitTop = True 
      elif self.y >= 400:
        self.hitTop = False

    # Returns true if the ball hits a wall
    def hitsWall(self):
      return self.x >= 400 or self.x <= 0


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
        self.direction = direction.RIGHT
      else:
        self.direction = direction.LEFT

    # If the collision was with the paddle
      if fromPaddle: 
        self.hitBottom = True
        self.hitTop = False
        self.direction = direction.getRandDirection()



    # Returns the x-pos of the ball
    def xPos(self):
      return self.x
    # Returns the y-pos of the ball
    def yPos(self):
      return self.y
    

    

