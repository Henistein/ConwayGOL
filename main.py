import time
from cell import Cell, pygame

def neighbors(grid, x, y):
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if grid[x + i][y + j] == 1:
        count += 1

  count -= grid[x][y]
  return count

def gol(grid):
  gs = len(grid) - 1
  newGrid = [[0 for i in range(gs+1)] for j in range(gs+1)]
  for row in range(gs):
    for col in range(gs):
      nb = neighbors(grid, row, col)
      state = grid[row][col]
      # Apply the rules
      if grid[row][col] == 1:
        if (nb < 2) or (nb > 3):
          newGrid[row][col] = 0
        else:
          newGrid[row][col] = 1
      else:
        if nb == 3:
          newGrid[row][col] = 1

  return newGrid.copy()

if __name__ == '__main__':
  # Call cell that inherits field
  cl = Cell(800, 800, 20, 20, 5)

  done = True
  PLAY = False
  while done:
    # Capture keyboard and mouse events
    for event in pygame.event.get():
      done = cl.capture_close(event)
      cl.spawn_cell_mouse(event)
      PLAY = cl.play(event, PLAY)
      cl.reset_grid(event)
    
    cl.fill_bg()
    cl.draw_grid()
    cl.fps_display_flip()

    if PLAY:
      cl.grid = gol(cl.grid)

  cl.quit()
