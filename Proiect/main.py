import Snap.snap as snap
import BlackJack.blackjack as blackjack
import Poker.poker as poker
'''import CardMatch.card as card'''
import pygame

pygame.init()

bounds = (1024, 768)
window = pygame.display.set_mode(bounds)

background = pygame.image.load("resurseMain/BG.png")
background = pygame.transform.scale(background, bounds)

imagine_joc_1 = pygame.image.load("resurseMain/preview_poker.jpg")
imagine_joc_2 = pygame.image.load("resurseMain/preview_blackjack.png")
imagine_joc_3 = pygame.image.load("resurseMain/preview_snap.png")
imagine_joc_4 = pygame.image.load("resurseMain/preview_match.jpg")

trofeu = pygame.image.load("resurseMain/Trophy.png")
trofeu = pygame.transform.scale(trofeu, (200, 200))

logo = pygame.image.load("resurseMain/logo.png")
logo = pygame.transform.scale(logo, (320, 180))

buton_poker_x = 100
buton_poker_y = 100
buton_poker_width = imagine_joc_1.get_width()
buton_poker_height = imagine_joc_1.get_height()

buton_blackjack_x = 724
buton_blackjack_y = 100
buton_blackjack_width = imagine_joc_2.get_width()
buton_blackjack_height = imagine_joc_2.get_height()

buton_snap_x = 100
buton_snap_y = 500
buton_snap_width = imagine_joc_3.get_width()
buton_snap_height = imagine_joc_3.get_height()

buton_match_x = 724
buton_match_y = 500
buton_match_width = imagine_joc_4.get_width()
buton_match_height = imagine_joc_4.get_height()

def show_menu(window):
    window.blit(background, (0, 0))
    font = pygame.font.SysFont("Arial", 40)

    text = font.render("Poker", True, (0, 0, 0))
    window.blit(imagine_joc_1, (100, 100))
    window.blit(text, (150, 50))

    text = font.render("BlackJack", True, (0, 0, 0))
    window.blit(imagine_joc_2, (724, 100))
    window.blit(text, (754, 50))

    text = font.render("Snap Game", True, (0, 0, 0))
    window.blit(imagine_joc_3, (100, 500))
    window.blit(text, (110, 450))

    text1 = font.render("Matching Card", True, (0, 0, 0))
    window.blit(imagine_joc_4, (724, 500))
    window.blit(text1, (722, 420))

    text2 = font.render("Game", True, (0, 0, 0))
    window.blit(text2, (770, 452))

    window.blit(trofeu, (420, 350))

    window.blit(logo, (350, 100))
    
    font = pygame.font.SysFont("Arial", 50)
    tasta = pygame.key.get_pressed()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    click_stanga, _, _ = pygame.mouse.get_pressed()

    if buton_poker_x < mouse_x < buton_poker_x + buton_poker_width and buton_poker_y < mouse_y < buton_poker_y + buton_poker_height:
        if click_stanga:
            poker.startPoker()
    if buton_blackjack_x < mouse_x < buton_blackjack_x + buton_blackjack_width and buton_blackjack_y < mouse_y < buton_blackjack_y + buton_blackjack_height:
        if click_stanga:
            blackjack.startBlackJack()
    if buton_snap_x < mouse_x < buton_snap_x + buton_snap_width and buton_snap_y < mouse_y < buton_snap_y + buton_snap_height:
        if click_stanga:
            snap.startSnapGame()
    '''if buton_match_x < mouse_x < buton_match_x + buton_match_width and buton_match_y < mouse_y < buton_match_y + buton_match_height:
        if click_stanga:
            card.card()'''


def meniu():
    pygame.display.set_caption("Cards Minigames")

    font = pygame.font.SysFont("Arial", 40)

    intro = pygame.image.load("resurseMain/BG2.png")
    window.blit(intro, (0,0))
    pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(2000)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        show_menu(window)
        pygame.display.update()

    pygame.quit()
    quit()

if __name__ == "__main__":
    meniu()
