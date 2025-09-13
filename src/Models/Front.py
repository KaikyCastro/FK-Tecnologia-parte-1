import customtkinter
from PIL import Image
from tkinter import END
from .Produto import Produto
from database.Conexao import ConexaoBD
class FrontModel(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("FK Tecnologia")
        self.resizable(False, False)
        self._fg_color = "#FFFFFF"
        self._set_appearance_mode("light")
        self.conn = ConexaoBD()
        self.conexao = self.conn.conectar()
        if self.conexao:
            print("Conexão ao banco de dados realizada com sucesso.")
        else:
            print("Falha na conexão ao banco de dados.")
        self.tela_inicial()
        

    def tela_inicial(self):
        if hasattr(self, 'frame_menu'):
            self.frame_menu.destroy()

        self.frame_inicial = customtkinter.CTkFrame(self, 
                                                    width=1280, 
                                                    height=720, 
                                                    fg_color="#FFFFFF")
        self.frame_inicial.pack()

        self.bem_vindo = customtkinter.CTkLabel(self.frame_inicial, 
                                                text="BEM VINDO A FK TECNOLOGIAS", 
                                                font=("Montserrat Medium", 30), 
                                                text_color="#000000", 
                                                fg_color="#FFFFFF", 
                                                width=400, 
                                                height=50)
        self.bem_vindo.place(relx=0.5, y=50, anchor="center")
        
        self.image = customtkinter.CTkImage(Image.open("assets/images/logo.jpeg"), size=(760, 570))
        self.logo = customtkinter.CTkLabel(self.frame_inicial, 
                                           image=self.image, 
                                           text="")
        self.logo.place(relx=0.5, rely=0.5, anchor="center")
        
        self.button = customtkinter.CTkButton(self.frame_inicial, 
                                                text="Próximo", 
                                                font=("Montserrat Medium", 20), 
                                                fg_color="#5D5C5C", 
                                                hover_color="#8D8C8C", 
                                                text_color="#060505", 
                                                bg_color="#FFFFFF", 
                                                command=self.tela_menu)
        self.button.place(x=1090, y=650)

    def tela_menu(self):
        self.frame_inicial.destroy()
        if hasattr(self, 'frame_cadastro'):
            self.frame_cadastro.destroy()
        if hasattr(self, 'frame_alterar'):
            self.frame_alterar.destroy()
        if hasattr(self, 'frame_pesquisar'):
            self.frame_pesquisar.destroy()
        if hasattr(self, 'frame_remover'):
            self.frame_remover.destroy()
        if hasattr(self, 'frame_listar'):
            self.frame_listar.destroy()
        if hasattr(self, 'frame_exibir'):
            self.frame_exibir.destroy()

        self.frame_menu = customtkinter.CTkFrame(self,
                                                    width=1280,
                                                    height=720,
                                                    fg_color="#FFFFFF")
        self.frame_menu.pack()

        self.label_menu = customtkinter.CTkLabel(self.frame_menu,
                                                    text="MENU",
                                                    font=("Montserrat Medium", 30),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_menu.place(relx=0.5, y=50, anchor="center")

        self.button_cadastrar = customtkinter.CTkButton(self.frame_menu,
                                                        text="F1 - Cadastrar Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#5D5C5C",
                                                        hover_color="#8D8C8C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200,
                                                        command=self.cadastrar_produto)
        self.button_cadastrar.place(x=100, y=150)
        self.bind("<F1>", lambda event: self.cadastrar_produto())

        self.button_alterar = customtkinter.CTkButton(self.frame_menu,
                                                        text="F2 - Alterar Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#5D5C5C",
                                                        hover_color="#8D8C8C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200)
        self.button_alterar.place(x=510, y=150)
        self.bind("<F2>", lambda event: self.alterar_produto_func())


        self.pesquisar_produto = customtkinter.CTkButton(self.frame_menu,
                                                        text="F3 - Pesquisar Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#5D5C5C",
                                                        hover_color="#8D8C8C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200)
        self.pesquisar_produto.place(x=920, y=150)
        self.bind("<F3>", lambda event: self.pesquisar_produto_func())

        self.remover_produto = customtkinter.CTkButton(self.frame_menu,
                                                        text="F4 - Remover Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#5D5C5C",
                                                        hover_color="#8D8C8C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200)
        self.remover_produto.place(x=100, y=400)
        self.bind("<F4>", lambda event: self.remover_produto_func())

        self.listar_todos_produtos = customtkinter.CTkButton(self.frame_menu,
                                                        text="F5 - Todos os Produtos",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#5D5C5C",
                                                        hover_color="#8D8C8C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200)
        self.listar_todos_produtos.place(x=510, y=400)
        self.bind("<F5>", lambda event: self.listar_todos_produtos_func())

        self.exibir_um_produto = customtkinter.CTkButton(self.frame_menu,
                                                        text="F6 - Exibir Um Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#5D5C5C",
                                                        hover_color="#8D8C8C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200)
        self.exibir_um_produto.place(x=920, y=400)
        self.bind("<F6>", lambda event: self.exibir_um_produto_func())

        self.buttor_voltar_tela_inicial = customtkinter.CTkButton(self.frame_menu,
                                                                    text="Voltar",
                                                                    font=("Montserrat Medium", 20),
                                                                    fg_color="#5D5C5C",
                                                                    hover_color="#8D8C8C",
                                                                    text_color="#060505",
                                                                    bg_color="#FFFFFF",
                                                                    width=100,
                                                                    height=40,
                                                                    command=self.tela_inicial)
        self.buttor_voltar_tela_inicial.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_inicial())



    def cadastrar_produto(self, event=None):
        self.frame_menu.destroy()

        self.frame_cadastro = customtkinter.CTkFrame(self,
                                                    width=1280,
                                                    height=720,
                                                    fg_color="#FFFFFF")
        self.frame_cadastro.pack()

        self.label_cadastro = customtkinter.CTkLabel(self.frame_cadastro,
                                                    text="CADASTRO DE PRODUTO",
                                                    font=("Montserrat Medium", 30),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_cadastro.place(relx=0.5, y=50, anchor="center")

        self.label_modelo = customtkinter.CTkLabel(self.frame_cadastro,
                                                    text="Modelo:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_modelo.place(x=300, y=150)

        self.entry_modelo = customtkinter.CTkEntry(self.frame_cadastro,
                                                    width=400,
                                                    height=40,
                                                    font=("Montserrat Medium", 16),
                                                    fg_color="#D9D9D9",
                                                    border_width=2,
                                                    border_color="#000000")
        self.entry_modelo.place(x=450, y=150)

        self.label_marca = customtkinter.CTkLabel(self.frame_cadastro,
                                                    text="Marca:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_marca.place(x=300, y=220)

        self.entry_marca = customtkinter.CTkEntry(self.frame_cadastro,
                                                    width=400,
                                                    height=40,
                                                    font=("Montserrat Medium", 16),
                                                    fg_color="#D9D9D9",
                                                    border_width=2,
                                                    border_color="#000000")
        self.entry_marca.place(x=450, y=220)

        self.label_categoria = customtkinter.CTkLabel(self.frame_cadastro,
                                                    text="Categoria:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_categoria.place(x=300, y=290)

        self.entry_categoria = customtkinter.CTkEntry(self.frame_cadastro,
                                                    width=400,
                                                    height=40,
                                                    font=("Montserrat Medium", 16),
                                                    fg_color="#D9D9D9",
                                                    border_width=2,
                                                    border_color="#000000")
        self.entry_categoria.place(x=450, y=290)

        self.button_voltar_cadastro = customtkinter.CTkButton(self.frame_cadastro,
                                                        text="Voltar",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#5D5C5C",
                                                        hover_color="#8D8C8C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=100,
                                                        height=40,
                                                        command=self.tela_menu)
        self.button_voltar_cadastro.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_menu())

    def alterar_produto_func(self):
        None

    def pesquisar_produto_func(self):
        None

    def remover_produto_func(self):
        None

    def listar_todos_produtos_func(self):

        None

    def exibir_um_produto_func(self):
        None
    