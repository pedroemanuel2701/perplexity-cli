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

Você pode criar uma função no seu `~/.zshrc` **ou** `~/.bashrc` para criar e ativar rapidamente um ambiente virtual com:

```
nano ~/.zshrc
#OU
nano ~/.bashrc
```
Colar
```
# Para zsh ou bash:
ambvirtual() {
  if [ ! -d "./env" ]; then
    python3 -m venv env
    echo "Ambiente virtual criado."
  fi
  source env/bin/activate
  echo "Ambiente virtual ativado."
}
```
e dar Ctrl + O , Enter , Ctrl + X, e por fim:
````
source ~/.zshrc
#OU
source ~/.bashrc
````
Além dessa dica há o chamado rápido para o perplexity no terminal:
Novamente
```
nano ~/.zshrc
#OU
nano ~/.bashrc
```
Colar o caminho até o código onde ficam os alias:
````
alias ppty="python3 /seu/caminho/até/perplexity.py"
````
e dar Ctrl + O , Enter , Ctrl + X, e por fim:
````
source ~/.zshrc
#OU
source ~/.bashrc
````
Configuração da chave de API

Atualmente, a chave de API deve ser colocada diretamente no código, no arquivo `perplexityai.py`, substituindo o valor da variável <PERPLEXIT_API_KEY> :

```python
os.environ["PERPLEXITY_API_KEY"] = "<PERPLEXIT_API_KEY>"
```
## Uso
Depois, basta rodar (em qualquer terminal):
```
ambvirtual

ppty "Sua pergunta"
```

**Atenção:** Não compartilhe sua chave de API com ninguém. Este programa é para uso pessoal. Futuramente, o método de configuração da chave pode ser atualizado.

## Observações
- Para dúvidas, consulte a [documentação oficial da Perplexity](https://docs.perplexity.ai/).
