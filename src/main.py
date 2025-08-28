from database.consulta import Consulta

if __name__ == "__main__":
    consulta = Consulta()
    #consulta.inserir("iPhone 13", "Apple", "Smartphone", 799.99, 50, 4.8)
    #consulta.pesquisar("Kaiky")
    consulta.listar_todos()
    #consulta.remover("iPhone 13")