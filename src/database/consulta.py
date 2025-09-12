from .conexao import BancoDeDados
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
        self.db.desconectar(self.cursor)

    def alterar_modelo(self, modelo_antigo, modelo_novo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo_antigo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET modelo = '{modelo_novo}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.db.desconectar(self.cursor)

    def alterar_marca(self, modelo, marca_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET marca = '{marca_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.db.desconectar(self.cursor)

    def alterar_categoria(self, modelo, categoria_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET categoria = '{categoria_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.db.desconectar(self.cursor)

    def alterar_preco(self, modelo, preco_novo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET preco = '{preco_novo}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.db.desconectar(self.cursor)

    def alterar_quant(self, modelo, quant_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET quant = '{quant_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.db.desconectar(self.cursor)

    def alterar_nota(self, modelo, nota_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET nota = '{nota_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.db.desconectar(self.cursor)

    def pesquisar(self, modelo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        for linha in resultado:
            print(linha)
        self.db.desconectar(self.cursor)

    def remover(self, modelo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"DELETE FROM produto WHERE modelo = '{modelo}'")
        self.conexao.commit()
        self.db.desconectar(self.cursor)

    def listar_todos(self):
        self.cursor = self.conexao.cursor()
        self.cursor.execute("SELECT * FROM produto")
        resultado = self.cursor.fetchall()
        for linha in resultado:
            print(linha)
        self.db.desconectar(self.cursor)

    def exibir_um(self):
        None