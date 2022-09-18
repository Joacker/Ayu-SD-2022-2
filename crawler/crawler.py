# Imports para requests y parse de metadata
from bs4 import BeautifulSoup
import requests

# Imports para Keywords
#from gensim.summarization import keywords
import warnings
warnings.filterwarnings('ignore')
from keybert import KeyBERT


def parse_csv(csv_name, max_lines=None):
    file = open(csv_name, 'r')
    Lines = file.readlines()[1:]
    
    # Para no exceder el límite propuesto
    count = 0
    
    for line in Lines:
        if (count == max_lines):
            return
        
        parses = line.split('\t')
        
        # Evitamos las url en blanco. Es \n porque es el último término antes de un salto de linea.
        if (parses[4] == '\n'):
            continue
        
        url = parses[4]
        c_url = url[:-1]
        
        data = get_data_from_url(c_url)
        
        if data is not None:
            print(f'[{count}] {data["url"]}\n Title: {repr(data["title"])}\n Description: {repr(data["description"])}\n Keywords: {repr(data["keywords"])}')
        
            count += 1
        
    return

def get_data_from_url(url):
    collected_data = {'url': url, 'title': None, 'description': None, 'keywords': []}
    try:
        r = requests.get(url, timeout=1)
    except Exception:
        return None
    
    if r.status_code == 200:
        # Se puede usar BeautifulSoap u otra librería que parsee la metadata de los docuementos HTML.
        soup = BeautifulSoup(r.content, 'html.parser')

        # Obtenemos el título
        title = soup.find('title')
        # Obtenemos la metadata
        meta = soup.find("meta")
        
        try:
            collected_data['title'] = title.string.replace('\n', '')
            if 'name' in meta.attrs.keys() and meta.attrs['name'].strip().lower() in ['description', 'keywords']:
                collected_data['description'] = meta.attrs['content']
        except Exception:
            return None
        
        # modelo de entrenamiento para Keywords. Comentar si no se quieren los keywords.
        model = KeyBERT('distilbert-base-nli-mean-tokens')
        collected_data['keywords'] = model.extract_keywords(str(collected_data['description']), keyphrase_ngram_range=(1, 2), stop_words=None)
        collected_data['keywords'] = model.extract_keywords(str(collected_data['title']), keyphrase_ngram_range=(1, 2), stop_words=None)
            
        return collected_data
    
    return None
    
    

if __name__ == "__main__":
    csv_name = './logs/file.txt'
    ht = parse_csv(csv_name, max_lines=100)
