menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=======>
"""

balance = 0
limit = 500
statement = []

draft_number = 0
DRAFT_LIMIT = 3

while True:
    option = input(menu)
    
    if option == "1":
        value = float(input("Informe o valor a depositar: "))

        if value > 0:
            balance += value
            statement.append(f"Depósito: R$ {value:.2f}")
        else:
            print("Falha na operação! O valor informado não é válido")

    elif option == "2":
        value = float(input("Informe o valor a sacar: "))

        insufficient_balance = value > balance

        limit_exceeded = value > limit

        draft_exceeded = draft_number >= DRAFT_LIMIT

        if insufficient_balance:
            print("Falha na operação! Saldo insuficiente.")

        elif limit_exceeded:
            print("Falha na operação! Limite de saques excedido.")
        
        elif draft_exceeded:
            print("Falha na operação! Número de saques excedido.")

        elif value > 0:
            balance -= value
            statement.append(f"Saque: R$ {value:.2f}")
            draft_number += 1
        else:
            print("Falha na operação! O valor informado não é válido")
    
    elif option == "3":
        print("\n======================= Extrato =======================")
        if not len(statement):
            print("Nenhuma movimentação foi realizada.")
        else:
            for state in statement:
                print(f"\n {state}")
        print(f"\n\n")
        print(f"Saldo: R$ {balance:.2f}")
        print("=======================================================")

    elif option == "0":
        break
    
    else:
        print("Opção do menu inválida, por favor selecione uma opção do menu válida.")
