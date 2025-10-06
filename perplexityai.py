import sys
import os
import re

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
        print("Uso: python perplexityai.py sua_pergunta_aqui | change-key")
        sys.exit(1)

    # Comando especial para manipular a chave da API
    if sys.argv[1] in ["change-key", "changekey", "key"]:
        print("\nOpções para a chave da API:")
        print("1 - Remover chave da API")
        print("2 - Manter chave atual")
        print("3 - Trocar chave da API")
        escolha = input("Digite o número da opção desejada: ").strip()
        if escolha == "1":
            if os.path.exists(API_KEY_FILE):
                os.remove(API_KEY_FILE)
                print("Chave removida com sucesso!")
            else:
                print("Nenhuma chave encontrada para remover.")
        elif escolha == "2":
            api_key = get_api_key()
            print(f"Chave atual: {api_key}")
        elif escolha == "3":
            nova = input("Digite a nova chave da API: ").strip()
            with open(API_KEY_FILE, "w") as f:
                f.write(nova)
            print("Nova chave salva!")
        else:
            print("Opção inválida.")
        sys.exit(0)

    pergunta = " ".join(sys.argv[1:])

    api_key = get_api_key()
    os.environ["PERPLEXITY_API_KEY"] = api_key

    print("Enviando pergunta para a Perplexity... Aguarde.\n")
    client = Perplexity()
    resposta = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": pergunta}]
    )

    texto = resposta.choices[0].message.content
    # Otimiza substituição de markdown para negrito ANSI
    def bold_ansi(match):
        return f"\033[1m{match.group(1)}\033[0m"
    # Primeiro **texto**
    texto = re.sub(r"\*\*(.*?)\*\*", bold_ansi, texto)
    # Depois *palavra*
    texto = re.sub(r"\*(\w[^*]*)\*", bold_ansi, texto)

    print("Resposta:\n")
    print(texto)

if __name__ == "__main__":
    main()
