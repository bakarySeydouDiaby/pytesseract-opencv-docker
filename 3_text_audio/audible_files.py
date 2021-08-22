import cv2
import pytesseract
from gtts import gTTS
import os
fic_image = cv2.imread("avis1.png")


txt = pytesseract.image_to_string(fic_image)
print(txt)
language = 'en'
outObj = gTTS(text=txt, lang=language, slow=False)
outObj.save("audio_genere.mp3")

## playing audio
# print('playing the audio file')
# os.system('rev.mp3')