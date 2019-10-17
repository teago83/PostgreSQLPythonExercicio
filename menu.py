import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user = "postgres",
                              password = "ads",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "postgresql_db")

cursor = connection.cursor()

op = 6
while op != 5:
    try:
        while op > 5 or op < 1:
            op = int(input("Menu de opções:\n"
                        "1) Inserir dados;\n"
                        "2) Ler dados;\n"
                        "3) Atualizar dados;\n"
                        "4) Deletar dados;\n"
                        "5) Sair."))
        if op == 1:
            postgre_insert_query = """INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
            a = int(input("Digite o ID do celular:"))
            b = input("Digite o modelo do celular:")
            c = float(input("Digite o preço do celular:"))
            values_to_insert = (a,b,c)
            cursor.execute(postgre_insert_query, values_to_insert)
            connection.commit()
            print("Dados inseridos com sucesso.")
            
        elif op == 2:
            postgre_select_query = """select * from mobile"""
            cursor.execute(postgre_select_query)
        elif op == 3:
            break
        elif op == 4:
            break
        else:
            print("Opção inválida.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating the table", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The PostgreSQL connection was successfully closed.")