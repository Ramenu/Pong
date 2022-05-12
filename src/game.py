# Initializes pygame and the Pong game itself

import pygame
import screen
import ball
import paddle
import time

class Game:
    def __init__(self, x, y):
        pygame.init()
        pygame.font.init()
        screen.initScreen(x, y)
        self.pad = paddle.Paddle(screen.SCR_WIDTH / 2, screen.SCR_HEIGHT - 5) # Draws the rectangle at the specified coordinates
        self.font = pygame.font.Font("./font/Minecraft.ttf", 32)
        self.score = 0
        self.scoreText = self.font.render(str(self.score), True, (255, 255, 255))

    # Starts the game
    def start(self):
        pygame.display.set_caption("Pong")
        pongIcon = pygame.image.load("./icon/icon.jpg") # Load the icon as a surface
        pygame.display.set_icon(pongIcon)
        # Allows for holding down keys, First argument is the # of milliseconds before the first keydown is sent, second is the interval
        pygame.key.set_repeat(1, 75) 
        pygame.mixer.music.load("./sounds/hit.wav")
        pongBall = ball.Ball(200, 50) # Creates the ball starting point at the (x,y) coordinates specified
        while True:
            self.pad.drawPaddle()
            pongBall.moveBall()
            pongBall.drawBall()
            if pongBall.yPos() + 7 >= self.pad.yPos(): # Check if the ball reaches the y-pos of the paddle
                if self.pad.collides(pongBall.xPos()): # Check if the paddle collides with the ball
                    pygame.mixer.music.play(-1)
                    time.sleep(0.05)
                    pongBall.bounce(True)
                    self.score += 1 # Score +1 for each ball hit
                    pygame.mixer.music.stop()
                else: # Quit game if the paddle fails to collide with the ball
                    Game.gameOver()
            self.displayScore()
            pygame.display.flip()
            self.readKeyboard() 
    
    # Reads input from the keyboard
    def readKeyboard(self):
        from screen import SCR_WIDTH
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # If "ESC" key is pressed, exit the game
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_RIGHT and self.pad.xPos() + 53 < SCR_WIDTH:
                    self.pad.movePaddle(True) # Move paddle to the right
                elif event.key == pygame.K_LEFT and self.pad.xPos() > 0: 
                    self.pad.movePaddle(False) # Move paddle to the left

    # Displays the current score of the player, second argument specifies to erase the score which should be done before drawing the next one
    def displayScore(self):
        from screen import SCR_SURFACE
        SCR_SURFACE.fill((0, 0, 0), (0, 0, 40, 40)) # Remove the previous score
        self.scoreText = self.font.render(str(self.score), True, (255, 255, 255))
        SCR_SURFACE.blit(self.scoreText, self.scoreText.get_rect())
    
    # Shows the game over screen before exitting the game
    def gameOver():
        from screen import SCR_SURFACE, SCR_HEIGHT, SCR_WIDTH
        pygame.mixer.music.unload()
        pygame.mixer.music.load("sounds/gameover.wav")
        SCR_SURFACE.fill((0, 0, 0))
        gameOverFont = pygame.font.Font("font/Minecraft.ttf", 40)
        gameOver = gameOverFont.render("GAME OVER", True, (255, 255, 255))
        gameOverRect = gameOver.get_rect()
        gameOverRect.center = (SCR_WIDTH / 2, SCR_HEIGHT / 2)
        SCR_SURFACE.blit(gameOver, gameOverRect)
        pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(1)
        pygame.mixer.music.stop()
        pygame.quit()
        quit()


        





