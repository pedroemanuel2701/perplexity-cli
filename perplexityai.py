import sys
import os

API_KEY_FILE = os.path.expanduser("~/.perplexity_api_key")

def get_api_key():
    # Se já existe variável de ambiente, prioriza ela
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if api_key:
        return api_key
    # Se não, tenta ler do arquivo
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, "r") as f:
            return f.read().strip()
    # Se não existe, pede ao usuário e salva
    api_key = input("Insira sua chave da API Perplexity: ").strip()
    with open(API_KEY_FILE, "w") as f:
        f.write(api_key)
    print("Chave salva em ~/.perplexity_api_key para os próximos usos.")
    return api_key

from perplexity import Perplexity

def main():
    if len(sys.argv) < 2:
        print("Uso: python perplexityai.py sua_pergunta_aqui")
        sys.exit(1)

    pergunta = " ".join(sys.argv[1:])

    api_key = get_api_key()
    os.environ["PERPLEXITY_API_KEY"] = api_key
    client = Perplexity()

    resposta = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": pergunta}]
    )

    print("\nResposta:\n")
    print(resposta.choices[0].message.content)

if __name__ == "__main__":
    main()
