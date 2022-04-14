booleanos = [False, True]

#Tabla de verdad de or

print('x\ty\tx or y')  #\t es tabulación
print('-'*22)  

for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep = '\t')

print()        

#tabla de verdad de and
print('x\ty\tx and y')
print('-'*22)

for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, sep='\t')

print()    

#tabla de verdad de not
print('x\tnot x')
print('-'*15)
for x in booleanos:
    print(x, not x, sep='\t')

print()    

#tabla de verdad de and
print('x\t y\tx and y\t x nand y')
print('-'*35)

for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, not(x and y), sep='\t ')

print()  


