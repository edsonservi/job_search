from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auxiliares import gravar_json
from time import sleep


def buscar_vagas_abler(sites):
    """
    Busca vagas de emprego em sites da plataforma Abler.
    Args: sites(list): Uma lista de URLs dos sites onde você deseja buscar vagas.
    Returns: None
    """
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    
    controle = []
    vagasAbler = []
    remover = '0123456789'
    
    for url in sites:
        nav.get(url)
        
        while True:
            sleep(1)
            tablerows = nav.find_elements('xpath', '//*[@id="list-vacancy"]/div/table/tbody/tr')
            for tablerow in tablerows:
                cells = tablerow.find_elements(by=By.TAG_NAME, value='td')
                titulo = (cells[0].text.replace('"', "'").lower().translate(str.maketrans('', '', remover))
                          .replace(" - ", " ").strip())
                if cells[0].text not in controle:
                    linha = {}
                    linha["data"] = cells[1].text
                    linha["local"] = cells[4].text.lower()
                    linha["cargo"] = titulo
                    linha["tipo"] = cells[3].text.lower()
                    linha["link"] = cells[5].find_element(by=By.TAG_NAME, value='a').get_attribute('href')
                    controle.append(cells[0].text)
                    vagasAbler.append(linha)
                    print(f"Vaga cadastrada: {titulo.title()}")

            btnnext = 0
            navigation = nav.find_element(by=By.XPATH, value='//*[@id="list-vacancy"]/div/ul')
            botoes = navigation.find_elements(by=By.TAG_NAME, value='button')
            
            for botao in botoes:
                if botao.text == "\u203A":
                    btnnext = botao
                
            if btnnext != 0:
                btnnext.click()
            else:
                break

    # GRAVA OS RESULTADOS
    gravar_json('Abler', "resultados/abler.json", vagasAbler )
