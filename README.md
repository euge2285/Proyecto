# MultiLabelViz - Análisis y Visualización

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?logo=kaggle&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.20-3F4F75?logo=plotly&logoColor=white)

Proyecto para el análisis interactivo de datos multilabel. Incluye una aplicación web en **Streamlit** (optimizada para despliegue desde GitHub) y un entorno de análisis basado en **Jupyter Notebooks**.

## 📂 Arquitectura del Proyecto

```text
MultiLabelViz/
├── data/                  # Contiene el dataset limpio (CSV) utilizado por Streamlit
├── notebooks/
│   └── notebook.ipynb     # Cuaderno de análisis inicial e integración con Kaggle
├── app.py                 # Aplicación de Streamlit interactiva
├── index.html             # Landing Page para GitHub Pages
├── requirements.txt       # Dependencias
└── README.md              # Este archivo
```

## 🚀 Despliegue

### 1. Landing Page (GitHub Pages)
El archivo `index.html` es una Landing Page moderna diseñada para desplegarse fácilmente:
1. Sube este repositorio a GitHub.
2. Ve a la configuración (Settings) de tu repositorio.
3. En la sección "Pages", selecciona la rama `main` y guarda. ¡Tu Landing Page estará disponible!

### 2. Streamlit App (Streamlit Community Cloud)
La aplicación `app.py` utiliza los datos ya descargados/procesados de la carpeta `data/` en formato CSV.
1. Ingresa a [share.streamlit.io](https://share.streamlit.io/).
2. Vincula tu cuenta de GitHub.
3. Selecciona el repositorio de este proyecto e indica `app.py` como la aplicación principal. ¡Y listo! No se requieren secretos ni variables de entorno.

## 🛠️ Desarrollo Local

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Analizar datos con Jupyter:
```bash
jupyter notebook notebooks/notebook.ipynb
```

3. Correr la aplicación de Streamlit:
```bash
streamlit run app.py
```
