import pygame
from field import Field

class Cell(Field):
  def __init__(self, W, H, WIDTH, HEIGHT, MARGIN):
    assert W == H, "Invalid window size"
    assert WIDTH == HEIGHT, "Invalid cell size"

    super().__init__(W, H)
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.MARGIN = MARGIN
    self.GS = W // (MARGIN + WIDTH)
    self.grid = [[0 for i in range(self.GS)] for j in range(self.GS)]

  def spawn_cell_mouse(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      # Change the x/y screen coordinates to grid coordinates
      column = pos[0] // (self.WIDTH + self.MARGIN)
      row = pos[1] // (self.HEIGHT + self.MARGIN)
      # Paint or not that grid position
      if self.grid[row][column] == 1:
        self.grid[row][column] = 0
      else:
        self.grid[row][column] = 1
  
  def draw_grid(self):
    for row in range(self.GS):
      for column in range(self.GS):
        color = self.GREY
        if self.grid[row][column] == 1:
          color = self.GREEN
        pygame.draw.rect(self.screen, color, [(self.MARGIN + self.WIDTH) * column + self.MARGIN, \
                                        (self.MARGIN + self.HEIGHT) * row + self.MARGIN,         \
                                        self.WIDTH,                                              \
                                        self.HEIGHT])

  def reset_grid(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_c:
        self.grid = [[0 for i in range(self.GS)] for j in range(self.GS)]
