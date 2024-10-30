# - Importação
import tkinter as tk
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from openpyxl import Workbook, load_workbook
import os

# - Funções

def salvar_dados_excel(data_hora, temperatura, umidade):
  # Verifica se o arquivo já existe
  if os.path.exists("historico_temperatura.xlsx"):
    # Abre o arquivo existente
    workbook = load_workbook("historico_temperatura.xlsx")
    sheet = workbook.active
  else:
    # Cria um novo arquivo
    workbook = Workbook()
    sheet = workbook.active
    # Cria cabeçalhos
    sheet.append(["Data e Hora", "Temperatura", "Umidade"])

  # Adiciona a nova linha com os dados
  sheet.append([data_hora, temperatura, umidade])

  # Salva o arquivo
  workbook.save("historico_temperatura.xlsx")

def salvar_temperatura():
  # Inicialização do WebDriver
  driver_path = "./static/web_drivers/msedgedriver"
  driver = webdriver.Edge()

  # Navegação até a página do tempo
  driver.get("https://weather.com/pt-BR/clima/hoje/l/ebe93c0e09d0cfe19844d4281461901cd8f083c310e64255954758c8dcab784b")

  # Extração da temperatura e umidade
  elemento_temperatura = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[4]/section/div/div[1]/div[1]/span[2]/span').text
  elemento_umidade = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[4]/section/div/div[2]/div[3]/div[2]/span')

  temperatura = elemento_temperatura if isinstance(elemento_temperatura, str) else elemento_temperatura.text
  umidade = elemento_umidade if isinstance(elemento_umidade, str) else elemento_umidade.text

  print(temperatura)
  print(umidade)
  
  # Captura da data e hora atuais
  data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

  # Fechar o navegador
  driver.quit()

  # Salvar os dados na planilha
  salvar_dados_excel(data_hora, temperatura, umidade)


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
label = tk.Label(janela, text="Atualize a situação do clima em São Paulo!")
label.pack() # Adicionar o widget à janela

# - Botões
# Botão Salvar Clima
botao = tk.Button(janela, text="Buscar previsão", command=salvar_temperatura)
botao.pack()


# - Loop da aplicação para exibir a janela
janela.mainloop()
