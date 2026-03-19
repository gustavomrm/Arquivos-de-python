var1 = float(input("Escreva o valor da primeira variável: "))
var2 = float(input("Escreva o valor da segunda variável: "))

print(f'Antes da troca: {var1, var2}')

var3 = var1
var1 = var2
var2 = var3

print(f'Depois da troca: {var1, var2}')