from flask import Flask, request, jsonify
import openai
import spacy

app = Flask(__name__)

# Variável global para armazenar a última resposta
ultima_resposta = None

# Insira sua chave de API do OpenAI aqui
api_key = "sua_chave_de_api"
openai.api_key = api_key

# Carregar o modelo spaCy
nlp = spacy.load("pt_core_news_sm")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt")
    temperature = data.get("temperature", 0.7)  # Valor padrão de 0.7 se não for fornecido
    max_tokens = data.get("max_tokens", 150)    # Valor padrão de 150 se não for fornecido
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    global ultima_resposta
    ultima_resposta = obter_resposta(prompt, temperature, max_tokens)
    
    if ultima_resposta is None:
        return jsonify({"error": "Failed to obtain response from ChatGPT"}), 500

    # Analise a resposta com spaCy
    analise_spacy = analisar_resposta_com_spacy(ultima_resposta)
    
    return jsonify({"response": ultima_resposta, "spacy_analysis": analise_spacy})

@app.route("/api/last_response", methods=["GET"])
def last_response():
    global ultima_resposta
    if ultima_resposta:
        return jsonify({"response": ultima_resposta})
    else:
        return jsonify({"response": "Nenhuma resposta disponível"})

def obter_resposta(prompt, temperature, max_tokens):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,  # Parâmetro personalizado
            max_tokens=max_tokens     # Parâmetro personalizado
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print("Erro ao obter resposta:", e)
        return None

def analisar_resposta_com_spacy(texto):
    doc = nlp(texto)
    tokens = [{"text": token.text, "lemma": token.lemma_, "pos": token.pos_, "tag": token.tag_, "dep": token.dep_, "shape": token.shape_, "is_alpha": token.is_alpha, "is_stop": token.is_stop} for token in doc]
    ents = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents]
    return {"tokens": tokens, "entities": ents}

if __name__ == "__main__":
    app.run(debug=True)
