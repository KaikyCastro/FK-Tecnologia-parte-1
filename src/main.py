

banco = BancoDeDados()


if banco.conexao:
    print("Conexão bem-sucedida ao banco de dados.")
    banco.fechar_conexao()
