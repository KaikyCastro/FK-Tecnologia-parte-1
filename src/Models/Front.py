import customtkinter
from PIL import Image

class FrontModel(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("FK Tecnologia")
        self.resizable(False, False)
        self._fg_color = "#FFFFFF"
        self._set_appearance_mode("light")
        self.tela_inicial()
        self.botao_proximo()


    def tela_inicial(self):
        self.bem_vindo = customtkinter.CTkLabel(self, text="BEM VINDO A FK TECNOLOGIAS", font=("Montserrat Medium", 30), text_color="#000000", fg_color="#FFFFFF", width=400, height=50)
        self.bem_vindo.pack(pady=20)
        self.image = customtkinter.CTkImage(Image.open("assets/images/logo.jpeg"), size=(760, 570))
        self.logo = customtkinter.CTkLabel(self, image=self.image, text="")
        self.logo.pack(pady=0)
        
    def botao_proximo(self):
        self.button = customtkinter.CTkButton(self, text="Próximo", font=("Montserrat Medium", 20), fg_color="#5D5C5C", hover_color="#8D8C8C", text_color="#060505", bg_color="#FFFFFF", command=self.proxima_tela)
        self.button.place(x=1100, y=600)

    def proxima_tela(self):
        self.button.destroy()
        self.bem_vindo.destroy()
        self.logo.destroy()

        self.botao_inserir = customtkinter.CTkButton(self, text="Inserir Produto", font=("Montserrat Medium", 20), fg_color="#5D5C5C", hover_color="#8D8C8C", text_color="#060505", bg_color="#FFFFFF", width=200, height=200, command=self.inserir_produto)
        self.botao_inserir.place(x=100, y=200)

        self.botao_remover = customtkinter.CTkButton(self, text="Remover Produto", font=("Montserrat Medium", 20), fg_color="#5D5C5C", hover_color="#8D8C8C", text_color="#060505", bg_color="#FFFFFF", width=200, height=200)
        self.botao_remover.place(x=320, y=200)

        self.botao_pesquisar = customtkinter.CTkButton(self, text="Pesquisar Produto", font=("Montserrat Medium", 20), fg_color="#5D5C5C", hover_color="#8D8C8C", text_color="#060505", bg_color="#FFFFFF", width=200, height=200)
        self.botao_pesquisar.place(x=550, y=200)

        self.botao_listar = customtkinter.CTkButton(self, text="Listar Produtos", font=("Montserrat Medium", 20), fg_color="#5D5C5C", hover_color="#8D8C8C", text_color="#060505", bg_color="#FFFFFF", width=200, height=200)
        self.botao_listar.place(x=1050, y=200)

        self.botao_voltar = customtkinter.CTkButton(self, text="Voltar", font=("Montserrat Medium", 20), fg_color="#5D5C5C", hover_color="#8D8C8C", text_color="#060505", bg_color="#FFFFFF", command=self.voltar_tela_inicial)
        self.botao_voltar.place(x=20, y=20)

    def voltar_tela_inicial(self):
        self.botao_inserir.destroy()
        self.botao_remover.destroy()
        self.botao_pesquisar.destroy()
        self.botao_listar.destroy()
        self.botao_voltar.destroy()

        self.tela_inicial()
        self.botao_proximo()


    def inserir_produto(self):
        self.botao_inserir.destroy()
        self.botao_remover.destroy()
        self.botao_pesquisar.destroy()
        self.botao_listar.destroy()
        self.botao_voltar.destroy()

        self.nome_produto = customtkinter.CTkEntry(self, placeholder_text="Nome do Produto", font=("Montserrat Medium", 20), width=300, height=50)
        self.nome_produto.place(x=490, y=100)

    

