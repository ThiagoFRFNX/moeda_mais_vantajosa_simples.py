import streamlit as st

st.set_page_config(page_title="Melhor Moeda para Pagamento", page_icon="💱")

st.title("💱 Melhor Moeda para Pagamento na Viagem")

st.markdown("Informe os valores abaixo para saber qual moeda é mais vantajosa para pagar.")

# Entradas do usuário
preco_pesos = st.number_input("Preço em pesos argentinos (ARS)", min_value=0.0, step=0.01)
preco_dolares = st.number_input("Preço em dólares (USD)", min_value=0.0, step=0.01)
cotacao_peso = st.number_input("Cotação do peso argentino (ARS → BRL)", min_value=0.0001, format="%.4f")
cotacao_dolar = st.number_input("Cotação do dólar (USD → BRL)", min_value=0.0001, format="%.4f")

# Botão de cálculo
if st.button("Calcular melhor opção"):
    valor_em_reais_peso = preco_pesos * cotacao_peso
    valor_em_reais_dolar = preco_dolares * cotacao_dolar

    st.subheader("💰 Valores convertidos")
    st.write(f"**Valor em reais pagando com pesos:** R$ {valor_em_reais_peso:.2f}")
    st.write(f"**Valor em reais pagando com dólares:** R$ {valor_em_reais_dolar:.2f}")

    st.subheader("🔎 Resultado")
    if valor_em_reais_peso < valor_em_reais_dolar:
        st.success("✅ Mais vantajoso pagar em **PESOS**.")
    elif valor_em_reais_peso > valor_em_reais_dolar:
        st.success("✅ Mais vantajoso pagar em **DÓLARES**.")
    else:
        st.info("⚖️ Tanto faz — os valores são iguais em reais.")
