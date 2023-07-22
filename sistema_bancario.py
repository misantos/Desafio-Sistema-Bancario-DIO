def inserir_usuario(clientes):
    dicionario = {}
    nome = input("Digite o nome do usuario da nova conta: ")
    cpf = input("Digite o cpf: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço: ")
    dicionario = {"nome" : nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    if not clientes:
        clientes.append(dicionario)
    else:
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                print("CPF já cadastrado")
                return clientes
            
        clientes.append(dicionario)
    print(clientes)
    return clientes
        
def criar_conta_corrente(conta_corrente, clientes, numero_da_conta):
    agencia = "0001"
    print("Cadastro de conta corrente\n")
    usuario_cpf = input("Digite o seu cpf: ")
    for cliente in clientes:
        if usuario_cpf == cliente["cpf"]:
            numero_da_conta += 1
            conta_corrente.append({"agência": agencia, "numero_conta": numero_da_conta, "cliente": cliente})
            print("Conta corrente cadastrada com sucesso!\n")
            print(conta_corrente)
            return conta_corrente, numero_da_conta
    
    print("CPF não está cadastrado!")
    return conta_corrente, numero_da_conta
        
    

def depositar(saldo, deposito, extrato,/):
    
    if deposito <= 0:
        print("Erro, vc só pode depositar valores acima de zero!")
    else:
        saldo += deposito
        extrato += f"deposito total: {deposito:.2f}\n"
        print(f"Confirmado, depósito de R$ {deposito:.2f} realizado com sucesso!")
    return saldo, extrato

def sacar(*,saldo, valor_saque, limite, LIMITE_SAQUES, extrato, numero_saques):
    
    if valor_saque < saldo and valor_saque > 0:
        if valor_saque <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"valor do saque total: {valor_saque:.2f}\n"
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        else:
            print("Não é possível realizar o saque nesse momento. Valor do saque acima do permitido ou saques diários preenchidos")
    else:
        print("Saldo insuficiente")
    return saldo, extrato, numero_saques
            
def extratos(saldo, /, *,  extrato):
    titulo = "Extrato"
    asterisco = "*" * 20
    print(titulo.center(20,"*"))
    if extrato == "":
        print("\nNão foram realizadas movimentações.\n")
    else:
        print(extrato)
        print(f"Saldo total: R$ {saldo:.2f}")
    print(asterisco)
    
def menu():
    menu = """

    [u] Criar usuário
    [c] Criar Conta corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    """
    return menu

def menu_principal():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    clientes = []
    conta_corrente = []
    numero_da_conta = 0
    while True:
        opcao = input(menu())
        
        if opcao == "u":
            clientes = inserir_usuario(clientes)
        
        elif opcao == "c":
            conta_corrente, numero_da_conta = criar_conta_corrente(conta_corrente, clientes, numero_da_conta)
    
        elif opcao == "d":
            print("Depósito")
            deposito = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == "s":
            print("Saque")
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor_saque=valor_saque, limite=500, LIMITE_SAQUES=3, extrato=extrato, numero_saques=numero_saques)
            
        elif opcao == "e":
            extratos(saldo, extrato=extrato)
        
        elif opcao == "q":
            print("Encerrando o programa.")
            break
     
        else:
            print("Operação inválida, por favor digite novamente.")



menu_principal()
