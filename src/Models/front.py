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
        self.label = customtkinter.CTkLabel(self, text="Bem vindo a FK Tecnologias", font=("Arial", 30), text_color="#000000", fg_color="#FFFFFF")
        self.label.pack(pady=20)
        self.image = customtkinter.CTkImage(Image.open("assets/images/logo.jpeg"), size=(760, 570))
        self.logo = customtkinter.CTkLabel(self, image=self.image, text="")
        self.logo.pack(pady=0)
        
    def botao_proximo(self):
        self.button = customtkinter.CTkButton(self, text="Próximo", font=("Arial", 20), fg_color="#FFFFFF", hover_color="#785252", text_color="#060505", bg_color="#FFFFFF" )
        self.button.place(x=1100, y=600)
