from pickle import FALSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
# import bs4
# import webbrowser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pesqpreco(item):
    login = 31240
    senha = "2105_kasa"
    # item = "impeller"
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('window-size=200,400')

    # Abre o Navegador e Entra no Site
    navegador = webdriver.Chrome(chrome_options=options, service=Service(
        ChromeDriverManager().install()))
    # navegador = webdriver.Chrome(chrome_options=options)
    navegador.get("https://portal.mercurymarine.com.br/epdv/epdv001.asp")
    # Insere o login e Senha
    navegador.find_element(
        By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/input').send_keys(login)
    navegador.find_element(
        By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/input').send_keys(senha)
    navegador.find_element(
        By.XPATH, '/html/body/center/form/table/tbody/tr/td/table[2]/tbody/tr[4]/td/input').send_keys(Keys.ENTER)

    navegador.get(
        "https://portal.mercurymarine.com.br/epdv/epdv002d2.asp?s_nr_pedido_web=11111111111111111&s_nr_tabpre=&s_fm_cod_com=null&s_desc_item=" + item)
    sleep(4)

    """
        Verifica se o termo digitado esta correto ou foi encontrado
        
        """
    teste = navegador.find_element(
        By.XPATH, '/html/body/form[1]/table/tbody/tr/td/table[2]/tbody/tr[3]')

    if teste.get_attribute("class") == 'NoRecords':
        print('Nenhum registro encontrado - favor verificar !')
        return FALSE
    else:
        print('Sucesso! item encontrado')

    # Pegar valor da pesquisa codigo  nome  valor custo e valor venda
    procura = navegador.page_source
    # site = BeautifulSoup(procura, 'html.parser')
    linha = len(navegador.find_elements(
        By.XPATH, '//*[@id="preco_item_web"]/table/tbody/tr/td/table[2]/tbody/tr'))
    coluna = len(navegador.find_elements(
        By.XPATH, '//*[@id="preco_item_web"]/table/tbody/tr/td/table[2]/tbody/tr[3]/td'))
    # Print rows and columns
    # print(linha)
    coluna -= 1
    linha -= 1
    # itens = 0
    # table = np.empty((linha, coluna), int)
    # table1 = [1,2,3]
    lista = []
    # descricao = []
    # qtdaEst = []
    valor = 0
    # valorTabela = []
    # valorCusto = []
    for r in range(3, int(linha + 1)):
        for p in range(2, int(coluna + 1)):
            element = navegador.find_element(
                By.XPATH,
                '//*[@id="preco_item_web"]/table/tbody/tr/td/table[2]/tbody/tr[' + str(r) + ']/td[' + str(p) + ']')
            html_content = element.get_attribute('outerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')
            # table = soup.find('td')
            lista.append(soup.find('td').text)

    lista = [el.replace('\xa0', ' ') for el in lista]

    # print(lista)

    # print(table.text)
    valor = len(lista)
    # print(f'Encontrado {valor / 5}')
    # print(valor)

    dicionario1 = dict()
    # lista1 = dict()
    dicionario = list()
    r = 0
    for i in range(0, valor, 7):
        dicionario1 = {
            'codigo': lista[i].replace(' ', ''),
            'qtd': lista[i+1],
            'descricao': lista[i+2].replace('     ', ''),
            'qtdaEst': lista[i+3].replace(' ', ''),
            'valorVenda': lista[i+4].replace(' ', ''),
            'valorTabela': lista[i+5].replace(' ', ''),
            'valorCusto': lista[i+6].replace(' ', ''),
            # 'qtdEncontrada': valor/5
        }
        dicionario1.update(dicionario1)
        dicionario.append(dicionario1)
        # print(dicionario)
    # print(dicionario)

        # for e in dicionario:
        #     for v in e.values():
        #         print(v, end=' ')
        #         print('')
    # print(len(dicionario))
    # qtdade_itens = len(dicionario)
    # print(qtdade_itens)
        # return str(dicionario[0].get("descricao"))
    return dicionario
