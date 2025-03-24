# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime("20/04/1987 09:30:30", fmt)
data_fim = datetime.strptime("20/11/2024 16:37:30", fmt)
delta = timedelta(days=10)
delta1 = relativedelta(data_fim, data_inicio)
# print(data_fim + delta)
print(data_fim)
print(data_fim + relativedelta(seconds=60, minutes=10,months=90))
print(delta1.day, delta1.years, delta1.months)

# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_inicio < data_fim)
# print(data_inicio > data_fim)
# print(data_inicio == data_fim)