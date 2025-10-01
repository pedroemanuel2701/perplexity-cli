import sys
import os
os.environ["PERPLEXITY_API_KEY"] = "<PERPLEXITY-API-KEY>"

from perplexity import Perplexity

def main():
    if len(sys.argv) < 2:
        print("Uso: python perplexityai.py sua_pergunta_aqui")
        sys.exit(1)

    pergunta = " ".join(sys.argv[1:])

    client = Perplexity()

    resposta = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": pergunta}]
    )

    print("\nResposta:\n")
    print(resposta.choices[0].message.content)

if __name__ == "__main__":
    main()
