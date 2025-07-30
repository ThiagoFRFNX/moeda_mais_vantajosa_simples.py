def melhor_moeda_para_pagamento(preco_pesos, preco_dolares, cotacao_peso, cotacao_dolar):
    valor_em_reais_peso = preco_pesos * cotacao_peso
    valor_em_reais_dolar = preco_dolares * cotacao_dolar

    print(f"\nValor em reais pagando com pesos: R$ {valor_em_reais_peso:.2f}")
    print(f"Valor em reais pagando com dólares: R$ {valor_em_reais_dolar:.2f}")

    if valor_em_reais_peso < valor_em_reais_dolar:
        print("➡️ Mais vantajoso pagar em PESOS.")
    elif valor_em_reais_peso > valor_em_reais_dolar:
        print("➡️ Mais vantajoso pagar em DÓLARES.")
    else:
        print("⚖️ Tanto faz — os valores são iguais em reais.")

# Exemplo de uso:
# Digite os valores conforme você vê nos locais da viagem
preco_em_pesos = float(input("Preço em pesos argentinos (ARS): "))
preco_em_dolares = float(input("Preço em dólares (USD): "))
cotacao_peso = float(input("Cotação do peso argentino em reais (ex: 0.0065): "))
cotacao_dolar = float(input("Cotação do dólar em reais (ex: 5.25): "))

melhor_moeda_para_pagamento(preco_em_pesos, preco_em_dolares, cotacao_peso, cotacao_dolar)