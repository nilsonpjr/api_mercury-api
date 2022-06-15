# from asyncore import dispatcher
# import webbrowser
from importlib.metadata import entry_points
from lib2to3.pgen2.token import EQUAL
from pickle import FALSE
from time import sleep
import bs4
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
from pyparsing import null_debug_action
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def conecta_login():
    login = 31240
    senha = "2105_kasa"
    # item = "impeller"
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('window-size=200,400')

    # Abre o Navegador e Entra no Site
    navegador = webdriver.Chrome(
        chrome_options=options, service=Service(ChromeDriverManager().install()))
    # navegador = webdriver.Chrome(chrome_options=options)
    navegador.get("https://portal.mercurymarine.com.br/epdv/epdv001.asp")
    # Insere o login e Senha
    navegador.find_element(
        By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/input').send_keys(login)
    navegador.find_element(
        By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/input').send_keys(senha)
    navegador.find_element(
        By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[4]/td/input').send_keys(Keys.ENTER)
    return navegador


def dados_cliente(nro_motor):
    navegador = conecta_login()
    navegador.get(
        "https://portal.mercurymarine.com.br/epdv/ewr010c.asp?s_nr_serie=" + nro_motor)
    sleep(4)
    navegador.switch_to.window(navegador.window_handles[0])
    sleep(4)
    nome_cli = navegador.find_element(
        By.XPATH, '//*[@id="warranty_clients"]/table/tbody/tr/td/table[2]/tbody/tr[3]').text
    nome_cli = nome_cli.upper()
    return nome_cli


def ConsultaGarantia(nro_motor):
    navegador = conecta_login()
    navegador.get(
        "https://portal.mercurymarine.com.br/epdv/ewr010.asp?s_nr_serie=" + nro_motor)
    sleep(5)
    navegador.switch_to.window(navegador.window_handles[0])
    sleep(5)
    teste = navegador.find_element(
        By.XPATH, '/html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/strong/font').text
    nro_motor = nro_motor.upper()
    """Verifica se o termo digitado esta correto ou foi encontrado"""
    if str(teste) != str(nro_motor):
        print('Nenhum Motor encontrado para esse número de série!')
        return '<h1> Nenhum Motor encontrado para esse numero de serie!</h1>'
    else:
        print('Sucesso! Motor encontrado')
        nro_serie = navegador.find_element(
            By.XPATH, '//*[@id="warr_cardnr_serie_1"]').text
        modelo = navegador.find_element(
            By.XPATH, '/html/body/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]').text
        dt_venda = navegador.find_element(
            By.XPATH, '/html/body/table/tbody/tr/td/table[2]/tbody/tr[3]/td[3]').text
        status_garantia = navegador.find_element(
            By.XPATH, '/html/body/table/tbody/tr/td/table[2]/tbody/tr[3]/td[5]').text
        vld_garantia = navegador.find_element(
            By.XPATH, '/html/body/table/tbody/tr/td/table[2]/tbody/tr[3]/td[6]').text
        nome_cli = dados_cliente(nro_motor)
        # print(nro_serie)
        modelo = modelo.replace("\n", '')
        # print(modelo)
        # print(dt_venda)
        # print(status_garantia)
        # print(vld_garantia)
        nome_cli = str(nome_cli)
        nome_cli = nome_cli.replace("NOME ", "")
        # print(str(nome_cli))
        dados_pesq = dict()
        for i in range(6):
            dados_pesq = {
                'nro_motor': nro_motor,
                'nro_serie': nro_serie,
                'modelo': modelo,
                'dt_venda': dt_venda,
                'status_garantia': status_garantia,
                'vld_garantia': vld_garantia,
                'nome_cli': nome_cli,
            }
        # print(dados_pesq)
        return dados_pesq
