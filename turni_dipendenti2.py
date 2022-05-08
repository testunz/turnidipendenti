import datetime
import calendar
import random
import csv

class Operatore:
    def __init__(self, nome, cognome, ruolo, notte, aggiornamento, skill):
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        self.notte = notte
        self.aggiornamento = aggiornamento #se fa turni di aggiornamento (il convenzionato non fa turni aggiornamento)
        self.skill = skill
        self.turni_effettuati = 0 #numero totale turni effettuati dal singolo operatore
        self.ore_totali = float(0) #numero totale ore effettuate dal singolo
        self.prefestivi = [] #prefestivi o festivi sotto per singolo operatore
        self.festivi = []
        self.turni = [] #elenco striscia del mese dei turni per singolo operatore

    def nomecognome(self):
        return f"{self.nome} {self.cognome}"

class Giorno:
    def __init__(self):
       self.gma = ''
       self.mattina = []
       self.pomeriggio = []
       self.notte = []
       self.aggiornamento = []

class Turno:
    def __init__(self, tipo_turno, ore_turno, peso_turno, operatore):
        self.tipo_turno = tipo_turno
        self.ore_turno = ore_turno
        self.peso_turno = peso_turno
        self.operatore = operatore #nome operatore che sta facendo quel turno

class Calendario: 
    def __init__(self):
        self.mese = ''
        self.anno = ''
        self.giorni = [] #la lista all'interno della quale salviano tutti gli oggetti giorno creati con dentro turni ed operatori di quello specifico giorno
        self.num_giorni_mese = 0
        self.totale_turni = 0
        self.turni_dir = 0
        self.turni_conv = 0
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
        print(self.turni_dir) #output da cancellare

        
        #    totale_giorni = calendar.monthrange(int(anno), int(mese))[1]
 
stampa = Calendario()
stampa.calcola_numturni_operatore()
#print(stampa.anno)
print(stampa.num_giorni_mese)

