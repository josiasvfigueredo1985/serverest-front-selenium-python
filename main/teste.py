from selenium import webdriver


# Configurar as opções do navegador (opcional)
# Executar em modo headless (sem interface gráfica)

# Inicializar o driver do Chrome
driver = webdriver.Chrome()

# Acessar o link
url = "https://www.metal-archives.com/"
driver.get(url)

# Realizar ações no site, se necessário (por exemplo, fazer uma pesquisa)

# Fechar o navegador
driver.quit()
