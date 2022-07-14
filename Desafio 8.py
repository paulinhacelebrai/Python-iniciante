# m = int(input('Por favor digite a medida em metros: '))
# c = m*100
# mi = m*1000
# print('A medida {} em centrimetros é igual a {} , e em milimetros é de {} .'.format(m, c, mi))
medida = float(input('Por favor digite uma medida em metros: '))
km = medida * (0.001)
hm = medida * (0.01)
dam = medida *(0.1)
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('o número {}m em km é igual a {} '.format(medida, km))
print('O número {}m em hm é igual a {} '.format(medida, hm))
print('O número {}m em dam é igual a {} '.format(medida, dam))
print('O número {}m em dm é igual a {} '.format(medida, dm))
print('O número {}m em cm é igual a {} '.format(medida, cm))
print('O número {}m em mm é gual a {} '.format(medida, mm))

