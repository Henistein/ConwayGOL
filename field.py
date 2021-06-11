import pygame

class Field:
  def __init__(self, W, H):
    # Define some colors
    self.WHITE = (255, 255, 255)
    self.GREEN = (0, 255, 0)
    self.GREY = (169, 169, 169)

    self.W = W
    self.H = H
    self.screen = pygame.display.set_mode([W, H])   
    self.clock = pygame.time.Clock()

  def init_pygame(self):
    pygame.init()

  def capture_close(self, event):
    if event.type == pygame.QUIT:
      return False
    else:
      return True
      
  def fill_bg(self):
    self.screen.fill(self.GREY)

  def fps_display_flip(self):
    # Limit to 60 frames per second
    self.clock.tick(60)
    pygame.display.flip()
  
  def quit(self):
    pygame.quit()
