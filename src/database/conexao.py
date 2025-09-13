import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv("PASSWORD")
if PASSWORD is None:
    print("Erro: A variável de ambiente 'PASSWORD' não está definida.")
    exit()

class ConexaoBD:
    def __init__(self):
        None
    
    def conectar(self) -> psycopg2.extensions.connection:
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="fk_tecnologia",
                user="kaikycastro",
                password=PASSWORD
            )   
            return self.conexao
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conexao = None

    def desconectar(self, cursor):
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print("Conexão fechada com sucesso.")
        else:
            print("Nenhuma conexão ativa para fechar.")

        self.cursor = cursor
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            print("Cursor fechado com sucesso.")
        else:
            print("Nenhum cursor ativo para fechar.")