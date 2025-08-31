import random

def gerar_dados_sensor(qtd_leituras):
    """
    Gera uma lista de leituras simuladas de temperatura.
    Cada leitura é um valor aleatório entre 15.0°C e 35.0°C, arredondado para duas casas decimais.
    """
    dados_sensor = [round(random.uniform(15.0, 35.0), 2) for _ in range(qtd_leituras)]
    return dados_sensor

def filtrar_temperaturas_altas(dados_sensor, limite=30.0):
    """
    Filtra e retorna as leituras cuja temperatura ultrapassa o valor limite.
    """
    leituras_altas = [temperatura for temperatura in dados_sensor if temperatura > limite]
    return leituras_altas

def inserir_leitura_sensor(dados_sensor, nova_leitura, posicao=None):
    """
    Insere uma nova leitura na lista de dados do sensor.
    Se a posição não for especificada ou for inválida, a nova leitura é adicionada ao final da lista.
    """
    if posicao is None or posicao >= len(dados_sensor):
        dados_sensor.append(nova_leitura)
    else:
        dados_sensor.insert(posicao, nova_leitura)
    return dados_sensor

def remover_leituras_anormais(dados_sensor, limite_inferior=15.0, limite_superior=35.0):
    """
    Remove da lista de dados as leituras que estejam fora do intervalo definido pelos limites inferior e superior.
    """
    dados_limpos = [temperatura for temperatura in dados_sensor if limite_inferior <= temperatura <= limite_superior]
    return dados_limpos

def principal():
    quantidade_leituras = 10000    # Número de leituras simuladas
    dados = gerar_dados_sensor(quantidade_leituras)
    print(f"Quantidade de leituras gerada: {len(dados)}")

    leituras_com_temperaturas_altas = filtrar_temperaturas_altas(dados, limite=30.0)
    print(f"Quantidade de leituras acima de 30°C: {len(leituras_com_temperaturas_altas)}")

    nova_leitura = 28.5  # Simula a inserção de um novo valor de leitura
    dados = inserir_leitura_sensor(dados, nova_leitura)

    dados_limpos = remover_leituras_anormais(dados)
    print(f"Quantidade de leituras após remoção de anomalias: {len(dados_limpos)}")

if __name__ == "__main__":
    principal()
