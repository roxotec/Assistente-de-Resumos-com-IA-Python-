import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resumo(texto):
  prompt = f""""'
  Analise o texto abaixo e gere:

    1. Um resumo claro (máx 5 linhas)
    2. 5 tópicos principais
    3. 3 perguntas para revisão

  Texto: {texto}
  '"""        
  response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
      {"role": "user","content": prompt}
    ],
    temperature=0.7,
  )

  return response.choices[0].message.content

if __name__ == "__main__":
  print("Assistente de Resumos com IA\n")

  texto_usuario = input("Cole o Texto para Análise:\n\n")

  resultado = gerar_resumo(texto_usuario)

  print("\n Resultado")
  print(resultado)