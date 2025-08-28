from database.conexao import BancoDeDados
from psycopg2.errors import UniqueViolation
class Consulta:
    def __init__(self):
        self.db = BancoDeDados()
        self.conexao = self.db.conectar()

    def inserir(self, modelo, marca, categoria, preco, quant, nota):
        self.cursor = self.conexao.cursor()
        try:
            self.cursor.execute(f"INSERT INTO produto (modelo, marca, categoria, preco, quant, nota) VALUES ('{modelo}', '{marca}', '{categoria}', '{preco}', '{quant}', '{nota}')")
        except UniqueViolation as e:
            print(f"Você está tentando inserir um modelo que já existe. \nErro: {e}")
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def alterar(self):
        None
    
    def pesquisar(self, modelo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        for linha in resultado:
            print(linha)
        self.cursor.close()
        self.conexao.close()

    def remover(self, modelo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"DELETE FROM produto WHERE modelo = '{modelo}'")
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def listar_todos(self):
        self.cursor = self.conexao.cursor()
        self.cursor.execute("SELECT * FROM produto")
        resultado = self.cursor.fetchall()
        for linha in resultado:
            print(linha)
        self.cursor.close()
        self.conexao.close()

    def exibir_um(self):
        None