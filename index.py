import openai

# Insira sua chave de API do OpenAI aqui
api_key = "sua_chave_de_api"

# Configuração da chave de API
openai.api_key = api_key

# Função para obter uma resposta do ChatGPT
def obter_resposta(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Escolha o modelo do ChatGPT
            prompt=prompt,
            temperature=0.7,  # Controla a criatividade das respostas
            max_tokens=150,   # Tamanho máximo da resposta
            n=1,              # Quantidade de respostas retornadas
            stop=None         # Condição de parada para a geração de texto
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Erro ao obter resposta:", e)
        return None