# source : 
import pytesseract
import cv2
import os
import pandas as pd

# Step 1: Create a list of all the available review images
#========================================================

folderPath = "avis_airbnb" # ce dossier contient les fichiers image .png
listeFichiersAvis = os.listdir(folderPath) # liste contenant les noms des fichiers PNG
print(listeFichiersAvis)

# Step 2: If needed view the images using cv2.imshow() method
#===========================================================

# for image in  listeFichiersAvis:
#     img = cv2.imread(f'{folderPath}/{image}')
#     cv2.imshow("Image", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Step 3: Read text from images using pytesseract
#===============================================

listeContenuAvis = []
for images in listeFichiersAvis:
    img = cv2.imread(f'{folderPath}/{images}')
    if img is None:
        listeContenuAvis.append("Could not read the image.")
    else:
        rev = pytesseract.image_to_string(img)
        listeContenuAvis.append(rev)
list(listeContenuAvis)
print(listeContenuAvis)

# Step 4: Create a data frame :  convert list to dataframe
#============================

import pandas as pd
data = pd.DataFrame(list(listeContenuAvis), columns=['commentaire'])
print(data)

# Step 5: Preprocess the text – remove special characters, stopwords

#removing special characters
import re
def clean(text):
    return re.sub('[^A-Za-z0-9" "]+', ' ', text)

data['Commentaire nettoye'] = data['commentaire'].apply(clean)
print("******************removed special character***************")
print(data['Commentaire nettoye'])

## export dataframe to csv file
#data.to_csv('/tesseract-opencv/1_wordcloud/data_cleaned.csv', index=False)
### read csv file
#df = pd.read_csv('/tesseract-opencv/1_wordcloud/data_cleaned.csv', header=None)
#print(df)

# tokenization de la colonne 'Commentaire nettoye' avec comme nouveau non 'tokenized'
import nltk
from nltk.tokenize import word_tokenize
data['tokenized'] = data.apply(lambda row: nltk.word_tokenize(row['Commentaire nettoye']), axis=1)
print("******************tokenized***************")
print(data['tokenized'].head()) # chaque rows devient tokenizé

# data.to_csv('/tesseract-opencv/1_wordcloud/data_tokenized.csv', index=False)
# df = pd.read_csv('/tesseract-opencv/1_wordcloud/data_tokenized.csv', header=None)

# print("******************tokenized***************")
# print(df)

## creer une liste contenant que les elements de la colonne 'tokenized' du dataframe 'data'
## on obtiendra une liste de 3 listes (le contenu des 3 fichiers images transformés)
import itertools
liste_finale = []
liste_finale.append(data.tokenized.tolist())
liste_finale=list(itertools.chain.from_iterable(liste_finale))

print('******************liste des rows tokenizés*********************')
print(liste_finale)


## morceler la liste imbriquée en une seule
def flatten(liste):
    return [item for sublist in liste for item in sublist]
liste_finale=flatten(liste_finale)

print('******************flatten liste finale ne contenant que les words des 3 fichiers de départ*********************')
print(liste_finale, "\n")

## il reste les numéros à enlever : '01' ; '02' ; '08'
digit=['01', '02', '08']

for items in digit:
    liste_finale.remove(items)
print(liste_finale)



# Step 6: Build positive, negative word clouds
#============================================

# with open(r"/tesseract-opencv/1_wordcloud/positive-words.txt","r") as pos:
#     poswords = pos.read().split()
# with open(r"/tesseract-opencv/1_wordcloud/negative-words.txt","r") as neg:
#     negwords = neg.read().split()


## Building Word Cloud
# Importing libraries to generate and show word clouds.
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# liste_finale to texte
text=" ".join(liste_finale)
print(text)

# suppression mots parasites
exclude_words = ['s', 'is', 'He', 'a', 'The', 'This', 'we', 'A', 'and', 'We', 'when', 'you', 'him', 'very', 'to', 'all', 'h', 'in', 'l', 'just', 'one', 'us', 'most', 'with', 'around', 'was', 'a']

# application d'un mask et generation worcloud
mask = np.array(Image.open("mask_cloud.png"))
mask[mask == 1] = 255 # Si une valeur du tableau est “255”, alors aucun mot d’apparaîtra dans la zone correspondante.

wordcloud = WordCloud(background_color = 'white', stopwords = exclude_words, max_words = 50).generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()