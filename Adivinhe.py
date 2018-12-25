import random


maiorValor = 10
resposta = random.randrange(maiorValor)
adivinhacao = raw_input('Adivinhe um numero entre 0 e 10 ')
while(int(adivinhacao) !=resposta):
    if(int(adivinhacao) < resposta):
        print 'a resposta e maior'
    else:
        print 'a resposta e menor'
    adivinhacao = raw_input('Adivinhe um numero entre 0 e 10 ')
raw_input('voce ganhou!!!')
