from bs4 import BeautifulSoup

arquivo = open("index.html", "r")

# Lê o arquivo e obtém o seu conteúdo, no caso, um html

html_content = arquivo.read()


# Carrega o HTML no BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')

lista_manchetes = []
article = soup.find_all('article')
for a in article:
    h2 = a.find ('h2')
    manchete=[h2.text]
    lista_pes=a.find_all('p')
    for p in lista_pes:
        manchete.append(p.text)
        lista_manchetes.append(manchete)
    for m in lista_manchetes:
        print(m)
