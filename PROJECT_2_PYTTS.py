import PySimpleGUI  as sg
layout=[[sg.Text('Enter Text:'), sg.InputText(),sg.Button('Speak')],
        [sg.Text('Select Voice Type'),sg.Radio('Male ', "gender", default = True), sg.Radio('Female',"gender")],
        [sg.Text('Volume'),sg.Slider(range=(0,1), default_value=0.5, orientation='h',size=(15, 15), key='volume')],
        [sg.Text('Speed'),sg.Slider(range=(0.1,2), default_value= 1, orientation='h',size=(15, 15), resolution = 0.1, key='speed')]
        ]


window=sg.Window('Text-To-Speech App',layout)



import pyttsx3 as tts
import threading
engine=tts.init()

def speak(text,gender,volume,speed):
    voices = engine.getProperty('voices')
    if gender== 'male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice', volume)
    engine.setProperty('rate', speed * 150)
    engine.say(text)
    engine.runAndWait()
 


while True:
    event, values =window.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        break
    if event == 'Speak':
        text = values[0]
        gender = 'male' if values[1] else 'female'
        volume= float(values['volume'])
        speed = float(values['speed'])
        threading.Thread(target=speak, args=(text, gender,volume,speed)).start()

window.close()