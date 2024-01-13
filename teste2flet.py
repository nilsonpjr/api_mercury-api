import flet as ft
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import webdriver_manager

def conecta_login():
    # Conecta ao site da Mercury Marine
    try:
        navegador = webdriver_manager.Chrome()
        navegador.get("https://www.mercurymarine.com/br/pt/garantia")

        # Faz o login
        navegador.find_element(By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/input').send_keys(os.environ["LOGIN"])
        navegador.find_element(By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td[4]/input').send_keys(os.environ["SENHA"])
        navegador.find_element(By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/input').click()
    except Exception as e:
        print("Erro ao conectar ao site:", e)
        return None

    return navegador


def get_garantia(item, nromotor):
    # Valida os dados de entrada
    if not item:
        raise ValueError("O item deve ser informado")
    if not nromotor:
        raise ValueError("O número do motor deve ser informado")

    # Conecta ao site da Mercury Marine
    navegador = conecta_login()

    # Faz a pesquisa
    navegador.find_element(By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[4]/td/input[1]').send_keys(item)
    navegador.find_element(By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[4]/td/input[2]').send_keys(nromotor)
    navegador.find_element(By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[5]/td/input').click()

    # Retorna os resultados da pesquisa
    try:
        dicionario = {}
        for linha in navegador.find_elements(By.TAG_NAME, "tr")[3:]:
            elementos = linha.find_elements(By.TAG_NAME, "td")
            dicionario[elementos[0].text] = elementos[1].text
        return dicionario
    except Exception as e:
        print("Erro ao processar os resultados:", e)
        return None


def main(page: ft.Page):
    # Define a página
    page.title = "Consultar Garantia"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Cria os elementos da interface
    item_input = ft.TextField(value="digite aqui", label="Item:")
    texto_retorno = ft.TextField(value="Aguarde", visible=False)

    # Adiciona os elementos à página
    page.add(
        ft.Row(
            [
                item_input,
                ft.ElevatedButton("Pesquisar", on_click=(on_submit)),
                texto_retorno,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # Define a função de callback do botão de pesquisa
    def on_submit():
        # Obtém os dados de entrada
        item = item_input.value

        # Raspa os dados
        dados = get_garantia(item, "1234567890")

        # Exibe os dados
        texto_retorno.visible = True
        texto_retorno.value = dados

    # Inicia o aplicativo
    ft.app(target=main)
