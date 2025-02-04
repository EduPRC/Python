#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai

from dotenv import load_dotenv, find_dotenv

import os

_ = load_dotenv(find_dotenv())


# In[2]:

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)


# In[3]:


def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=mensagens,
        max_tokens=1000,  
        temperature=0,
        stream=True
    )
    
    print('Assitant:', end='')
    resposta_completa = ''
    for stream_resposta in resposta:
        texto = stream_resposta.choices[0].delta.content
        if texto:
            resposta_completa += texto
            print(texto, end='')
    print()
            
    mensagens.append({'role': 'assistant', 'content': resposta_completa})
    return mensagens
# In[ ]:

if __name__ == '__main__':
    print("Bem-vindo ao ChatBot da Asimov. Digite sua mensagem abaixo:")
    mensagens = []
    while True:
        input_usuario = input('User: ')
        mensagens.append({'role': 'user', 'content': input_usuario})
        mensagens = geracao_texto(mensagens)


# %%
