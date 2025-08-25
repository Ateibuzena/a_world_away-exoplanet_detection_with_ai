---

# Meteor Madness — Impact Simulation & Visualization Tool

### NASA Space Apps Challenge 2025

**Impactor-2025** es una aplicación web interactiva que permite simular impactos de asteroides sobre la Tierra, visualizar sus efectos y estimar la población e infraestructuras afectadas. Está pensada para público general, educadores y gestores de emergencias, utilizando datos reales de NASA y capas geográficas abiertas.

---

## 0. Pitch (60s)

Una app web interactiva para explorar el riesgo de impactos de asteroides. Selecciona un asteroide real o define tamaño y velocidad, elige el punto de impacto y visualiza las consecuencias: onda de choque, radiación térmica, cráter, eyección e incluso tsunamis. Integra datos NASA (órbitas, probabilidades de impacto) y capas USGS con población para estimar exposición. Transparente, educativa y rápida: menos de 3 segundos por escenario.

---

## 1. Objetivos del Producto

* **Comprensión**: traducir la física de impactos en visualizaciones claras.
* **Toma de decisiones**: mostrar métricas clave (área afectada, población expuesta, infraestructura crítica).
* **Transparencia**: parámetros visibles, supuestos claros, datos abiertos.

**KPIs:**

* Simulación en menos de 3 segundos por escenario.
* Mapa interactivo con capas dinámicas.
* Exportación en PNG, PDF y JSON.

---

## 2. Usuarios y Historias de Usuario

**Perfiles:**

* Ciudadanía curiosa: entender el riesgo mediante sliders.
* Gestores de emergencia: estimar población afectada, exportar resultados.
* Educadores: usar presets y compartir capturas.

**Historias (MVP):**

* Seleccionar asteroide real o manual y ver radios de daño.
* Estimar población en cada anillo de afectación.
* Activar capas educativas (uso del suelo, elevación).

---

## 3. Alcance del Proyecto

**MVP:**

* UI web (Streamlit) con mapa interactivo.
* Motor de efectos básicos (onda de choque, térmica, cráter).
* Estimación de población afectada.
* Exportación de resultados.

**Stretch Goals:**

* Modelado de tsunami y shakemap sísmica.
* Estrategias de mitigación (desvío, fragmentación).
* Story mode educativo.

---

## 4. Fuentes de Datos

* **Asteroides:** NASA SBDB, Sentry, NEO feeds.
* **Topografía:** USGS 3DEP.
* **Población:** WorldPop, GPW, HRSL.
* **Costas y batimetría:** GEBCO, ETOPO1.
* **Otros:** mock de POIs para infraestructuras.

---

## 5. Arquitectura

**Front-end:** Streamlit con Leaflet/pydeck para mapas.
**Back-end:** Motor físico en Python con módulos organizados por funcionalidad.
**Geo:** GeoPandas, Shapely, Rasterio para análisis espacial.
**Numérico:** NumPy, SciPy.
**Visualización:** Altair, pydeck.

**Diagrama lógico:**
NASA APIs + USGS DEM → Data Loaders + Caché → Motor de efectos → Análisis de exposición → Streamlit UI → Exportación.

---

## 6. Diseño de la UI

**Sidebar:**

* Selección de asteroide o input manual.
* Parámetros: tamaño, velocidad, ángulo, densidad, superficie (tierra/agua).
* Botón de simulación.

**Lienzo principal:**

* Mapa interactivo con anillos de daño.
* Tarjetas con métricas (energía, radios, población).
* Pestañas: Resultado, Supuestos, Mitigación, Exportar.

---

## 7. Modelado de Efectos

* Entrada atmosférica: decide airburst o impacto.
* Cráter: escalado con π-group.
* Onda de choque: decaimiento de sobrepresión vs distancia.
* Térmica: fracción radiada, atenuación.
* Eyección: radio de depósito.
* **Opcional:** tsunami simplificado y shakemap sintética.

---

## 8. Esquema de Datos

* **ScenarioIn:** parámetros del asteroide, ubicación y superficie.
* **ScenarioOut:** energía, radios de daño, geometrías de anillos, población afectada.

---

## 9. Estructura del Repositorio

meteor-madness/

* app/ (Streamlit)
* src/ (motor físico, analytics, loaders, export)
* data/ (caché y muestras)
* tests/ (pytest + hypothesis)
* notebooks/ (validación y análisis)
* environment.yml
* README.md

---

## 10. Plan de Trabajo (1–2 semanas)

* Día 1-2: Configuración de repo y entorno, motor físico básico.
* Día 3-4: Conectores NASA y mapa interactivo.
* Día 5-6: Story mode y Monte Carlo para incertidumbre.
* Día 7+: Stretch goals.

---

## 11. Stack Tecnológico

* **Lenguaje:** Python 3.11+
* **Framework UI:** Streamlit
* **Geoespacial:** GeoPandas, Shapely, Rasterio, pyproj
* **Visualización:** Folium, pydeck, Altair
* **Otros:** Pydantic, Requests, loguru
* **Testing:** pytest, hypothesis

---

## 12. Licencia y Atribuciones

* Datos NASA y USGS (open data).
* Proyecto bajo licencia MIT.

---

## 13. Entregables Finales

* Repositorio en GitHub con instrucciones.
* Video demo (2–3 minutos).
* Informe PDF de ejemplo.
* Capturas PNG de escenarios.

---

### **¿Qué sigue?**

* Generar el repositorio base con esta estructura.
* Crear prototipo Streamlit: mapa con círculo de 1 km + tarjetas dummy.

---
