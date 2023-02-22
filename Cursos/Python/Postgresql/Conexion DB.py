import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="test_db"
)

try: #Usamos un bloque try catch para que pase lo que pase se cierre la DB
    with conexion:
        with conexion.cursor() as cursor: #Este segundo bloque with nos ayuda a cerrar automaticamente el cursor
            sentencia = "SELECT * FROM persona"
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f"Ocurrio un erorr: {e}")
finally:
    conexion.close()
    #cursor.close()
