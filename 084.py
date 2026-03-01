temp = list()
princ = list()
mai = men = 0
while True:
     temp.append(str(input('nome: ')))
     temp.append(float(input('peso: ')))
     if len(princ) == 0:
          mai = men = temp[1]
     else:
          if temp[1] > mai:
              mai = temp[1]
          if temp[1] < men:
              men = temp[1]
     princ.append(temp[:])
     temp.clear()
     resp =str(input('quer continuar [s/n]? '))
     if resp in 'Nn':
        break
print(f'temos o total de {len(princ)}')
print(f'o maior peso é {mai}kg o peso de ',end='')
for p in princ:
     if p[1] == mai:
          print(f'{p[0]}',end='')
print()
print(f'o menor peso é  {men}kg o peso de ',end='')
for p in princ:
     if p[1] == men:
          print(f'{p[0]}')
print()

