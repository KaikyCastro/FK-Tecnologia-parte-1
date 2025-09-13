from Models.front import FrontModel
from Models.Produto import Produto


if __name__ == "__main__":
    produto = Produto("iPhone 13", "Apple", "Smartphone", 799.99, 50, 4.8)
    #consulta.pesquisar("Kaiky")
    #consulta.listar_todos()
    #consulta.remover("iPhone 13")
    #consulta.alterar_modelo("iPhone 13", "iPhone 14")
    #consulta.alterar_marca("iPhone 13", "Apple Inc.")
    #consulta.alterar_categoria("iPhone 13", "Celular")
    #consulta.alterar_preco("iPhone 13", 899.99)
    #consulta.alterar_quant("iPhone 13", 45)
    #consulta.alterar_nota("iPhone 13", 4.9)
    #consulta.inserir("Galaxy S21", "Samsung", "Smartphone", 699.99, 30, 4.6)
    produto.listar_todos()
    #consulta.inserir("Book 4", "Samsung", "Notebook", 3499.99, 20, 4.7)

    #app = FrontModel()
    #app.mainloop()