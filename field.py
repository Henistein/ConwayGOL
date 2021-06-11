import pygame

class Field:
  def __init__(self, W, H):
    pygame.init()
    pygame.display.set_caption('Game of Life')
    # Define some colors
    self.WHITE = (255, 255, 255)
    self.GREEN = (0, 255, 0)
    self.GREY = (169, 169, 169)

    self.W = W
    self.H = H
    self.screen = pygame.display.set_mode([W, H])   
    self.clock = pygame.time.Clock()

  def capture_close(self, event):
    if event.type == pygame.QUIT:
      return False
    else:
      return True

  def play(self, event, PLAY):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        PLAY = True
      if event.key == pygame.K_s:
        PLAY = False
    return PLAY
      
  def fill_bg(self):
    self.screen.fill(self.GREY)

  def fps_display_flip(self):
    # Limit to 30 frames per second
    self.clock.tick(30)
    pygame.display.flip()
  
  def quit(self):
    pygame.quit()
