from time import sleep
from threading import Thread

def vai_demorar(texto,tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá Mundo! 1', 5))
t1.start()

while t1.is_alive():
    print('Esperando a thread')
    sleep(2)

print("Thread acabou!!")