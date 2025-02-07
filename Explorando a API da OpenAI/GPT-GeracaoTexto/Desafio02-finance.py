#!/usr/bin/env python
# coding: utf-8

# In[29]:


import json
import yfinance as yf
import openai
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)


# In[30]:


def retorna_cotacao_historica(ticker, periodo):
    print('retorna_cotação_historica', ticker)
    ticker_obj = yf.Ticker(f'{ticker}.SA')
    hist = ticker_obj.history(period=periodo, auto_adjust=False)
    hist = round(hist, 2)
    if len(hist) > 30:
        slice_size = int(len(hist) / 30)
        hist = hist.iloc[::-slice_size][::-1]
    hist.index = hist.index.strftime('%Y-%m-%d')
    return hist['Close'].to_json()
    


# In[31]:


tools = [
    {
        'type': 'function',
        'function': {
            'name': 'retorna_cotacao_historica',
            'description': 'retorna a cotação diaria historica para uma ação da bovespa',
            'parameters': {
                'type': 'object',
                'properties': {
                    'ticker': {
                        'type': 'string',
                        'description': 'O ticker da ação. Exemplo: "ABEC3" para ambev, "PETR4" para petrobras, etc'
                    },
                    'periodo': {
                        'type': 'string',
                        'description': 'O periodo que sera retornado de dados historicos \
                                        sendo "1mo" equivalente a um mes de dados, "1d" a \
                                        1 dia e "1y" a 1 ano',
                        'enum': ["1d","5d","1mo","5mo","1y","5y","10y","ytd","max"]                
                    }
                }
            }
        }
    }
]

funcoes_disponiveis = {
    "retorna_cotacao_historica": retorna_cotacao_historica,
}

def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=mensagens,
    tools=tools,
    tool_choice="auto",
    )
    
    tool_calls = resposta.choices[0].message.tool_calls
    
    if tool_calls:
        mensagens.append(resposta.choices[0].message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = funcoes_disponiveis[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(**function_args)
            mensagens.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
        segunda_resposta = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=mensagens,
        )

        mensagens.append(segunda_resposta.choices[0].message)
        print(f'Assitant: {mensagens[-1].content}')


# In[28]:


if __name__ == '__main__':
    print("Bem-vindo ao ChatBot financeiro da Asimov. Digite sua mensagem abaixo:")
    while True:
        input_usuario = input('User: ')
        mensagens = [{'role': 'user', 'content': input_usuario}]
        mensagens = geracao_texto(mensagens)

