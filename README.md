
### Inserindo sua chave de API pelo terminal (recomendado)

Ao rodar o programa pela primeira vez, será solicitado que você insira sua chave da API Perplexity no terminal. Ela será salva em um arquivo oculto (`~/.perplexity_api_key`) no seu diretório de usuário e será usada automaticamente nos próximos usos.

Se quiser trocar a chave depois, basta apagar o arquivo:
```sh
rm ~/.perplexity_api_key
```
e rodar o programa novamente.
# Perplexity CLI

![GitHub license](https://img.shields.io/github/license/pedroemanuel2701/perplexity-cli)
![GitHub last commit](https://img.shields.io/github/last-commit/pedroemanuel2701/perplexity-cli)
![Python version](https://img.shields.io/badge/python-3.8%2B-blue)

[Repositório no GitHub](https://github.com/pedroemanuel2701/perplexity-cli)

Este projeto é um CLI simples para interagir com a API da Perplexity usando Python.

## Pré-requisitos
- Python 3.8 ou superior
- Uma chave de API válida da Perplexity
- [Oh My Zsh (Opcional, para bash/zsh no Windows)](https://ohmyz.sh/)

## Instalação

### Windows (cmd ou PowerShell)
### Usando Oh My Zsh ou Bash no Windows

Se você deseja usar as funções `ambvirtual` e `ppty` no Windows, é necessário instalar um terminal compatível, como o [Oh My Zsh](https://ohmyz.sh/) (com zsh) ou o bash (via WSL, Git Bash, etc). Essas funções não funcionam no cmd ou PowerShell.

#### Passo a passo para adicionar as funções no Oh My Zsh (ou bash)

1. Abra o terminal Oh My Zsh (ou bash/WSL/Git Bash).

2. Edite o arquivo de configuração do shell:
  ```sh
  nano ~/.zshrc   # para Oh My Zsh/zsh
  # ou
  nano ~/.bashrc  # para bash
  ```
3. Cole as funções/alias no final do arquivo:
  ```sh
  ambvirtual() {
    if [ ! -d "./env" ]; then
     python3 -m venv env
     echo "Ambiente virtual criado."
    fi
    source env/bin/activate
    echo "Ambiente virtual ativado."
  }

  # Exemplo de caminho real (ajuste para o seu usuário):
  alias ppty="python3 /home/seuusuario/códigos/perplexity/perplexityai.py"
  ```
4. Salve e feche o arquivo (Ctrl+O, Enter, Ctrl+X).
5. Recarregue o terminal:
  ```s
  source ~/.zshrc
  # ou
  source ~/.bashrc
  ```
6. Agora você pode usar os comandos `ambvirtual` e `ppty` normalmente nesse terminal.

> **Obs:** No Windows, esses comandos só funcionarão em terminais compatíveis com bash/zsh, como Oh My Zsh, WSL ou Git Bash. Não funcionam no cmd ou PowerShell.

> **Dica:** Os comandos `ambvirtual` e `ppty` são funções/alias criados no bash/zsh (Linux/macOS). No Windows, use os comandos abaixo diretamente no terminal:

- Para ativar o ambiente virtual (cmd):
  ```cmd
  env\Scripts\activate
  ```
- Para ativar o ambiente virtual (PowerShell):
  ```powershell
  .\env\Scripts\Activate.ps1
  ```
- Para rodar o script:
  ```cmd
  python perplexityai.py "Sua pergunta"
  ```

> **Obs:** Os comandos `ambvirtual` e `ppty` não funcionam nativamente no cmd/PowerShell, pois são exclusivos do bash/zsh (Linux/MacOS). Se quiser, pode criar scripts `.bat` ou funções no PowerShell para facilitar o uso no Windows.

1. Clone o repositório:
  ```cmd
  git clone https://github.com/pedroemanuel2701/perplexity-cli.git
  cd perplexity-cli
  ```

2. Instale as dependências:
  ```cmd
  pip install perplexity-ai
  ```

3. (Opcional) Crie e ative um ambiente virtual:
  - No cmd:
    ```cmd
    python -m venv env
    env\Scripts\activate
    ```
  - No PowerShell:
    ```powershell
    python -m venv env
    .\env\Scripts\Activate.ps1
    ```


1. Clone o repositório:
   ```sh
   git clone https://github.com/pedroemanuel2701/perplexity-cli.git
   cd perplexity-cli
   ```

2. Instale as dependências:
   ´´´
   pip install perplexity-ai
   ´´´

## Dica de uso rápido (Linux/macOS)

Você pode criar uma função no seu `~/.zshrc` **ou** `~/.bashrc` para criar e ativar rapidamente um ambiente virtual com:

```sh
nano ~/.zshrc
#OU
nano ~/.bashrc
```
Colar
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
```
e dar Ctrl + O , Enter , Ctrl + X, e por fim:
````sh
source ~/.zshrc
#OU
source ~/.bashrc
````
Além dessa dica há o chamado rápido para o perplexity no terminal:
Novamente
```sh
nano ~/.zshrc
#OU
nano ~/.bashrc
```
Colar o caminho até o código onde ficam os alias:
````sh
# Exemplo de caminho real (ajuste para o seu usuário):
alias ppty="python3 /home/seuusuario/códigos/perplexity/perplexityai.py"
````
e dar Ctrl + O , Enter , Ctrl + X, e por fim:
````sh
source ~/.zshrc
#OU
source ~/.bashrc
````

> **Dica:** Sempre que abrir um novo terminal, execute `ambvirtual` para ativar o ambiente virtual antes de rodar o script.
Configuração da chave de API

Atualmente, a chave de API deve ser colocada diretamente no código, no arquivo `perplexityai.py`, substituindo o valor da variável `<PERPLEXIT_API_KEY>`:

```python
os.environ["PERPLEXITY_API_KEY"] = "<PERPLEXIT_API_KEY>"
```
## Uso
ppty "Sua pergunta"

Depois, basta rodar (em qualquer terminal):
```s
ambvirtual

ppty "Sua pergunta"
```

Ou, se preferir rodar sem alias:
```s
ambvirtual
python3 /home/seuusuario/códigos/perplexity/perplexityai.py "Sua pergunta"
```


## Exemplo de saída

´´´
ambvirtual                                                                
Ambiente virtual ativado.
(env) 

ppty 'Qual a capital do Brasil?'                                          

Resposta:

A capital do Brasil é **Brasília**[1][2][3][4][5].

Brasília está localizada na Região Centro-Oeste do país e foi inaugurada como capital federal em 21 de abril de 1960, substituindo o Rio de Janeiro[1][2][4]. É considerada uma obra-prima da arquitetura moderna, concebida por Oscar Niemeyer e Lúcio Costa, e foi planejada para ser o centro político do Brasil, abrigando as sedes dos três poderes da República (Executivo, Legislativo e Judiciário) e embaixadas estrangeiras[2][4].

A cidade possui também o status de Patrimônio Histórico e Cultural da Humanidade pela Unesco devido ao seu projeto urbanístico inovador[2][4].
(env)
´´´


**Atenção:** Não compartilhe sua chave de API com ninguém. Este programa é para uso pessoal. Futuramente, o método de configuração da chave pode ser atualizado.

## Observações
- Para dúvidas, consulte a [documentação oficial da Perplexity](https://docs.perplexity.ai/).

## Contribuição

Contribuições são bem-vindas! Para contribuir:
- Faça um fork do projeto
- Crie uma branch para sua feature ou correção (`git checkout -b minha-feature`)
- Faça commit das suas alterações (`git commit -m 'Minha nova feature'`)
- Faça push para o seu fork (`git push origin minha-feature`)
- Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
