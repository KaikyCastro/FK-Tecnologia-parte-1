from Models.Front import FrontModel
from Models.Produto import Produto
from database.Conexao import ConexaoBD


if __name__ == "__main__":
    conn = ConexaoBD()
    conexao = conn.conectar()
    if conexao:
        print("Conexão bem-sucedida ao banco de dados.")
    else:
        print("Falha na conexão ao banco de dados.")


    #produto = Produto()
    #produto.inserir_produto("Samsung Book 4", "Samsung", "Notebook", 3499.99, 20, 4.7, conexao)
    #produto.listar_todos_produtos(conexao)
    #produto.pesquisar_modelo_produto("Samsung Book 4", conexao)
    app = FrontModel()
    app.mainloop()
    
    conn.desconectar()
    print("Programa finalizado.")