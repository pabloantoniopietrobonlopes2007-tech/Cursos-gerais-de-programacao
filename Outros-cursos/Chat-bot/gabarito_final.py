# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# pip install streamlit openai

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="SUA_CHAVE_AQUI",
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")

st.write("### ChatBot com IA") # markdown

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"],
    content = mensagem["content"],
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

# # listas
# nomes = ["Lira", "Gui", "Thalia", "Michely"]
# print(nomes[0])
# nomes.append("Alon") # adicionar 

# print(nomes)

# # dicionarios
# idades = {"Lira": 31, "Alon": 30, "Thalia": 25}
# idades["Michely"] = 27 # adicionar 
# print(idades)

# texto_usuario = "Coe galera"
# mensagem = {"usuario": "Lira", "texto": texto_usuario}
# usuario = mensagem["usuario"] # pegar info: dicionario[chave]
# print(mensagem)
# print(usuario)

# # listas + dicionarios
# lista_mensagens = [
#     {"role": "Lira", "content": texto_usuario}, 
#     {"role": "IA", "content": texto_usuario}, 
#     {"role": "Lira", "content": texto_usuario}
#     ]

# nova_mensagem = {"role": "Lira", "content": "Resposta do Lira"}

# lista_mensagens.append(nova_mensagem)
# print(lista_mensagens)