import pandas as pd
import matplotlib.pyplot as plt
import os

# Definimos rutas relativas para que el proyecto pueda ejecutarse
# desde Google Colab sin depender de una carpeta específica.
ruta_datos = "datos/sales_sample_2024.csv"
carpeta_resultados = "resultados"

# Creamos la carpeta de resultados si no existe.
os.makedirs(carpeta_resultados, exist_ok=True)

# Cargamos el dataset de ventas sugerido por la consigna.
ventas = pd.read_csv(ruta_datos)

# Convertimos la columna de fecha a formato datetime para poder agrupar por mes.
ventas["sales_date"] = pd.to_datetime(ventas["sales_date"])

# Creamos una columna de mes para analizar la evolución mensual de ventas.
ventas["mes"] = ventas["sales_date"].dt.to_period("M").astype(str)

# Calculamos indicadores principales.
ventas_totales = ventas["sales_amount"].sum()
venta_promedio = ventas["sales_amount"].mean()
venta_maxima = ventas["sales_amount"].max()
venta_minima = ventas["sales_amount"].min()

# Identificamos el día con mayor venta.
fila_mayor_venta = ventas.loc[ventas["sales_amount"].idxmax()]
fecha_mayor_venta = fila_mayor_venta["sales_date"].strftime("%Y-%m-%d")
monto_mayor_venta = fila_mayor_venta["sales_amount"]

# Calculamos las ventas por mes.
ventas_por_mes = ventas.groupby("mes")["sales_amount"].sum().reset_index()

# Guardamos un resumen general en la carpeta resultados.
resumen = pd.DataFrame({
    "indicador": [
        "Ventas totales",
        "Venta promedio diaria",
        "Venta máxima diaria",
        "Venta mínima diaria",
        "Fecha de mayor venta",
        "Monto de mayor venta"
    ],
    "resultado": [
        round(ventas_totales, 2),
        round(venta_promedio, 2),
        round(venta_maxima, 2),
        round(venta_minima, 2),
        fecha_mayor_venta,
        round(monto_mayor_venta, 2)
    ]
})

resumen.to_csv("resultados/resumen_ventas.csv", index=False)
ventas_por_mes.to_csv("resultados/ventas_por_mes.csv", index=False)

# Generamos un gráfico de evolución mensual de ventas.
plt.figure(figsize=(10, 5))
plt.plot(ventas_por_mes["mes"], ventas_por_mes["sales_amount"], marker="o")
plt.title("Evolución mensual de ventas - Año 2024")
plt.xlabel("Mes")
plt.ylabel("Monto total de ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("resultados/grafico_ventas_mensuales.png")

# Mostramos resultados principales por consola.
print("Análisis de ventas finalizado correctamente.")
print("Ventas totales:", ventas_totales)
print("Venta promedio diaria:", round(venta_promedio, 2))
print("Fecha de mayor venta:", fecha_mayor_venta)
print("Monto de mayor venta:", monto_mayor_venta)
print("Los resultados fueron guardados en la carpeta resultados.")
