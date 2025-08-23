def calcular_saldo (rendimento, despesas):
    return rendimento - despesas

def sugerir_poupanca(saldo):
    return saldo * 0.2

try:
    rendimento = float(input("Digite seu rendimento mensal em reias:"))
    if rendimento < 0:
        raise ValueError("O rendimento nao pode ser negativo")

    despesas = float(input("Digite o total de suas despesas mensais em reais:"))
    if despesas < 0:
        raise ValueError("As despesas nao podem ser negativas")

    tem_poupanca = input("Voce tem um plano de poupança (sim/nao): ").strip().lower()
    if tem_poupanca not in ["sim", "nao"]:
        raise ValueError("resposta invalida. digite 'sim' ou 'nao'.")

    saldo = calcular_saldo(rendimento, despesas)
    print(f"\nSeu saldo mensal é r$ {saldo:.2f}")

    if saldo < 0:
        print("Atençao! Suas despesas estao maiores que seus rendimentos")
    elif saldo > 0:
        if tem_poupanca == "sim":
            poupanca_sugerida = sugerir_poupanca(saldo)
            print(f"Recomendamos poupar R$ {poupanca_sugerida:.2f} este mês.")
        else:
            print("Considere criar um plano de poupança para aproveitar seu saudo positivo.")
    else:
        print("Seu orçamento está equilibrado, sem saldo restante para poupar")
except ValueError as e:
    print(f"Erro na sua entrada de dados: {e}")