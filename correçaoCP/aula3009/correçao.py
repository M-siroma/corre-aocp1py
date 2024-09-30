sal = float(input("salario:"))

# cauculo do inss
if sal <= 1412:
    inss = sal * 0.075 - 0
elif sal <= 2666.68:
    inss = sal * 0.09 - 21.18
elif sal <= 4000.03:
    inss = sal * 0.12 - 101.18
elif sal <= 7786.02:
    inss = sal * 0.14 - 181.1
else:
    inss = 7786.02 * 0.14

# cauculo imposto de renda
if sal <= 2259.20:
    ir = sal *0
elif sal <= 2826.65:
    ir = sal * 0.75 - 169.44
elif sal <= 3751.05:
    ir = sal * 0.15 - 381.44
elif sal <= 4664.68:
    ir = sal * 0.225 - 662.77
else:
    ir = sal * 0.275 - 896
    
# calcular o salario liquido
salario_liquido = sal - inss -ir 
#exibir o relatorio 
print(f"""
salario brudo...:{sal}
inss............:{inss}
ir..............:{ir}
salario liquido.:{salario_liquido}
""")