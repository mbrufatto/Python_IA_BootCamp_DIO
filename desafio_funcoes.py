import textwrap

def menu():
    menu = """\n
    ==================== Menu ====================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar Contas
    [0]\tSair
    =======>
    """
    return input(textwrap.dedent(menu))
# 1
def deposit(balance, value, statement, /):
    if value > 0:
        balance += value
        statement.append(f"Depósito:\tR$ {value:.2f}\n")
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n !!!! Falha na operação! Valor informado inválido.")

    return balance, statement

# 2
def withdraw(*, balance, value, statement, limit, draft_number, draft_limit):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawal = draft_number >= draft_limit

    if exceeded_balance:
        print("\n !!!! Falha na operação! Saldo insuficiente.")

    elif exceeded_limit:
        print("\n !!!! Falha na operação! Limite de saque excedido.")
    
    elif exceeded_withdrawal:
        print("\n !!!! Falha na operação! Quantidade de saques esgotado.")
    
    elif value > 0:
        balance -= value
        statement.append(f"Saque:\t\tR$ {value:.2f}\n")
        draft_number += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n !!!! Falha na operação! O valor informado não é válido")
    
    return balance, statement

# 3
def show_statement(balance, /, *, statement):
    print("\n======================= Extrato =======================")
    if not len(statement):
        print("Nenhuma movimentação foi realizada.")
    else:
        for s in statement:
            print(f"\n {s}")
    print(f"\n\n")
    print(f"Saldo: R$ {balance:.2f}")
    print("=======================================================")
# 4
def create_user(users):
    cpf = input("Informe o CPF (apenas números): ")
    user = search_user(cpf, users)

    if user:
        print("\n !!!! Usuário já cadastrado com esse CPF")
        return

    name = input("Informe o nome completo: ")
    birth_date = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, nro - bairro - cidade/siga estado): ")
    users.append({"name": name, "birth_date" : birth_date, "cpf": cpf, "address": address})

    print("\n=== Usuário criado com sucesso! ===")

# 5
def create_account(agency, account_number, users):
    cpf = input("Informe o CPF (apenas números): ")
    user = search_user(cpf, users)

    if user:
        print("\n=== Conta criada com sucesso! ===")
        return {"agency": agency, "account_number": account_number, "user": user}
    
    print("\n !!!! Usuário não encontrado. Verifique o número do CPF e tente novamente")

# 6
def list_account(accounts):
    for account in accounts:
        row = f"""\
            Agência:\t{account['agency']}
            C/c:\t\t{account['account_number']}
            Titular:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(row))

def search_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

def main():
    balance = 0
    limit = 500
    statement = []
    draft_number = 0
    users = []
    accounts = []

    DRAFT_LIMIT = 3
    AGENCY = "0001"

    while True:
        option = menu()

        if option == "1":
            value = float(input("Informe o valor a depositar: "))
            balance, statement = deposit(balance, value, statement)

        elif option == "2":
            value = value = float(input("Informe o valor a sacar: "))

            balance, statement = withdraw(
                balance = balance,
                value = value,
                statement = statement,
                limit = limit,
                draft_number = draft_number,
                draft_limit = DRAFT_LIMIT,
            )
        
        elif option == "3":
            show_statement(balance, statement = statement)
        
        elif option == "4":
            create_user(users)
        
        elif option == "5":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)
            
            if account:
                accounts.append(account)

        elif option == "6":
            list_account(accounts)

        elif option == "0":
            break
        
        else:
            print("Opção do menu inválida, por favor selecione uma opção do menu válida.")

main()