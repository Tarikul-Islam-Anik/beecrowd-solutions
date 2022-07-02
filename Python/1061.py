start_day = input().split()
starting_hour = input().split()
end_day = input().split()
ending_hour = input().split()
dia_start, dia_final = int(start_day[1]), int(end_day[1])
h_start, minute_start, second_start = (
    int(starting_hour[0]),
    int(starting_hour[2]),
    int(starting_hour[4]),
)
h_end, minute_end, second_end = (
    int(ending_hour[0]),
    int(ending_hour[2]),
    int(ending_hour[4]),
)

minutes = 60
hours = minutes * 60
days = hours * 24
start, end = (
    second_start + minute_start * minutes + h_start * hours + dia_start * days,
    second_end + minute_end * minutes + h_end * hours + dia_final * days,
)

if start < end:
    difference = end - start
    dias = int(difference / days)
    difference = difference % days
    horas = int(difference / hours)
    difference = difference % hours
    minutos = int(difference / minutes)
    difference = difference % minutes
    segundos = difference
    print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")
