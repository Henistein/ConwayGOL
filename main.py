from cell import Cell, pygame

if __name__ == '__main__':

  # Call cell that inherits field
  cl = Cell(600, 600, 20, 20, 5)
  cl.init_pygame()    

  done = True
  while done:
    for event in pygame.event.get():
      done = cl.capture_close(event)
      cl.spawn_cell_mouse(event)
    cl.fill_bg()
    cl.draw_grid()
    cl.fps_display_flip()

  cl.quit()
