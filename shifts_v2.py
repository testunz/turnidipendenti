import datetime
import calendar
import random
import csv

class Operatore:

    def __init__(self, nome, cognome, ruolo, notte, skill, ferie, preferenze):
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        self.notte = notte
        self.skill = skill
        self.turni_effettuati = 0       #numero totale turni effettuati dal singolo operatore
        self.ore_totali = float(0)      #numero totale ore effettuate dal singolo
        self.prefestivi = []            #prefestivi o festivi sotto per singolo operatore
        self.festivi = []
        self.turni = []                 #elenco striscia del mese dei turni per singolo operatore
        self.ferie = ferie
        self.preferenze = preferenze


    def nomecognome(self):
        return f"{self.nome} {self.cognome}"

class Giorno:

    def __init__(self, gma):
       self.gma = gma
       self.nome_giorno = ''
       self.mattina = []
       self.pomeriggio = []
       self.notte = []
       self.aggiornamento = []

class Calendario:

    def __init__(self):
        self.mese = ''
        self.anno = ''
        self.giorni = []                #la lista all'interno della quale salviano tutti gli oggetti giorno creati con dentro turni ed operatori di quello specifico giorno
        self.num_giorni_mese = 0
        self.totale_turni = 0
        self.turni_dir = 0
        self.turni_conv = 0
        self.turni_agg = 4
        self.operatori = []

    def calcola_numturni_operatore(self):
        num_festivi = ''
        while num_festivi not in ['0','1','2','3','4']:
            num_festivi = input('Quanti giorni festivi ha questo mese (domeniche escluse)? se la festività è già domenica non si conta ')
        num_festivi = int(num_festivi)
        while self.mese not in ['1','2','3','4','5','6','7','8','9','10', '11', '12']:
            self.mese = input('Mese? (scrivi il numero del mese da 1 a 12)')

        data = datetime.date.today()
        self.anno = data.strftime("%Y")
        self.num_giorni_mese = calendar.monthrange(int(self.anno), int(self.mese))[1]
        nome_giorno = ''
        i = 1
        while i <= self.num_giorni_mese:
            ng = calendar.day_name[calendar.weekday(int(self.anno), int(self.mese), i)]
            if ng == 'Sunday':
                num_festivi += 1
            i += 1
        if self.num_giorni_mese == 31:
            self.turni_conv = 27

        elif self.num_giorni_mese == 30:
            self.turni_conv = 26
        else:
            self.turni_conv = 25
        self.turni_dir = self.num_giorni_mese - num_festivi

    def lista_operatori(self):
        listaop = []
        with open('operatori.csv', 'r') as file:
            reader = csv.reader (file)
            for riga in reader:
                listaop.append(riga)
        listaop.pop(0)
        for op in listaop:
            self.operatori.append(Operatore(op[0], op[1], op[2], op[3], op[4], op[5].split(';'), op[6].split(';')))
        for op in self.operatori:
            print(op.ferie, op.preferenze) #for da eliminare, serve solo per controllare inserimento di ferie e preferenze giorni liberi

    def popola_cal(self):
        numgg = 1
        while numgg <= self.num_giorni_mese:
            self.giorni.append(Giorno(numgg))
            numgg += 1
        for op in self.operatori:
            controllo_num_turni = 0
            if op.ruolo == 'd':
                controllo_num_turni = self.turni_dir
            elif op.ruolo == 'c':
                controllo_num_turni = self.turni_conv


    def stampa_cal(self):
        for g in self.giorni:
            print(g.gma)
            print('MATTINA')
            for op in g.mattina:
                print(op.nomecognome())
            print('POMERIGGIO')
            for op in g.pomeriggio:
                print(op.nomecognome())
            print('NOTTE')
            for op in g.notte:
                print(op.nomecognome())
        for op in self.operatori:
            print(op.nomecognome(), op.turni_effettuati, round(op.ore_totali, 2))

maggio = Calendario()
maggio.calcola_numturni_operatore()
maggio.lista_operatori()
#maggio.popola_cal()
#maggio.stampa_cal()
