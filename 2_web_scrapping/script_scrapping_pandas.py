# source : https://www.datacorner.fr/sentiment-analysis/
import requests
import lxml.html as lh
import pandas as pd

url = 'http://www.jeuxvideo.com/meilleurs/'

tags = ['//a[@class="gameTitleLink__196nPy"]', '//p[@class="description__1-Pqha"]', \
        '//span[@class="releaseDate__1RvUmc"]', '//span[@class="editorialRating__1tYu_r"]', '//span[@class="userRating__1y96su"]']

cols = ['nomJeux', 'desc', 'sortie', 'test', 'avis']
page = requests.get(url)
doc = lh.fromstring(page.content)

def getPage(url):
    # Get the Web data via XPath
    content = []
    for i in range(len(tags)):
        content.append(doc.xpath(tags[i]))
 
    # Gather the data into a Pandas DataFrame array
    df_liste = []
    for j in range(len(tags)):
        tmp = pd.DataFrame([content[j][i].text_content().strip() for i in range(len(content[i]))], columns=[cols[j]])
        tmp['key'] = tmp.index
        df_liste.append(tmp)
 
    # Build the unique Dataframe with one tag (xpath) content per column
    liste = df_liste[0]
    for j in range(len(tags)-1):
        liste = liste.join(df_liste[j+1], on='key', how='left', lsuffix='_l', rsuffix='_r')
        liste['key'] = liste.index
        del liste['key_l']
        del liste['key_r']
 
    return liste

#print(getPage(url).head())
## sauvegarder dans un fichier csv
liste_page= getPage(url)
liste_page.to_csv('/tesseract-opencv/2_web_scrapping/liste_webscrapping.csv', index=False)

## affichade 5 premieres lignes
df = pd.read_csv('/tesseract-opencv/2_web_scrapping/liste_webscrapping.csv', header=None)
print(df)


##### si on veut scrapper sur 3 pages par exemple
uri_pages = '?page='
nbPages = 3
def getPages(_nbPages, _url):
    liste_finale = pd.DataFrame()
    for i in range (_nbPages):
        liste = getPage(_url + uri_pages + str(i+1))
        liste_finale = pd.concat([liste_finale, liste], ignore_index=True)
    return liste_finale