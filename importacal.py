import calendar
import datetime
import csv
def impostacalendario():
    mese = input("Dimmi il mese ")
    anno = input("Dimmi l'anno ")
    totale_giorni = calendar.monthrange(int(anno), int(mese))[1]
    giornidelmese = ['        ']
    numgiorni = ['        ']
    nome_giorno = ''
    i = 1
    while i <= totale_giorni:
        ng = calendar.day_name[calendar.weekday(int(anno), int(mese), i)]
        if ng == 'Sunday':
            nome_giorno = 'D'
        elif ng == 'Monday':
            nome_giorno = 'L'
        elif ng == 'Tuesday':
            nome_giorno = 'M'
        elif ng == 'Wednesday':
            nome_giorno = 'M'
        elif ng == 'Thursday':
            nome_giorno = 'G'
        elif ng == 'Friday':
            nome_giorno = 'V'
        elif ng == 'Saturday':
            nome_giorno = 'S'
        giornidelmese.append(i)
        numgiorni.append(nome_giorno)
        print(nome_giorno, i)
        i += 1
    
    with open('cal.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow('')
        writer.writerow('')
        writer.writerow(giornidelmese)
        writer.writerow(numgiorni)
impostacalendario()


