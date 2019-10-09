import psycopg2
from PostgreSQLPythonExercicio.connection import Connection

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

"""
class Operacoes():
    
    def salvar(self, nome, sobrenome, matricula):
        connection = Connection().get_connection()
        cursor = connection.cursor()
        insert = """"insert into aluno (matricula, nome, sobrenome) values ('{0}', '{1}', '{2}');""".format(nome, sobrenome, matricula)"""
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
            select = "select * from aluno"
            cursor.execute(select)
            alunos = cursor.fetchball()

            for row in alunos:
                print("Matrícula = ", row[0], )
                print("Nome = ", row[1])
                print("Sobrenome = ", row[2], "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def atualizar(self, matricula, nome, sobrenome):
        """atualizar aluno baseando-se em seus dados"""
        sql = """ UPDATE alunos
                    SET nome = %s 
                    SET sobrenome = %s 
                    SET matricula = %d 
                    WHERE matricula = %d"""
        connection = None
        updated_rows = 0
        try:
            params = config()