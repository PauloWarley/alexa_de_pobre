import os
import openai
import json

class OpenAiCompletion():

    def __init_(self):
        pass
    def create(self, prompt = ''):
        openai.api_key = "SUA API KEY"

        
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n "],
        # echo=True
        )
        
        print(response["choices"])

        # return (response["choices"][0]["text"])
        
        response = response["choices"][0]["text"]
        
        print('response', response)
        
        # response = '\n{\n"id": null,\n"r": \"Claro querido, que s\u00e9rie voc\u00ea gostaria de assistir?\"\n}'
        
        response = json.loads(response.replace('Exemplo:', '')) 
        
        # import requests
        
        # url = "http://127.0.0.1:5000/textspeach"
        # data = {"text": response['r']}
        # headers = {"Content-type": "application/json"}

        # requests.post(url, json=data, headers=headers)
        
        return response
    
# print(OpenAiCompletion().create())