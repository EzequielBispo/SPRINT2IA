import openai

api_key = "chaveapi"

openai.api_key = api_key

def obter_resposta(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002", 
            prompt=prompt,
            temperature=0.7,  
            max_tokens=150,  
            n=1,              
            stop=None         
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Erro ao obter resposta:", e)
        return None