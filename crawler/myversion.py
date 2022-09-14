from time import time
from unicodedata import name
import requests, csv
from bs4 import BeautifulSoup

# ------------------- READ_CSV ------------------- #
def read_csv(path, max_lines):
       
    with open(path, 'r') as f:
        cont = 0
        lines = f.readlines()[1:]
        for line in lines:
            if (cont == max_lines):
                return
            tab = line.split('\t')
            #print(tab)
            # ------------------Evitamos las url en blanco. Es \n porque es el último término antes de un salto de linea.------------------ #
            if tab[4] == '\n':
                continue
            url = tab[4]
            #print(url)
            # ------------------Evitamos el salto de linea.------------------ #
            c_url = url[:-1]
            #print(c_url)
            
            data = getDataFromUrl(c_url)
            
            if data is not None:
                print(f'[{cont}] {data["url"]}\n Title: {repr(data["title"])}\n Description: {repr(data["description"])}\n Keywords: {repr(data["keywords"])}')
                cont += 1
            
    return 

# ------------------- SCRAPING ------------------- #
def getDataFromUrl(url):
    collected_data = {'url': url, 'title': None, 'description': None, 'keywords': []}
    try:
        r = requests.get(url, timeout=1)
    except Exception:
        return None

    if r.status_code == 200:
        
        # Se puede usar BeautifulSoap u otra librería que parsee la metadata de los docuementos HTML.
        source = requests.get(url).text
        soup = BeautifulSoup(source, features='html.parser')

        # Obtenemos el título
        title = soup.find("meta", {'name': 'title'})
        title = title['content'] if title else None
        
        # Obtenemos la descripción
        description = soup.find("meta", {'name': "description"})
        description = description['content'] if description else None
        
        # Obtenemos la keywords y las limpiamos
        keywords = soup.find("meta", {'name': "keywords"})
        keywords = keywords['content'] if keywords else None
        if keywords is None:
            return None
        keywords = keywords.replace(" ", "") if keywords else None
        keywords = keywords.replace(".", "") if keywords else None
        keywords = keywords.split(",") if keywords else None

        try:
            collected_data['title'] = title
            collected_data['description'] = description
            collected_data['keywords'] = keywords          
                
        except Exception:
            pass

    return collected_data


# ------------------- MAIN ------------------- #
if __name__ == '__main__':
    path = './logs/file.txt'
    read_csv(path, 100)
    
    #url = 'https://www.styleweekly.com'
    #data = getDataFromUrl(url)
    #print(data)