from enum import Enum
import pygame
from Snap.objects import *

class StareJoc(Enum):
    JOC = 0
    SNAP = 1
    FINAL = 2

class SnapEngine:  # logica jocului
    pachet = None
    jucator1 = None
    jucator2 = None
    teanc = None
    stare = None
    jucatorCurent = None
    rezultat = None
    scor_jucator1 = 0
    scor_jucator2 = 0
    pot_aplica_sunet_final = 0

    def __init__(self):
        self.pachet = Pachet()
        self.pachet.amesteca()
        self.jucator1 = Jucator("Jucator 1", pygame.K_a, pygame.K_d)
        self.jucator2 = Jucator("Jucator 2", pygame.K_LEFT, pygame.K_RIGHT)
        self.teanc = TeancDeCarti()
        self.imparteCarti()
        self.jucatorCurent = self.jucator1
        self.stare = StareJoc.JOC
        self.scor_jucator1 = 0
        self.scor_jucator2 = 0
        self.pot_aplica_sunet_final = 0

    def imparteCarti(self):
        jumatate_de_pachet = self.pachet.length() // 2
        for i in range(0, jumatate_de_pachet):
            self.jucator1.trage(self.pachet)
            self.jucator2.trage(self.pachet)

    def schimbaJucator(self):
        if self.jucatorCurent == self.jucator1:
            self.jucatorCurent = self.jucator2
        else:
            self.jucatorCurent = self.jucator1

    def castigaRunda(self, jucator):
        self.stare = StareJoc.SNAP
        jucator.mana.extend(self.teanc.scoateToate())
        self.teanc.elibereazaPachet()

    def joacaJoc(self, tasta):
        if tasta == None:
            return

        if self.stare == StareJoc.FINAL:
            return # de adaugat aici sa se poata incepe un joc nou

        if tasta == self.jucatorCurent.tasta_flip:
            self.teanc.adauga(self.jucatorCurent.joaca())  # jucatorul curent joaca o carte
            self.schimbaJucator()

        snapCaller = None
        nonSnapCaller = None
        isSnap = self.teanc.esteSnap()

        if tasta == self.jucator1.tasta_snap:
            snapCaller = self.jucator1
            nonSnapCaller = self.jucator2

        elif tasta == self.jucator2.tasta_snap:
            snapCaller = self.jucator2
            nonSnapCaller = self.jucator1

        if isSnap and snapCaller:  # daca este Snap si a fost dat
            self.castigaRunda(snapCaller)
            self.rezultat = {
                "castigator": snapCaller,
                "este_snap": True,
                "snapCaller": snapCaller
            }
            self.castigaRunda(snapCaller)
        elif not isSnap and snapCaller:  # daca nu este Snap si a fost dat
            self.rezultat = {
                "castigator": nonSnapCaller,
                "este_snap": False,
                "snapCaller": snapCaller
            }
            self.castigaRunda(nonSnapCaller)

        if len(self.jucator1.mana) == 0:
            self.rezultat = {
                "castigator": self.jucator2,
            }
            self.stare = StareJoc.FINAL
        elif len(self.jucator2.mana) == 0:
            self.rezultat = {
                "castigator": self.jucator1,
            }
            self.stare = StareJoc.FINAL
