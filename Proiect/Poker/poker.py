import pygame
from pygame.locals import *
import random
import copy
import main

icon = pygame.transform.scale(pygame.image.load('resurseJoc/ICON.png'), (223, 312))
spate = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/SPATE.png'), (223, 312))
ConnyA = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/01C.png'), (223, 312))
RobbyA = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/01R.png'), (223, 312))
SamA = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/01S.png'), (223, 312))
ViviA = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/01V.png'), (223, 312))
Conny2 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/02C.png'), (223, 312))
Robby2 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/02R.png'), (223, 312))
Sam2 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/02S.png'), (223, 312))
Vivi2 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/02V.png'), (223, 312))
Conny3 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/03C.png'), (223, 312))
Robby3 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/03R.png'), (223, 312))
Sam3 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/03S.png'), (223, 312))
Vivi3 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/03V.png'), (223, 312))
Conny4 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/04C.png'), (223, 312))
Robby4 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/04R.png'), (223, 312))
Sam4 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/04S.png'), (223, 312))
Vivi4 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/04V.png'), (223, 312))
Conny5 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/05C.png'), (223, 312))
Robby5 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/05R.png'), (223, 312))
Sam5 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/05S.png'), (223, 312))
Vivi5 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/05V.png'), (223, 312))
Conny6 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/06C.png'), (223, 312))
Robby6 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/06R.png'), (223, 312))
Sam6 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/06S.png'), (223, 312))
Vivi6 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/06V.png'), (223, 312))
Conny7 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/07C.png'), (223, 312))
Robby7 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/07R.png'), (223, 312))
Sam7 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/07S.png'), (223, 312))
Vivi7 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/07V.png'), (223, 312))
Conny8 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/08C.png'), (223, 312))
Robby8 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/08R.png'), (223, 312))
Sam8 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/08S.png'), (223, 312))
Vivi8 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/08V.png'), (223, 312))
Conny9 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/09C.png'), (223, 312))
Robby9 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/09R.png'), (223, 312))
Sam9 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/09S.png'), (223, 312))
Vivi9 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/09V.png'), (223, 312))
Conny10 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/10C.png'), (223, 312))
Robby10 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/10R.png'), (223, 312))
Sam10 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/10S.png'), (223, 312))
Vivi10 = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/10V.png'), (223, 312))
ConnyJ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/12C.png'), (223, 312))
RobbyJ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/12R.png'), (223, 312))
SamJ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/12S.png'), (223, 312))
ViviJ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/12V.png'), (223, 312))
ConnyQ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/13C.png'), (223, 312))
RobbyQ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/13R.png'), (223, 312))
SamQ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/13S.png'), (223, 312))
ViviQ = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/13V.png'), (223, 312))
ConnyK = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/14C.png'), (223, 312))
RobbyK = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/14R.png'), (223, 312))
SamK = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/14S.png'), (223, 312))
ViviK = pygame.transform.scale(pygame.image.load('resurseJoc/Carduri/14V.png'), (223, 312))
carduri = [ ConnyA, RobbyA, SamA, ViviA, Conny2, Robby2, Sam2, Vivi2, Conny3, Robby3, Sam3, Vivi3, \
            Conny4, Robby4, Sam4, Vivi4, Conny5, Robby5, Sam5, Vivi5, Conny6, Robby6, Sam6, Vivi6, \
            Conny7, Robby7, Sam7, Vivi7, Conny8, Robby8, Sam8, Vivi8, Conny9, Robby9, Sam9, Vivi9, \
            Conny10, Robby10, Sam10, Vivi10, ConnyJ, RobbyJ, SamJ, ViviJ, ConnyQ, RobbyQ, SamQ, ViviQ, ConnyK, RobbyK, SamK, ViviK ]
cardA = [ ConnyA, RobbyA, SamA, ViviA ]
card2 = [ Conny2, Robby2, Sam2, Vivi2 ]
card3 = [ Conny3, Robby3, Sam3, Vivi3 ]
card4 = [ Conny4, Robby4, Sam4, Vivi4 ]
card5 = [ Conny5, Robby5, Sam5, Vivi5 ]
card6 = [ Conny6, Robby6, Sam6, Vivi6 ]
card7 = [ Conny7, Robby7, Sam7, Vivi7 ]
card8 = [ Conny8, Robby8, Sam8, Vivi8 ]
card9 = [ Conny9, Robby9, Sam9, Vivi9 ]
card10 = [ Conny10, Robby10, Sam10, Vivi10 ]
cardJ = [ ConnyJ, RobbyJ, SamJ, ViviJ ]
cardQ = [ ConnyQ, RobbyQ, SamQ, ViviQ ]
cardK = [ ConnyK, RobbyK, SamK, ViviK ]
cardC = [ ConnyA, Conny2, Conny3, Conny4, Conny5, Conny6, Conny7, Conny8, Conny9, Conny10, ConnyJ, ConnyQ, ConnyK]
cardR = [ RobbyA, Robby2, Robby3, Robby4, Robby5, Robby6, Robby7, Robby8, Robby9, Robby10, RobbyJ, RobbyQ, RobbyK]
cardS = [ SamA, Sam2, Sam3, Sam4, Sam5, Sam6, Sam7, Sam8, Sam9, Sam10, SamJ, SamQ, SamK]
cardV = [ ViviA, Vivi2, Vivi3, Vivi4, Vivi5, Vivi6, Vivi7, Vivi8, Vivi9, Vivi10, ViviJ, ViviQ, ViviK]

def returneazaValoare(card):
    valoare = []
    if card in cardC:
        valoare.append("C")
    elif card in cardR:
        valoare.append("R")
    elif card in cardS:
        valoare.append("S")
    elif card in cardV:
        valoare.append("V")
    if card in cardA:
        valoare.append(15)
    elif card in card2:
        valoare.append(2)
    elif card in card3:
        valoare.append(3)
    elif card in card4:
        valoare.append(4)
    elif card in card5:
        valoare.append(5)
    elif card in card6:
        valoare.append(6)
    elif card in card7:
        valoare.append(7)
    elif card in card8:
        valoare.append(8)
    elif card in card9:
        valoare.append(9)
    elif card in card10:
        valoare.append(10)
    elif card in cardJ:
        valoare.append(12)
    elif card in cardQ:
        valoare.append(13)
    elif card in cardK:
        valoare.append(14)
    return valoare

def generareCard(listaCarduri):
    card = random.choice(listaCarduri)
    listaCarduri.remove(card)
    return card

def incepeJocul(listaCarduri):
    listaCarduriJucator = []
    listaCarduriDealer = []
    card1Jucator = generareCard(listaCarduri)
    listaCarduriJucator.append(card1Jucator)
    card1Dealer = generareCard(listaCarduri)
    listaCarduriDealer.append(card1Dealer)
    card2Jucator = generareCard(listaCarduri)
    listaCarduriJucator.append(card2Jucator)
    card2Dealer = generareCard(listaCarduri)
    listaCarduriDealer.append(card2Dealer)
    card3Jucator = generareCard(listaCarduri)
    listaCarduriJucator.append(card3Jucator)
    card3Dealer = generareCard(listaCarduri)
    listaCarduriDealer.append(card3Dealer)
    card4Jucator = generareCard(listaCarduri)
    listaCarduriJucator.append(card4Jucator)
    card4Dealer = generareCard(listaCarduri)
    listaCarduriDealer.append(card4Dealer)
    card5Jucator = generareCard(listaCarduri)
    listaCarduriJucator.append(card5Jucator)
    card5Dealer = generareCard(listaCarduri)
    listaCarduriDealer.append(card5Dealer)
    return listaCarduriJucator, listaCarduriDealer

def analizaCarduri(listaCarduriJucator, listaCarduriDealer):
    rezultat = 0
    flushJucator = []
    flushDealer = []
    cvadrupletJucator = []
    cvadrupletDealer = []
    straightJucator = []
    straightDealer = []
    tripletJucator = []
    tripletDealer = []
    perecheJucator = []
    perecheDealer = []
    listaValoriCarduriJucator = []
    for card in listaCarduriJucator:
        listaValoriCarduriJucator.append(returneazaValoare(card))
    listaValoriCarduriJucator = sorted(listaValoriCarduriJucator, key=lambda x: x[1])
    highestvalueJucator = max(valoareCard[1] for valoareCard in listaValoriCarduriJucator)
    for numaratoare in range(2, 16):
        count = sum(numaratoare == valoareCard[1] for valoareCard in listaValoriCarduriJucator)
        if count == 4:
            cvadrupletJucator.append(numaratoare)
        if count == 3:
            tripletJucator.append(numaratoare)
        if count == 2:
            perecheJucator.append(numaratoare)
    for culoare in ["C", "R", "S", "V"]:
        count = sum(culoare in valoareCard[0] for valoareCard in listaValoriCarduriJucator)
        if count == 5:
            flushJucator.append(culoare)
    if (listaValoriCarduriJucator[0][1] == listaValoriCarduriJucator[1][1] - 1) or (listaValoriCarduriJucator[0][1] == 10 and listaValoriCarduriJucator[1][1] == 12):
        if (listaValoriCarduriJucator[1][1] == listaValoriCarduriJucator[2][1] - 1) or (listaValoriCarduriJucator[1][1] == 10 and listaValoriCarduriJucator[2][1] == 12):
            if (listaValoriCarduriJucator[2][1] == listaValoriCarduriJucator[3][1] - 1) or (listaValoriCarduriJucator[2][1] == 10 and listaValoriCarduriJucator[3][1] == 12):
                if (listaValoriCarduriJucator[3][1] == listaValoriCarduriJucator[4][1] - 1) or (listaValoriCarduriJucator[3][1] == 10 and listaValoriCarduriJucator[4][1] == 12):
                    straightJucator.append(listaValoriCarduriJucator[4][1])
    listaValoriCarduriDealer = []
    for card in listaCarduriDealer:
        listaValoriCarduriDealer.append(returneazaValoare(card))
    listaValoriCarduriDealer = sorted(listaValoriCarduriDealer, key=lambda x: x[1])
    highestvalueDealer = max(valoareCard[1] for valoareCard in listaValoriCarduriDealer)
    for numaratoare in range(2, 16):
        count = sum(numaratoare == valoareCard[1] for valoareCard in listaValoriCarduriDealer)
        if count == 4:
            cvadrupletDealer.append(numaratoare)
        if count == 3:
            tripletDealer.append(numaratoare)
        if count == 2:
            perecheDealer.append(numaratoare)
    for culoare in ["C", "R", "S", "V"]:
        count = sum(culoare in valoareCard[0] for valoareCard in listaValoriCarduriDealer)
        if count == 5:
            flushDealer.append(culoare)
    if (listaValoriCarduriDealer[0][1] == listaValoriCarduriDealer[1][1] - 1) or (listaValoriCarduriDealer[0][1] == 10 and listaValoriCarduriDealer[1][1] == 12):
        if (listaValoriCarduriDealer[1][1] == listaValoriCarduriDealer[2][1] - 1) or (listaValoriCarduriDealer[1][1] == 10 and listaValoriCarduriDealer[2][1] == 12):
            if (listaValoriCarduriDealer[2][1] == listaValoriCarduriDealer[3][1] - 1) or (listaValoriCarduriDealer[2][1] == 10 and listaValoriCarduriDealer[3][1] == 12):
                if (listaValoriCarduriDealer[3][1] == listaValoriCarduriDealer[4][1] - 1) or (listaValoriCarduriDealer[3][1] == 10 and listaValoriCarduriDealer[4][1] == 12):
                    straightDealer.append(listaValoriCarduriDealer[4][1])
    manaJucator = 0
    manaDealer = 0
    # Royal & Straight Flush
    if len(listaValoriCarduriJucator) == 1 and len(straightJucator) == 1:
        manaJucator = 8
    if len(listaValoriCarduriDealer) == 1 and len(straightDealer) == 1:
        manaDealer = 8
    if manaJucator == manaDealer == 8:
        if straightJucator[0] >= straightDealer[0]:
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # Four of a Kind
    if len(cvadrupletJucator) == 1:
        manaJucator = 7
    if len(cvadrupletDealer) == 1:
        manaDealer = 7
    if manaJucator == manaDealer == 7:
        if cvadrupletJucator[0] > cvadrupletDealer[0]:
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # Full House
    if len(tripletJucator) == 1 and len(perecheJucator) == 1:
        manaJucator = 6
    if len(tripletDealer) == 1 and len(perecheDealer) == 1:
        manaDealer = 6
    if manaJucator == manaDealer == 6:
        if tripletJucator[0] > tripletDealer[0]:
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # Flush
    if len(flushJucator) == 1:
        manaJucator = 5
    if len(flushDealer) == 1:
        manaDealer = 5
    if manaJucator == manaDealer == 5:
        if highestvalueJucator >= highestvalueDealer:
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # Straight
    if len(straightJucator) == 1:
        manaJucator = 4
    if len(straightDealer) == 1:
        manaDealer = 4
    if manaJucator == manaDealer == 4:
        if straightJucator[0] >= straightDealer[0]:
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # Three of a Kind
    if len(tripletJucator) == 1:
        manaJucator = 3
    if len(tripletDealer) == 1:
        manaDealer = 3
    if manaJucator == manaDealer == 3:
        if tripletJucator[0] > tripletDealer[0]:
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # Two pair
    if len(perecheJucator) == 2:
        manaJucator = 2
    if len(perecheDealer) == 2:
        manaDealer = 2
    if manaJucator == manaDealer == 2:
        if max(perecheJucator) > max(perecheDealer):
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # Pair
    if len(perecheJucator) == 1:
        manaJucator = 1
    if len(perecheDealer) == 1:
        manaDealer = 1
    if manaJucator == manaDealer == 1:
        if perecheJucator[0] > perecheDealer[0]:
            rezultat = 1
            return rezultat
        else:
            return rezultat
    if manaJucator > manaDealer:
        rezultat = 1
        return rezultat
    if manaJucator < manaDealer:
        return rezultat
    # High card
    if highestvalueJucator >= highestvalueDealer:
        rezultat = 1
    return rezultat

def startPoker():
    pygame.init()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Poker')
    screen = pygame.display.set_mode((1024, 768))
    background = pygame.image.load("resurseJoc/BG.png")
    screen.blit(background, (0, 0))
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (19, 85, 52)
    font = pygame.font.SysFont('Arial', 50)
    ChangeButon = pygame.draw.rect(background, green, (20, 330, 150, 60))
    ChangeText = font.render('Change', 1, white)
    screen.blit(ChangeText, (20, 330))
    StandButon = pygame.draw.rect(background, green, (190, 330, 150, 60))
    StandText = font.render('Stand', 1, white)
    screen.blit(StandText, (210, 330))
    MenuButton = pygame.draw.rect(background, green, (700, 670, 300, 50))
    MenuText = font.render('Back to Menu', 1, black)
    screen.blit(MenuText, (730, 665))
    pygame.draw.rect(background, green, (700, 10, 300, 200))

    card1Buton = pygame.draw.rect(background, green, (10, 400, 110, 312))
    card2Buton = pygame.draw.rect(background, green, (120, 400, 110, 312))
    card3Buton = pygame.draw.rect(background, green, (230, 400, 110, 312))
    card4Buton = pygame.draw.rect(background, green, (340, 400, 110, 312))
    card5Buton = pygame.draw.rect(background, green, (450, 400, 223, 312))
    numarWins = 0
    numarLosses = 0
    copieBackground = copy.copy(background)
    GameOver = False
    copieCarduri = copy.copy(carduri)
    carduriJucator, carduriDealer = incepeJocul(copieCarduri)
    card1Changed = False
    card2Changed = False
    card3Changed = False
    card4Changed = False
    card5Changed = False
    Stand = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card1Changed) and card1Buton.collidepoint(pygame.mouse.get_pos()):
                for card in carduriJucator:
                    if (carduriJucator.index(card) != 0):
                        x = 10 + carduriJucator.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(spate, (10, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButon.collidepoint(pygame.mouse.get_pos()):
                            carduriJucator[0] = generareCard(copieCarduri)
                            card1Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card1Buton.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card2Changed) and card2Buton.collidepoint(pygame.mouse.get_pos()):
                for card in carduriJucator:
                    if (carduriJucator.index(card) != 1):
                        x = 10 + carduriJucator.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(spate, (120, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButon.collidepoint(pygame.mouse.get_pos()):
                            carduriJucator[1] = generareCard(copieCarduri)
                            card2Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card2Buton.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card3Changed) and card3Buton.collidepoint(pygame.mouse.get_pos()):
                for card in carduriJucator:
                    if (carduriJucator.index(card) != 2):
                        x = 10 + carduriJucator.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(spate, (230, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButon.collidepoint(pygame.mouse.get_pos()):
                            carduriJucator[2] = generareCard(copieCarduri)
                            card3Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card3Buton.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card4Changed) and card4Buton.collidepoint(pygame.mouse.get_pos()):
                for card in carduriJucator:
                    if (carduriJucator.index(card) != 3):
                        x = 10 + carduriJucator.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(spate, (340, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButon.collidepoint(pygame.mouse.get_pos()):
                            carduriJucator[3] = generareCard(copieCarduri)
                            card4Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card4Buton.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card5Changed) and card5Buton.collidepoint(pygame.mouse.get_pos()):
                for card in carduriJucator:
                    if (carduriJucator.index(card) != 4):
                        x = 10 + carduriJucator.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(spate, (450, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButon.collidepoint(pygame.mouse.get_pos()):
                            carduriJucator[4] = generareCard(copieCarduri)
                            card5Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card5Buton.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card1Changed or card2Changed or card3Changed or card4Changed or card5Changed) and ChangeButon.collidepoint(pygame.mouse.get_pos()):
                carduriJucator.clear()
                card1NouJucator = generareCard(copieCarduri)
                carduriJucator.append(card1NouJucator)
                card2NouJucator = generareCard(copieCarduri)
                carduriJucator.append(card2NouJucator)
                card3NouJucator = generareCard(copieCarduri)
                carduriJucator.append(card3NouJucator)
                card4NouJucator = generareCard(copieCarduri)
                carduriJucator.append(card4NouJucator)
                card5NouJucator = generareCard(copieCarduri)
                carduriJucator.append(card5NouJucator)
                GameOver = True
                if analizaCarduri(carduriJucator, carduriDealer) == 1:
                    numarWins = numarWins + 1
                else:
                    numarLosses = numarLosses + 1
            elif event.type == pygame.MOUSEBUTTONDOWN and not GameOver and StandButon.collidepoint(pygame.mouse.get_pos()):
                Stand = True
                GameOver = True
                if analizaCarduri(carduriJucator, carduriDealer) == 1:
                    numarWins = numarWins + 1
                else:
                    numarLosses = numarLosses + 1
            elif event.type == pygame.MOUSEBUTTONDOWN and (GameOver or Stand) and RestartButon.collidepoint(pygame.mouse.get_pos()):
                GameOver = False
                copieCarduri = copy.copy(carduri)
                carduriJucator, carduriDealer = incepeJocul(copieCarduri)
                card1Changed = False
                card2Changed = False
                card3Changed = False
                card4Changed = False
                card5Changed = False
                Stand = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not GameOver and MenuButton.collidepoint(pygame.mouse.get_pos()):
                main.meniu()
        screen.blit(background, (0, 0))
        screen.blit(ChangeText, (20, 330))
        screen.blit(StandText, (210, 330))
        screen.blit(MenuText, (730, 665))
        WinsText = font.render('Wins: %i' % numarWins, 1, black)
        screen.blit(WinsText, (790, 35))
        LossesText = font.render('Losses: %i' % numarLosses, 1, black)
        screen.blit(LossesText, (770, 105))
        for card in carduriDealer:
            x = 10 + carduriDealer.index(card) * 110
            screen.blit(spate, (x, 10))
        for card in carduriJucator:
            x = 10 + carduriJucator.index(card) * 110
            screen.blit(card, (x, 400))
        if GameOver or Stand:
            GAMEOVERText = font.render('GAME OVER', 1, black)
            screen.blit(GAMEOVERText, (400, 330))
            RestartButon = pygame.draw.rect(background, green, (700, 600, 300, 50))
            RestartText = font.render('Restart', 1, black)
            screen.blit(RestartText, (785, 595))
            for card in carduriDealer:
                x = 10 + carduriDealer.index(card) * 110
                screen.blit(card, (x, 10))
            background = copy.copy(copieBackground)
        pygame.display.update()