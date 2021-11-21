# Pset 6 CS50Xni

1.  Implementa <a href="#Sentimental" class="btn btn-sm btn-default">Sentimental</a>
2.  Implementa cualquiera de estos dos:
    
    -  <a href="#Similarities (More)" class="btn btn-sm btn-default">Similarities (More)</a> more comfortable (más cómodo - más difícil)
        
    -  <a href="#Similarities (Less)" class="btn btn-sm btn-default">Similarities (Less)</a> Less comfortable (menos cómodo - más facil)


## Sentimental

1.  Traslada/traduce  `hello.c`  a  `hello.py`.
2.  Traslada/traduce  `mario.c`  a  `mario.py`.
3.  Traslada/traduce  `cash.c`  a  `cash.py`  o  `credit.c`  `credit.py`.
4.  Traslada/traduce  `caesar.c`  a  `caesar.py`  o  `vigenere.c`  `vigenere.py`

## Similarities (More)

### Comprendiendo

#### `score`

Abre  `score`  (puntaje). Basta decir que el nombre de este archivo termina en  `.py`, aunque el archivo contiene un programa escrito en Python. ¡Pero eso está bien! Observa el "shebang" encima del archivo:

```
#!/usr/bin/env python3
```

Esa línea le dice a la computadora que interprete (por ejemplo: run) el programa usando  `python3`  (aka  `python`  en el IDE CS50), un intérprete que entiende Python 3.

Observa como el archivo define una función llamada  `main`  y llama esa función hasta el final del archivo. Definir  `main`  no es estrictamente necesario en Python, pero no es inusual

Observa como  `score`  usa el módulo de Python argparse para analizar dos argumentos de línea de la línea de comandos,  `FILE1`  y  `FILE2`, que son los archivos a comparar. El programa, entonces, intenta leer el contenido de esos archivos en cadenas  `file1`  y  `file2`. Si algo sale mal, como lo indicado en  `IOError`, la "excepción" es capturada. Revisar  [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)  para más excepciones.

Finalment, el programa pasa esas cadenas a  `distances`, una función que veremos más adelante, ¡Y finalmente imprimimos la distancia de edición entre los dos archivos!

#### `helpers.py`

Abre  `helpers.py`. Ah, el familiar  `TODO`  (por hacer). Declarado en este archivo se encuentra una función llamada  `distances`(distancias) que toma dos cadenas como argumentos,  `a`  y  `b`, y se supone que retorna (a través de una matriz de costos) la distancia de edición entre uno y otro. ¡Por el momento, sin embargo, devuelve una  `list`  bidimensional vacía!

Este archivo también define una "enumeración" (i.e.,  `Enum`) que esencialmente define tres constantes, donde cada una representa una operación a través en la cual una cadena podría ser transformada en otra:  `Operation.DELETED`,  `Operation.INSERTED`, y  `Operation.SUBSTITUTED`.

#### `application.py`

Abre  `application.py`. Este archivo implementa una aplicación web en la cuál, al final, te permitirá visualizar la distancia de edición entre dos cadenas como también las operaciones necesarias para transformar una cadena en otra al mínimo costo. No necesitas comprender la totalidad del archivo, pero si considerar que  `score`  infiere para la matriz retornada por  `distances`  la secuencia de operaciones que producen ese costo mínimo.

#### `templates/layout.html`

Abre  `templates/layout.html`. Este archivo es un modelo para el diseño general de la aplicación web. Lo más probable es que reconozcas algunas de las etiquetas HTML dentro del archivo y descubras algunas nuevas. Fíjate, en particular, como los modelos usan Bootstrap, una popular librería. De hecho, basamos este modelo en su propio  [modelo inicializador](http://getbootstrap.com/docs/4.0/getting-started/introduction/).

#### `templates/index.html`

Abre  `templates/index.html`. Ah, otro  `TODO`  (por hacer). Observa como los modelos extienden ("extends") a  `layout.html`, lo cual es como decir que  `layout.html`  es el "molde" en el cual  `index.html`  por sí mismo puede ser creado. El bloque definido (`block`) en  `index.html`  efectivamente conectará en el marcador de posición de  `block`  en  `layout.html.`

Finalmente, este archivo contedrá el formulario donde los usuarios podrán enviar sus dos cadenas a tu aplicación web para comparación.

#### `templates/score.html`

Open up  `templates/score.html`. We took the liberty of implementing this file for you. Thanks to its use of some CSS (particularly a class called  `row`), it ensures that  `matrix.html`  will fill the top half of a browser’s viewport and that  `log.html`  will fill the bottom half of the same.

#### `templates/matrix.html`

Open up  `templates/matrix.html`. Ah, another  `TODO`. It’s via this file that you’ll need to generate an HTML table that depicts the costs via which one string can be transformed into another

#### `templates/log.html`

Open up  `templates/log.html`. Phew, looks like we implemented this file for you. Indeed, it’s via this file that your web app will generate an HTML table that summarizes the operations via which one string can be transformed into another.

#### `templates/error.html`

Abre  `templates/error.html`. Este archivo es un template (modelo) donde se envía cualquier error HTTP que será mostrado. Sucede que también usa las características de  [Jumbotron](https://getbootstrap.com/docs/4.0/components/jumbotron/)  de Bootstrap.

#### `static/styles.css`

Abre  `static/styles.css`. En este archivo hay un poco de propiedades CSS que colectivamente implementan tu aplicación de interfaz de usuario. Esencialmente, estos modifican un poco de las propiedades de Bootstrap por defecto.

#### `requirements.txt`

Abre  `requirements.txt`  (sin cambiarlo, pese a que puedas hacerlo luego si gustas). Este archivo especifica las librerías, una por línea, de donde dependen todas estas funcionalidades.

## Especificaciones More

### `helpers.py`

#### `distances`

Implement  `distances`  in such a way that, given two strings,  `a`  and  `b`, it calculates the edit distance from  `a`  to  `b`, returning (as a  `list`  of  `lists`) the matrix of operational costs incurred along the way. Treat the matrix’s top-left corner as  `[0][0]`  and the matrix’s bottom-right corner as  `[len(a)][len(b)]`. Stored in each element of the matrix should be a  `tuple`,  `(cost, operation)`, where  `cost`  is an  `int`  and  `operation`  is an  `Operation`.

### `templates/index.html`

Implementar  `templates/index.html`  de tal manera que contenga un formulario HTML en el cual el usuario pueda enviar:

-   una cadena llamada  `string1`
    
-   una cadena llamada  `string2`
    

Eres bienvenido de observar a los HTML de las soluciones del staff si lo necesitas, pero intenta descubrir la sintáxis correcta por tu cuenta

### `templates/matrix.html`

Implementar  `templates/matrix.html`  de tal manera que genere, usando  [Jinja2](http://jinja.pocoo.org/), una visualización de una matriz retornada por  `distances`  (dado por algún  `a`  y  `b`) a través de una tabla HTML. En la cual cada célula de la table debería ser un costo, no una operación. A lo largo de la columna más a la izquierda deben estar los caracteres de  `a`, cada uno en su propia celda (y fila); a lo largo de la fila más superior deberían de estar los caracteres de  `b`, en cada celda (y columna).

## Similarities (Less)

### Comprendiendo

#### `compare`

Abre  `compare`. Basta decir que el archivo no termina en  `.py`, aunque el archivo contiene un programa escrito en Python. ¡Pero eso está bien! Observa el “shebang” en la parte superior del archivo:

```
#!/usr/bin/env python3
```

Esa línea le dice a la computadora que interprete (por ejemplo: que corra/ejecute) el programa usando  `python3`  (también conocido como  `python`  en el IDE CS50), un intérprete que entiende Python 3.

Observa como el archivo define una función llamada  `main`  y cómo llama esa función al final del archivo. Definir  `main`  no es estrictamente necesario en Python, pero es necesario definir funciones antes de llamarlas. En consecuencia, a causa que  `main`  llama a la función  `positive`, y a causa que queremos mantener la porción “main” de este programa de en la parte superior del archivo, tiene sentido implementar  `main`  como una función también. De esta manera,  `main`  no es llamado sino hasta el final del archivo (después que  `positive`  haya sido implementado), aún cuando  `main`  fue implementado en la parte superior del archivo.

No se necesita entender cada una de las líneas en  `compare`, pero sí notar a través de los comentarios lo que hace en general: analiza cada argumento de la línea de comandos, lee dos archivos en variables como strings, y compara esos strings, y luego imprime a la lista de similitudes. Las cadenas por si mismas son comparadas en una de las tres posibles formas, a como se especifica en el argumento de la línea de comandos: línea por línea, oración por oración o subcadena por subcadena.

### `helpers.py`

Abre  `helpers`.py. ¡Ah!, y ahí está el tan familiar  `TODO`  (a realizar). Declarado en este archivo están tres funciones, cada una de ellas están hechas para implementar un algoritmo diferente:  `lines`  (líneas),  `sentences`  (oraciones), y  `substrings`  (subcadenas). Hasta el momento, cada una de ellas retorna una lista vacía. ¡Pero no por mucho tiempo!

### `application.py`

Abre  `application`.py. Este archivo implementa una aplicación web que en su finalidad te permitirá ejecutar cualquiera de esos tres algoritmos en cualquiera de los dos archivos de texto. No se necesita entender la totalidad de este archivo, particularmente  `highlight`  y  `errorhandler`. Pero debes saber que  `highlight`, dado una cadena,  `s`, y una lista de otras cadenas,  `strings`, resaltará todas las coincidencias del primero en el segundo (cubriéndolo de etiquetas  `span`  en HTML). Y  `errorhandler`  asegura que cualquier error HTTP será mostrado en su propia página.

Pero tienes que leer  `index`  y  `compare`, ya que estos manejan los envíos del formulario.

### `templates/layout.html`

Abre  `templates/layout.html`. Este archivo es un modelo para el diseño general de la aplicación web. Lo más probable es que reconozcas algunas de las etiquetas HTML dentro del archivo y descubras algunas nuevas. Fíjate, en particular, como el modelo (template) usa Bootstrap, una biblioteca popular. De hecho, basamos este modelo en su propio  [modelo para empezar (starter template)](http://getbootstrap.com/docs/4.0/getting-started/introduction/).

### `templates/index.html`

Abre  `templates/index.html`. Ah, el último  `TODO`  (por hacer). Observa como este modelo se extiende ("extends" desde  `layout.html`, lo cual es como decir que  `layout.html`  es el "molde" con el cual  `index.html`  por sí mismo será creado. El bloque definido (`block`) en  `index.html`  efectivamente conectará en el marcador de posición de  `block`  en  `layout.html`.

Finalmente, este archivo contendrá un formulario a través del cual los usuarios serán capaces de subir dos archivos a tu aplicación web para ser comparado por de uno de tus tres tipos de algoritmos.

### `templates/compare.html`

Abre  `templates/compare.html`. Nos tomamos la libertad de implementar este archivo por ti. Gracias al uso de CSS (particularmente de la clase llamada  `col-6`), se asegura que el archivo del usuarios, una vez subido y resaltado, será mostrado uno al lado al lado del otro (side by side).

### `templates/error.html`

Abre  `templates/error.html`.Este archivo es un template (modelo) con el cual se envía cualquier error HTTP será mostrado. Sucede que también usa las características de un  [Jumbotron](https://getbootstrap.com/docs/4.0/components/jumbotron/)  de Bootstrap.

### `static/styles.css`

Abre  `static/styles.css`. En este archivo hay algunas propiedades CSS que colectivamente implementan la interfaz de usuario de tu aplicación. Esencialmente, estas modifican algunas de las propiedades por defecto de Bootstrap .

#### `requirements.txt`

Abre  `requirements.txt`  (sin cambiarlo, pese a que puedas hacerlo luego si gustas). Este archivo especifica las librerías, una por línea, de las que dependen todas estas funcionalidades.

## Especificaciones Less

### `helpers.py`

#### `lines (líneas)`

Implementa  `lines`  (líneas) de tal manera que, dados dos strings,  `a`  y  `b`, retornará una  `list`  de las líneas que sean idénticas tanto en  `a`  como en  `b`. La  `list`  no debería de tener ningún duplicado. Asume que las líneas en  `a`  y  `b`  serán separadas por  `\n`, pero las cadenas en la  `list`  retornada no deberían terminar en  `\n`. Si ambos  `a`  y  `b`  contienen una o más líneas en blanco (por ejemplo, un  `\n`  inmediatamente precedido por ningún otro carácter), la  `list`  retornada debería de incluir una cadena vacía (por ejemplo,  `" "`).

#### `sentences (oraciones)`
Implementar  `sentences`  (oraciones) de tal manera que, dadas dos cadenas,  `a`  y  `b`, retornará una  `list`  _única_  de oraciones idénticas en inglés presentes en  `a`  y  `b`. La  `list`  no debería contener ningún duplicado. Usa  `sent_tokenize`  de la Natural Language Toolkit (Kit de Herramientas de Lenguaje Natural) para"tokenize" (por ejemplo, separar) cada cadena en una  `list`  de oraciones. Puede ser importado con:

```
from nltk.tokenize import sent_tokenize
```

De acuerdo con la  [documentación](http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize),  `sent_tokenize`, dado un  `str`  como entrada, retorna una  `list`  de oraciones en Inglés. Asumimos que la entrada es un texto en Inglés (y no, por ejemplo, código, que podría coincidir en tener puntos también).

#### `substrings (subcadenas)`

Implementar  `substrings`  (subcadenas) de tal manera que, dados dos tipos de cadenas,  `a`  y  `b`, y un entero,  `n`, retorne una  `list`  de todas las subcadenas de tamaño  `n`  que sean idénticas y que estén presentes en  `a`  y  `b`. La  `list`  no debería contener ningún duplicado.

Recuerda que una subcadena de tamaño n no es más que sólo una secuencia de n caracteres de esa cadena. Por ejemplo, si n es 2 y la cadena es Yale, entonces, habrá tres posibles subcadenas de tamaño 2: Ya, al, y le. Mientras que si n es 1 y la cadena es Harvard, entonces hay siete posibles cadenas de tamaño 1: H, a, r, v, a, r, y d. Pero si eliminamos duplicados, entonces habrá solamente cinco cadenas únicas: H, a, r, v, and d

### `templates/index.html`

Implementar  `templates/index.html`  de una manera tal que contenga un formulario HTML a través el cual un usuario pueda enviar:

-   Un archivo llamado  `file1`  (archivo1)
    
-   Un archivo llamado  `file2`  (archivo2)
    
-   Un valor de  `lines`,  `sentences`, o  `substrings`  para una  `input`  (entrada) llamada  `algorithm`  (algoritmo).
    
-   Un número llamado  `length`  (tamaño)
    

Eres bienvenido a echar un vistazo al HTML de la solución del Staff si lo necesitas, pero intenta descubrir la sintaxis correcta por tu cuenta
