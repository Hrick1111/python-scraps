from gtts import gTTS
import os


text = open('open me.txt','r').read()
language='en'
output = gTTS(text=text,lang=language,slow=False)
output.save('newoutput.mp3')

os.system("start newoutput.mp3")