import os
import google.generativeia as genai
genai.configure(api_key=(chave_Api))
for ss in ganai.list_model():
  if 'generateContent' in ss.supported_generation_methods:
    model=genai.generativeModel('gemini-1.5-pro')
chat=model.start_chat(history=[])
context='responda em pt-br nativo'
chat.send_message(context)
conversa=chat.send_message(input('mande usas perguntas: '))
while conversa != 'fechar':
  resposta=chat.send_message(conversa)
  print(resposta.text)
  conversa=chat.send_message(input('Para sair digite "fechar", se não pergunte o que quiser: '))
