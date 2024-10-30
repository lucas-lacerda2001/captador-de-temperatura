# - Importação
import tkinter as tk
from PIL import Image, ImageTk

# - Funções
def salvar_clima():
  print("Salvando o clima...")

# - Configurações da janela
# Criação
janela = tk.Tk()

# Título da janela
janela.title("Weather Now")

# Tamanho da janela
janela.geometry("300x200")

# Impedir o redimensionamento
janela.resizable(False, True)

# - Widgets
# Imagem (Logo)
logo = Image.open("./static/images/logo.png")
logo = logo.resize((100, 100))
imagem_tk = ImageTk.PhotoImage(logo)

label_imagem = tk.Label(janela, image=imagem_tk)
label_imagem.pack()

# Texto
label = tk.Label(janela, text="Olá, Mundo!")
label.pack() # Adicionar o widget à janela

# - Botões
# Botão Salvar Clima
botao = tk.Button(janela, text="Salvar clima", command=salvar_clima)
botao.pack()


# - Loop da aplicação para exibir a janela
janela.mainloop()
