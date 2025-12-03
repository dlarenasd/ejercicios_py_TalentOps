import pandas as pd
import sqlite3
import json
import openpyxl

# Crear CSV
ventas_csv = pd.DataFrame({
    'id_venta': range(1, 7),
    'producto': ['Laptop', 'Mouse', 'Mouse', 'Teclado', 'Monitor', 'Audífonos'],
    'precio': [1200, 25, 25, 80, 300, 150], 
    'id_pedido': [1, 1, 2, 3, 3, 4]
})
ventas_csv.to_csv('ventas.csv', index=False)

# Crear Excel con múltiples hojas
clientes_df = pd.DataFrame({
    'id_cliente': [1, 2, 3],
    'nombre': ['Ana', 'Carlos', 'María'],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia']
})

with pd.ExcelWriter('datos.xlsx') as writer:
    ventas_csv.to_excel(writer, sheet_name='Ventas', index=False)
    clientes_df.to_excel(writer, sheet_name='Clientes', index=False)

# Crear JSON
productos_json = [
    {'id': 101, 'nombre': 'Laptop', 'categoria': 'Electrónica'},
    {'id': 102, 'nombre': 'Mouse', 'categoria': 'Accesorios'},
    {'id': 103, 'nombre': 'Teclado', 'categoria': 'Accesorios'},
    {'id': 104, 'nombre': 'Monitor', 'categoria': 'Electrónica'},
    {'id': 105, 'nombre': 'Audífonos', 'categoria': 'Accesorios'}
]
with open('productos.json', 'w', encoding="utf-8") as f:
    json.dump(productos_json, f, ensure_ascii=False)

# Crear base de datos SQLite
conn = sqlite3.connect('ventas.db')
pedidos_df = pd.DataFrame({
    'id_pedido': [1, 2, 3, 4],
    'id_cliente': [1, 2, 1, 3],
    'fecha': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-17'],
    'total': [1225, 25, 380, 150]
})
pedidos_df.to_sql('pedidos', conn, index=False, if_exists='replace')
conn.close()