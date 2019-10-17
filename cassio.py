import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "ads",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgresql_db")

    cursor = connection.cursor()

    #um cursor usado pra criar uma tabela no PostgreSQL
    create_table_query = '''CREATE TABLE mobile
           (ID INT PRIMARY KEY    NOT NULL,
           MODEL           TEXT   NOT NULL,
           PRICE          REAL);'''

    #usar o cursor para se comunicar com o PostgreSQL e tacar o comando
    #detalhado nele pra fazer a magia.
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating the table", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("The PostgreSQL connection was successfully closed.")