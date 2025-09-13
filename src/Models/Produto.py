from psycopg2.errors import UniqueViolation

class Produto:
    def __init__(self):
        None

    def inserir_produto(self, modelo, marca, categoria, preco, quant, nota, conexao):
        self.cursor = conexao.cursor()
        try:
            self.cursor.execute(f"INSERT INTO produto (modelo, marca, categoria, preco, quant, nota) VALUES ('{modelo}', '{marca}', '{categoria}', '{preco}', '{quant}', '{nota}')")
        except UniqueViolation as e:
            print(f"Você está tentando inserir um modelo que já existe. \nErro: {e}")
        conexao.commit()
        self.cursor.close()

    def alterar_produto(self, modelo_antigo, modelo_novo, marca, categoria, preco, quant, nota, conexao):
        self.cursor = conexao.cursor()
        self.cursor.execute(f"UPDATE produto SET modelo = '{modelo_novo}', marca = '{marca}', categoria = '{categoria}', preco = '{preco}', quant = '{quant}', nota = '{nota}' WHERE modelo = '{modelo_antigo}'")
        conexao.commit()
        self.cursor.close()

    def pesquisar_modelo_produto(self, modelo, conexao):
        self.cursor = conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        for linha in resultado:
            print(linha)
        self.cursor.close()

    def remover_produto(self, modelo, conexao):
        self.cursor = conexao.cursor()
        self.cursor.execute(f"DELETE FROM produto WHERE modelo = '{modelo}'")
        conexao.commit()
        self.cursor.close()

    def listar_todos_produtos(self, conexao):
        self.cursor = conexao.cursor()
        self.cursor.execute("SELECT * FROM produto")
        resultado = self.cursor.fetchall()
        for linha in resultado:
            print(linha)
        self.cursor.close()

    def exibir_um_produto(self, modelo, conexao):
        self.cursor = conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        print(resultado)

