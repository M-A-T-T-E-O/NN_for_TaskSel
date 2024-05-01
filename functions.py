import random
def calcola_probabilita_rilevamento(distanza_target, angolo_rispetto_target, altezza, velocita_vento):
    # Simulazione della probabilità di rilevamento basata sulle caratteristiche dell'input
    probabilita_rilevamento = (distanza_target / 10000) * (angolo_rispetto_target / 90) * (altezza / 20000) * (
                velocita_vento / 40)
    return probabilita_rilevamento
def prendi_decisione(distanza_target, angolo_rispetto_target, altezza, velocita_vento):
    # Calcolo della probabilità di rilevamento in base alle caratteristiche dell'input
    probabilita_rilevamento = calcola_probabilita_rilevamento(distanza_target, angolo_rispetto_target, altezza,
                                                              velocita_vento)

    # Se la probabilità di rilevamento è alta, adotta una strategia conservativa per ridurla
    if probabilita_rilevamento > 0.5:
        azione = "Rallenta_e_scendi_di_quota"
    # Altrimenti, continua sulla traiettoria corrente
    else:
        azione = "Continua_sulla_traiettoria_corrente"

    return azione

# Creazione del dataset
counter1 = 0
counter2 = 0
dataset = []
while (counter1 <= 100 or counter2 <= 100):
    distanza_target = random.randint(500, 10000)  # miglia nautiche
    angolo_rispetto_target = random.randint(0, 90)  # gradi
    altezza = random.randint(1000, 20000)  # piedi
    velocita_vento = random.randint(0, 40)  # nodi

    azione = prendi_decisione(distanza_target, angolo_rispetto_target, altezza, velocita_vento)

    if (azione == "Continua_sulla_traiettoria_corrente" and counter1 <= 100):
        counter1 = counter1 + 1
        riga = [distanza_target, angolo_rispetto_target, altezza, velocita_vento, azione]
        dataset.append(riga)

    if (azione == "Rallenta_e_scendi_di_quota" and counter2 <= 100):
        counter2 = counter2 + 1
        riga = [distanza_target, angolo_rispetto_target, altezza, velocita_vento, azione]
        dataset.append(riga)

# Salvataggio del dataset su file
with open("dataset.csv", "w") as file:
    file.write("Distanza_Target,Angolo_Rispetto_Target,Altezza,Velocita_Vento,Azione\n")
    for riga in dataset:
        riga_csv = ",".join(map(str, riga))
        file.write(riga_csv + "\n")

print("Dataset creato e salvato con successo!")