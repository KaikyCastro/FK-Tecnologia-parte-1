from PIL import Image
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")
app.title("FK Tecnologia")

imagem = customtkinter.CTkImage(light_image=Image.open("assets/images/logo.jpeg"),
                                dark_image=Image.open("assets/images/logo.jpeg"),
                                size=(200, 150))

label_imagem = customtkinter.CTkLabel(app, image=imagem, text="")
label_imagem.pack(pady=20)


app.mainloop()
