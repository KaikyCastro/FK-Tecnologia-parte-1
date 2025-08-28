from conexao import BancoDeDados

class Consulta:
    def __init__(self):
        None

    def inserir(self, nome, preco):
        self.db = BancoDeDados()
        self.conexao = self.db.conectar()
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f'INSERT INTO produto VALUES ({nome}, {preco})')
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def alterar(self):
        None
    
    def pesquisar(self, nome):
        None

    def remover(self):
        None

    def listar_todos(self):
        None

    def exibir(self):
        None