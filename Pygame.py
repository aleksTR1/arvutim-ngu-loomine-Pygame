import pygame
import random

pygame.init()

# Akna suurus
LAIUS, KÕRGUS = 600, 400
aken = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.display.set_caption("Aleks_Tagirov_Logitpv24")

# Värvid
VALGE = (255, 255, 255)
PUNANE = (200, 0, 0)
SININE = (0, 100, 255)
MUST = (0, 0, 0)

# Mängija andmed
mängija_suurus = 50
mängija_x = LAIUS // 2
mängija_y = KÕRGUS - mängija_suurus - 10
mängija_kiirus = 7

# Takistuse andmed
takistus_suurus = 50
takistus_x = random.randint(0, LAIUS - takistus_suurus)
takistus_y = 0
takistus_kiirus = 5

# Punktid ja font
punktid = 0
font = pygame.font.SysFont("Arial", 24)

# Helid
kaotus_heli = pygame.mixer.Sound("lose.wav")
pygame.mixer.music.load("background_music.wav")
pygame.mixer.music.play(-1)

kell = pygame.time.Clock()
jookseb = True
mäng_läbi = False

while jookseb:
    kell.tick(30)
    aken.fill(VALGE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jookseb = False

    if not mäng_läbi:
        # Mängija liigutamine
        klahvid = pygame.key.get_pressed()
        if klahvid[pygame.K_LEFT] and mängija_x > 0:
            mängija_x -= mängija_kiirus
        if klahvid[pygame.K_RIGHT] and mängija_x < LAIUS - mängija_suurus:
            mängija_x += mängija_kiirus

        # Takistus langeb alla
        takistus_y += takistus_kiirus
        if takistus_y > KÕRGUS:
            takistus_y = 0
            takistus_x = random.randint(0, LAIUS - takistus_suurus)
            punktid += 1

        mängija_ristkülik = pygame.Rect(mängija_x, mängija_y, mängija_suurus, mängija_suurus)
        takistus_ristkülik = pygame.Rect(takistus_x, takistus_y, takistus_suurus, takistus_suurus)

        # Kontroll kokkupõrke kohta
        if mängija_ristkülik.colliderect(takistus_ristkülik):
            pygame.mixer.music.stop()  # Vaigistab taustamuusika
            kaotus_heli.play()         # Mängib kaotusheli
            pygame.time.delay(1000)    # Ootab, et heli kostaks
            mäng_läbi = True

        # Joonistame mängija ja takistuse
        pygame.draw.rect(aken, SININE, mängija_ristkülik)
        pygame.draw.rect(aken, PUNANE, takistus_ristkülik)

        # Kuvame punktid
        punktid_tekst = font.render(f"Punktid: {punktid}", True, MUST)
        aken.blit(punktid_tekst, (10, 10))

    else:
        # Lihtne mängu lõpu ekraan
        lõpp_tekst = font.render("Mäng läbi!", True, MUST)
        punktid_tekst = font.render(f"Sinu punktid: {punktid}", True, MUST)
        aken.blit(lõpp_tekst, (LAIUS // 2 - lõpp_tekst.get_width() // 2, KÕRGUS // 2 - 30))
        aken.blit(punktid_tekst, (LAIUS // 2 - punktid_tekst.get_width() // 2, KÕRGUS // 2 + 10))

    pygame.display.update()

pygame.quit()