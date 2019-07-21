# Projeto: Cash Machine
<b>Desenvolvedor:</b> Daniel Vieira <p>
<b>E-mail:</b> danielsrosa13@gmail.com

## Desafio Proposto

### Teste Para Desenvolvedor Python: <i>Cash Machine</i>

Crie um projeto em Python que exiba quantas notas são
necessárias para compor um valor 'X' e qual a quantidade
de cada uma. As notas disponíveis serão informadas pelo
usuário, podendo utilizar-se de quantas notas forem
necessárias para compor o valor. As notas devem ser
qualquer valor inteiro entre 1 e 1000

O projeto poderá ser feito preferencialmente
através de uma Task do Celery(framework que utilizamos),
caso não tenha conhecimento de tal framework, o mesmo
poderá ser feito utilizando uma interface web(aiohttp,
Flask...), caso não possua conhecimento para desenvolvimento
web poderá ser feito uma aplicação para terminal.

Exemplo 1:
```
   Notas disponíveis: 1, 30, 50
```
```
   Valor desejado: 134
```
```
   Resultado: 4 notas de 1, 1 nota de 30 e 2 notas de 50
```
Exemplo 2:
```
   Valor desjado: 10
```
```
   Resultado: 10 notas de 1
```

Alem da lógica do código, também será avaliado organização e
documentação do mesmo.

## Versão Python
Versão: 3.7.4

## Como executar o projeto?
Abra o terminal do seu sistema operacional na mesma pasta onde se enconta o arquivo: cashMachine.py
```
..\seu_diretorio\terminal_application>_
```
e execute o comando 
```
python cashMachine.py
```
você irá ver:
```
...:::  CASH MACHINE  :::...
PARA SAIR DIGITE 0 (ZERO)...


ADICIONANDO NOTAS...
Digite o valor da nota e aperte ENTER para salvar:
```
pronto, aplicação já está funcionando...
