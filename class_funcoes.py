from class_sistema import *
class Funcoes:
    def __init__(self):
        self.listaprodutos = []


    def salvar_informaçoes(self):
        self.listaprodutos.append(sistema())

    def listar_produtos(self):
        for i in range(len(self.listaprodutos)):
            print('Código: ', self.listaprodutos[i].cod,
            'descriçao: ', self.listaprodutos[i].desc,
            'fabricante: ', self.listaprodutos[i].fabricante,
            'quantidade: ', self.listaprodutos[i].quant)


    def procurar_por_cod(self):
        controle = input('Informe o codigo:')
        for i in range(len(self.listaprodutos)):
            if controle == self.listaprodutos[i].cod:
                print('Código: ', self.listaprodutos[i].cod,
                      'descriçao: ', self.listaprodutos[i].desc,
                      'fabricante: ', self.listaprodutos[i].fabricante,
                      'quantidade: ', self.listaprodutos[i].quant)



    def Mudar_desc(self):
        controle = input('Informe o código que deseja alterar:')
        for i in range(len(self.listaprodutos)):
            if controle == self.listaprodutos[i].cod:
                self.listaprodutos[i].desc = input('Digite a nova descrição')

    def excluir_produtos(self):
        self.listar_produtos()
        in_cod = input('Insira o código do produto.\n: ')
        for i in range(len(self.listaprodutos)):
            if self.listaprodutos[i].cod == in_cod:
                self.listaprodutos.pop(i)
                print('Produto excluido com sucesso!!!')
                self.listar_produtos()
                break
            else:
                pass


