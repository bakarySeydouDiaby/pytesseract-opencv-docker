# tesseract-python-opencv

installation opencv, pytesseract, tesseract-ocr et lancement container 


## quelques commandes docker :
`docker compose up` pour lancer le container \
`docker exec -it tesseract-python-opencv_app_1tesseract-python_app_1 bash` pour acceder au container et lancer notre script python \
`python 1_script.py` pour executer le script python et generer du texte à partir de l'image


## quelques commandes git

> creer le repos github d'abord

revenir sur notre espace locale et ajouter le repos git : on change origin en opencv
```
    git init
    git remote add opencv https://github.com/bakarySeydouDiaby/pytesseract-opencv-docker.git
    git add .
    git commit -m "message"
    git push -u opencv master
```
maintenant, après chaque modif, on refait :
 ```
    git status
    git add
    git commit
    git push
```


## Parti Python deep learning

ajout de plusieurs dossiers :
- 1_worcloud : pour tester des scripts python generant un wordcloud avec les librairies  : numpy, pandas, pytesseract, matplotlib, PIL, itertools, nltk, wordcloud, cv2, os
- 2_web_scrapping : pour extraire des infos sur des pages web avec : pandas, requests, lxml
- 3_text_audio : pour generer un fichier audio .mp3 à partir d'un fichier image contenant du texte : gtts, pytesseract, cv2
