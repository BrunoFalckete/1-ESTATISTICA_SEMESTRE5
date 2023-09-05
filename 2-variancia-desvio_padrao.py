#1 - Calcular a variancia do array do exercicio anterior
#2 - Calcular o desvio padrao da variancia

import numpy as np

alturas = [
    1.73, 1.63, 1.90, 1.70, 1.70, 1.93, 1.70, 1.78, 1.68, 1.70,
    1.78, 1.68, 1.75, 1.67, 1.80, 1.73, 0.20
]

# Passo 1: Calcular a média
media_alturas = np.mean(alturas)

# Passo 2: Calcular as diferenças e os quadrados das diferenças
diferencas_quadradas = [(altura - media_alturas) ** 2 for altura in alturas]

# Passo 3: Calcular a variância
variancia = np.mean(diferencas_quadradas)

# Passo 4: Calcular o desvio padrão
desvio_padrao = np.sqrt(variancia)

print("Variância:", variancia)
print("Desvio Padrão:", desvio_padrao)

#Tarefa: Encontrar aplicaçoes computacionais praticas quem envolvem vaviancia e desvio padrao (APRESENTACAO DIA 22/08 TRAZER VARIOS EXEPLOS POIS NAO PODERA REPTIR: TEMPO DE APRESENTAÇÃO MAXIMO DE 2MIN)
