from database import BancoDeDados

class CRUD:
    def __init__(self):
        None

    def inserir(self, nome, preco):
        self.db = BancoDeDados()
        self.conexao = self.db.conectar()

        self.cursor = self.conexao.cursor()
        self.cursor.execute('INSERT INTO produtos (nome, preco) VALUES (%s, %s)')
        self.conexao.commit()
        self.cursor.close()
        self.db.desconectar()

    def alterar(self, id, nome, preco):
        self.db = BancoDeDados()
        self.conexao = self.db.conectar()

        self.cursor = self.conexao.cursor()
        self.cursor.execute('UPDATE produtos SET nome = %s, preco = %s WHERE id = %s', (nome, preco, id))
        self.conexao.commit()
        self.cursor.close()
        self.db.desconectar()

    def pesquisar(self, nome):
        None

    def remover(self):
        None

    def listar(self):
        None
    
    def exibir(self):
        None