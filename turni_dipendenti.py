import datetime
import calendar
import random
import csv

class Persone:
    def __init__(self, nome, cognome, notte):
        self.nome = nome
        self.cognome = cognome
        self.notte = notte
        self.numero_turni = 0

    def nomecognome(self):
        return f"{self.nome} {self.cognome}"

class Giorno:
    def __init__(self):
        self.gma = 0
        self.nome_giorno = ''
        self.mattina = []
        self.pomeriggio = []
        self.notte = []

class Calendario:
    def __init__(self):
        self.mese = ''
        self.anno = ''
        self.giorni = []
        self.totale_giorni = 0
        self.totale_turni = 0
        self.turni_persona = 0
        self.persone = []

    def azzera_turni_giorni(self):
        for i in self.persone:
            i.numero_turni = 0
        while self.giorni:
            self.giorni.pop()

    def calcola_giorni_turni(self):
        while self.mese not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            self.mese = input('Selezionare mese: \n  1 -> Gennaio \n  2 -> Febbraio \n  3 -> Marzo \n  4 -> Aprile \n  5 -> Maggio \n  6 -> Giugno \n  7 -> Luglio \n  8 -> Agosto \n  9 -> Settembre \n 10 -> Ottobre \n 11 -> Novembre \n 12 -> Dicembre \n ')
        date = datetime.date.today()
        self.anno = date.strftime("%Y")
        self.totale_giorni = calendar.monthrange(int(self.anno), int(self.mese))[1]
        if self.totale_giorni == 31:
            self.turni_persona = 26
        elif self.totale_giorni == 30:
               self.turni_persona = 25
        elif self.totale_giorni == 28:
               self.turni_persona == 24
           # print('Febbraio')
        #else:
        print(self.mese, self.anno, self.totale_giorni, self.turni_persona)

    def lista_persone(self):
        pp = []
        with open('dipendenti.csv', 'r') as file:
            reader = csv.reader(file, delimiter  = ';')
            for each_row in reader:
                pp.append(each_row)
        pp.pop(0)
        for p in pp:
            self.persone.append(Persone(p[0], p[1], p[2]))
        i = 0

        for i in self.persone:
            print(i.nomecognome())

    def popola_calendario(self):
        i = 0
        while i < self.totale_giorni:
            g = Giorno()
            g.gma = str(i + 1) + '/' + self.mese + '/' + self.anno
            g.nome_giorno = calendar.day_name[calendar.weekday(int(self.anno), int(self.mese), i + 1)]
            dip_meno_turni = sorted(self.persone, key=lambda x: x.numero_turni)
            while ((dip_meno_turni[-1].numero_turni - dip_meno_turni[0].numero_turni) > 4):
                dip_meno_turni.pop()
            if i == 0:
                while len(g.mattina) < 2:
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina:
                        g.mattina.append(p)
                        p.numero_turni += 1
                while len(g.pomeriggio) < 2:
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in g.pomeriggio:
                        g.pomeriggio.append(p)
                        p.numero_turni += 1
                while len(g.notte) < 2:
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in g.pomeriggio and p not in g.notte:
                        g.notte.append(p)
                        p.numero_turni += 2
                self.giorni.append(g)
            elif i == 1:
                while len(g.mattina) < 2:
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in self.giorni[i-1].notte:
                        g.mattina.append(p)
                        p.numero_turni += 1
                while len(g.pomeriggio) < 2:
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in g.pomeriggio and p not in self.giorni[i-1].notte:
                        g.pomeriggio.append(p)
                        p.numero_turni += 1
                while len(g.notte) < 2:
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in g.pomeriggio and p not in g.notte and p not in self.giorni[i-1].notte:
                        g.notte.append(p)
                        p.numero_turni += 2
                self.giorni.append(g)
            else:
                x = 0
                while len(g.mattina) < 2:
                    x += 1
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in self.giorni[i-1].notte and p not in self.giorni[i-2].notte and p.numero_turni < 26:
                        g.mattina.append(p)
                        p.numero_turni += 1
                    if x > 1000000:
                        x = 0
                        return False
                while len(g.pomeriggio) < 2:
                    x += 1
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in g.pomeriggio and p not in self.giorni[i-1].notte and p not in self.giorni[i-2].notte and p.numero_turni < 26:
                        g.pomeriggio.append(p)
                        p.numero_turni += 1
                    if x > 1000000:
                        x = 0
                        return False
                while len(g.notte) < 2:
                    x += 1
                    p = random.choice(dip_meno_turni)
                    if p not in g.mattina and p not in g.pomeriggio and p not in g.notte and p not in self.giorni[i-1].notte and p not in self.giorni[i-2].notte and p.numero_turni < 25:
                        g.notte.append(p)
                        p.numero_turni += 2
                    if x > 1000000:
                        x = 0
                        return False
                self.giorni.append(g)
            i += 1
        print('uscito dal while')
        return True

    def stampa_calendario(self):
        for t in self.giorni:
            d = t.gma
            data = d.ljust(80)
            m = 'MATTINA'
            mat = m.ljust(40)
            p = 'POMERIGGIO'
            pom = p.ljust(40)
            n = 'NOTTE'
            notte = n.ljust(40)
            m1 = t.mattina[0].nomecognome()
            mat1 = m1.ljust(40)
            m2 = t.mattina[1].nomecognome()
            mat2 = m2.ljust(40)
            p1 = t.pomeriggio[0].nomecognome()
            pom1 = p1.ljust(40)
            p2 = t.pomeriggio[1].nomecognome()
            pom2 = p2.ljust(40)
            n1 = t.notte[0].nomecognome()
            notte1 = n1.ljust(40)
            n2 = t.notte[1].nomecognome()
            notte2 = n2.ljust(40)
            print('-' * 120)
            print(t.gma)
            print('-' * 120)
            print(mat, pom, notte)
            print(mat1, pom1, notte1)
            print(mat2, pom2, notte2)
        print()

    def salva_calendario(self):
        with open('calendario.csv', 'w') as file:
            writer = csv.writer(file)

            for t in self.giorni:
                d = ['', t.gma]
                vuota = ['']
                intestazione = ['MATTINA', 'POMERIGGIO', 'NOTTE']
                m1 = t.mattina[0].nomecognome()
                m2 = t.mattina[1].nomecognome()
                p1 = t.pomeriggio[0].nomecognome()
                p2 = t.pomeriggio[1].nomecognome()
                n1 = t.notte[0].nomecognome()
                n2 = t.notte[1].nomecognome()
                f = [m1, p1, n1]
                s = [m2, p2, n2]
                writer.writerow(d)
                writer.writerow(intestazione)
                writer.writerow(f)
                writer.writerow(s)
                writer.writerow(vuota)


    def stampa_numero_turni(self):
        for t in self.persone:
            print(t.nomecognome(), t.numero_turni)

nuovo = Calendario()
nuovo.lista_persone()
nuovo.calcola_giorni_turni()
riuscito = False
while riuscito == False:
    nuovo.azzera_turni_giorni()
    print('riparto')
    riuscito = nuovo.popola_calendario()
nuovo.stampa_calendario()
nuovo.stampa_numero_turni()
nuovo.salva_calendario()
print('finito')
