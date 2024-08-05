import pygame
import gameButtons
pygame.init()
window_size = (800, 600)  # Width, Height
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Pygame Window")
button = gameButtons.Tile(300,200)


# Initialize Pygame clock
clock = pygame.time.Clock()

running = True
while running:
   # Limit the frame rate to 60 FPS
   clock.tick(60)
    
   # Handle events
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
        
      # Handle mouse events
      if event.type == pygame.MOUSEBUTTONDOWN:
         mouse_pos = pygame.mouse.get_pos()
         if button.button_rect.collidepoint(mouse_pos):
            print("Button clicked!")
        
      if event.type == pygame.MOUSEMOTION:
         mouse_pos = pygame.mouse.get_pos()
         if button.button_rect.collidepoint(mouse_pos):
            button_color = button.button_hover_color
         else:
            button_color = (255, 255, 255)
    
   # Draw button and clock
   window.fill((128, 128, 128))
   pygame.draw.rect(window, button_color, button.button_rect)
   current_time = pygame.time.get_ticks()
   clock_text = button.button_font.render(f"Time: {current_time/1000:.2f} s", True, (255, 255, 255))
   clock_text_rect = clock_text.get_rect(topright=(780, 10))
   window.blit(clock_text, clock_text_rect)
    
   pygame.display.flip()
pygame.quit()