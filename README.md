# Perplexity CLI

![GitHub license](https://img.shields.io/github/license/pedroemanuel2701/perplexity-cli)
![GitHub last commit](https://img.shields.io/github/last-commit/pedroemanuel2701/perplexity-cli)
![Python version](https://img.shields.io/badge/python-3.8%2B-blue)

[Repositório no GitHub](https://github.com/pedroemanuel2701/perplexity-cli)

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
# Exemplo de caminho real (ajuste para o seu usuário):
alias ppty="python3 /home/seuusuario/códigos/perplexity/perplexityai.py"
````
e dar Ctrl + O , Enter , Ctrl + X, e por fim:
````
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
```
ambvirtual

ppty "Sua pergunta"
```

Ou, se preferir rodar sem alias:
```
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
