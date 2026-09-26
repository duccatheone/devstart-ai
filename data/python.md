# Python

## O que é?

Python é uma linguagem de programação de alto nível, criada para ser fácil de ler e escrever. É uma das linguagens mais usadas do mundo, presente em áreas como desenvolvimento web, ciência de dados, automação, inteligência artificial e scripts do dia a dia.

## Conceitos básicos

### Variáveis
Uma variável é um espaço para guardar um valor que pode ser usado e alterado durante a execução do programa. Em Python, não é preciso declarar o tipo da variável antes de usá-la.

```python
nome = "Ana"
idade = 25
```

### Condicionais
Estruturas condicionais permitem que o programa tome decisões diferentes dependendo de uma condição, usando `if`, `elif` e `else`.

```python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### Laços de repetição
Usados para repetir um bloco de código várias vezes. Os principais são `for` (quando se sabe quantas vezes repetir) e `while` (enquanto uma condição for verdadeira).

```python
for i in range(5):
    print(i)
```

### Funções
Blocos de código reutilizáveis, que recebem entradas (parâmetros) e podem devolver uma saída (retorno).

```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

### Estruturas de dados básicas
- **Listas**: coleções ordenadas e mutáveis de itens (`[1, 2, 3]`).
- **Dicionários**: pares de chave e valor (`{"nome": "Ana"}`).
- **Tuplas**: coleções ordenadas e imutáveis (`(1, 2, 3)`).

## Próximos passos

Depois de dominar os conceitos básicos, o estudante pode seguir para:

- manipulação de arquivos;
- tratamento de erros (`try`/`except`);
- orientação a objetos (classes e objetos);
- bibliotecas populares, como `pandas` para dados ou `requests` para consumir APIs.
