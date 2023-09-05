#1 - Calcular a media, moda e mediana dos valores das alturas da sala

from statistics import StatisticsError, mean, median, mode

# Dicionário com nomes como chaves e alturas como valores
pessoas = {
    'alexandre': 1.73,
    'alisson': 1.63,
    'ana': 1.90,
    'antonia': 1.70,
    'bruno henrique': 1.70,
    'bruno matheus': 1.93,
    'christian': 1.70,
    'eduardo': 1.78,
    'grabriel': 1.68,
    'george': 1.70,
    'matias': 1.78,
    'paulo': 1.68,
    'sergio': 1.75,
    'victor': 1.67,
    'vinicios': 1.80,
    'carol': 1.73,
    'anao': 0.20
}

# Calcular média, mediana e moda
alturas = list(pessoas.values())

media_alturas = mean(alturas)
mediana_alturas = median(alturas)

try:
    moda_alturas = mode(alturas)
except StatisticsError:
    moda_alturas = "Não há moda única"

print(f"Média das alturas: {media_alturas:.2f}")
print(f"Mediana das alturas: {mediana_alturas:.2f}")
print(f"Moda das alturas: {moda_alturas}")
