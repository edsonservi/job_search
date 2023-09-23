from buscar_vagas_infojobs import buscar_vagas_infojobs
from buscar_vagas_gupy import buscar_vagas_gupy
from buscar_vagas_solides import buscar_vagas_solides
from buscar_vagas_abler import buscar_vagas_abler
from auxiliares import agrupar_jsons

sites = ["https://agibank.gupy.io/",
         "https://americanas.pandape.infojobs.com.br/",
         "https://audacy.vagas.solides.com.br/",
         "https://calvinkleinbrasil.pandape.infojobs.com.br/",
         "https://grupoboticario.gupy.io/",
         "https://lojaspanvel.gupy.io/",
         "https://neopessoas.abler.com.br/#list-vacancy",
         "https://organizacionalconsultoria.vagas.solides.com.br/",
         "https://pensefarma.pandape.infojobs.com.br/",
         "https://sparkgestaodetalentos.abler.com.br/#list-vacancy",
         "https://uniquerh.vagas.solides.com.br/",
         "https://workgenteegestao.abler.com.br/#list-vacancy",
]
pandape = []
gupy = []
solides = []
abler = []

for site in sites:
    if "pandape.infojobs.com.br" in site and site not in pandape:
        pandape.append(site)
    elif "gupy.io" in site and site not in gupy:
        gupy.append(site)
    elif "vagas.solides.com.br" in site and site not in solides:
        solides.append(site)
    elif "abler.com.br" in site and site not in abler:
        abler.append(site)

# PANDAPES / INFOJOB
print(f"{len(pandape)} Sites da infojobs cadastrados")
buscar_vagas_infojobs(pandape)
print("FIM DO SCRIPT - Pandape")

# GUPY
print(f"{len(gupy)} Sites da Gupy cadastrados")
buscar_vagas_gupy(gupy)
print("FIM DO SCRIPT - Gupy")

# SOLIDES
print(f"{len(solides)} Sites da Solides cadastrados")
buscar_vagas_solides(solides)
print("FIM DO SCRIPT - Solides")

# ABLER
print(f"{len(abler)} Sites da Abler cadastrados")
buscar_vagas_abler(abler)
print("FIM DO SCRIPT - Abler")

agrupar_jsons()
print("FIM DO SCRIPT")
