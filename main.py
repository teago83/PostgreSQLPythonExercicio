from aluno import Aluno 
import random
    
cassio = Aluno()

while True:
    op = int(input("MENU DE OPÇÕES:\n"
                   "1) Cadastrar aluno;"
                   "\n2) Mostrar todos os alunos;"
                   "\n3) Atualizar aluno;"
                   "\n4) Deletar aluno;"
                   "\n5) Buscar por aluno;"
                   "\n6) Sair."
                   "\nDigite a opção que lhe desperta o interesse."))

    if op == 1:
        print("Cadastro do(a) aluno(a):")
        nome = input("Digite o nome do(a) aluno(a):")
        sobrenome = input("Digite o sobrenome do(a) aluno(a):")
        matricula = 100000 + random.randint(1, 99999)
        print("Matrícula atribuída: %d" % (matricula))
        cassio.insert(nome, sobrenome, matricula)
    
    elif op == 2: 
        print("Todos os alunos registrados:\n")
        cassio.print_all()

    elif op == 3:
        print("Atualizar dados de um(a) aluno(a):")
        matricula = int(input("Digite a matrícula do(a) aluno(a) que terá seus dados atualizados:"))
        nome = input("Digite o novo nome do(a) aluno(a):")
        sobrenome = input("Digite o novo sobrenome do(a) %s:" % (nome))
        cassio.update(matricula, nome, sobrenome)
    
    elif op == 4:
        print("Deletar dados de um(a) aluno(a):")
        matricula = int(input("Digite a matrícula do(a) aluno(a)"
                           "que terá seus dados deletados:"))
        cassio.delete(matricula)
    
    elif op == 5:
        print("Procurar por um(a) aluno(a):")
        search = int(input("Digite a matrícula do(a) aluno(a)"
                           "pelo(a) qual buscas:"))
        cassio.print_one(search)

    elif op == 6:
        break

    else:
        print("Opção inexistente. Tente novamente.")
