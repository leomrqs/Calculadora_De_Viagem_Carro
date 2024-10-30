# Parâmetros da viagem
distancia = 600.0 # em km
consumo = 12.0 # por litro
preco_combustivel = 5 # em reais
velocidade_media = 80 # em km
descanso_por_parada = 30  # em minutos
distancia_por_parada = 200 # em km

# Funções de cálculo
def calcular_combustivel(distancia, consumo):
    return distancia / consumo

def calcular_custo_combustivel(quantidade_combustivel, preco_combustivel):
    return quantidade_combustivel * preco_combustivel

def calcular_paradas(distancia, distancia_parada):
    return int(distancia / distancia_parada)

def calcular_tempo_viagem(distancia, velocidade_media):
    return distancia / velocidade_media

def converter_horas_minutos(horas):
    horas_inteiras = int(horas)
    minutos = int((horas - horas_inteiras) * 60)
    return horas_inteiras, minutos

# Cálculos
total_combustivel = calcular_combustivel(distancia, consumo)
custo_total_combustivel = calcular_custo_combustivel(total_combustivel, preco_combustivel)

quantidade_paradas = calcular_paradas(distancia, distancia_por_parada)
tempo_viagem_sem_parada = calcular_tempo_viagem(distancia, velocidade_media)

# Tempo adicional devido às paradas (em horas)
tempo_total_descanso = (quantidade_paradas * descanso_por_parada) / 60

# Tempo total de viagem com paradas
tempo_total_com_descanso = tempo_viagem_sem_parada + tempo_total_descanso

# Conversão para horas e minutos
horas_total, minutos_total = converter_horas_minutos(tempo_total_com_descanso)

# Resultados formatados
print(f"Total de Litros necessários para a viagem: {total_combustivel:.2f} L")
print(f"Custo total do combustível: R$ {custo_total_combustivel:.2f}")
print(f"Quantidade de paradas no trajeto: {quantidade_paradas} paradas")
print(f"Tempo total para percorrer o trajeto (sem paradas): {tempo_viagem_sem_parada:.2f} horas")
print(f"Tempo total com descanso: {tempo_total_com_descanso:.2f} horas")
print(f"Convertido para Horas e Minutos: {horas_total}h {minutos_total}min")
