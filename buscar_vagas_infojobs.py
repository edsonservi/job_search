from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auxiliares import gravar_json
from time import sleep


def buscar_vagas_infojobs(sites):
    """
    Busca vagas de emprego em sites da plataforma Pandape Infojobs.
    Args: sites(list): Uma lista de URLs dos sites onde você deseja buscar vagas.
    Returns: None
    """
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    
    vagasPandape = []

    for url in sites:
        nav.get(url)
        try:
            botao = nav.find_element('xpath', '//*[@id="didomi-notice-agree-button"]/span')
            nav.execute_script("arguments[0].click();", botao)
        except NoSuchElementException:
            pass
        nav.get(url)
        sleep(1)

        while True:
            try:
                more = nav.find_element(by=By.ID, value='btLoadMore')
                more.click()
                print("+ -> Wait...")
                sleep(1)
            except NoSuchElementException:
                break
            except ElementNotInteractableException:
                break

        vagas = nav.find_elements(by=By.CLASS_NAME, value='vacancy-item')
        for vaga in vagas:
            linha = {}
            linha["data"] = vaga.find_elements(by=By.CLASS_NAME, value='vacancy-date')[0].text.replace('"', "'").lower()
            linha["local"] = vaga.find_elements(by=By.CLASS_NAME, value='vacancy-location')[0].text.replace('"', "'").lower()
            linha["cargo"] = vaga.find_elements(by=By.CLASS_NAME, value='vacancy-title')[0].text.replace('"', "'").lower()
            linha["tipo"] = "não consta"
            linha["link"] = vaga.get_attribute('href')
            vagasPandape.append(linha)
            print(f"Vaga cadastrada: {linha['cargo'].title()}")

    # GRAVA OS RESULTADOS
    gravar_json("Pandape // Infojobs", "resultados/pandape.json", vagasPandape)
