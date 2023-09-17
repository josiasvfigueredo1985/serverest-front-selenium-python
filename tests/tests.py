from flask import Flask, render_template
from selenium import webdriver

app = Flask(__name__)

@app.route('./templates')
def home():
    return render_template('index.html')

@app.route('/demo')
def demo():
    # Inicie o WebDriver (neste caso, usaremos o Chrome)
    driver = webdriver.Chrome(executable_path='caminho/para/chromedriver.exe')
    
    # Abra a página de demonstração
    driver.get('http://localhost:5000')
    
    # Localize elementos e interaja com eles usando o Selenium
    element = driver.find_element_by_id('elemento_id')
    element.click()
    
    input_element = driver.find_element_by_name('nome_do_input')
    input_element.send_keys('Texto de exemplo')
    
    # Feche o WebDriver
    driver.quit()
    
    return 'Interagiu com elementos da página de demonstração.'

if __name__ == '__main__':
    app.run(debug=True)
