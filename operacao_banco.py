import psycopg2
from connection import Connection

#pip install psycopg2

class Operacoes():

    def salvar(self, autor, tipo):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = """insert into livro (autor, tipo) values ('{0}', '{1}');""".format(autor, tipo)
            cursor.execute(insert)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


    def buscar(self):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            select = "select * from livro"
            cursor.execute(select)
            livros = cursor.fetchall()

            for row in livros:
                print("Id = ", row[0], )
                print("autor = ", row[1])
                print("tipo  = ", row[2], "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()