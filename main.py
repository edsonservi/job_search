from buscar_vagas_infojobs import buscar_vagas_infojobs
from buscar_vagas_gupy import buscar_vagas_gupy
from buscar_vagas_solides import buscar_vagas_solides
from buscar_vagas_abler import buscar_vagas_abler
from buscar_vagas_thor import buscar_vagas_thor
from auxiliares import agrupar_jsons

sites = ["https://aegea.gupy.io/", "https://agibank.gupy.io/", "https://ambev.gupy.io/",
         "https://americanas.pandape.infojobs.com.br/",
         "https://arcolconstrucoes.vagas.solides.com.br/", "https://assai.gupy.io/",
         "https://audacy.vagas.solides.com.br/", "https://autoglasslojas.gupy.io/",
         "https://autozone.pandape.infojobs.com.br/", "https://braveo.gupy.io/",
         "https://brzinsurance.vagas.solides.com.br/", "https://caldiclatam.gupy.io/",
         "https://calvinkleinbrasil.pandape.infojobs.com.br/", "https://camicadocarreiras.gupy.io/",
         "https://carreiramarcopolo.gupy.io/", "https://cellularcom.gupy.io/", "https://centaurotalentos.gupy.io/",
         "https://cresolcarreiras.gupy.io/", "https://edimo.gupy.io/", "https://edimoflorianopolis.gupy.io/",
         "https://elmo.abler.com.br/#list-vacancy", "https://epharma.gupy.io/",
         "https://fiesc.pandape.infojobs.com.br/", "https://fortbras.gupy.io/",
         "https://genialepromocaodeeventosemerchandising.pandape.infojobs.com.br/",
         "https://grupobarigui.abler.com.br/#list-vacancy", "https://grupoboticario.gupy.io/",
         "https://grupogiassi.pandape.infojobs.com.br/", "https://grupopereira.pandape.infojobs.com.br/",
         "https://iel.pandape.infojobs.com.br/", "https://imc.gupy.io/", "https://iplace.gupy.io/",
         "https://jovemaprendizseredeconecta.gupy.io/", "https://konecta.pandape.infojobs.com.br/",
         "https://localiza.gupy.io/", "https://lojaspanvel.gupy.io/", "https://lojasvivo.gupy.io/",
         "https://martins.gupy.io/", "https://minsait.gupy.io/", "https://natter.gupy.io/",
         "https://neobpo.pandape.infojobs.com.br/", "https://neopessoas.abler.com.br/#list-vacancy",
         "https://obahortifruti.gupy.io/", "https://orcali.abler.com.br/#list-vacancy",
         "https://organizacionalconsultoria.vagas.solides.com.br/", "https://orsegups.pandape.infojobs.com.br/",
         "https://orthodontic.gupy.io/", "https://pensefarma.pandape.infojobs.com.br/",
         "https://playnacarreiraesm.gupy.io/", "https://poptrade.gupy.io/", "https://porto.gupy.io/",
         "https://randstad-filialcuritibapr.pandape.infojobs.com.br/", "https://renner.gupy.io/",
         "https://sejaesm.gupy.io/", "https://sparkgestaodetalentos.abler.com.br/#list-vacancy",
         "https://strattner.gupy.io/", "https://strattner.gupy.io/", "https://studioz.gupy.io/",
         "https://unicredcentralconexao.gupy.io/", "https://unicredscpr.gupy.io/",
         "https://unimedgrandeflorianopolis.gupy.io/", "https://unimedrb.vagas.solides.com.br/",
         "https://uniquerh.vagas.solides.com.br/", "https://vempraestacio.gupy.io/", "https://vempropecege.gupy.io/",
         "https://vivara.gupy.io/", "https://vyttra.gupy.io/", "https://workgenteegestao.abler.com.br/#list-vacancy",
         "https://yduqs.gupy.io/", "https://programathor.com.br/jobs"]

pandape = []
gupy = []
solides = []
abler = []
thor = []

for site in sites:
    if "pandape.infojobs.com.br" in site and site not in pandape:
        pandape.append(site)
    elif "gupy.io" in site and site not in gupy:
        gupy.append(site)
    elif "vagas.solides.com.br" in site and site not in solides:
        solides.append(site)
    elif "abler.com.br" in site and site not in abler:
        abler.append(site)
    elif "programathor.com.br" in site and site not in thor:
        thor.append(site)

# PANDAPE / INFOJOBS
while True:
    answer = input(f"Deseja indexar as vagas dos {len(pandape)} site(s) Pandape / Infojobs? (Y/N)").strip().lower()
    if answer == 'n':
        break
    elif answer == 'y':
        buscar_vagas_infojobs(pandape)
        print("FIM DO SCRIPT - Pandape")
        answer = ""
        break
    else:
        print("Responda 'Y' para sim e 'N' para não por favor.")

# GUPY
while True:
    answer = input(f"Deseja indexar as vagas dos {len(gupy)} site(s) Gupy? (Y/N)").strip().lower()
    if answer == 'n':
        break
    elif answer == 'y':
        buscar_vagas_gupy(gupy)
        print("FIM DO SCRIPT - Gupy")
        answer = ""
        break
    else:
        print("Responda 'Y' para sim e 'N' para não por favor.")

# SOLIDES
while True:
    answer = input(f"Deseja indexar as vagas dos {len(solides)} site(s) Solides? (Y/N)").strip().lower()
    if answer == 'n':
        break
    elif answer == 'y':
        buscar_vagas_solides(solides)
        print("FIM DO SCRIPT - Solides")        
        answer = ""
        break
    else:
        print("Responda 'Y' para sim e 'N' para não por favor.")

# ABLER
while True:
    answer = input(f"Deseja indexar as vagas dos {len(abler)} site(s) Abler? (Y/N)").strip().lower()
    if answer == 'n':
        break
    elif answer == 'y':
        buscar_vagas_abler(abler)
        print("FIM DO SCRIPT - Abler")
        answer = ""
        break
    else:
        print("Responda 'Y' para sim e 'N' para não por favor.")

# THOR
while True:
    answer = input(f"Deseja indexar as vagas do programa Thor? (Y/N)").strip().lower()
    if answer == 'n':
        break
    elif answer == 'y':
        buscar_vagas_thor(thor)
        print("FIM DO SCRIPT - Thor")
        answer = ""
        break
    else:
        print("Responda 'Y' para sim e 'N' para não por favor.")

agrupar_jsons()
print("FIM DO SCRIPT")
