nome_vendedor = (input("Informe o nome do vendedor: "))
qtd_vendas = float(input("informe a quantidade de vendas: "))
valor_total = float(input("Informe o valor total das vendas: "))

salario_base = float("1800")
comissao = float(150)

salario = float(comissao * qtd_vendas)
porcentagem = valor_total / 0.03
salario_final = (salario + porcentagem + salario_base) 
print(f'O salario final com as comissoes é: {salario_final}')
vendas = 0.3
