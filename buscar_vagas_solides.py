from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, ElementNotInteractableException,
                                        ElementClickInterceptedException)
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auxiliares import gravar_json
from time import sleep


def buscar_vagas_solides(sites):
    """
    Busca vagas de emprego em sites da plataforma Solide.
    Args: sites(list): Uma lista de URLs dos sites onde você deseja buscar vagas.
    Returns: None
    """
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    
    controle = []
    vagasSolides = []
    
    for url in sites:
        nav.get(url)
        sleep(5)

        n = 0
        while True:
            sleep(1)
            vagas = nav.find_elements('xpath', '//*[@id="__next"]/main/div/div/section[1]/ul/li')
            for vaga in vagas:
                titulo = vaga.find_element(by=By.TAG_NAME, value='h3').text.replace('"', "'").lower()
                local = vaga.find_elements(by=By.TAG_NAME, value='p')[0].text.replace('"', "'").lower()
                dataVG = vaga.find_element(by=By.TAG_NAME, value='time').get_attribute('datetime')
                s_id = f"{dataVG}{local}{titulo}"
                if s_id not in controle:
                    linha = {}
                    linha["data"] = dataVG
                    linha["local"] = local
                    linha["cargo"] = titulo
                    linha["tipo"] = "não consta"
                    linha["link"] = f"{url}?page=1&locations=&title={titulo.replace(' ', '+')}"
                    vagasSolides.append(linha)
                    controle.append(s_id)
                    print(f"Vaga cadastrada: {titulo.title()}")
                    n = 0

            if n == 5:
                break

            try:
                btnnext = nav.find_element(by=By.ID, value='next-page')
            except NoSuchElementException:
                n += 1
                sleep(1)
                pass
            except ElementClickInterceptedException:
                n += 1
                sleep(1)
                pass
            except ElementNotInteractableException:
                n += 1
                sleep(1)
                pass
            else:
                try:
                    btnnext.click()
                except ElementClickInterceptedException:
                    n += 1
                    sleep(1)
                    pass

    # GRAVA OS RESULTADOS
    gravar_json("Solides", "resultados/solides.json", vagasSolides)
