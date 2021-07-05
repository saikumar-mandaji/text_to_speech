import gtts
import playsound
import os
msg = 'hello world'
def speak(x):
    v_obj = gtts.gTTS(text = x,lang='en',slow=False, tld='ca')
    v_obj.save('voice.mp3')
    os.system("mpg321 voice.mp3 &")
speak(msg)

