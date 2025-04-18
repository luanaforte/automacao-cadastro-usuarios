from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(r"C:\Users\Youth_Space_23\Desktop\automacao\login.html")
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[1]').send_keys('luana@gmail.com')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[2]').send_keys('luana0246')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/a/button').click()
sleep(1)

navegador.find_element('xpath', '//*[@id="formulario"]/div/input[1]').send_keys('Luana Forte')
sleep(1)

navegador.find_element('xpath', '//*[@id="formulario"]/div/input[2]').send_keys('Fortaleza')
sleep(1)

navegador.find_element('xpath', '//*[@id="formulario"]/div/input[3]').send_keys('Ceará')
sleep(1)

navegador.find_element('xpath', '//*[@id="formulario"]/div/input[4]').send_keys('Brasil')
sleep(1)

navegador.find_element('xpath', '//*[@id="download"]').click()
sleep(1)

sleep(5)