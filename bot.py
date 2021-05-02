from selenium import webdriver
import time
from selenium.webdriver import chrome
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

#DIRETORIO DO CHROMEDRIVER
driver = webdriver.Chrome(executable_path=r"DIRETORIO AONDE ESTÁ O SEU CHROMEDRIVER")

#LINK DA PAGINA
driver.get("https://pt-br.facebook.com/")

#PASSSANDO O EMAIL E A SENHA DO USUARIO
email = driver.find_element_by_xpath("XPATH DO CAMPO DE EMAIL").send_keys('<Seu Email>')
password = driver.find_element_by_xpath("XPATH DO CAMPO DE SENHA").send_keys('<Sua Senha>')

#CLICK DO BOTAO
btn = driver.find_element_by_tag_name("button").click()

#TEMPO
time.sleep(2)

#URL PARA SER REDIRECIONADO APOS O LOGIN
link = driver.get("LINK DA PUBLICAÇAO")

#CAIXA DE TEXTO
caixa = driver.find_elements_by_xpath("XPATH DA EDIT TEXT")

#TEMPO
time.sleep(2)

#LOOPING
i=0

for i in range(100):
    #MENSAGEM QUE SERÁ REPETIDA DE ACORDO O LOOPING
    caixa = driver.find_element_by_xpath("XPATH DA EDIT TEXT").send_keys("HELLO WORLD",Keys.ENTER)