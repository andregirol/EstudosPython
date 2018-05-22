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

# Tudo em Python é um objeto

Módulos, funções, literais, todos são objetos.

Se você abrir agora o shell interativo do Python e rodar o seguinte:

```python
import humansize
```

Você acabou de instanciar um **objeto** do tipo **módulo** e pode acessar seus atributos, métodos, classes funções, constantes, etc...

```python

