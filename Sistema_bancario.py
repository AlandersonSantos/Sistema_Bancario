

saldo = 0
saque = 0
VALOR_DEPOSITADO = 0
LIMITE_SAQUE = 3
NUMERO_DE_SAQUE = 0
LIMITE_VALOR = 500

while True:

    menu = """
=========================

    Escolha uma opção:
    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair
   
==========================
"""


    opcao = input(menu)

    if opcao.strip().upper() == "D":

        deposito = float(input("Deposite um valor: "))



        if deposito >= 0:

            print("Deposito realizado com sucesso...!!")
            VALOR_DEPOSITADO += deposito
            saldo += deposito

        else:

            print("Deposito não efetuado...")








    elif opcao.strip().upper() == "S":

        valor_saque = float(input("Informe o valor de saque: "))

        if saldo >= valor_saque > 0:

            if valor_saque <= LIMITE_VALOR:

                if NUMERO_DE_SAQUE < LIMITE_SAQUE:
                    NUMERO_DE_SAQUE += 1

                    print('Saque sendo efetuado...')
                    saldo -= valor_saque
                    saque += valor_saque

                else:
                    print('Bateu seu limite de saque diarios')
            else:
                print('Ultrapassou seu limite de saque')
        else:
            print("Saldo insuficiente para saque...")






    elif opcao.strip().upper() == "E":

        print("Extrato bancário".center(22,'='))
        print(f'Foi depositado o valor total de: R${VALOR_DEPOSITADO:.2f}')
        print(f'Seu saldo atual: R${saldo:.2f}')
        print(f'total de saque realizados: R$ -{saque:.2f}')





    elif opcao.strip().upper() == "Q":

        print("Sistama bancário, finalizado!!")
        break


    else:
        print('Opção não é valida, tente novamente!!')







