MENU = {
    "expresso": {
        "ingredientes": {
            "água": 50,
            "café": 18,
        },
        "custo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "água": 200,
            "leite": 150,
            "café": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "água": 250,
            "leite": 100,
            "café": 24,
        },
        "custo": 3.0,
    }
}

recursos = {
    "água": 300,
    "leite": 200,
    "café": 100,
}

MOEDAS = [0.25, 0.10, 0.05, 0.01]

saldo = 0


def recursoSuficiente(ingredientes):
    isSuficiente = True
    for chave in ingredientes:
        if ingredientes[chave] > recursos[chave]:
            isSuficiente = False
            print(f"Não há {chave} suficiente...")
    return isSuficiente


def pagamentoSuficiente(pagamento, custo):
    global saldo
    if pagamento >= custo:
        troco = pagamento - custo
        saldo += custo
        if troco > 0:
            print(f"Aqui está o seu troco de R${round(troco, 2)}.")
        return True
    else:
        print("O valor não é suficiente... Dinheiro reembolsado.")
        return False


def fazPagamento():
    pagamento = 0
    print("Digite a quantidade de cada moeda: ")
    for moeda in MOEDAS:
        pagamento += moeda * int(input(f"Moedas de {int(moeda * 100)} centavos: "))
    return pagamento


def fazCafe(nome, ingredientes):
    for chave in ingredientes:
        recursos[chave] -= ingredientes[chave]
    print(f"Aqui está o seu {nome} ☕!")


def main():
    global saldo
    isOn = True
    escolhaUsuario = input("Você deseja um expresso, um latte ou um cappuccino? ").lower()

    if escolhaUsuario == "off":
        isOn = False
    elif escolhaUsuario == "report":
        print(f"Água: {recursos['água']}ml")
        print(f"Leite: {recursos['leite']}ml")
        print(f"Café: {recursos['café']}g")
        print(f"Saldo: R${saldo}")
    elif escolhaUsuario in ["expresso", "latte", "cappuccino"]:
        pedido = MENU[escolhaUsuario]
        custoPedido = pedido["custo"]
        ingredientesPedido = pedido["ingredientes"]
        if recursoSuficiente(ingredientesPedido):
            pagamentoPedido = fazPagamento()
            if pagamentoSuficiente(pagamentoPedido, custoPedido):
                fazCafe(escolhaUsuario, ingredientesPedido)
    else:
        print("Você digitou uma opção inválida!")
    if isOn:
        main()


if __name__ == "__main__":
    main()
