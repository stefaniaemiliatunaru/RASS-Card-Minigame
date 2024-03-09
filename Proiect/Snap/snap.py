import pygame

from Snap.objects import *
from Snap.engine import *
import main

pygame.init()
pygame.mixer.init()

bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("SlapJack")

engineJoc = SnapEngine()

spateCarte = pygame.image.load("resurseJoc/carduri/spate.png")
spateCarte = pygame.transform.scale(spateCarte, (223, 312))

trophy = pygame.image.load("resurseJoc/Trophy.png")
trophy = pygame.transform.scale(trophy, (50, 50))

background = pygame.image.load("resurseJoc/BG.png")
background = pygame.transform.scale(background, bounds)

sunet_de_start = pygame.mixer.Sound("sounds/shuffling-cards-4.mp3")
sunet_de_snap = pygame.mixer.Sound("sounds/sunet_snap2.mp3")
sunet_de_snap_gresit = pygame.mixer.Sound("sounds/wrong_snap.mp3")
sunet_de_sfarsit = pygame.mixer.Sound("sounds/end_game_sound.mp3")

def sunet_sfarsit():
    sunet_de_sfarsit.play()

def sunet_snap_gresit():
    sunet_de_snap_gresit.play()

def sunet_snap():
    sunet_de_snap.play()
    
def sunet_inceput():
    sunet_de_start.play()

def renderGame(window):
    window.fill((15, 0, 169))
    window.blit(background, (0, 0))
    font = pygame.font.Font("Grand9k Pixel.ttf", 30)

    window.blit(spateCarte, (100, 200))
    window.blit(spateCarte, (700, 200))

    text = font.render(str(len(engineJoc.jucator1.mana)) + " carti", True, (255,255,255))
    window.blit(text, (110, 520))

    text = font.render(str(len(engineJoc.jucator2.mana)) + " carti", True, (255,255,255))
    window.blit(text, (710, 520))

    text = font.render(str(engineJoc.scor_jucator1) + " | " + str(engineJoc.scor_jucator2), True, (255,255,255))
    window.blit(text, (470, 700))

    window.blit(trophy, (478, 660))

    topCard = engineJoc.teanc.scoate()
    if topCard != None:
        window.blit(topCard.imagine, (400, 200))

    if engineJoc.stare == StareJoc.JOC:
        text = font.render("Este randul lui " + engineJoc.jucatorCurent.nume, True, (255,255,255))
        window.blit(text, (20, 50))

    if engineJoc.stare == StareJoc.SNAP:
        rezultat = engineJoc.rezultat
        if rezultat["este_snap"] == True:
            mesaj1 = "Snap Corect! " + "dat de " + rezultat["snapCaller"].nume
            sunet_snap()
        else:
            mesaj1 = "Snap Gresit! " + "dat de " + rezultat["snapCaller"].nume + ". "
            sunet_snap_gresit()
        window.fill((0, 0, 0))
        text = font.render(mesaj1, True, (255, 255, 255))
        window.blit(text, (270, 250))

        if rezultat["este_snap"] == False:
            mesaj2 = rezultat["castigator"].nume + " primeste cartile!"
            text2 = font.render(mesaj2, True, (255, 255, 255))
            window.blit(text2, (300, 300))

    if engineJoc.stare == StareJoc.FINAL:
        rezultat = engineJoc.rezultat
        window.fill((0, 0, 0))
        mesaj = "Jocul s-a terminat! " + rezultat["castigator"].nume + " a castigat!"
        restart_joc = "Apasa R pentru a incepe un joc nou!"
        inapoi_la_meniu = "Apasa M pentru a te intoarce la meniu!"
        text_inapoi_la_meniu = font.render(inapoi_la_meniu, True, (255, 255, 255))
        text_restart = font.render(restart_joc, True, (255, 255, 255))
        text = font.render(mesaj, True, (255, 255, 255))
        window.blit(text, (190, 250))
        window.blit(text_restart, (225, 300))
        window.blit(text_inapoi_la_meniu, (210, 350))
        tasta = pygame.key.get_pressed()
        if engineJoc.pot_aplica_sunet_final == 0:
            sunet_sfarsit()
            engineJoc.pot_aplica_sunet_final = 1
        if tasta[pygame.K_r] or tasta[pygame.K_m]:
            if rezultat["castigator"].nume == "Jucator 1":
                engineJoc.scor_jucator1 += 1
            else:
                engineJoc.scor_jucator2 += 1
            engineJoc.pachet = Pachet()
            engineJoc.pachet.amesteca()
            engineJoc.jucator1 = Jucator("Jucator 1", pygame.K_a, pygame.K_d)
            engineJoc.jucator2 = Jucator("Jucator 2", pygame.K_LEFT, pygame.K_RIGHT)
            engineJoc.teanc = TeancDeCarti()
            engineJoc.imparteCarti()
            engineJoc.jucatorCurent = engineJoc.jucator1
            engineJoc.stare = StareJoc.JOC
            engineJoc.rezultat = None
            engineJoc.pot_aplica_sunet_final = 0
            if tasta[pygame.K_m]:
                engineJoc.scor_jucator1 = 0
                engineJoc.scor_jucator2 = 0
                main.meniu()
            else:
                snap(window)

def afiseaza_shuffle_screen():
    window.fill((0, 0, 0))
    font = pygame.font.Font("Grand9K Pixel.ttf", 30)
    text = font.render("Se amesteca cartile...", True, (255, 255, 255))
    window.blit(text, (325, 320))
    pygame.display.update()

def snap(window):
    pygame.display.set_caption("Snap Card Game")
    afiseaza_shuffle_screen()
    sunet_inceput()
    pygame.time.delay(1000)
    run = True
    while run:
        tasta = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                tasta = event.key

        engineJoc.joacaJoc(tasta)
        renderGame(window) # functie care afiseaza grafica jocului
        pygame.display.update()

        if engineJoc.stare == StareJoc.SNAP:
            pygame.time.delay(3000)
            engineJoc.stare = StareJoc.JOC


    pygame.quit()
    quit()

def startSnapGame():
    snap(window)
