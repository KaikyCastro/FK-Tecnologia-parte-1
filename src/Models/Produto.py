from psycopg2.errors import UniqueViolation
from database.Conexao import ConexaoBD
from logger_config import log

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

        log.info(f"Produto inserido: Modelo='{modelo}', Marca='{marca}', Categoria='{categoria}', Preço='{preco}', Quantidade='{quant}', Nota='{nota}'")

    def alterar_produto(self, modelo_antigo, modelo_novo, marca, categoria, preco, quant, nota):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"UPDATE produto SET modelo = '{modelo_novo}', marca = '{marca}', categoria = '{categoria}', preco = '{preco}', quant = '{quant}', nota = '{nota}' WHERE modelo = '{modelo_antigo}'")
        self.conexao.commit()

        log.info(f"Produto alterado: Modelo Antigo='{modelo_antigo}', Modelo Novo='{modelo_novo}', Marca='{marca}', Categoria='{categoria}', Preço='{preco}', Quantidade='{quant}', Nota='{nota}'")

    def pesquisar_modelo_produto(self, modelo) -> tuple:
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"SELECT * FROM produto WHERE modelo = '{modelo}'")
        resultado = self.cursor.fetchone()
        return resultado

        log.info(f"Pesquisa de produto realizada para o modelo: '{modelo}'")
    
    def remover_produto(self, modelo):
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"DELETE FROM produto WHERE modelo = '{modelo}'")
        self.conexao.commit()

        log.info(f"Produto removido: Modelo='{modelo}'")

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
    
        log.info(f"Exibição de produto realizada para o modelo: '{modelo}'")
    
    def pesquisar_produto_parcial (self, modelo_parcial) -> list:
        self.cursor = self.conexao.cursor()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE modelo ILIKE '%{modelo_parcial}%'")
            resultado = self.cursor.fetchall()
            return resultado
        except Exception as e:
            print(f"Erro ao pesquisar produto: {e}")
            return []

    def contar_total_produtos(self):
        try:
            self.cursor = self.conexao.cursor()
            self.cursor.execute("SELECT COUNT(*) FROM produto")
            total = self.cursor.fetchone()
            return total[0] if total else 0
        except Exception as e:
            print(f"Erro ao contar produtos: {e}")
            return 0
        
    def calcular_valor_total_estoque(self):
        try:
            self.cursor = self.conexao.cursor()
            self.cursor.execute("SELECT SUM(preco * quant) FROM produto")
            total_valor = self.cursor.fetchone()
            return total_valor[0] if total_valor and total_valor[0] is not None else 0.0
        except Exception as e:
            print(f"Erro ao calcular valor total do estoque: {e}")
            return 0.0
        
    def listar_todos_modelos_marcas(self):
        try:
            self.cursor = self.conexao.cursor()
            self.cursor.execute("SELECT modelo, marca FROM produto")
            resultados = self.cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar modelos e marcas: {e}")
            return []