import os
from google import genai
from google.genai import types

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("chave_Api")

if not api_key:
    raise ValueError("API key não encontrada.")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="Responda em pt-BR nativo."
    ),
)

conversa = input('Mande suas perguntas: ').strip()

while conversa.lower() != "fechar":
    resposta = chat.send_message(conversa)
    print(resposta.text)
    conversa = input('Para sair digite "fechar", se não pergunte o que quiser: ').strip()

print("Conversa encerrada.")
client.close()
