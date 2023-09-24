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
            data = vaga.find_elements(by=By.CLASS_NAME, value='vacancy-date')[0].text.replace('"', "'").lower()
            linha["data"] = data.replace(" jan", "/01/23").replace(" fev", "/02/23").replace(" mar", "/03/23").replace(" abr", "/04/23").replace(" mai", "/05/23").replace(" jun", "/06/23").replace(" jul", "/07/23").replace(" ago", "/08/23").replace(" set", "/09/23").replace(" out", "/10/23").replace(" nov", "/11/23").replace(" dez", "/12/23").replace(".", "")
            linha["local"] = vaga.find_elements(by=By.CLASS_NAME, value='vacancy-location')[0].text.replace('"', "'").lower()
            linha["cargo"] = vaga.find_elements(by=By.CLASS_NAME, value='vacancy-title')[0].text.replace('"', "'").lower()
            linha["tipo"] = "não consta"
            linha["link"] = vaga.get_attribute('href')
            vagasPandape.append(linha)
            print(f"Vaga cadastrada: {linha['cargo'].title()}")

    # GRAVA OS RESULTADOS
    gravar_json("Pandape // Infojobs", "resultados/pandape.json", vagasPandape)
