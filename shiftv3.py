import datetime
import calendar
import random
import csv

class Operatore:

    def __init__(self, nome, cognome, ruolo, notte, skill, ferie, preferenze, aggiornamento, h12):
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        self.notte = notte
        self.skill = skill
        self.turni_effettuati = 0  #numero totale turni effettuati dal singolo operatore
        self.turni_max = 0
        self.ore_totali = 0      #numero totale ore effettuate dal singolo
        self.prefestivi = []            #prefestivi o festivi sotto per singolo operatore
        self.festivi = []
        self.turni = []                 #elenco striscia del mese dei turni per singolo operatore
        self.ferie = ferie
        self.preferenze = preferenze
        self.aggiornamento = aggiornamento
        self.h12 = h12

    def nomecognome(self):
        return f"{self.cognome}" # {self.nome}

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
        self.operatori = []
        self.minuti_turno_mp = 380
        self.minuti_turno_n = 760
        self.minuti_turno_a = 240

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
            self.operatori.append(Operatore(op[0], op[1], op[2], op[3], op[4], op[5].split(';'), op[6].split(';'), op[7], op[8]))
        for op in self.operatori:
            if op.ruolo == 'd':
                op.turni_max = self.turni_dir
            elif op.ruolo == 'c':
                op.turni_max = self.turni_conv

            print(op.ferie, op.preferenze, op.aggiornamento, op.h12) #for da eliminare, serve solo per controllare inserimento di ferie e preferenze giorni liberi

    def popola_cal(self):
        conto_iterazioni = 0
        numgg = 1
        while numgg <= self.num_giorni_mese:
            self.giorni.append(Giorno(numgg))
            numgg += 1
        i = 0
        while i < len(self.giorni):
            self.giorni[i].gma = str(i + 1) + '/' + self.mese + '/' + self.anno
            self.giorni[i].nome_giorno = calendar.day_name[calendar.weekday(int(self.anno), int(self.mese), i + 1)]
            op_meno_turni = list(sorted(self.operatori, key=lambda x: x.turni_effettuati))
            while ((op_meno_turni[-1].turni_effettuati - op_meno_turni[0].turni_effettuati) > 3):
                op_meno_turni.pop()
            while len(self.giorni[i].mattina) < 3:
                conto_iterazioni += 1
                op = random.choice(op_meno_turni)
                if op not in self.giorni[i].mattina and op not in self.giorni[i-1].notte and op.turni_effettuati < op.turni_max: # and op not in self.giorni[i-2].notte:
                    self.giorni[i].mattina.append(op)
                    op.turni_effettuati += 1
                    op.ore_totali += self.minuti_turno_mp
                if conto_iterazioni >1000000:
                    conto_iterazioni = 0
                    return False
            while len(self.giorni[i].pomeriggio) < 2:
                conto_iterazioni += 1
                op = random.choice(op_meno_turni)
                if op not in self.giorni[i].mattina and op not in self.giorni[i].pomeriggio and op not in self.giorni[i-1].notte and op.turni_effettuati < op.turni_max:
                    self.giorni[i].pomeriggio.append(op)
                    op.turni_effettuati +=1
                    op.ore_totali += self.minuti_turno_mp
                if conto_iterazioni > 1000000:
                    conto_iterazioni = 0
                    return False

            while len(self.giorni[i].notte) < 2:
                conto_iterazioni += 1
                op = random.choice(op_meno_turni)
                if op not in self.giorni[i].mattina and op not in self.giorni[i].pomeriggio and op not in self.giorni[i].notte and op not in self.giorni[i-1].notte and op.turni_effettuati < (op.turni_max - 1):
                    self.giorni[i].notte.append(op)
                    op.turni_effettuati += 2
                    op.ore_totali += self.minuti_turno_n
                if conto_iterazioni > 1000000:
                    conto_iterazioni = 0
                    return False



            i += 1

        for op in self.operatori:
            print(op.nomecognome(), op.turni_effettuati)

        return True


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
            print(op.nomecognome(), op.turni_effettuati, op.turni_max) #round(op.ore_totali, 2))

    def reset(self):
        for op in self.operatori:
            op.turni_effettuati = 0
            op.ore_totali = 0
        while self.giorni:
            self.giorni.pop()
        print(self.giorni)


maggio = Calendario()
maggio.calcola_numturni_operatore()
maggio.lista_operatori()
riuscito = False
while riuscito == False:
    maggio.reset()
    print('Ricalcolo')
    riuscito = maggio.popola_cal()

maggio.stampa_cal()
