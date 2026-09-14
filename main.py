# All rights reserved for now.
import time
import pygame

# Pygame initialisieren
pygame.init()

# Farben
BLAU = (0, 0, 255)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
ORANGE = (255, 204, 51)

Farben = [BLAU, ROT, GRUEN, SCHWARZ, WEISS, ORANGE]


def komplementaerfarbe(rgb):
    return tuple(255 - n for n in rgb)


# Fenster
Fensterbreite = 800
Fensterhöhe = 600

screen = pygame.display.set_mode((Fensterbreite, Fensterhöhe))
pygame.display.set_caption("Spiel")

clock = pygame.time.Clock()
font = pygame.font.SysFont("freesans", 48)

# Farbe des Hintergrunds
color = 4


# SPIELER
player = pygame.Rect(
    Fensterbreite // 2 - 25,
    Fensterhöhe // 2 - 25,
    50,
    50
)

spieler_geschwindigkeit = 300  # Pixel pro Sekunde
spieler_herzen = 5
herzen = spieler_herzen


# GEGNER
enemy = pygame.Rect(
    0,
    0,
    50,
    50
)

gegner_geschwindigkeit = 90  # Pixel pro Sekunde

letzerschaden = time.time()


# SPIEL
running = True

while running:

    # Delta Time:
    # Macht die Bewegung unabhängig von der FPS-Zahl
    dt = clock.tick(60) / 1000

        # EVENTS
        for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # SPIELER BEWEGEN
        Tasten = pygame.key.get_pressed()

    if Tasten[pygame.K_a] or Tasten[pygame.K_LEFT]:
        player.x -= int(spieler_geschwindigkeit * dt)

    if Tasten[pygame.K_d] or Tasten[pygame.K_RIGHT]:
        player.x += int(spieler_geschwindigkeit * dt)

    if Tasten[pygame.K_w] or Tasten[pygame.K_UP]:
        player.y -= int(spieler_geschwindigkeit * dt)

    if Tasten[pygame.K_s] or Tasten[pygame.K_DOWN]:
        player.y += int(spieler_geschwindigkeit * dt)

        # SPIELER IM FENSTER HALTEN
        if player.left < 0:
        player.left = 0

    if player.right > Fensterbreite:
        player.right = Fensterbreite

    if player.top < 0:
        player.top = 0

    if player.bottom > Fensterhöhe:
        player.bottom = Fensterhöhe

        # GEGNER ZUM SPIELER BEWEGEN
    

    dx = player.centerx - enemy.centerx
    dy = player.centery - enemy.centery

    # Schrittweite pro Frame
    schritt = gegner_geschwindigkeit * dt

    # Horizontal bewegen
    if dx > 0:
        enemy.x += min(int(schritt), abs(dx))
    elif dx < 0:
        enemy.x -= min(int(schritt), abs(dx))

    # Vertikal bewegen
    if dy > 0:
        enemy.y += min(int(schritt), abs(dy))
    elif dy < 0:
        enemy.y -= min(int(schritt), abs(dy))

        # KOLLISION
        jetzt = time.time()

    if player.colliderect(enemy):

        # Alle 0,5 Sekunden darf Schaden entstehen
        if jetzt - letzerschaden >= 0.5:
            herzen -= 1
            letzerschaden = jetzt

            # Hintergrund kurz rot färben
            color = 5

    # Nach der Schadensanzeige wieder weiß
    if jetzt - letzerschaden >= 0.5:
        color = 4

        # GAME OVER
        if herzen <= 0:

        screen.fill(ROT)

        Game_over_text = font.render(
            "Game over!",
            True,
            SCHWARZ
        )

        screen.blit(
            Game_over_text,
            (
                Fensterbreite / 2 - Game_over_text.get_width() / 2,
                Fensterhöhe / 2 - Game_over_text.get_height() / 2
            )
        )

        pygame.display.flip()

        pygame.time.delay(3000)

        running = False
        continue

        # HINTERGRUND
        screen.fill(Farben[color])

        # LEBENSLEISTE / HERZEN
    
    for i in range(spieler_herzen):
        if i < herzen:
            herz = pygame.Rect(
                player.x + i * 20,
                player.y - 20,
                10,
                10
            )

            pygame.draw.rect(
                screen,
                ROT,
                herz
            )

        # SPIELER ZEICHNEN
        pygame.draw.rect(
        screen,
        SCHWARZ,
        player
    )

        # GEGNER ZEICHNEN
        pygame.draw.rect(
        screen,
        BLAU,
        enemy
    )

        # ANZEIGEN
        pygame.display.flip()


# Pygame beenden
pygame.quit()
