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
        self.label = customtkinter.CTkLabel(self, text="BEM VINDO A FK TECNOLOGIAS", font=("Montserrat Medium", 30), text_color="#000000", fg_color="#FFFFFF", width=400, height=50)
        self.label.pack(pady=20)
        self.image = customtkinter.CTkImage(Image.open("assets/images/logo.jpeg"), size=(760, 570))
        self.logo = customtkinter.CTkLabel(self, image=self.image, text="")
        self.logo.pack(pady=0)
        
    def botao_proximo(self):
        self.button = customtkinter.CTkButton(self, text="Próximo", font=("Montserrat Medium", 20), fg_color="#5D5C5C", hover_color="#8D8C8C", text_color="#060505", bg_color="#FFFFFF", command=self.proxima_tela)
        self.button.place(x=1100, y=600)


    def proxima_tela(self):
        None