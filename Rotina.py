import datetime
import time

def hora_ok(hora, minuto, data_atual):
    if data_atual.hour == hora and data_atual.minute == minuto:
        return True
    return False

def dia_ok(dias, data_atual):
    if data_atual.weekday() == dias:
        return True
    return False

hora = 8
minuto = 30
dias = 1

while True:
    agora = datetime.datetime.now()

    if hora_ok(hora, minuto, agora) and dia_ok(dias, agora):
        print('Executando rotina!')
    time.sleep(60)