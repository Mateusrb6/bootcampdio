def inicio():
    print('Sistema bancário'.center(32, "="))

def opcoes():
    print("""
    Selecione uma opção:  
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [mc] Mostrar contas
    [nu] Novo usuario
    [q] Sair
    """
    )
    opcao = str(input('').lower().strip())
    return opcao


def deposito(saldo, extrato):
    print('DEPÓSITO')
    try:
        deposito = float(input('Quanto deseja depositar? '))
    except ValueError:
        print('Valor inválido. Tente novamente.')
        return saldo, extrato
    
    if deposito > 0:
        saldo += deposito
        extrato.append(f'Depósito: +R${deposito:.2f}')
        print(f'Você depositou R${deposito:.2f}')  
    else:
        print('Valor inválido. O depósito deve ser positivo e diferente de zero.')
    return saldo, extrato

def saque(saldo, saque, extrato, limite, numero_saques, limite_saques):
    print('SAQUE')
    if numero_saques >= limite_saques:
        print('Limite de saques atingido')
        return saldo, extrato, numero_saques
    
    try:
        saque = float(input('Quanto deseja sacar? '))
    except ValueError:
        print('Valor inválido. Tente novamente.')

    if saque > saldo:
        print('Saldo insuficiente.')
    elif saque > limite:
        print('O valor do saque excede o limite.')
    else:
        saldo -= saque
        extrato.append(f'Saque: -R${saque:.2f}')
        numero_saques += 1
        print(f'Você sacou R${saque:.2f}')
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, / , *, extrato):
    if len(extrato) == 0:
        print('nao foram realizadas transacoes')
    else:
        for item in extrato:
            print(item)
        print(f'Saldo atual: R${saldo:.2f}')

def mostrar_contas(contas):
    print('LISTA DE CONTAS')
    if not contas:
        print('Não há contas cadastradas.')
    else:
        for conta in contas:
            print(f"Conta {conta['numero_conta']} - CPF: {conta['cpf']}")

def novo_usuario(usuarios):
    cpf = input('Informe o CPF (apenas números): ')
    nome = input('Informe o nome: ')
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print('Usuário já cadastrado.')
    else:
        usuarios.append({'cpf': cpf, 'nome': nome})
        print('Usuário cadastrado com sucesso!')
    return usuarios

def main():
    saldo = 0
    extrato = []
    limite_saques = 3
    numero_saques = 0
    limite = 500
    usuarios = []
    contas = []

    inicio()
    opcao = opcoes()

    while True:
        match opcao:
            case 'd':
                saldo, extrato = deposito(saldo, extrato)
                break
            case 's':
                saldo, extrato, numero_saques = saque(saldo, extrato, limite, numero_saques, limite_saques)
                break
            case 'e':
                mostrar_extrato(saldo, extrato)
                break
            case 'mc':
                mostrar_contas(contas)
                break                    
            case 'nu':
                usuarios = novo_usuario(usuarios)
                break
            case 'q':
                print('saindo...')
                break
            case _ :
                print('Opção inválida. Tente novamente.')
                break
                    
main()