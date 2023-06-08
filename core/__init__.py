import datetime
import pandas as pd

months = ['janeiro', 'fevereiro', 'março', 'abriu', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',  'novembro', 'dezembro']

class SystemInfo():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        day = now.day
        month = months[now.month - 1]
        answer = "Hoje é {} de {}".format(day, month)
        return answer