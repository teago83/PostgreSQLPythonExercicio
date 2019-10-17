import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "ads",              
                                  host = "127.0.0.1",              
                                  port = "5432",              
                                  database = "postgresql_db")
    cursor = connection.cursor()
    #print postgreSQL connection properties
    print(connection.get_dsn_parameters(),"\n")

    #print postgreSQL version
    cursor.execute("SELECT version();")
    record  = cursor.fetchone()
    print("You're connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connection to PostgreSQL", error)
finally:
    #closing database connection
    if (connection):
        cursor.close()
        connection.close()
        print("The PostgreSQL connection has been closed.")                                  
        