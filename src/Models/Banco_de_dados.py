import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv("PASSWORD")
if PASSWORD is None:
    print("Erro: A variável de ambiente 'PASSWORD' não está definida.")
    exit()

class BancoDeDados:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="fk_tecnologia",
                user="kaikycastro",
                password=PASSWORD
            )
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conexao = None

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print("Conexão fechada com sucesso.")
        else:
            print("Nenhuma conexão ativa para fechar.")


    
