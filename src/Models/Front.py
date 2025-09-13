import customtkinter
from PIL import Image
from tkinter import END, messagebox
from .Produto import Produto
class FrontModel(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("FK Tecnologia")
        self.resizable(False, False)
        self._fg_color = "#FFFFFF"
        self._set_appearance_mode("light")
        self.tela_inicial()
        self.produto = Produto()
        

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
                                                fg_color="#818181", 
                                                hover_color="#9C9C9C", 
                                                text_color="#060505", 
                                                bg_color="#FFFFFF", 
                                                command=self.tela_menu)
        self.button.place(x=1090, y=650)
        self.bind("<Return>", lambda event: self.tela_menu())

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
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200,
                                                        command=self.pagina_cadastrar_produto)
        self.button_cadastrar.place(x=100, y=150)
        self.bind("<F1>", lambda event: self.pagina_cadastrar_produto())

        self.button_alterar = customtkinter.CTkButton(self.frame_menu,
                                                        text="F2 - Alterar Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200,
                                                        command=self.pagina_alterar_produto)
        self.button_alterar.place(x=510, y=150)
        self.bind("<F2>", lambda event: self.pagina_alterar_produto())


        self.pesquisar_produto = customtkinter.CTkButton(self.frame_menu,
                                                        text="F3 - Pesquisar Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200,
                                                        command=self.pagina_pesquisar_produto)
        self.pesquisar_produto.place(x=920, y=150)
        self.bind("<F3>", lambda event: self.pagina_pesquisar_produto())

        self.remover_produto = customtkinter.CTkButton(self.frame_menu,
                                                        text="F4 - Remover Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200,
                                                        command=self.pagina_remover_produto)
        self.remover_produto.place(x=100, y=400)
        self.bind("<F4>", lambda event: self.pagina_remover_produto())

        self.listar_todos_produtos = customtkinter.CTkButton(self.frame_menu,
                                                        text="F5 - Todos os Produtos",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200,
                                                        command=self.pagina_listar_todos_produtos)
        self.listar_todos_produtos.place(x=510, y=400)
        self.bind("<F5>", lambda event: self.pagina_listar_todos_produtos())

        self.exibir_um_produto = customtkinter.CTkButton(self.frame_menu,
                                                        text="F6 - Exibir Um Produto",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=250,
                                                        height=200,
                                                        command=self.pagina_exibir_um_produto)
        self.exibir_um_produto.place(x=920, y=400)
        self.bind("<F6>", lambda event: self.pagina_exibir_um_produto())

        self.buttor_voltar_tela_inicial = customtkinter.CTkButton(self.frame_menu,
                                                                    text="Voltar",
                                                                    font=("Montserrat Medium", 20),
                                                                    fg_color="#818181",
                                                                    hover_color="#9C9C9C",
                                                                    text_color="#060505",
                                                                    bg_color="#FFFFFF",
                                                                    width=100,
                                                                    height=40,
                                                                    command=self.tela_inicial)
        self.buttor_voltar_tela_inicial.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_inicial())

    def pagina_cadastrar_produto(self, event=None):
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
                                                    border_color="#000000",
                                                    text_color="#000000")
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
                                                    border_color="#000000",
                                                    text_color="#000000")
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
                                                    border_color="#000000",
                                                    text_color="#000000")
        self.entry_categoria.place(x=450, y=290)

        self.label_preco = customtkinter.CTkLabel(self.frame_cadastro,
                                                    text="Preço:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_preco.place(x=300, y=360)

        self.entry_preco = customtkinter.CTkEntry(self.frame_cadastro,
                                                    width=400,
                                                    height=40,
                                                    font=("Montserrat Medium", 16),
                                                    fg_color="#D9D9D9",
                                                    border_width=2,
                                                    border_color="#000000",
                                                    text_color="#000000")
        self.entry_preco.place(x=450, y=360)

        self.label_quant = customtkinter.CTkLabel(self.frame_cadastro,
                                                    text="Quantidade:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_quant.place(x=300, y=430)

        self.entry_quant = customtkinter.CTkEntry(self.frame_cadastro,
                                                    width=400,
                                                    height=40,
                                                    font=("Montserrat Medium", 16),
                                                    fg_color="#D9D9D9",
                                                    border_width=2,
                                                    border_color="#000000",
                                                    text_color="#000000")
        self.entry_quant.place(x=450, y=430)

        self.label_nota = customtkinter.CTkLabel(self.frame_cadastro,
                                                    text="Nota (0-5):",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_nota.place(x=300, y=500)

        self.entry_nota = customtkinter.CTkEntry(self.frame_cadastro,
                                                    width=400,
                                                    height=40,
                                                    font=("Montserrat Medium", 16),
                                                    fg_color="#D9D9D9",
                                                    border_width=2,
                                                    border_color="#000000",
                                                    text_color="#000000")
        self.entry_nota.place(x=450, y=500)

        self.button_cadastrar_produto = customtkinter.CTkButton(self.frame_cadastro,
                                                                text="Cadastrar",
                                                                font=("Montserrat Medium", 20),
                                                                fg_color="#818181",
                                                                hover_color="#9C9C9C",
                                                                text_color="#060505",
                                                                bg_color="#FFFFFF",
                                                                width=150,
                                                                height=40,
                                                                command=self.cad_prod)
        self.button_cadastrar_produto.place(x=550, y=600)
        self.bind("<Return>", lambda event: self.cad_prod())

        self.button_voltar_cadastro = customtkinter.CTkButton(self.frame_cadastro,
                                                        text="Voltar",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=100,
                                                        height=40,
                                                        command=self.tela_menu)
        self.button_voltar_cadastro.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_menu())

    def cad_prod(self):
        try:
            if (self.entry_modelo.get() == "" or self.entry_marca.get() == "" or self.entry_categoria.get() == "" or
                self.entry_preco.get() == "" or self.entry_quant.get() == "" or self.entry_nota.get() == ""):
                raise ValueError("Todos os campos devem ser preenchidos.")
            if not self.entry_preco.get().replace('.', '', 1).isdigit():
                raise ValueError("O campo 'Preço' deve ser um número válido.")
            if not self.entry_quant.get().isdigit():
                raise ValueError("O campo 'Quantidade' deve ser um número inteiro válido.")
            if not self.entry_nota.get().replace('.', '', 1).isdigit():
                raise ValueError("O campo 'Nota' deve ser um número válido entre 0 e 5.")
            nota = float(self.entry_nota.get())
            if nota < 0 or nota > 5:
                raise ValueError("O campo 'Nota' deve estar entre 0 e 5.")
        except ValueError as ve:
            messagebox.showerror("Erro de Validação", str(ve))
            return

        modelo = self.entry_modelo.get().capitalize()
        marca = self.entry_marca.get().capitalize()
        categoria = self.entry_categoria.get().capitalize()
        preco = self.entry_preco.get()
        quant = self.entry_quant.get()
        nota = self.entry_nota.get()

        self.produto.inserir_produto(modelo, marca, categoria, preco, quant, nota)

        self.entry_modelo.delete(0, END)
        self.entry_marca.delete(0, END)
        self.entry_categoria.delete(0, END)
        self.entry_preco.delete(0, END)
        self.entry_quant.delete(0, END)
        self.entry_nota.delete(0, END)


    def pagina_alterar_produto(self):
        self.frame_menu.destroy()

        self.frame_alterar = customtkinter.CTkFrame(self,
                                                    width=1280,
                                                    height=720,
                                                    fg_color="#FFFFFF")
        self.frame_alterar.pack()

        self.label_alterar = customtkinter.CTkLabel(self.frame_alterar,
                                                    text="ALTERAR PRODUTO",
                                                    font=("Montserrat Medium", 30),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_alterar.place(relx=0.5, y=50, anchor="center")

        self.label_modelo_antigo = customtkinter.CTkLabel(self.frame_alterar,
                                                            text="Digite o modelo do produto que deseja alterar:",
                                                            font=("Montserrat Medium", 20),
                                                            text_color="#000000",
                                                            fg_color="#FFFFFF")
        self.label_modelo_antigo.place(x=100, y=150)

        self.entry_modelo_antigo = customtkinter.CTkEntry(self.frame_alterar,
                                                            width=400,
                                                            height=40,
                                                            font=("Montserrat Medium", 16),
                                                            fg_color="#D9D9D9",
                                                            border_width=2,
                                                            border_color="#000000",
                                                            text_color="#000000")
        self.entry_modelo_antigo.place(x=600, y=150)




    def pagina_pesquisar_produto(self):
        None

    def pagina_remover_produto(self):
        self.dialog_remover = customtkinter.CTkInputDialog(text="Digite o modelo do produto que deseja remover:", title="Remover Produto")
        input_user = self.dialog_remover.get_input()
        try:
            if input_user == "":
                raise ValueError("O campo 'Modelo' deve ser preenchido.")
        except ValueError as ve:
            messagebox.showerror("Erro de Validação", str(ve))
            return
        if input_user:
            modelo = input_user.capitalize()
            if modelo:
                resultado = self.produto.pesquisar_modelo_produto(modelo)
                if resultado:
                    confirm = messagebox.askyesno("Confirmação", f"Tem certeza que deseja remover o produto '{modelo}'?")
                    if confirm:
                        self.produto.remover_produto(modelo)
                        messagebox.showinfo("Remoção Bem Sucedida", f"O produto '{modelo}' foi removido com sucesso.")
                    else:
                        messagebox.showinfo("Remoção Cancelada", "A remoção do produto foi cancelada.")
                else:
                    messagebox.showinfo("Produto Não Encontrado", f"Nenhum produto encontrado com o modelo '{modelo}'.")

    def pagina_listar_todos_produtos(self):

        None

    def pagina_exibir_um_produto(self):
        self.frame_menu.destroy()

        self.frame_exibir = customtkinter.CTkFrame(self,
                                                    width=1280,
                                                    height=720,
                                                    fg_color="#FFFFFF")
        self.frame_exibir.pack()

        self.label_exibir = customtkinter.CTkLabel(self.frame_exibir,
                                                    text="EXIBIR UM PRODUTO",
                                                    font=("Montserrat Medium", 30),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_exibir.place(relx=0.5, y=50, anchor="center")

        self.label_modelo = customtkinter.CTkLabel(self.frame_exibir,
                                                    text="Qual modelo deseja exibir?",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_modelo.place(x=300, y=200)

        self.entry_modelo = customtkinter.CTkEntry(self.frame_exibir,
                                                    width=400,
                                                    height=40,
                                                    font=("Montserrat Medium", 16),
                                                    fg_color="#D9D9D9",
                                                    border_width=2,
                                                    border_color="#000000",
                                                    text_color="#000000")
        self.entry_modelo.place(x=650, y=200)

        self.button_exibir_produto = customtkinter.CTkButton(self.frame_exibir,
                                                                text="Exibir",
                                                                font=("Montserrat Medium", 20),
                                                                fg_color="#818181",
                                                                hover_color="#9C9C9C",
                                                                text_color="#060505",
                                                                bg_color="#FFFFFF",
                                                                width=150,
                                                                height=40,
                                                                command=self.exibir_produto)
        self.button_exibir_produto.place(x=550, y=300)
        self.bind("<Return>", lambda event: self.exibir_produto())

        button_voltar_exibir = customtkinter.CTkButton(self.frame_exibir,
                                                        text="Voltar",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=100,
                                                        height=40,
                                                        command=self.tela_menu)
        button_voltar_exibir.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_menu())

    def exibir_produto(self):
        try:
            if self.entry_modelo.get() == "":
                raise ValueError("O campo 'Modelo' deve ser preenchido.")
        except ValueError as ve:
            messagebox.showerror("Erro de Validação", str(ve))
            return
        
        modelo = self.entry_modelo.get().capitalize()
        resultado = self.produto.exibir_um_produto(modelo)
        if not resultado:
            messagebox.showinfo("Produto Não Encontrado", f"Nenhum produto encontrado com o modelo '{modelo}'.")
            self.entry_modelo.delete(0, END)
            return

        frame_result = customtkinter.CTkFrame(self.frame_exibir,
                                                width=800,
                                                height=200,
                                                fg_color="#B9B9B9")
        frame_result.place(anchor="center", relx=0.5, rely=0.7)

        label_modelo = customtkinter.CTkLabel(frame_result,
                                                text="Modelo:",
                                                font=("Montserrat Medium", 25),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_modelo.place(x=20, y=20)

        label_modelo_result = customtkinter.CTkLabel(frame_result,
                                                text=resultado[1],
                                                font=("Montserrat Medium", 20),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_modelo_result.place(x=130, y=24)

        label_marca = customtkinter.CTkLabel(frame_result,
                                                text="Marca:",
                                                font=("Montserrat Medium", 25),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_marca.place(x=20, y=85)

        label_marca_result = customtkinter.CTkLabel(frame_result,
                                                text=resultado[2],
                                                font=("Montserrat Medium", 20),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_marca_result.place(x=115, y=89)

        label_categoria = customtkinter.CTkLabel(frame_result,
                                                text="Categoria:",
                                                font=("Montserrat Medium", 25),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_categoria.place(x=20, y=150)

        label_categoria_result = customtkinter.CTkLabel(frame_result,
                                                text=resultado[3],
                                                font=("Montserrat Medium", 20),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_categoria_result.place(x=160, y=154)

        label_preco = customtkinter.CTkLabel(frame_result,
                                                text="Preço:",
                                                font=("Montserrat Medium", 25),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_preco.place(x=400, y=20)

        label_preco_result = customtkinter.CTkLabel(frame_result,
                                                text=f"R$ {resultado[4]:.2f}",
                                                font=("Montserrat Medium", 20),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_preco_result.place(x=490, y=24)

        label_quant = customtkinter.CTkLabel(frame_result,
                                                text="Quantidade:",
                                                font=("Montserrat Medium", 25),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_quant.place(x=400, y=85)

        label_quant_result = customtkinter.CTkLabel(frame_result,
                                                text=resultado[5],
                                                font=("Montserrat Medium", 20),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_quant_result.place(x=568, y=89)

        label_nota = customtkinter.CTkLabel(frame_result,
                                                text="Nota:",
                                                font=("Montserrat Medium", 25),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_nota.place(x=400, y=150)

        label_nota_result = customtkinter.CTkLabel(frame_result,
                                                text=f"{resultado[6]:.1f}",
                                                font=("Montserrat Medium", 20),
                                                text_color="#000000",
                                                fg_color="#B9B9B9")
        label_nota_result.place(x=480, y=154)

        self.entry_modelo.delete(0, END)

