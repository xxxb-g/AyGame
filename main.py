# All rights reserved for now.
import time

import pygame
# Initialize Pygame
pygame.init()

# Setup colors
BLAU  = ( 0, 0, 255)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
ORANGE = ( 255, 204, 51 )
Farben = [BLAU, ROT, GRUEN, SCHWARZ, WEISS, ORANGE]

def komplementaerfarbe(rgb):
    komplement = tuple(255 - n for n in rgb)
    return komplement

Fensterbreite = 800
Fensterhöhe = 600

# Set up the game window
screen = pygame.display.set_mode((Fensterbreite, Fensterhöhe))
clock = pygame.time.Clock()
# Versuche eine andere Schriftart
font = pygame.font.SysFont('freesans', 48)
color = 4

# Spieler-Eigenschaften
spieler_breite = 50
spieler_höhe = 50
spieler_x = Fensterbreite // 2 - spieler_breite // 2
spieler_y = Fensterhöhe // 2 - spieler_höhe // 2
spieler_geschwindigkeit = 1.25
spieler_herzen = 5
herzen = spieler_herzen

gegner_breite = 50
gegner_höhe = 50
gegner_x = 0
gegner_y = 0
gegner_geschwindigkeit = 0.375
letzerschaden = float(time.time())

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                if color >= len(Farben)-1:
                    color = 0
                else:
                    color += 1

    # Spieler-Bewegung mit WASD
    Tasten = pygame.key.get_pressed()
    if Tasten[pygame.K_a] or Tasten[pygame.K_LEFT]:
        spieler_x -= spieler_geschwindigkeit
    if Tasten[pygame.K_d] or Tasten[pygame.K_RIGHT]:
        spieler_x += spieler_geschwindigkeit
    if Tasten[pygame.K_w] or Tasten[pygame.K_UP]:
        spieler_y -= spieler_geschwindigkeit
    if Tasten[pygame.K_s] or Tasten[pygame.K_DOWN]:
        spieler_y += spieler_geschwindigkeit

    #Gegner-Bewegung mit Algorithmus
    if spieler_x > gegner_x:
        gegner_x += gegner_geschwindigkeit
    if spieler_x < gegner_x:
        gegner_x -= gegner_geschwindigkeit
    if spieler_y > gegner_y:
        gegner_y += gegner_geschwindigkeit
    if spieler_y < gegner_y:
        gegner_y -= gegner_geschwindigkeit
    #Kontakterkennung
    if gegner_x-2 <= spieler_x <= gegner_x+2 and spieler_y-2 <= gegner_y <= spieler_y+2 and letzerschaden+.5 < float(time.time()):
        herzen -= 1
        letzerschaden = float(time.time())
        color = 5
    if letzerschaden+.5 < float(time.time()):
        color = 4
    # Stopbildschirm
    if herzen <= 0:
        screen.fill(ROT)
        Game_over_text = font.render("Game over!", True, (SCHWARZ))
        screen.blit(Game_over_text, (Fensterbreite/2 - Game_over_text.get_width()/2, Fensterhöhe/2 - Game_over_text.get_height()/2))
        pygame.display.flip()
        time.sleep(3)
        running = False



    # Spieler innerhalb der Fenstergrenzen halten
    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > Fensterbreite - spieler_breite:
        spieler_x = Fensterbreite - spieler_breite
    if spieler_y < 0:
        spieler_y = 0
    if spieler_y > Fensterhöhe - spieler_höhe:
        spieler_y = Fensterhöhe - spieler_höhe

    screen.fill(Farben[color])

    # Lebensleiste zeichnen
    if herzen >= 1/3*spieler_herzen: pygame.draw.rect(screen,ROT, (spieler_x+spieler_breite*0/5, spieler_y-spieler_höhe/3 , 10, 10))
    if herzen >= 2/3*spieler_herzen: pygame.draw.rect(screen,ROT, (spieler_x+spieler_breite*2/5, spieler_y-spieler_höhe/3 , 10, 10))
    if herzen >= 3/3*spieler_herzen: pygame.draw.rect(screen,ROT, (spieler_x+spieler_breite*4/5, spieler_y-spieler_höhe/3 , 10, 10))

    # Spieler zeichnen
    pygame.draw.rect(screen, SCHWARZ, (spieler_x, spieler_y, spieler_breite, spieler_höhe))
    pygame.draw.rect(screen,BLAU, (gegner_x, gegner_y, gegner_breite, gegner_höhe))


    clock.tick(500)
    pygame.display.flip()

# Quit Pygame
pygame.quit()