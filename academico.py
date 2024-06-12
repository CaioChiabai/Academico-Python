def verifica_login(matricula,senha,dic_login):
    if matricula in dic_login["matricula"]:
        indice = dic_login["matricula"].index(matricula)
        if dic_login["senha"][indice] == senha:
            return True;
    else:
        return False;


def main():

    matricula = str(input("Insira sua matricula: "))
    senha = str(input("Insira sua senha: "))
    
    dic_login = {
        "matricula": [],
        "senha": []
        }

    with open("BD_ALUNOS.txt") as arqLogin:
        linha = arqLogin.readline()
        while linha != '':
            lst_dados = linha.strip().split(',')
            dic_login["matricula"].append(lst_dados[0])
            dic_login["senha"].append(lst_dados[1].strip())
            linha = arqLogin.readline()
    
    if verifica_login(matricula,senha,dic_login) == True:
        print("Matricula encontrada")
        if matricula[0] == '1':
            print("Bem vindo Diretor")
            print("Escolha qual dos itens abaixo deseja realizar:")
            print("1. Visualizar base de dados\n2. Adicionar\n3. Remover\n4. Editar")
            escolha = int(input("Escolha qual dos itens acima deseja realizar: "))
        elif matricula[0] == '5':
            print("Bem vindo Professor(a)")
        elif matricula[0] == '9':
            print("Bem vindo Aluno(a)")

    else:
        print("Erro no login")

    #close(arqLogin)
main()