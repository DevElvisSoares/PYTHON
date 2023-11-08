entrada = input('[E] para entrar e [P] para passar: ')
senha_digitada = input('Digite a senha de acesso: ')
senha = "15975312"

if (entrada == 'E' or entrada == 'e'):
    if (senha == senha_digitada):
        print("Sucesso, você entrou")
    else:
        print("você não entrou, senha incorreta")
elif (entrada == 'S' or entrada == 's'):
    if(senha == senha_digitada):
       print("Você escolheu passar!")

else:
    print("Você não selecionou uma opção valida")