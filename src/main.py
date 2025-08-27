from database import conexao

banco = conexao.BancoDeDados()


if banco.conectar():
    print("Conexão bem-sucedida ao banco de dados.")
    banco.desconectar()
