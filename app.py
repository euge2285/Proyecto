import streamlit as st
import pandas as pd
import plotly.express as px
import os
import numpy as np

# Configuración de la página
st.set_page_config(page_title="MultiLabelViz", page_icon="📊", layout="wide")

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard MultiLabelViz")
st.markdown("Análisis exploratorio de datos con tarjetas, filtros interactivos y gráficos.")

# Ruta al archivo de datos
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "dataset.csv")

@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
    else:
        # Datos de prueba si el archivo no existe
        st.warning(f"No se encontró el archivo en {DATA_PATH}. Usando datos de prueba.")
        df = pd.DataFrame({
            "Categoria": np.random.choice(["A", "B", "C", "D"], size=200),
            "Valor": np.random.randn(200).cumsum(),
            "Etiqueta_1": np.random.choice([0, 1], size=200, p=[0.7, 0.3]),
            "Etiqueta_2": np.random.choice([0, 1], size=200, p=[0.5, 0.5]),
            "Fecha": pd.date_range(start="2023-01-01", periods=200)
        })
    return df

df = load_data()

# ====================
# BARRA LATERAL (Filtros)
# ====================
st.sidebar.header("🔍 Filtros")

# Identificar columnas categóricas para filtros
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

filtros = {}
for col in cat_cols:
    opciones = ["Todos"] + list(df[col].unique())
    seleccion = st.sidebar.selectbox(f"Filtrar por {col}", opciones)
    if seleccion != "Todos":
        filtros[col] = seleccion

# Aplicar filtros
df_filtrado = df.copy()
for col, val in filtros.items():
    df_filtrado = df_filtrado[df_filtrado[col] == val]

# ====================
# TARJETAS (KPIs)
# ====================
st.markdown("### 📈 Indicadores Clave")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total de Registros", value=len(df_filtrado))

# Intento mostrar suma de columnas numéricas/booleanas típicas de multilabel
num_cols = df_filtrado.select_dtypes(include=[np.number]).columns.tolist()

with col2:
    if num_cols:
        val2 = df_filtrado[num_cols[0]].sum() if len(num_cols) > 0 else 0
        st.metric(label=f"Suma de {num_cols[0]}" if num_cols else "Métrica 2", value=f"{val2:,.2f}")
    else:
        st.metric(label="Métrica 2", value="N/A")

with col3:
    if len(num_cols) > 1:
        val3 = df_filtrado[num_cols[1]].mean()
        st.metric(label=f"Promedio de {num_cols[1]}", value=f"{val3:,.2f}")
    else:
        st.metric(label="Métrica 3", value="N/A")

st.markdown("---")

# ====================
# GRÁFICOS
# ====================
st.markdown("### 📊 Visualizaciones")

col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    if cat_cols:
        st.subheader("Distribución por Categorías")
        conteo = df_filtrado[cat_cols[0]].value_counts().reset_index()
        conteo.columns = [cat_cols[0], 'Frecuencia']
        fig_bar = px.bar(conteo, x=cat_cols[0], y='Frecuencia', color=cat_cols[0], template="plotly_white")
        st.plotly_chart(fig_bar, use_container_width=True)
    elif num_cols:
        st.subheader("Histograma")
        fig_hist = px.histogram(df_filtrado, x=num_cols[0], template="plotly_white")
        st.plotly_chart(fig_hist, use_container_width=True)

with col_graph2:
    if len(num_cols) >= 2:
        st.subheader("Relación entre Variables")
        fig_scatter = px.scatter(df_filtrado, x=num_cols[0], y=num_cols[1], color=cat_cols[0] if cat_cols else None, template="plotly_white")
        st.plotly_chart(fig_scatter, use_container_width=True)
    elif 'Fecha' in df_filtrado.columns and num_cols:
        st.subheader("Evolución en el Tiempo")
        fig_line = px.line(df_filtrado, x='Fecha', y=num_cols[0], template="plotly_white")
        st.plotly_chart(fig_line, use_container_width=True)

# Vista de datos
with st.expander("Ver Datos Originales"):
    st.dataframe(df_filtrado)
