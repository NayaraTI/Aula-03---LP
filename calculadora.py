
numero1 =0
numero2 =0
resultado = 0
operação = ''

numero1 = int(input("Digite o número 1:  "))
operação = input("Digite a operação: ")
numero2 = int(input("Digite o número 2: "))

if operação =='+':
    resultado = numero1+numero2
elif operação == '-':
    resultado = numero1 - numero2
elif operação == '/':
    resultado = numero1 / numero2
elif operação == '*':
    resultado = numero1 * numero2
else:
    resultado = 'Operação Inválida'
    
print(str (numero1) + '' + str (operação) + '' + str (numero2) + '=' + str (resultado))




