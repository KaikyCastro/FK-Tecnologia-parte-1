from database.consulta import Consulta

class Produto:
    def __init__(self, modelo, marca, categoria, preco, quant, nota):
        self.modelo = modelo
        self.marca = marca
        self.categoria = categoria
        self.preco = preco
        self.quant = quant
        self.nota = nota

        self.con = Consulta()
        self.con.inserir(self.modelo, self.marca, self.categoria, self.preco, self.quant, self.nota)

    def listar_todos(self):
        self.con.listar_todos()
    

        
        