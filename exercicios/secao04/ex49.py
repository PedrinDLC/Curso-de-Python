"""
Exercicio 49:

Faça um programa que leia um horário (horas,minutos,segundos) de inicio
e a duração, em segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora,minuto,segundo) do termino da mesma.

"""

print("Digite o horário inicial da experiência:")
hora = int(input("Hora: "))
minuto = int(input("Minutos: "))
segundos = int(input("Segundos: "))

duracao_experiencia = int(input("Digite quanto tempo durou a experiência, em segundos: "))

conversao_hora = int((duracao_experiencia / 3600))
conversao_minutos = int((duracao_experiencia / 60) % 60)
conversao_segundos = int((duracao_experiencia % 60) % 60)

hora_total = hora + conversao_hora
minuto_total = minuto + conversao_minutos
segundos_total = segundos + conversao_segundos
dia = 0

while hora_total >= 24 or minuto_total >= 60 or segundos_total >= 60:
    if segundos_total >= 60:
        segundos_total = segundos_total - 60
        minuto_total = minuto_total + 1
    if minuto_total >= 60:
        minuto_total = minuto_total - 60
        hora_total = hora_total + 1
    if hora_total >= 24:
        hora_total = hora_total - 24
        dia = dia + 1

print(f"Hora inicial: {hora}:{minuto}:{segundos}\n")

print(f"A experiência terminou em : +{dia} Dia(s) ás {hora_total}:{minuto_total}:{segundos_total}")
