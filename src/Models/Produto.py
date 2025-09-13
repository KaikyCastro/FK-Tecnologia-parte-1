from psycopg2.errors import UniqueViolation
from database.Conexao import ConexaoBD

class Produto:
    def __init__(self):
        self.conn = ConexaoBD()
        self.conexao = self.conn.conectar()

    def inserir_produto(self, modelo, marca, categoria, preco, quant, nota):
        self.cursor = self.conexao.cursor()
        try:
            self.cursor.execute(f"INSERT INTO produto (modelo, marca, categoria, preco, quant, nota) VALUES ('{modelo}', '{marca}', '{categoria}', '{preco}', '{quant}', '{nota}')")
        except UniqueViolation as e:
            print(f"Você está tentando inserir um modelo que já existe. \nErro: {e}")
        self.conexao.commit()

    def alterar_produto(self, modelo_antigo, modelo_novo, marca, categoria, preco, quant, nota):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"UPDATE produto SET modelo = '{modelo_novo}', marca = '{marca}', categoria = '{categoria}', preco = '{preco}', quant = '{quant}', nota = '{nota}' WHERE modelo = '{modelo_antigo}'")
        self.conexao.commit()

    def pesquisar_modelo_produto(self, modelo) -> tuple:
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchone()
        return resultado
    
    def remover_produto(self, modelo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"DELETE FROM produto WHERE modelo = '{modelo}'")
        self.conexao.commit()

    def listar_todos_produtos(self) -> list:
        self.cursor = self.conexao.cursor()
        self.cursor.execute("SELECT * FROM produto")
        resultado = self.cursor.fetchall()
        return resultado

    def exibir_um_produto(self, modelo) -> tuple:
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchone()
        return resultado

