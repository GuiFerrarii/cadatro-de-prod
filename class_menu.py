from class_funcoes import *

class Menu:
    def __init__(self):
        funcoes = Funcoes()
        while True:
            entrada=input(('1 - Novo produto\n2 - Listar produtos\n3 - Mudar descriçao\n4 - Procurar por código\n5 - Excluir produto\n0 - Sair  ->'))
            if entrada == '1':
                funcoes.salvar_informaçoes()
            elif entrada == '2':
                funcoes.listar_produtos()
            elif entrada == '3':
                funcoes.Mudar_desc()
            elif entrada == '4':
                funcoes.procurar_por_cod()
            elif entrada == '5':
                funcoes.excluir_produtos()
            elif entrada == '0':
                break
            else:
                print('OPÇÃO INVÁLIDA lerdão!!')
