from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, ElementNotInteractableException,
                                        ElementClickInterceptedException)
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auxiliares import gravar_json, pegar_data, agrupar_jsons
from time import sleep


def buscar_vagas_thor(sites):
    """
    Busca vagas de emprego em sites da plataforma Thor.
    Args: sites(list): Uma lista de URLs dos sites onde você deseja buscar vagas.
    Returns: None
    """
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    
    controle = []
    vagasThor = []
    
    for url in sites:
        nav.get(url)
        sleep(5)

        count = 0
        count_prev_loop = 0

        while True:
            sleep(1)
            vagas = nav.find_elements(by=By.CLASS_NAME, value='cell-list ')
            for vaga in vagas:
                try:
                    titulo = vaga.find_element(by=By.TAG_NAME, value='h3')
                except NoSuchElementException:
                    pass
                else:
                    if "Vencida" not in titulo.text:
                        linha = {}
                        linha["data"] = pegar_data()
                        linha["cargo"] = titulo.text
                        local_mark = vaga.find_element(by=By.CLASS_NAME, value='fa-map-marker-alt')
                        linha["local"] = local_mark.find_element('xpath', '..').text
                        tipo_mark = vaga.find_element(by=By.CLASS_NAME, value='fa-file-alt')
                        linha["tipo"] = tipo_mark.find_element('xpath', '..').text
                        linha["link"] = vaga.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
                        if linha["link"] not in controle:
                            controle.append(linha["link"])
                            vagasThor.append(linha)
                            print(f"Vaga cadastrada: {linha['cargo']}")
                            count = 0
            
            if len(vagasThor) <= count_prev_loop:
                count += 1
                print(f"wait...")
            else:
                count_prev_loop = len(vagasThor)
            
            if count >= 5:
                print("\nFim por falta de registros ativos\n")
                break

            pag = nav.find_element(by=By.CLASS_NAME, value='pagination')
            try:
                nextlink = pag.find_element(by=By.LINK_TEXT, value='Next ›')
            except NoSuchElementException:
                break
            else:
                print(f"Indo para: {nextlink.get_attribute('href')}")
                nav.get(nextlink.get_attribute('href'))
                

    # GRAVA OS RESULTADOS
    gravar_json("Thor", "resultados/thor.json", vagasThor)
    agrupar_jsons()


deposito = ["https://programathor.com.br/jobs"]
buscar_vagas_thor(deposito)
