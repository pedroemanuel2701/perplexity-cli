# perplexity-cli

Este projeto é um CLI simples para interagir com a API da Perplexity usando Python.

## Pré-requisitos
- Python 3.8 ou superior
- Uma chave de API válida da Perplexity

## Instalação


1. Clone o repositório:
   ```sh
   git clone https://github.com/pedroemanuel2701/perplexity-cli.git
   cd perplexity-cli
   ```

2. Instale as dependências:
   ```sh
   pip install perplexity-ai
   ```

## Dica de uso rápido (Linux/macOS)

Você pode criar uma função no seu `~/.zshrc` **ou** `~/.bashrc` para criar e ativar rapidamente um ambiente virtual:

```sh
# Para zsh ou bash:
ambvirtual() {
  if [ ! -d "./env" ]; then
    python3 -m venv env
    echo "Ambiente virtual criado."
  fi
  source env/bin/activate
  echo "Ambiente virtual ativado."
}


## Configuração da chave de API
# Adicione em um dos arquivos:

### Sobre a chave de API

Atualmente, a chave de API deve ser colocada diretamente no código, no arquivo `perplexityai.py`, substituindo o valor da variável <PERPLEXIT_API_KEY> :

```python
os.environ["PERPLEXITY_API_KEY"] = "<PERPLEXIT_API_KEY>"
```
```

Depois, basta rodar (em qualquer terminal):
```
ambvirtual
```

Também pode criar um alias para rodar o script rapidamente (adicione no mesmo arquivo):

```sh
alias ppty="python3 /home/pedroemanuel/códigos/perplexity/perplexityai.py"
```

Assim, basta digitar:
```sh
ppty "Sua pergunta para a Perplexity"
```

**Atenção:** Não compartilhe sua chave de API com ninguém. Este programa é para uso pessoal. Futuramente, o método de configuração da chave pode ser atualizado.

## Uso

No terminal, execute:
```sh
python perplexityai.py "Sua pergunta para a Perplexity"
```

Exemplo:
```sh
python perplexityai.py "Quem descobriu o Brasil?"
```

## Observações
- Não compartilhe sua chave de API publicamente. O uso é **pessoal**.
- Para dúvidas, consulte a [documentação oficial da Perplexity](https://docs.perplexity.ai/).
