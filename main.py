import pygame
import math
from colorsys import hsv_to_rgb

# ---------- INIT ----------
pygame.init()
WIDTH, HEIGHT = 1500, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced 3D Abstract Motion | Sukuna")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
cx, cy = WIDTH // 2, HEIGHT // 2

t = 0
running = True

# ---------- MAIN LOOP ----------
while running:
    clock.tick(60)

    # fade instead of clear (cinematic trail)
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.set_alpha(25)
    fade.fill(BLACK)
    screen.blit(fade, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  MULTI-LAYER 3D CURVES
    for layer in range(4):
        for i in range(160):
            z = (i + layer * 40) * 0.015
            depth = 1 / (z + 0.6)

            # Lissajous motion (ADVANCED LOOK)
            x3d = math.sin(t * 0.01 + i * 0.08 + layer) * 400
            y3d = math.sin(t * 0.013 + i * 0.11) * 260

            x = int(cx + x3d * depth)
            y = int(cy + y3d * depth)

            size = int(14 * depth) + 2

            hue = (i * 0.01 + layer * 0.2 + t * 0.002) % 1
            r, g, b = hsv_to_rgb(hue, 0.9, 1)
            color = (int(r*255), int(g*255), int(b*255))

            pygame.draw.circle(screen, color, (x, y), size)

    t += 1
    pygame.display.flip()

pygame.quit()
