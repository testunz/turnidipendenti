import datetime
import calendar
import random
import csv

class Persona:
    def __init__(self, nome, cognome, ruolo, notte, skill):
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        self.notte = notte
        self.skill = skill
        self.turni_effettuati = 0
        self.turni = []
        self.prefestivi = []
        self.festivi = []

    def nomecognome(self):
        return f"{self.nome} {self.cognome}"
