# Iniciando

Editor básico: IDLE

Instalar no ubuntu: 

    apt install idle3

Estará disponível nos menus de aplicativos

### Ajuda interativa do python:

    help()

Depois seguir as instruções do interpretador


**Nota sobre funções:**

Uma função em Python não especifica um tipo de dado ao ser executada, mas sempre retorna um valor. Se a expressão `return` for utilizada, ela retornará aquele valor. Caso contrário retornará `None`, o equivalente a **nulo** em Python

Uma função aceita valores default. Os argumentos de uma função podem ser especificados em qualquer ordem se chamados pelo nome;

Exemplo:

```python
def soma(valor1, valor2):
    return valor1 + valor2

```

Essa função pode ser chamada assim:

```python
soma(valor2 = 10, valor1 = 5)
```

No entanto, desde que o primeiro argumento nomeado apareça, todos os subsequentes devem ser nomeados também


