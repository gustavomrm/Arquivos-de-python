peso = float(input(f'Informe o seu peso:'))
altura = float(input(f'informe a sua altura:'))

imc = (peso / (altura * altura) )
print(f'O seu IMC é: {imc}')