# Exemplos de strings e slices

# Documentação com help

A função `help` do Python nos mostra  documentação de qualquer recurso da linguagem. Por exemplo, para ver a documentação de string fazemos: 


```python
# help(str)
```

## Ordenando listas

O método `sort()` deve ser chamado a partir do objeto lista e ordena no mesmo local. Dizemos que é sort *in-place*.

Ele recebe um argumento `reverse` que determina se a ordenação será em ordem crescente ou decrescente. 


```python
lista = [5 , 3 , 8, 2, 0, 1]
```


```python
lista.sort(reverse=True)
```

Note que é o próprio objeto *lista* que apareceu ordenado


```python
lista
```




    [8, 5, 3, 2, 1, 0]




```python
#help(lista.sort)
```

## A função *sorted*

A função `sorted` faz parte do Python, recebe uma lista e devolve uma nova lista com seus elementos ordenados.


```python
lista2 = [5 , 3 , 8, 2, 0, 1]
```


```python
saida = sorted(lista2)
```

Notem que a nova lista `saida` vem ordenada


```python
saida
```




    [0, 1, 2, 3, 5, 8]



E a estrutura original `lista2`  ainda está inalterada


```python
lista2
```




    [5, 3, 8, 2, 0, 1]



## Método find


```python
frase = "you never never  give me your money"
```


```python
frase.find("never")
```




    4




```python
help(frase.find)
```

    Help on built-in function find:
    
    find(...) method of builtins.str instance
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
    
    


```python
frase.find("never", 5)
```




    10




```python
# help(frase.findall)
```

## Método replace




```python
frase_2 = "ai se eu te pego pego pego"
```


```python
frase_2.replace("pego", "ajudo", 2)
```




    'ai se eu te ajudo ajudo pego'




```python
help(frase_2.replace)
```

    Help on built-in function replace:
    
    replace(old, new, count=-1, /) method of builtins.str instance
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
    
    

## Método strip()


```python
zoada = """					     oi bom dia	    


				"""

```


```python
limpa = zoada.strip()
```


```python
#help(zoada.strip)
```

    Help on built-in function strip:
    
    strip(chars=None, /) method of builtins.str instance
        Return a copy of the string with leading and trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
    
    


```python
limpa
```




    'oi bom dia'



## Método split


```python
pagode = """
É coisa de pele, um lance criminoso
Um frio na barriga, arrepio no corpo
Longe do mundo inteiro
Amor do nosso jeito
Deixa em off
Off, o nosso amor é mais gostoso em off
Proibido, escondido em off
Só eu e você perdido em love
Deixa em off
"""
```


```python
pagode = pagode.strip()
```


```python
help(pagode.split)
```

    Help on built-in function split:
    
    split(sep=None, maxsplit=-1) method of builtins.str instance
        Return a list of the words in the string, using sep as the delimiter string.
        
        sep
          The delimiter according which to split the string.
          None (the default value) means split according to any whitespace,
          and discard empty strings from the result.
        maxsplit
          Maximum number of splits to do.
          -1 (the default value) means no limit.
    
    


```python
#pgd = pagode.split(sep = "\n")
pgd = pagode.split()
```


```python
pgd
```




    ['É',
     'coisa',
     'de',
     'pele,',
     'um',
     'lance',
     'criminoso',
     'Um',
     'frio',
     'na',
     'barriga,',
     'arrepio',
     'no',
     'corpo',
     'Longe',
     'do',
     'mundo',
     'inteiro',
     'Amor',
     'do',
     'nosso',
     'jeito',
     'Deixa',
     'em',
     'off',
     'Off,',
     'o',
     'nosso',
     'amor',
     'é',
     'mais',
     'gostoso',
     'em',
     'off',
     'Proibido,',
     'escondido',
     'em',
     'off',
     'Só',
     'eu',
     'e',
     'você',
     'perdido',
     'em',
     'love',
     'Deixa',
     'em',
     'off']




```python
for p in pgd:
    print(p, end = "|||")
```

    É|||coisa|||de|||pele,|||um|||lance|||criminoso|||Um|||frio|||na|||barriga,|||arrepio|||no|||corpo|||Longe|||do|||mundo|||inteiro|||Amor|||do|||nosso|||jeito|||Deixa|||em|||off|||Off,|||o|||nosso|||amor|||é|||mais|||gostoso|||em|||off|||Proibido,|||escondido|||em|||off|||Só|||eu|||e|||você|||perdido|||em|||love|||Deixa|||em|||off|||

## Caracteres e português


```python
panda = "🐼"
```


```python
"🐼"*5
```




    '🐼🐼🐼🐼🐼'



## Método Join


```python
"🐼".join(pgd)
```




    'É🐼coisa🐼de🐼pele,🐼um🐼lance🐼criminoso🐼Um🐼frio🐼na🐼barriga,🐼arrepio🐼no🐼corpo🐼Longe🐼do🐼mundo🐼inteiro🐼Amor🐼do🐼nosso🐼jeito🐼Deixa🐼em🐼off🐼Off,🐼o🐼nosso🐼amor🐼é🐼mais🐼gostoso🐼em🐼off🐼Proibido,🐼escondido🐼em🐼off🐼Só🐼eu🐼e🐼você🐼perdido🐼em🐼love🐼Deixa🐼em🐼off'



## Converter string em lista


```python
lista_frase = list(frase)
```


```python
lista_frase
```




    ['y',
     'o',
     'u',
     ' ',
     'n',
     'e',
     'v',
     'e',
     'r',
     ' ',
     'n',
     'e',
     'v',
     'e',
     'r',
     ' ',
     ' ',
     'g',
     'i',
     'v',
     'e',
     ' ',
     'm',
     'e',
     ' ',
     'y',
     'o',
     'u',
     'r',
     ' ',
     'm',
     'o',
     'n',
     'e',
     'y']



# Slices


```python
lsl = [7, 13, 19, 15, 6]
```

Índices convencionais retornam só uma posição


```python
lsl[2]
```




    19



Slides retornam do primeiro elemento até *antes* do segundo. Por exemplo no exemplo abaixo vai retornar
os elementos de 0 até antes do 2


```python
lsl[0:2]
```




    [7, 13]



Quando usamos a notação **:**  o slice entende "vá do início ao fim de lista"


```python
lsl[:]
```




    [7, 13, 19, 15, 6]



O índice $-1$ é um atalho para o último elemento da lista


```python
lsl[-1]
```




    6



O exemlo abaixo significa: vá desde o último elemento, até o elemento zero, com passo de tamanho $-1$. Ou seja: ande para trás do fim para o começo


```python
lsl[-1:0:-1]
```




    [6, 15, 19, 13]



O exemplo abaixo significa: vá do início até o fim andando de 2 em 2


```python
lsl[::2]
```




    [7, 19, 6]




```python
lsl[0:1]
```




    [7]




```python
lsl[0:3]
```




    [7, 13, 19]




```python
lsl[3]
```




    15




```python

```
