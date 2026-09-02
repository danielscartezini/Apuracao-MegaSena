import csv
import random

def gerar_aposta():
    numeros = random.sample(range(1, 61), 6) # 6 números
    return ["AP-A1B2C3"] + numeros

with open('apostas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(gerar_aposta())

# Adicione esta função ao seu gerador.py
def aposta_valida(numeros):
    return 6 <= len(numeros) <= 15