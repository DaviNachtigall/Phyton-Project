# 📘 Referência Rápida de Sintaxe Python

---

## 🔀 Condicionais (if / elif / else)

```python
age = 16

if age <= 15:
    print("You are younger than 16")
elif age == 16:
    print("You are 16")
elif age == 17:
    print("You are 17")
else:
    print("You are older than 16")
```

---

## 🧵 Placeholders em Strings

### Estilo `%s` (antigo)
```python
sentence = "%s %s was the president of the United States"
print(sentence % ("Barack", "Obama"))

name = "jake"
sentence = "%s is 15 years old"
print(sentence % name)
```

### Concatenação com `+`
```python
name = "jake"
print(name + " is 15 years old")
```

### f-strings (recomendado, moderno)
```python
name = "avi"
print(f"Hello, {name}")

x = 10
y = 20
print(f"The sum of x and y is {x + y}")
```

---

## 🔁 Laço While

```python
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        continue        # pula a iteração quando c == 3
    print(c)
```

---

## 🔁 Laço For

### `range(start, stop, step)`
```python
for i in range(0, 11, 2):
    print(i)
```

### Percorrendo uma lista
```python
list1 = ['apples', 'bananas', 'cherries']

for item in list1:
    print(item)
```

---

## 📦 Tuplas (imutáveis!)

```python
tup = ('oranges', 'apples', 'bananas')
# tup[0] = 'cherries'   ❌ ERRO! Tuplas não podem ser alteradas
print(tup)
```

> ⚠️ Diferente de listas, tuplas **não permitem** alterar itens depois de criadas.

---

## 📚 Dicionários

```python
students = {'bob': 12, 'rachel': 13, 'emily': 15}

students['rachel'] = 14   # atualizar valor
del students['emily']     # remover chave
print(len(students))      # tamanho do dicionário
```

---

## 📋 Listas

### O que é uma lista?
- Conjunto **ordenado** de itens
- Possui **índice**
- Mantém a **ordem** de inserção

### Operações básicas
```python
shopping_list = ['apples', 'oranges', 'bananas', 'cheese']

shopping_list.append('blueberries')  # adicionar item
shopping_list[0] = 'cherries'        # atualizar item
del shopping_list[1]                 # remover item

print(shopping_list)
```

### Funções úteis
```python
list_num = [1, 4, 7, 23, 6]
print(max(list_num))   # maior valor
print(min(list_num))   # menor valor
```

---

## ✂️ Strings: Concatenação e Slicing

```python
string1 = 'ola'
string2 = 'tudo bem?'

print(string1 + ' ' + string2)   # concatenação
print(string2[0:4])              # slicing → 'tudo'
```

---

## 🚨 Try / Except

```python
try:
    if name > 3:
        print("hello")
except:
    print("An error was detected in your code")
```

---

## 🏗️ Classes (Programação Orientada a Objetos)

### Classe básica
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
```

### Herança (`super()`)
```python
class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 5

    def drive(self):
        print("Driving a car...")


class SportsCar(Car):
    def __init__(self):
        super().__init__()          # chama o __init__ da classe pai
        self.engine_power = '400 HP'
        self.seats = 2               # sobrescreve o valor herdado
```

---

## ⚙️ Funções

```python
def hello_world():
    print("Hello World")

hello_world()
```

---

## 📝 Notas Rápidas

| Estrutura | Mutável? | Ordenada? | Índice? |
|---|---|---|---|
| Lista `[]` | ✅ Sim | ✅ Sim | ✅ Sim |
| Tupla `()` | ❌ Não | ✅ Sim | ✅ Sim |
| Dicionário `{}` | ✅ Sim | ✅ Sim (desde Python 3.7) | 🔑 Chave |
