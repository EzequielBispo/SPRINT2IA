# ChatGPT & SpaCy API

Este é um projeto Flask que integra a API do OpenAI (ChatGPT) e SpaCy para fornecer respostas a prompts e realizar análises linguísticas detalhadas dessas respostas.

## Requisitos

- Python 3.7+
- Flask
- OpenAI Python Client
- SpaCy
- Modelo de idioma SpaCy (`pt_core_news_sm`)

## Vídeo Pitch

[Vídeo Pitch](https://youtu.be/K-pVUeK4ni4)

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```
2. Crie um ambiente virtual e ative-o:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`

3. Instale as dependências:

   ```sh
   pip install flask openai spacy
   python -m spacy download pt_core_news_sm

