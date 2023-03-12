from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://azure.microsoft.com/pt-br/products/cognitive-services/text-to-speech/")
driver.set_window_size(1183, 711)

def send_text(text = 'teste'):
  erro = True
  while erro:
    try:

      driver.find_element(By.ID, "ttstext").clear()

      driver.find_element(By.ID, "ttstext").send_keys(text)
      driver.find_element(By.CSS_SELECTOR, "#playbtn > span").click()
      erro = False
      
    except:
      pass


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello, World!")

@app.route('/textspeach', methods=['POST'])
def create_user():
    data = request.get_json()
    text = data.get('text')
    
    send_text(text = text)
    
    return jsonify(message="Tudo certo")

if __name__ == '__main__':
    app.run(port=5000)




    