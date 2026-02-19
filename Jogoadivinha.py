from random import randint
from time import sleep
cont = 1

computador = randint(0, 10)
numero = int(input('informe um número entre 1 e 10: '))
print ('aguarde, estou gerando um número')
sleep(3)
while numero != computador:
    print("Tente novamente, você errou.")
    numero = int(input("informe um número entre 1 e 10: "))
    sleep(3)
    cont += 1
print("Parabéns, você acertou, o número que pensei foi o {} e você levou {} tentativas para acertar".format(computador,cont))