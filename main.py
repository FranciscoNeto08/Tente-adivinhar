from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número')
print('Duvido você acertar qual é o numero que estou pensando !!!')
acertou = False
palpites = 0
while not acertou:
  jogador = int(input('Qual é o seu palpite?'))
  palpites += 1
  if jogador == computador:
    acertou = True
    print('Parabéns, você advinhou o número que eu estou pensando !!!')
  else:
    if jogador < computador:
      print('Tente um número maior!')

    elif jogador > computador:
      print('Tente um número menor')

  

      


   

  

