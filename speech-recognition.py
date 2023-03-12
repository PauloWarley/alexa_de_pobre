import requests
import speech_recognition as sr
import json
import os
from OpenAiCompletion import OpenAiCompletion
from datetime import datetime
import serial

# ser = serial.Serial('COM3', 9600)   # Define a porta serial e a velocidade de transmissão


openAiCompletion = OpenAiCompletion()

def main():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        # print("Recognizing Now .... ")


        # recognize speech using google

        try:
            text = r.recognize_google(audio, language='pt-BR')
            
            print("You have said \n" + text)
            
            
            
            lista_comandos = '''
                1- deixe a luz acesa ou clareie o quarto
                2- Apaga a luz
                3- Abrir o Google Chrome "start chrome"
                4- Abrir o Firefox "start firefox"
                5- Abrir o Internet Explorer "start iexplore"
                6- Abrir o Microsoft Edge "start microsoft-edge:"
                7- Abrir o Microsoft Word "start winword"
                8- Abrir o Microsoft Excel "start excel"
                9- Abrir o Microsoft PowerPoint "start powerpnt"
                10- Abrir o Microsoft Outlook "start outlook"
                11- Abrir o Notepad "start notepad"
                12- Abrir o Gerenciador de tarefas "start taskmgr"
                13- Abrir o Painel de Controle "start control"
                14- Abrir o Explorador de arquivos "start explorer"
                15- Abrir o Calendário do Windows "start outlookcal:"
                16- Abrir o OneNote "start onenote"
                17- Abrir o Spotify "start spotify"
                18- Abrir o Skype "start skype"
                19- Abrir o Discord "start discord"
                20- Abrir o VLC "start vlc"
                21- Abrir o Zoom "start zoom"
                22- Abrir o Genshin Impact "start genshinimpact.exe"
                23- Abrir netflix.com"
                24- Abrir youtube music"
            '''
            
            try:
                f = open('conversation.json', 'r').read()
            except:
                f = '[]'
                    
            f = json.loads(f)
            
            # print(json.dumps(f[-10:]))
            
            # return
            # se ''' + f'"{text}"' + ''' for um comando com tom afetivo, r também será uma resposta com tom 
                        
            prompt = f'''

considere o seguinte contexto mão retorne uma resposta que esteja no dicionario:
''' + json.dumps(f[-10:]) + f'''

considere as seguintes opções:

{lista_comandos}

se ''' + f'"{text}"' + ''' tiver o mesmo sentido de alguma das opções, id é igual o número da opção
senão id será 0.

r será a resposta que a alexia daria para o comando: ''' + f'"{text}"' + '''

r deverá ter uma resposta simulando uma jovem e seu nome é Faire

me responda apenas um json em formato válido:
{
"id": number,
"r": "response text like alexa"
}
 '''
            
            print(prompt)
            
            response = openAiCompletion.create(prompt)
            
            print("IA said \n" + json.dumps(response) )
            

            # f = json.loads(f)
            
            f.append({
                'time': datetime.now().ctime(),
                'phrase':text,
                # 'prompt': prompt,
                'response': response
            })
            
            # print(f)
            
            file = open('conversation.json', 'w', )
            file.write(json.dumps(f,indent=4))

            url = "http://127.0.0.1:5000/textspeach"
            data = {"text": response['r']}
            headers = {"Content-type": "application/json"}

            requests.post(url, json=data, headers=headers)
            
            
            if (response['id'] != 0):
                # command = input("Digite '1' para ligar o LED ou '2' para desligar: ")  # Lê o comando do usuário
                print("enviando comando para o arduino", response['id'])
                
                # ser.write(str(response['id']).encode())   # Envia o comando para o Arduino

                commands = {
                    "3": 'start chrome',
                    "4": 'start firefox',
                    "5": 'start iexplore',
                    "6": 'start "microsoft":edge:',
                    "7": 'start winword',
                    "8": 'start excel',
                    "9": 'start powerpnt',
                    "10": 'start outlook',
                    "11": 'start notepad',
                    "12": 'start taskmgr',
                    "13": 'start control',
                    "14": 'start explorer',
                    "15": 'start outlookcal:',
                    "16": 'start onenote',
                    "17": 'start spotify',
                    "18": 'start skype',
                    "19": 'start discord',
                    "20": 'start vlc',
                    "21": 'start zoom',
                    "22": 'start genshinimpact.exe',
                    "23": 'start opera netflix.com',
                    "24": 'start opera https://music.youtube.com/watch?v=ymjNGjuBCTo&list=RDAMVMymjNGjuBCTo',
                    
                }
                
                os.system(commands[str(response['id'])])

            # print(response.status_code)
            # print(response.json())

            
            #print("Audio Recorded Successfully \n ")


        except Exception as e:
            print("Error :  " + str(e))




        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

while True:
    main()
