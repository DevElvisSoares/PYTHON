# Crie um código que receba o salário atual de um funcionário, que receba o valor em porcentagem de reajuste e calcule o valor do novo salário reajustado de acordo com valor de reajuste(%).
salario_atual = float(input("Informe o valor do seu salario em reais: "))
reajuste = float(input("Informe o valor do reajuste em porcentagem: "))
valor_do_reajuste = salario_atual *  reajuste / 100
salario_com_reajuste = salario_atual + valor_do_reajuste
print(f'O valor do salário com reajuste é R$ {salario_com_reajuste} ')