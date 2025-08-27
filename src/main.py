from Models import Banco_de_dados

banco = Banco_de_dados.BancoDeDados()


if banco.conexao:
    print("Conexão bem-sucedida ao banco de dados.")
    banco.fechar_conexao()
