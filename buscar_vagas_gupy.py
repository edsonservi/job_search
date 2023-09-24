from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auxiliares import pegar_data, gravar_json
from time import sleep


def buscar_vagas_gupy(sites):
    """
    Busca vagas de emprego em sites da plataforma Gupy.
    Args: sites(list): Uma lista de URLs dos sites onde você deseja buscar vagas.
    Returns: None
    """
    data = pegar_data()
    
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    
    controle = []
    vagasGupy = []

    for url in sites:
        nav.get(url)
        try:
            botao = nav.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]')
            nav.execute_script("arguments[0].click();", botao)
        except NoSuchElementException:
            pass
        nav.get(url)
        sleep(1)
        
        while True:
            vagas = nav.find_elements('xpath', '//*[@id="job-listing"]/ul/li/a')
            for vaga in vagas:
                link = vaga.get_attribute('href')
                if link not in controle:

                    # DEFINE OS DADOS A SEREM SALVOS
                    linha = {}
                    linha["data"] = data
                    linha["local"] = (vaga.find_element(by=By.CLASS_NAME, value='sc-d868c80d-6')
                                      .text.replace('"', "'").lower())
                    linha["cargo"] = (vaga.find_element(by=By.CLASS_NAME, value='sc-d868c80d-5')
                                      .text.replace('"', "'").lower())
                    linha["tipo"] = (vaga.find_element(by=By.CLASS_NAME, value='sc-d868c80d-7')
                                     .text.replace('"', "'").lower())
                    linha["link"] = link
                    controle.append(link)
                    vagasGupy.append(linha)
                    print(f"Vaga cadastrada: {linha['cargo'].title()}")
                
            try:
                nextbtn = nav.find_element('xpath', '//*[@id="job-listing"]/div[3]/nav/ul/li[5]/button')
                nextbtn.click()
            except NoSuchElementException:
                break
            except ElementNotInteractableException:
                break
            if nextbtn.get_attribute('aria-disabled') != "false":
                break
    
    # GRAVA OS RESULTADOS
    gravar_json("Gupy", "resultados/gupy.json", vagasGupy)
