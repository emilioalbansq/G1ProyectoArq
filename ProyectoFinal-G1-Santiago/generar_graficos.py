import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Leer el archivo CSV
df = pd.read_csv("clima-santiago-hoy.csv", on_bad_lines='skip')

# Convertir la columna de fecha a datetime
df["fecha_hora"] = pd.to_datetime(df["fecha_hora"])

# Crear la figura
fig = plt.figure(figsize=(8,6))

# 1. TEMPERATURA VS TIEMPO
plt.plot(df["fecha_hora"], df["main_temp"], color='tab:red')

plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m %H:%M"))
plt.grid()
plt.title(f"Temperatura vs Tiempo en {next(iter(set(df['name'])))}")
plt.xticks(rotation=40)
fig.tight_layout()

# Guardar y LIMPIAR
plt.savefig("./weather-site/content/images/temperatura.png")
plt.clf()


# 2. HUMEDAD VS TIEMPO
plt.plot(df["fecha_hora"], df["main_humidity"], color='tab:blue')

plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m %H:%M"))
plt.grid()
plt.title(f"Humedad vs Tiempo en {next(iter(set(df['name'])))}")
plt.xticks(rotation=40)
fig.tight_layout()

# Guardar y LIMPIAR
plt.savefig("./weather-site/content/images/humedad.png")
plt.clf()


# 3. PRESION VS TIEMPO
plt.plot(df["fecha_hora"], df["main_pressure"], color='tab:purple')

plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m %H:%M"))
plt.grid()
plt.title(f"Presión vs Tiempo en {next(iter(set(df['name'])))}")
plt.xticks(rotation=40)
fig.tight_layout()

# Guardar y LIMPIAR
plt.savefig("./weather-site/content/images/presion.png")
plt.clf()


# 4. VELOCIDAD DEL VIENTO VS TIEMPO
plt.plot(df["fecha_hora"], df["wind_speed"], color='tab:green')

plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m %H:%M"))
plt.grid()
plt.title(f"Velocidad del viento vs Tiempo en {next(iter(set(df['name'])))}")
plt.xticks(rotation=40)
fig.tight_layout()

# Guardar y cerrar al final
plt.savefig("./weather-site/content/images/viento.png")
plt.close()
