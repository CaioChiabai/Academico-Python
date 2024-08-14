def verifica_login(matricula,senha,dic_login):
    if matricula in dic_login["matricula"]:
        indice = dic_login["matricula"].index(matricula)
        if dic_login["senha"][indice] == senha:
            return True;
    else:
        return False;

def menu_banco_de_dados(nome_banco):
    print(f"\nVocê escolheu o Banco de Dados {nome_banco}")
    print("1. Visualizar\n2. Adicionar\n3. Remover\n4. Editar")
    escolha = int(input("Escolha qual dos itens acima deseja realizar: "))
    return escolha

def visul_bd_login(dicionario_login):
    print("Você escolheu visualizar o Banco de Dados Login.\n")
    for matricula, senha in zip(dicionario_login["matricula"], dicionario_login["senha"]):
        print(f"Matrícula: {matricula}, Senha: {senha}\n")

def adic_bd_login(dicionario_login):
    print("\nVocê escolheu adicionar no Banco de Dados Login.\n")
    new_matricula = str(input("Insira a matricula que deseja adicionar: "))
    if new_matricula in dicionario_login["matricula"]:
        print("Matricula ja existente.\n")
    else:
        new_senha = str(input("Insira a senha que deseja adicionar: "))
        #adicionando o novo login no dicionario login
        dicionario_login["matricula"].append(new_matricula)
        dicionario_login["senha"].append(new_senha)
        #adicionando o novo login no banco de dados login
        arq = open("BD_LOGIN.txt","a")
        arq.write(f"\n{new_matricula}, {new_senha}")
        
        print("Novo login gerado com sucesso.\n")
 
def remov_bd_login(dicionario_login):
    matric = str(input("Digite a matricula do login que deseja remover: "))
    if matric not in dicionario_login["matricula"]:
        print("Matricula não existente.\n")
    else:
        #Salvo todo o arquivo em linhas
        with open("BD_LOGIN.txt","r") as file:
            linhas = file.readlines()
        
        #Abro o arquivo para escrita apagando todo o conteudo dele
        with open("BD_LOGIN.txt","w") as file:
            for linha in linhas:
                #Escrevo todas as linhas menos a escolhida
                if matric not in linha:
                    file.write(linha)
        

        lst_mat = dicionario_login["matricula"]
        pos_mat = lst_mat.index(matric)
        dicionario_login["matricula"].remove(matric)
        
        lst_sen = dicionario_login["senha"]
        senha = lst_sen[pos_mat]
        dicionario_login["senha"].remove(senha)
        
        print("Login removido com sucesso!")

    


def main():

    matricula = str(input("Insira sua matricula: "))
    senha = str(input("Insira sua senha: "))
    
    dic_login = {
        "matricula": [],
        "senha": []
        }

    with open("BD_LOGIN.txt") as arqLogin:
        linha = arqLogin.readline()
        while linha != '':
            lst_dados = linha.strip().split(',')
            dic_login["matricula"].append(lst_dados[0])
            dic_login["senha"].append(lst_dados[1].strip())
            linha = arqLogin.readline()
    
    if verifica_login(matricula,senha,dic_login) == True:
        print("Matricula encontrada\n")
        
    match matricula[0]:
        case "1":
            print("\nBem-vindo, Diretor\n")
            print("1. Banco de dados Login\n2. Banco de dados Matérias")

            escolha1 = int(input("Escolha a base de dados que deseja acessar: "))

            match escolha1:
                case 1:
                    operacao = menu_banco_de_dados("Login")
                    match operacao:
                        case 1:
                            visul_bd_login(dic_login)
                        case 2:
                            adic_bd_login(dic_login)
                        case 3:
                            remov_bd_login(dic_login)
                        case _:
                            print("Opção inválida.")

                case 2:
                    operacao = menu_banco_de_dados("Matérias")
                    match operacao:
                        case 1:
                            print("Você escolheu visualizar o Banco de Dados Matérias.")
                        case _:
                            print("Opção inválida.")
                case _:
                    print("Escolha inválida.")
        case "5":
            print("Bem vindo Professor(a)")
        case "9":
            print("Bem vindo Aluno(a)")

#    else:
#        print("Erro no login")

    
main()
