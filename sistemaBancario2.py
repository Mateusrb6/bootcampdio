def inicio():
    print('Sistema bancário'.center(32, "="))

def opcoes():
    print("""
    Selecione uma opção:  
    1) Depositar
    2) Sacar
    3) Extrato
    4) Sair
    """
)

saldo = 0
extrato = []
saques_maximos = 3
numero_saques = 0


while True:
    inicio()
    opcoes()

    try:
        opcao = int(input('Opção: '))
    except ValueError:
        print('Opção inválida. Tente novamente.')
        continue

    match opcao:
        case 1:
            print('DEPÓSITO')
            try:
                deposito = float(input('Quanto deseja depositar? '))
            except ValueError:
                print('Valor inválido. Tente novamente.')
                continue

            if deposito > 0:
                saldo += deposito
                extrato.append(f'Depósito: +R${deposito:.2f}')
                print(f'Você depositou R${deposito:.2f}')  
            else:
                print('Valor inválido. O depósito deve ser positivo e diferente de zero.')

        case 2:
            print('SAQUE')
            if numero_saques >= saques_maximos:
                print('Número de saques máximo atingido.')
                continue

            try:
                saque = float(input('Quanto deseja sacar? '))
            except ValueError:
                print('Valor inválido. Tente novamente.')
                continue

            if saque > 0:
                if saque <= saldo:
                    saldo -= saque
                    extrato.append(f'Saque: -R${saque:.2f}')
                    numero_saques += 1
                    print(f'Você sacou R${saque:.2f}')
                else:
                    print('Saldo insuficiente.')
            else:
                print('Valor inválido. O saque deve ser positivo.')

        case 3:
            print('EXTRATO')
            if extrato:
                for item in extrato:
                    print(item)
                print(f'Saldo atual: R${saldo:.2f}')
            else:
                print('Não há transações para exibir.')

        case 4:
            print('Saindo...')
            break

        case _:
            print('Opção inválida. Tente novamente.')

