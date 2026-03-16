# Calendario

import calendar

print(calendar.calendar(2026))  # Imprime o calendário do ano
print(calendar.month(2026, 3))  # Imprime o calendário do mês

print(
    calendar.monthrange(2026, 3)
)  # Retona o primeiro dia do mês e o número de dias do mês
first_day, last_day = calendar.monthrange(2026, 3)
print(first_day, last_day)

print(list(calendar.day_name))  # Imprime os nomes dos dias da semana

print(
    calendar.weekday(2026, 3, last_day)
)  # Retorna o número do dia da semana, onde 0 é segunda-feira e 6 é domingo
print(calendar.weekday(2026, 3, 1))

print(
    calendar.monthcalendar(2026, 3)
)  # Retorna uma lista de semanas, onde cada semana é uma lista de dias do mês.
# Os dias que não pertencem ao mês são representados por 0.

# Imprime os dias do mês de março de 2026
for week in calendar.monthcalendar(2026, 3):
    for day in week:
        if day == 0:
            continue
        print(day)
