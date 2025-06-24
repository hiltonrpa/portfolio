import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerar dados aleatórios
data = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D', 'E'],
    'Valores': np.random.randint(1, 100, 5)
})

st.subheader("Dados Aleatórios")
st.write(data)

# Criar gráfico de barras
fig, ax = plt.subplots()
ax.bar(data['Categoria'], data['Valores'])
ax.set_xlabel('Categoria')
ax.set_ylabel('Valores')
ax.set_title('Gráfico de Barras de Dados Aleatórios')

st.subheader("Gráfico de Barras")
st.pyplot(fig)
