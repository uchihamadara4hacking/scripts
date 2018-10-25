'''
Agenda de Contatos
Python 3.6
-
by R4MSOLO
'''
def registrar():
    nome     = input("\nNome.....: ")
    email    = input("\nEmail....: ")
    telefone = input("\nTelefone.: ")
    endereco = input("\nEndereco.: ")
   
    arq = open('agenda.txt', 'a+')
    texto = f'{nome} {email} {telefone} {endereco}\n'
    arq.writelines(texto)
    arq.close()
 
    main()
 
def lista_Contato(): #lista ordenando por nomes na exibição
    print('=============================================')
    print('   Lista: (A-Z)')
    print('=============================================\n')
 
    contatos = []
 
    # Lendo do arquivo
    arq = open('agenda.txt', 'r')
    texto = arq.readlines()
    for linha in texto :
        contatos.append(linha)
    arq.close()
 
    # Ordenando
    contatos.sort()
 
    # Exibindo
    for linha in contatos:
        print(linha)
 
    resp = input('[-]Final da lista, tecle ENTER para continuar... ')
    if resp == 'X' or 'x':
        main()
 
def pesquisar():
    f = open('agenda.txt','r')
    pesquisa = input("[+]Pesquise pelo nome: ")
    lista = []
    for x in f.readlines():
        y = x.split(' ')
        for item in y:
            lista.append(item)
    print('\n=============================================')
    print('[+]Resultado da busca:')
    print('=============================================\n')
 
    for index, i in enumerate(lista):
        if pesquisa.lower() == i.lower():
            print(lista[index])
            print(lista[(index+1)])
            print(lista[(index+2)])
            print(lista[(index+3)])
            print('---------------------------------------------------')
        else:
            pass
 
    f.close()
    resp = input('[-]Final da lista, tecle ENTER para continuar... ')
    if resp == 'X' or 'x':
        main()
 
def deletar():
    f = open('agenda.txt','r+')
    pesquisa = input("[!]Entre com o nome para deletar dados: ")
 
    contatos = []
    apagou = 0
 
    # Lendo do arquivo
    arq = open('agenda.txt', 'r')
    texto = arq.readlines()
    for linha in texto:
        dado = linha.split(' ')
        if dado[0] == pesquisa:
            apagou = 1
        else:
            contatos.append(linha)
        linha=''
 
    arq.close()
 
    if apagou:
        print('\nRegistro apagado\n')
    else:
        print('\nNome não encontrado\n')
 
    # Escrevendo novamente o arquivo
    arq = open('agenda.txt', 'w')
    arq.writelines(contatos)
    arq.close()
    main()
 
def main():
    try:
        print("--------------- AGENDA DE CONTATOS ----------------\n")
        print("1 - Registra contato")
        print("2 - Exibe contatos")
        print("3 - Pesquisa contato")
        print("4 - Deleta contato")
        print("0 - Sair					    GreenHub              ")
        print("-----------------------------------------------------\n")
        resposta = input("[+]Insira um valor: ")
        print('\n')
        if resposta == "1":
            registrar()
        elif resposta == "2":
            lista_Contato()
        elif resposta == "3":
            pesquisar()
        elif resposta == "4":
            deletar()
        elif resposta == "0":
            quit()
        else:
            print("[!]Digite o valor correspondente as opcoes!\n")
            main()
 
    except KeyboardInterrupt:
        quit()
main()
