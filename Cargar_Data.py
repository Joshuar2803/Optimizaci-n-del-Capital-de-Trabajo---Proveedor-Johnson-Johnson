import pandas as pd
from sqlalchemy import create_engine, text

# 1. Leer la hoja específica del archivo Excel
# Asegúrate de que el archivo esté en la misma carpeta o pon la ruta completa
archivo_excel = 'DATOS GENERALES 20252 og.xlsx'  # Verifica la extensión real
df_cumplimiento = pd.read_excel(archivo_excel, sheet_name='CUMPLIMIENTO ')

# 2. Limpiar nombres de columnas (quitar espacios extras)
df_cumplimiento.columns = df_cumplimiento.columns.str.strip()

# 3. Conexión a la base de datos (ajusta si cambió el nombre o contraseña)
engine = create_engine('mysql+pymysql://root:@localhost/datos_48_horas?charset=utf8mb4')

# 4. Desactivar restricciones de claves foráneas por seguridad
with engine.connect() as conn:
    conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
    conn.commit()

# 5. Subir el DataFrame a MySQL como tabla 'cumplimiento'
# Si ya existe, la reemplaza (if_exists='replace')
df_cumplimiento.to_sql('cumplimiento', con=engine, if_exists='replace', index=False)

# 6. Reactivar restricciones
with engine.connect() as conn:
    conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
    conn.commit()

print("¡Sistema Cargado! SEGUIMOS AVANZANDO AVANZANDO.")