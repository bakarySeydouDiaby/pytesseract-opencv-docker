# source code : https://www.datacorner.fr/webscrapython/

import requests
import lxml.html as lh
page = requests.get('http://www.jeuxvideo.com/meilleurs/') # c'est l'url
doc = lh.fromstring(page.content)


## récupèrer le contenu de la page http://www.jeuxvideo.com/meilleurs/

# Dans notre exemple ci-dessus par exemple le titre (enfin tous les titres) 
# se retrouve via le chemin XPATH: //a[@class= »gameTitleLink__196nPy »]
nomJeux = doc.xpath('//a[@class="gameTitleLink__196nPy"]')
desc = doc.xpath('//p[@class="description__1-Pqha"]')
sortie = doc.xpath('//span[@class="releaseDate__1RvUmc"]')
test = doc.xpath('//span[@class="editorialRating__1tYu_r"]')
avis = doc.xpath('//span[@class="userRating__1y96su"]')

## affichage avec un boucle des elements recuperes

for i in range(len(nomJeux)):
    print("nom :"+ nomJeux[i].text_content().strip() + "\n" + \
          "description :"+ desc[i].text_content().strip() + "\n" + \
          sortie[i].text_content().strip()+ "\n" + \
          "avis du texte : " + test[i].text_content().strip() + "\n" + \
          "note jeux : " + avis[i].text_content().strip() + "\n")

