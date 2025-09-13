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

    def alterar_modelo_produto(self, modelo_antigo, modelo_novo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo_antigo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET modelo = '{modelo_novo}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.cursor.close()

    def alterar_marca_produto(self, modelo, marca_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET marca = '{marca_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.cursor.close()

    def alterar_categoria_produto(self, modelo, categoria_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET categoria = '{categoria_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.cursor.close()

    def alterar_preco_produto(self, modelo, preco_novo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET preco = '{preco_novo}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.cursor.close()

    def alterar_quant_produto(self, modelo, quant_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET quant = '{quant_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.cursor.close()

    def alterar_nota_produto(self, modelo, nota_nova):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchall()
        self.cursor.execute(f"UPDATE produto SET nota = '{nota_nova}' WHERE id = {resultado[0][0]}")
        self.conexao.commit()
        self.cursor.close()

    def pesquisar_produto(self, modelo, conexao):
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
        for linha in resultado:
            print(linha)
        self.cursor.close()

