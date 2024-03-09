from enum import Enum
import pygame
import random

class Simbol(Enum):
    C = 0 # TREFLA
    R = 1 # INIMA NEAGRA
    v = 2 # INIMA ROSIE
    S = 3 # ROMB

class Carte:
    simbol = None
    valoare = None
    imagine = None

    def __init__(self, simbol, valoare):
        self.simbol = simbol
        self.valoare = valoare
        numar = ""
        if self.valoare < 10:
            numar = "0" + str(self.valoare)
        else:
            numar = str(self.valoare)
        self.imagine = pygame.image.load("resurseJoc/carduri/" + numar + self.simbol.name + ".png")
        self.imagine = pygame.transform.scale(self.imagine, (223, 312))

class Pachet:
    carti = None

    def __init__(self):
        self.carti = []
        for simbol in Simbol:
            for valoare in range(1, 15):
                if valoare != 11:
                    self.carti.append(Carte(simbol, valoare))

    def amesteca(self):
        random.shuffle(self.carti)

    def imparte(self):  # scoate ultima carte din pachet
        return self.carti.pop()

    def length(self):  # intoarce numarul de carti ramase in pachet
        return len(self.carti)

class TeancDeCarti:
    carti = None

    def __init__(self):
        self.carti = []

    def adauga(self, carte):
        self.carti.append(carte)

    def scoate(self):
        if (len(self.carti) > 0):
            return self.carti[-1]
        else:
            return None

    def scoateToate(self):
        return self.carti

    def elibereazaPachet(self):
        self.carti = []

    def esteSnap(self):
        if (len(self.carti) > 1):
            return self.carti[-1].valoare == self.carti[-2].valoare
        else:
            return False

class Jucator:
    mana = None
    nume = None
    tasta_flip = None
    tasta_snap = None

    def __init__(self, nume, tasta_flip, tasta_snap):
        self.mana = []
        self.nume = nume
        self.tasta_flip = tasta_flip
        self.tasta_snap = tasta_snap

    def trage(self, pachet):  # primeste cartile
        self.mana.append(pachet.imparte())

    def joaca(self):  # joaca o carte
        return self.mana.pop(0)
