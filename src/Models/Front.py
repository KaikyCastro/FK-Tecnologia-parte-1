import customtkinter
from PIL import Image
from tkinter import END, messagebox
from .Produto import Produto
from fpdf import FPDF
from datetime import datetime
import os
import subprocess
import sys
from logger_config import log

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

    def unbind_pagina(self):
        self.unbind("<F1>")
        self.unbind("<F2>")
        self.unbind("<F3>")
        self.unbind("<F4>")
        self.unbind("<F5>")
        self.unbind("<F6>")
        self.unbind("<F7>")
        self.unbind("<Escape>")
        self.unbind("<Return>")


    def tela_inicial(self):
        if hasattr(self, 'frame_menu'):
            self.frame_menu.destroy()

        self.unbind_pagina()

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

        self.unbind("<Return>")
        self.unbind("<Escape>")

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

        self.bind("<F7>", lambda event: self.evento_gerar_relatorio())

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

    def evento_gerar_relatorio(self, event=None):
        try:
            nome_arquivo = self.gerar_relatorio_pdf()
            messagebox.showinfo("Sucesso", f"Relatório PDF gerado com sucesso!\nSalvo como: {nome_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar relatório PDF: {e}")
            log.error(f"Erro ao gerar relatório PDF: {e}")

    
    def gerar_relatorio_pdf(self):
        """
        Gera um PDF com um resumo do estoque e o log de atividades.
        Versão final e limpa.
        """
        try:
            log_file_path = 'logs/atividades.log'
            
            pdf = FPDF()
            pdf.add_page()

            # --- TÍTULO PRINCIPAL ---
            pdf.set_font('Helvetica', 'B', 16)
            pdf.cell(w=0, h=10, txt='Relatório Completo - FK Tecnologia', border=0, ln=1, align='C')
            pdf.ln(5)

            # --- SEÇÃO 1: RESUMO DO ESTOQUE ATUAL ---
            pdf.set_font('Helvetica', 'B', 14)
            pdf.cell(w=0, h=10, txt='1. Resumo do Estoque', border=0, ln=1, align='L')
            pdf.ln(2)

            # Busca os dados de resumo no banco de dados
            total_produtos = self.produto.contar_total_produtos()
            valor_estoque = self.produto.calcular_valor_total_estoque()
            lista_modelos_marcas = self.produto.listar_todos_modelos_marcas()

            pdf.set_font('Helvetica', '', 12)
            pdf.cell(w=0, h=8, txt=f"   - Total de Produtos Cadastrados: {total_produtos}", border=0, ln=1)
            pdf.cell(w=0, h=8, txt=f"   - Valor Total do Estoque: R$ {valor_estoque:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), border=0, ln=1)
            pdf.ln(5)

            pdf.set_font('Helvetica', 'B', 12)
            pdf.cell(w=0, h=8, txt="   - Inventário de Modelos e Marcas:", border=0, ln=1)
            pdf.set_font('Courier', '', 10)
            
            largura_util = pdf.w - 2 * pdf.l_margin

            if lista_modelos_marcas:
                for modelo, marca in lista_modelos_marcas:
                    marca_str = str(marca)
                    modelo_str = str(modelo)
                    # Coluna 1: MARCA
                    pdf.cell(w=largura_util * 0.45, h=6, txt=f"     - {marca_str}", border=0)
                    # Coluna 2: MODELO
                    pdf.cell(w=largura_util * 0.55, h=6, txt=f"| {modelo_str}", border=0, ln=1)
            else:
                pdf.cell(w=0, h=6, txt="     Nenhum produto cadastrado.", border=0, ln=1)

            pdf.ln(10)

            # --- SEÇÃO 2: LOG DE ATIVIDADES ---
            pdf.set_font('Helvetica', 'B', 14)
            pdf.cell(w=0, h=10, txt='2. Histórico de Atividades', border=0, ln=1, align='L')
            pdf.ln(2)
            pdf.set_font('Courier', '', 8)
            
            if os.path.exists(log_file_path):
                with open(log_file_path, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha_strip = linha.strip()
                        palavras = linha_strip.split(' ')
                        altura_linha = 5
                        pdf.set_x(pdf.l_margin)

                        for palavra in palavras:
                            texto_para_escrever = ' ' + palavra
                            largura_palavra = pdf.get_string_width(texto_para_escrever)
                            
                            if pdf.get_x() + largura_palavra > (pdf.w - pdf.r_margin):
                                pdf.ln(altura_linha)
                                pdf.set_x(pdf.l_margin)
                                pdf.cell(txt=palavra)
                            else:
                                pdf.cell(txt=texto_para_escrever)
                                
                        pdf.ln(altura_linha)
            else:
                pdf.cell(w=0, h=5, txt="Nenhuma atividade registrada ainda.", border=0, ln=1)
            
            nome_arquivo = f"relatorio_completo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
            pdf.output(nome_arquivo)
            
            return nome_arquivo
        
        except Exception as e:
            # Mantemos o log de erro, mas removemos os prints do terminal
            # Supondo que você tenha o objeto 'log' importado e configurado
            log.error(f"FALHA CRÍTICA AO GERAR RELATÓRIO PDF: {e}")
            # Re-levanta a exceção para que o método que chamou saiba que algo deu errado
            raise e
            
    def pagina_cadastrar_produto(self, event=None):
        self.unbind_pagina()
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

        modelo = self.entry_modelo.get().title().strip()
        marca = self.entry_marca.get().title().strip()
        categoria = self.entry_categoria.get().title().strip()
        preco = self.entry_preco.get().strip()
        quant = self.entry_quant.get().strip()
        nota = self.entry_nota.get().strip()

        self.produto.inserir_produto(modelo, marca, categoria, preco, quant, nota)

        self.entry_modelo.delete(0, END)
        self.entry_marca.delete(0, END)
        self.entry_categoria.delete(0, END)
        self.entry_preco.delete(0, END)
        self.entry_quant.delete(0, END)
        self.entry_nota.delete(0, END)

        messagebox.showinfo("Sucesso", f"O produto '{modelo}' foi cadastrado com sucesso.")


    def pagina_alterar_produto(self):
        self.unbind_pagina()
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
        self.label_modelo_antigo.place(x=100, y=152)

        self.entry_modelo_antigo = customtkinter.CTkEntry(self.frame_alterar,
                                                            width=400,
                                                            height=40,
                                                            font=("Montserrat Medium", 16),
                                                            fg_color="#D9D9D9",
                                                            border_width=2,
                                                            border_color="#000000",
                                                            text_color="#000000")
        self.entry_modelo_antigo.place(x=600, y=150)

        self.button_procurar_produto = customtkinter.CTkButton(self.frame_alterar,
                                                                   text="Procurar",
                                                                   font=("Montserrat Medium", 20),
                                                                   fg_color="#818181",
                                                                   hover_color="#9C9C9C",
                                                                   text_color="#000000",
                                                                   bg_color="#FFFFFF",
                                                                   width=150,
                                                                   height=40,
                                                                   command=self.button_alterar_produto)
        self.button_procurar_produto.place(x=1050, y=150)
        self.bind("<Return>", lambda event: self.button_alterar_produto())        

        self.button_voltar_alterar = customtkinter.CTkButton(self.frame_alterar,
                                                        text="Voltar",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=100,
                                                        height=40,
                                                        command=self.tela_menu)
        self.button_voltar_alterar.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_menu())

    def button_alterar_produto(self):
        try:
            if self.entry_modelo_antigo.get() == "":
                raise ValueError("O campo 'Modelo' deve ser preenchido.")
            if not self.produto.pesquisar_modelo_produto(self.entry_modelo_antigo.get().title()):
                raise ValueError("Modelo não encontrado. Verifique o modelo e tente novamente.")
        except ValueError as ve:
            messagebox.showerror("Erro de Validação", str(ve))
            return

        modelo_antigo = self.entry_modelo_antigo.get().title().strip()
        resultado = self.produto.pesquisar_modelo_produto(modelo_antigo)
    
        self.frame_alterar_dados = customtkinter.CTkFrame(self.frame_alterar,
                                                            width=1100,
                                                            height=400,
                                                            fg_color="#D9D9D9")
        self.frame_alterar_dados.place(x=90, y=230)

        self.label_instrucoes = customtkinter.CTkLabel(self.frame_alterar_dados,
                                                        text="Altere os dados do produto abaixo:",
                                                        font=("Montserrat Medium", 20),
                                                        text_color="#000000",
                                                        fg_color="#D9D9D9")
        self.label_instrucoes.place(relx=0.5, y=10, anchor="n")

        self.label_modelo = customtkinter.CTkLabel(self.frame_alterar_dados,
                                                    text="Modelo:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
        self.label_modelo.place(x=50, y=70)

        self.entry_modelo = customtkinter.CTkEntry(self.frame_alterar_dados,
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF",
                                                    width=300)
        self.entry_modelo.place(x=200, y=70)
        self.entry_modelo.insert(0, resultado[1])

        self.label_marca = customtkinter.CTkLabel(self.frame_alterar_dados,
                                                    text="Marca:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
        self.label_marca.place(x=50, y=140)

        self.entry_marca = customtkinter.CTkEntry(self.frame_alterar_dados,
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF",
                                                    width=300)
        self.entry_marca.place(x=200, y=140)
        self.entry_marca.insert(0, resultado[2])

        self.label_categoria = customtkinter.CTkLabel(self.frame_alterar_dados,
                                                    text="Categoria:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
        self.label_categoria.place(x=50, y=210)

        self.entry_categoria = customtkinter.CTkEntry(self.frame_alterar_dados,
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF",
                                                    width=300)
        self.entry_categoria.place(x=200, y=210)
        self.entry_categoria.insert(0, resultado[3])

        self.label_preco = customtkinter.CTkLabel(self.frame_alterar_dados,
                                                    text="Preço:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
        self.label_preco.place(x=50, y=280)

        self.entry_preco = customtkinter.CTkEntry(self.frame_alterar_dados,
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF",
                                                    width=300)
        self.entry_preco.place(x=200, y=280)
        self.entry_preco.insert(0, resultado[4])

        self.label_quant = customtkinter.CTkLabel(self.frame_alterar_dados,
                                                    text="Quantidade:",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
        self.label_quant.place(x=550, y=70)

        self.entry_quant = customtkinter.CTkEntry(self.frame_alterar_dados,
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF",
                                                    width=300)
        self.entry_quant.place(x=750, y=70)
        self.entry_quant.insert(0, resultado[5])

        self.label_nota = customtkinter.CTkLabel(self.frame_alterar_dados,
                                                    text="Nota (0-5):",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
        self.label_nota.place(x=550, y=140)
        self.entry_nota = customtkinter.CTkEntry(self.frame_alterar_dados,
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF",
                                                    width=300)
        self.entry_nota.place(x=750, y=140)
        self.entry_nota.insert(0, resultado[6])

        self.button_salvar_alteracoes = customtkinter.CTkButton(self.frame_alterar,
                                                                text="Salvar Alterações",
                                                                font=("Montserrat Medium", 20),
                                                                fg_color="#818181",
                                                                hover_color="#9C9C9C",
                                                                text_color="#060505",
                                                                bg_color="#D9D9D9",
                                                                width=200,
                                                                height=40,
                                                                command=lambda: self.salvar_alteracoes(modelo_antigo))
        self.button_salvar_alteracoes.place(x=1030, y=650)
        self.bind("<Return>", lambda event: self.salvar_alteracoes(modelo_antigo))

    def salvar_alteracoes(self, modelo_antigo):
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

        modelo_novo = self.entry_modelo.get().title().strip()
        marca = self.entry_marca.get().title().strip()
        categoria = self.entry_categoria.get().title().strip()
        preco = self.entry_preco.get().strip()
        quant = self.entry_quant.get().strip()
        nota = self.entry_nota.get().strip()

        self.produto.alterar_produto(modelo_antigo, modelo_novo, marca, categoria, preco, quant, nota)
        messagebox.showinfo("Sucesso", f"O produto '{modelo_antigo}' foi alterado para '{modelo_novo}' com sucesso.")
        self.tela_menu()

    def pagina_pesquisar_produto(self):
        self.unbind_pagina()
        self.frame_menu.destroy()
        
        self.frame_pesquisar = customtkinter.CTkFrame(self,
                                                    width=1280,
                                                    height=720,
                                                    fg_color="#FFFFFF")
        self.frame_pesquisar.pack()

        self.label_pesquisar = customtkinter.CTkLabel(self.frame_pesquisar,
                                                    text="PESQUISAR PRODUTO",
                                                    font=("Montserrat Medium", 30),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_pesquisar.place(relx=0.5, y=50, anchor="center")

        self.label_modelo_parcial = customtkinter.CTkLabel(self.frame_pesquisar,
                                                    text="Digite o modelo do produto que deseja pesquisar:",
                                                    font=("Montserrat Medium", 16),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_modelo_parcial.place(relx=0.5, y=150, anchor="center")

        self.entry_modelo_parcial = customtkinter.CTkEntry(self.frame_pesquisar,
                                                            width=400,
                                                            height=40,
                                                            placeholder_text="Modelo do Produto",
                                                            placeholder_text_color="#494949",
                                                            font=("Montserrat Medium", 16),
                                                            fg_color="#D9D9D9",
                                                            border_width=2,
                                                            border_color="#000000",
                                                            text_color="#000000",
                                                            )
        self.entry_modelo_parcial.place(relx=0.5, y=200, anchor="center")

        self.resultado_frame = customtkinter.CTkScrollableFrame(self.frame_pesquisar,
                                                    width=1100,
                                                    height=370,
                                                    fg_color="#D9D9D9")
        self.resultado_frame.place(relx=0.5, y=440, anchor="center")

        self.entry_modelo_parcial.bind("<KeyRelease>", self.atualizar_lista_produtos)
        self.atualizar_lista_produtos()

        button_voltar_pesquisar = customtkinter.CTkButton(self.frame_pesquisar,
                                                        text="Voltar",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=100,
                                                        height=40,
                                                        command=self.tela_menu)
        button_voltar_pesquisar.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_menu())


    def atualizar_lista_produtos(self, event=None):
        termo_busca = self.entry_modelo_parcial.get().strip().title()

        for widget in self.resultado_frame.winfo_children():
            widget.destroy()

        lista_produtos = self.produto.pesquisar_produto_parcial(termo_busca)

        if not lista_produtos:
            label_sem_resultado = customtkinter.CTkLabel(self.resultado_frame,
                                                        text="Nenhum produto encontrado.",
                                                        font=("Montserrat Medium", 20),
                                                        text_color="#000000",
                                                        fg_color="#D9D9D9")
            label_sem_resultado.place(relx=0.5, rely=0.5, anchor="center")
            return
        
        for produto in lista_produtos:
            modelo = produto[1]
            marca = produto[2]
            categoria = produto[3]
            preco = produto[4]
            quant = produto[5]
            nota = produto[6]

            label_produto = customtkinter.CTkLabel(self.resultado_frame,
                                                    text=f"Modelo: {modelo} | Marca: {marca} | Categoria: {categoria} | Preço: R$ {preco:.2f} | Quantidade: {quant} | Nota: {nota:.1f}",
                                                    font=("Montserrat Medium", 18),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
            label_produto.pack(pady=10)

            label_separar = customtkinter.CTkLabel(self.resultado_frame,
                                                    text="________________________________________________________________________________________________________________________________________________________________",
                                                    font=("Montserrat Medium", 14),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
            label_separar.pack()

    def pagina_remover_produto(self):
        self.dialog_remover = customtkinter.CTkInputDialog(text="Digite o modelo do produto que deseja remover:", title="Remover Produto")
        input_user = self.dialog_remover.get_input().strip()
        try:
            if input_user == "":
                raise ValueError("O campo 'Modelo' deve ser preenchido.")
        except ValueError as ve:
            messagebox.showerror("Erro de Validação", str(ve))
            return
        if input_user:
            modelo = input_user.title()
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
        self.unbind_pagina()
        self.frame_menu.destroy()
        
        self.frame_listar = customtkinter.CTkFrame(self,
                                                    width=1280,
                                                    height=720,
                                                    fg_color="#FFFFFF")
        self.frame_listar.pack()

        self.label_todos_produtos = customtkinter.CTkLabel(self.frame_listar,
                                                    text="LISTA DE TODOS OS PRODUTOS",
                                                    font=("Montserrat Medium", 30),
                                                    text_color="#000000",
                                                    fg_color="#FFFFFF")
        self.label_todos_produtos.place(relx=0.5, y=50, anchor="center")

        produtos = self.produto.listar_todos_produtos()
        if not produtos:
            messagebox.showinfo("Nenhum Produto", "Não há produtos cadastrados no sistema.")
            self.tela_menu()
            return

        label_modelo = customtkinter.CTkLabel(self.frame_listar,
                                                text="Modelo     |     Marca      |     Categoria     |     Preço     |     Quantidade     |     Nota",
                                                font=("Montserrat Medium", 30),
                                                text_color="#000000",
                                                fg_color="#FFFFFF")
        label_modelo.place(relx=0.5, y=180, anchor="center")

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.frame_listar,
                                                                width=1200,
                                                                height=400,
                                                                fg_color="#D9D9D9")
        self.scrollable_frame.place(relx=0.5, y=410, anchor="center")

        for produto in produtos:
            modelo = produto[1]
            marca = produto[2]
            categoria = produto[3]
            preco = produto[4]
            quant = produto[5]
            nota = produto[6]

            label_produto = customtkinter.CTkLabel(self.scrollable_frame,
                                                    text=f"{modelo}       |       {marca}       |       {categoria}       |       R$ {preco:.2f}       |       {quant}       |       {nota:.1f}",
                                                    font=("Montserrat Medium", 22),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
            label_produto.pack(pady=10)

            label_separar = customtkinter.CTkLabel(self.scrollable_frame,
                                                    text="______________________________________________________________________________________________________________________________",
                                                    font=("Montserrat Medium", 20),
                                                    text_color="#000000",
                                                    fg_color="#D9D9D9")
            label_separar.pack()

        button_voltar_listar = customtkinter.CTkButton(self.frame_listar,
                                                        text="Voltar",
                                                        font=("Montserrat Medium", 20),
                                                        fg_color="#818181",
                                                        hover_color="#9C9C9C",
                                                        text_color="#060505",
                                                        bg_color="#FFFFFF",
                                                        width=100,
                                                        height=40,
                                                        command=self.tela_menu)
        button_voltar_listar.place(x=50, y=650)
        self.bind("<Escape>", lambda event: self.tela_menu())

    def pagina_exibir_um_produto(self):
        self.unbind_pagina()
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

        modelo = self.entry_modelo.get().title().strip()
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

