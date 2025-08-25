# A World Away: Hunting for Exoplanets with AI

> **Proyecto:** 2025 NASA Space Apps Challenge  
> **Descripción:** App interactiva para entrenar y desplegar modelos de IA que detecten exoplanetas usando datasets abiertos de misiones espaciales (Kepler, K2, TESS).  

---

## 🪐 Resumen

**A World Away** permite a usuarios explorar datasets reales de curvas de luz, entrenar modelos de ML, visualizar predicciones y entender cómo se detectan exoplanetas. Está pensado tanto para investigadores amateurs como para público general curioso por la astrofísica.

---

## 🎯 Objetivos

- **Automatización:** detectar exoplanetas sin intervención manual.  
- **Interpretabilidad:** mostrar cómo el modelo identifica candidatos con métricas y visualizaciones.  
- **Educación:** aprender sobre métodos de detección y parámetros de exoplanetas.

**KPIs demo:**

- Precisión del modelo > 85% sobre dataset de test.  
- Tiempo de predicción < 1 s por curva de luz.  
- Visualización interactiva de al menos 3 datasets de misión diferentes.

---

## 👤 Usuarios y Historias

**Perfiles:**

1. Investigador amateur: entrenar y probar modelos con datos reales.  
2. Educador / estudiante: explorar datasets y visualizar detección de exoplanetas.  
3. Público general curioso: interactuar con gráficos y predicciones sin conocimientos de ML.

**Historias MVP:**

- Como usuario, quiero **cargar un dataset** y **ver curvas de luz**.  
- Como usuario, quiero **visualizar predicciones** del modelo en nuevos datos.  
- Como educador, quiero **explicaciones de métricas y parámetros** para enseñar sobre detección de exoplanetas.

---

## 🏗️ Arquitectura del proyecto

```
[NASA APIs / CSV / FITS]
|
[data/loaders] --> [preprocessing] --> [models] --> [metrics]
| |
+--> [visualization/plots] <---------+
|
+--> [Streamlit UI]
|
+--> [export/io]
```

**Stack Python:**

- **Web/UI:** Streamlit, Plotly, Altair  
- **ML:** Scikit-learn, TensorFlow/Keras o PyTorch, pandas, NumPy  
- **Otros:** Pydantic (schemas), Requests/HTTPX para APIs  
- **Tests:** pytest para pipelines y funciones críticas  

---

## 📂 Estructura del repositorio
```
world-away/
├─ app/
│ ├─ Home.py
│ ├─ pages/
│ │ ├─ 1_Explorar_Datasets.py
│ │ ├─ 2_Entrenar_Modelo.py
│ │ └─ 3_Prediccion_Exoplanetas.py
│ └─ assets/
├─ src/
│ ├─ core/preprocessing.py
│ ├─ core/models.py
│ ├─ core/metrics.py
│ ├─ data/loaders.py
│ ├─ visualization/plots.py
│ ├─ export/io.py
├─ data/samples/
├─ tests/
├─ notebooks/
├─ env.example
├─ environment.yml
├─ README.md
└─ LICENSE
```

---

## ⚡ Pipeline de ML

1. **Preprocesamiento:** normalización, detrending, padding/interpolación.  
2. **Split dataset:** train / validation / test.  
3. **Entrenamiento:** Random Forest / CNN 1D / LSTM según elección.  
4. **Evaluación:** métricas de clasificación y validación cruzada.  
5. **Predicción:** aplicar a nuevos archivos y mostrar probabilidades.  
6. **Interpretabilidad (stretch):** SHAP / LIME sobre curvas de luz.

---

## 📊 Funcionalidades principales

- Cargar datasets CSV o FITS y visualizar curvas de luz.  
- Entrenar modelos de ML y predecir exoplanetas automáticamente.  
- Panel de métricas: precisión, recall, F1, curva ROC.  
- Exportar resultados en CSV y PNG.  
- Interpretabilidad básica: probabilidades, curvas ROC.  
- Contenido educativo: guía de lectura de curvas, glosario y ejemplos interactivos.

---

## 🔧 Instalación

1. Clonar el repositorio:  
```bash
git clone https://github.com/<usuario>/a_world_away-exoplanet_detection_with_ai.git
cd a_world_away-exoplanet_detection_with_ai
```
2. Crear entorno Conda:
```bash
conda env create -f environment.yml
conda activate world-away
```
3. Variables de entorno (env.example):
```bash
NASA_API_KEY=DEMO_KEY
CACHE_TTL_H=24
```
4. Ejecutar la app:
```bash
streamlit run app/Home.py
```
5. Ejecutar tests:
```bash
pytest -q
```

---

## 📦 Fuentes de datos

NASA Exoplanet Archive (Kepler, K2, TESS) – CSV o API.

Light curves datasets: FITS/CSV abiertos para entrenamiento y validación.

Datos de referencia para validación de candidatos confirmados.

---

## 📝 Tests

test_preprocessing.py: normalización, padding y detrending correctos.

test_models.py: predicción dummy coherente, shapes correctas.

test_metrics.py: métricas calculadas sin errores.

---

## 🛠️ Plan de trabajo (MVP, 1–2 semanas)

Día 1–2: Repo, entorno, loaders de datasets de ejemplo.

Día 3–4: Implementar Random Forest y CNN 1D, gráficos dummy.

Día 5–6: Entrenamiento real, métricas, exportación.

Día 7+: Stretch: LSTM, interpretabilidad, modo educativo, UI refinada.

---

## 🎓 Contenido educativo

Explicación de detección de exoplanetas.

Guía de lectura de curvas de luz.

Tarjetas “¿Qué estoy viendo?” con ejemplos y predicciones.

Glosario: tránsito, profundidad, periodo orbital, etc.

---

## 🚀 Entregables

Repo GitHub público con README y ejemplos de uso.

Modelos entrenados guardados (.h5 / pickle).

Capturas de pantalla / PNG de curvas y resultados.

PDF resumen de flujo de trabajo y métricas.

Video demo de 2–3 min.

---

## 🤝 Contribución

Ana Zubieta – ciencia de datos, preprocesamiento, entrenamiento de modelos y métricas.
Christophe Hanin – UI Streamlit, visualización, export, contenido educativo.
Juntos – pruebas finales, documentación, video demo, repo público.

---

## 📄 Licencia

MIT License – ver LICENSE.
