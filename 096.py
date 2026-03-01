def area(larg,comp):
    a =  larg * comp
    print(f'a area de um terreno de {larg}x{comp} = {a}')

print('controle de terreno')
print('=-='*15)
l = float(input('largura(M): '))
c = float(input('comprimento(M): '))
area(l,c)