# TP2 - Análisis de Ventas

## Descripción del proyecto

Este repositorio corresponde al Trabajo Práctico de la materia Organización Empresarial, basado en la gestión colaborativa, el control de versiones y la trazabilidad mediante Jira, Git, GitHub y Google Colab.

El proyecto se desarrolla bajo el enfoque de una célula de desarrollo, respetando los roles propuestos en la consigna:

* P1 / Hugo: Líder y Organizador.
* P2 / Paco: Desarrollador Técnico.
* P3 / Luis: Revisor y QA.

## Escenario elegido

Se seleccionó el Escenario B: Análisis de Ventas de una Pequeña Empresa.

El objetivo del proyecto es analizar un conjunto de datos de ventas comerciales para obtener indicadores básicos que permitan interpretar el desempeño de la empresa.

## Dataset utilizado

Se utilizó el dataset sugerido por la consigna del trabajo práctico:

* Nombre del archivo: `sales_sample_2024.csv`
* Ubicación: carpeta `datos/`
* Columnas principales:

  * `id`: identificador del registro.
  * `sales_date`: fecha de la venta.
  * `sales_amount`: monto de la venta.

## Estructura del repositorio

```text
tp2-analisis-de-ventas/
├── datos/
│   └── sales_sample_2024.csv
├── scripts/
│   └── analisis_ventas.py
├── resultados/
│   ├── grafico_ventas_mensuales.png
│   ├── resumen_ventas.csv
│   └── ventas_por_mes.csv
├── README.md
└── .gitignore
```

## Análisis realizado

El script `analisis_ventas.py` realiza las siguientes acciones:

* Importa el dataset de ventas.
* Convierte la fecha de venta a formato de fecha.
* Calcula las ventas totales del año.
* Calcula la venta promedio diaria.
* Identifica la venta máxima y mínima.
* Identifica la fecha de mayor venta.
* Agrupa las ventas por mes.
* Genera archivos de resultados en formato CSV.
* Genera un gráfico de evolución mensual de ventas.

## Resultados generados

Los resultados se guardan en la carpeta `resultados/`:

* `resumen_ventas.csv`: contiene los principales indicadores del análisis.
* `ventas_por_mes.csv`: contiene el total de ventas agrupado por mes.
* `grafico_ventas_mensuales.png`: muestra la evolución mensual de ventas durante el año 2024.

## Instrucciones de ejecución

Desde Google Colab, luego de clonar el repositorio, ejecutar:

```bash
python scripts/analisis_ventas.py
```

El script lee el archivo ubicado en `datos/sales_sample_2024.csv` y genera automáticamente los resultados dentro de la carpeta `resultados/`.

## Herramientas utilizadas

* Jira
* Git
* GitHub
* Google Colab
* Python
* Pandas
* Matplotlib

## Trazabilidad

Las tareas del proyecto fueron organizadas en Jira mediante los siguientes issues:

* PROY-1: Inicializar repositorio y estructura del proyecto.
* PROY-2: Desarrollar script de análisis de ventas.
* PROY-3: Revisar documentación, seguridad y Pull Request.

Los commits del repositorio respetan el criterio de trazabilidad solicitado, utilizando el ID del issue correspondiente en cada mensaje de commit.
