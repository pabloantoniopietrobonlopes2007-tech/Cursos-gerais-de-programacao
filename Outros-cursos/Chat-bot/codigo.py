#titulo 
#campo mensagem
#

from chave import minha_chave_api
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key=minha_chave_api,
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")

#Titulo
st.write("# ChatBot com IA")

#criar memoria para manter o historico de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    qm_enviou = mensagem["role"]
    texto_msg = mensagem["content"]
    st.chat_message(qm_enviou).write(texto_msg)

#mensagem do usuario
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

#caso a mensagem do usuario nao seja vazia, exibir a mensagem na tela e mandar para o modelo de IA
if mensagem_usuario:

    #exibir mensagem na tela
    st.chat_message("user").write(mensagem_usuario)
    #st.chat_message("quem esta mandando").write("mensagem a ser exibida")
    #quem manda:
        #user -> ser humano
        #assistant -> inteligencia artificial
    mensagem1 = {"role": "user", "content": mensagem_usuario}
    #mensagem = {"role": "user/assistant", "content": "mensagem a ser exibida"}
    st.session_state["lista_mensagens"].append(mensagem1)

    #mandar a mensagem do usuario para o modelo de IA e pegar a resposta
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )

    resposta_ia = resposta_ia.choices[0].message.content

    #mandar a resposta da IA para o chat
    st.chat_message("assistant").write(resposta_ia)
    mensagem2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem2)




#tornasr as respostas inteligentes