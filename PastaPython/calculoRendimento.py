def calcular_saldo (rendimento, despesas):  #palavra-chave def serve para definir funções.
    return rendimento - despesas #a palavra-chave return serve para enviar um valor de volta de uma função para o lugar onde ela foi chamada.

def sugerir_poupanca(saldo): #palavra-chave def serve para definir funções.
    return saldo * 0.2 

try: #a palavra-chave try é usada para tratar erros (exceções) que podem acontecer durante a execução do código
    rendimento = float(input("Digite seu rendimento mensal em reias:")) #float é um tipo de dado que representa números decimais, ou seja, números que têm parte fracionária.
    if rendimento < 0:
        raise ValueError("O rendimento nao pode ser negativo") #a palavra-chave raise serve para gerar (lançar) uma exceção manualmente

    despesas = float(input("Digite o total de suas despesas mensais em reais:"))
    if despesas < 0:
        raise ValueError("As despesas nao podem ser negativas")

    tem_poupanca = input("Voce tem um plano de poupança (sim/nao): ").strip().lower() #strip() é um método de strings que serve para remover espaços em branco (ou outros caracteres) do início e do fim de uma string.
    if tem_poupanca not in ["sim", "nao"]: #Em Python, lower() é um método de strings que converte todos os caracteres da string para letras minúsculas.
        raise ValueError("resposta invalida. digite 'sim' ou 'nao'.")

    saldo = calcular_saldo(rendimento, despesas)
    print(f"\nSeu saldo mensal é R$ {saldo:.2f}")

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