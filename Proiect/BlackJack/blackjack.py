import pygame
from pygame.locals import *
import random
import copy
import main

pygame.init()
pygame.mixer.init()

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
cards = [ ConnyA, RobbyA, SamA, ViviA, Conny2, Robby2, Sam2, Vivi2, Conny3, Robby3, Sam3, Vivi3, \
            Conny4, Robby4, Sam4, Vivi4, Conny5, Robby5, Sam5, Vivi5, Conny6, Robby6, Sam6, Vivi6, \
            Conny7, Robby7, Sam7, Vivi7, Conny8, Robby8, Sam8, Vivi8, Conny9, Robby9, Sam9, Vivi9, \
            Conny10, Robby10, Sam10, Vivi10, ConnyJ, RobbyJ, SamJ, ViviJ, ConnyQ, RobbyQ, SamQ, ViviQ, ConnyK, RobbyK, SamK, ViviK ]
cardACE = [ ConnyA, RobbyA, SamA, ViviA ]
card2 = [ Conny2, Robby2, Sam2, Vivi2 ]
card3 = [ Conny3, Robby3, Sam3, Vivi3 ]
card4 = [ Conny4, Robby4, Sam4, Vivi4 ]
card5 = [ Conny5, Robby5, Sam5, Vivi5 ]
card6 = [ Conny6, Robby6, Sam6, Vivi6 ]
card7 = [ Conny7, Robby7, Sam7, Vivi7 ]
card8 = [ Conny8, Robby8, Sam8, Vivi8 ]
card9 = [ Conny9, Robby9, Sam9, Vivi9 ]
card10 = [ Conny10, Robby10, Sam10, Vivi10, ConnyJ, RobbyJ, SamJ, ViviJ, ConnyQ, RobbyQ, SamQ, ViviQ, ConnyK, RobbyK, SamK, ViviK ]

start_sound = pygame.mixer.Sound("sounds/shuffling-cards-4.mp3")
win_sound = pygame.mixer.Sound("sounds/sunet_snap2.mp3")
lose_sound = pygame.mixer.Sound("sounds/wrong_snap.mp3")

def play_start_sound():
    start_sound.play()

def play_win_sound():
    win_sound.play()

def play_lose_sound():
    lose_sound.play()

def returnValue(card):
    if card in cardACE:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        exit()

def generateCard(cardsList, playerList):
    card = random.choice(cardsList)
    cardsList.remove(card)
    playerList.append(card)
    cardA = 0
    if card in cardACE:
        cardA = 1
    return card, cardA

def startGame(cardsList, cardsListPlayer, cardsListDealer):
    numberOfPlayerAces = 0
    numbeOfDealerAces = 0
    card1Player, cardA = generateCard(cardsList, cardsListPlayer)
    numberOfPlayerAces += cardA
    card1Dealer, cardA = generateCard(cardsList, cardsListDealer)
    numbeOfDealerAces += cardA
    card2Player, cardA = generateCard(cardsList, cardsListPlayer)
    numberOfPlayerAces += cardA
    card2Dealer, cardA = generateCard(cardsList, cardsListDealer)
    numbeOfDealerAces += cardA
    return returnValue(card1Player) + returnValue(card2Player), numberOfPlayerAces, returnValue(card1Dealer) + returnValue(card2Dealer), numbeOfDealerAces

black = (0,0,0)
white = (255,255,255)
green = (19,85,52)

def startBlackJack():
    pygame.init()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Blackjack')
    screen = pygame.display.set_mode((1024, 768))
    background = pygame.image.load("resurseJoc/BG.png")
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont('Arial', 50)
    HitButton = pygame.draw.rect(background, green, (20, 330, 150, 60))
    HitText = font.render('Hit', 1, black)
    screen.blit(HitText, (70, 330))
    StandButton = pygame.draw.rect(background, green, (190, 330, 150, 60))
    StandText = font.render('Stand', 1, black)
    screen.blit(StandText, (210, 330))
    MenuButton = pygame.draw.rect(background, green, (700, 670, 300, 50))
    MenuText = font.render('Back to Menu', 1, white)
    resultBox = pygame.draw.rect(background, green, (700, 10, 300, 200))
    
    numberOfWins = 0
    numberOfLosses = 0
    backgroundCopy = copy.copy(background)
    gameover = False
    cardscopy = copy.copy(cards)
    playerCards = []
    dealerCards = []
    playerCardsSum, numberOfPlayerAces, dealerCardsSum, numbeOfDealerAces = startGame(cardscopy, playerCards, dealerCards)
    stand = False
    start_sound_played = False
    while True:
        if start_sound_played == False:
            play_start_sound()
            start_sound_played = True
        if (playerCardsSum >= 21 and numberOfPlayerAces == 0) or len(playerCards) == 5:
            gameover = True
        elif len(playerCards) == 2 and playerCardsSum == 21:
            gameover = True
        elif len(dealerCards) == 2 and dealerCardsSum == 21:
            gameover = True
        WinsText = font.render('Wins: %i' % numberOfWins, 1, white)
        LosesText = font.render('Losses: %i' % numberOfLosses, 1, white)
        RestartText = font.render('Restart', 1, white)
        GAMEOVERText = font.render('GAME OVER', 1, white)
        for event in pygame.event.get():
            win_sound_played = False
            lose_sound_played = False
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and HitButton.collidepoint(pygame.mouse.get_pos()):
                card, cardA = generateCard(cardscopy, playerCards)
                numberOfPlayerAces += cardA
                playerCardsSum += returnValue(card)
                print('Jucator: %i' % playerCardsSum)
                while playerCardsSum > 21 and numberOfPlayerAces > 0:
                    numberOfPlayerAces -= 1
                    playerCardsSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and StandButton.collidepoint(pygame.mouse.get_pos()):
                stand = True
                while dealerCardsSum <= playerCardsSum and dealerCardsSum < 17:
                    card, cardA = generateCard(cardscopy, dealerCards)
                    numbeOfDealerAces += cardA
                    dealerCardsSum += returnValue(card)
                    print('Dealer: %i' % dealerCardsSum)
                    while dealerCardsSum > 21 and numbeOfDealerAces > 0:
                        numbeOfDealerAces -= 1
                        dealerCardsSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and RestartButon.collidepoint(pygame.mouse.get_pos()):
                if playerCardsSum == dealerCardsSum:
                    pass
                elif playerCardsSum <= 21 and len(playerCards) == 5:
                    numberOfWins += 1
                    if win_sound_played == False:
                        play_win_sound()
                        win_sound_played = True
                elif playerCardsSum <= 21 and (playerCardsSum > dealerCardsSum or dealerCardsSum > 21):
                    numberOfWins += 1
                    if win_sound_played == False:
                        play_win_sound()
                        win_sound_played = True
                else:
                    numberOfLosses += 1
                    if lose_sound_played == False:
                        play_lose_sound()
                        lose_sound_played = True
                gameover = False
                cardscopy = copy.copy(cards)
                playerCards = []
                dealerCards = []
                playerCardsSum, numberOfPlayerAces, dealerCardsSum, numbeOfDealerAces = startGame(cardscopy, playerCards, dealerCards)
                stand = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and MenuButton.collidepoint(pygame.mouse.get_pos()):
                main.meniu()

        screen.blit(background, (0, 0))
        screen.blit(HitText, (70, 330))
        screen.blit(StandText, (210, 330))
        screen.blit(WinsText, (790, 35))
        screen.blit(LosesText, (770, 105))
        screen.blit(MenuText, (730, 665))

        for card in dealerCards:
            x = 10 + dealerCards.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(spate, (120, 10))
        for card in playerCards:
            x = 10 + playerCards.index(card) * 110
            screen.blit(card, (x, 400))
        if gameover or stand:
            screen.blit(GAMEOVERText, (400, 330))
            MenuButton = pygame.draw.rect(background, green, (700, 670, 300, 50))
            RestartButon = pygame.draw.rect(background, green, (700, 600, 300, 50))
            screen.blit(RestartText, (785, 595))
            for card in dealerCards:
                x = 10 + dealerCards.index(card) * 110
                screen.blit(card, (x, 10))
            background = copy.copy(backgroundCopy)
        pygame.display.update()
