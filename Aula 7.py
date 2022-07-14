# n = 5+3*2
# print(n)
# n1 = 3*5+4**2
# print(n1)
# n2 = 3*(5+4)**2
# print(n2)
# nome = input('Por favor digite o seu nome: ')
# print('Prazer em te conhecer {:20}!' .format(nome))
# print('Prazer em te conhecer {:>20}!' .format(nome))
# print('Prazer em te conhecer {:<20}!' .format(nome))
# print('Prazer em te conhecer {:^20}!' .format(nome))
# print('Prazer em te conhecer {:=^20}!' .format(nome))

n1= int(input('Por favor digite um número: '))
n2= int(input('Por favor digite outro número: '))
s= n1+n2
m= n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}, a multiplicação vale {}, a divisão inteira vale {:.3f} \n'
      'A divisão real vale {} e a potencia do primeiro pelo seegundo número vale {}'
      .format(s, m, d, di, e))
