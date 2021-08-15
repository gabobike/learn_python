# Unidad II - Tipos de datos I.

## **Tematicas** 

1. ## **Jupyter IPython.**

2. ## **Números.**

3. ## **Strings.**

4. ## **Listas.**

5. ## **Diccionarios.**

6. ## **Herramientas de sistemas.**



1. ## **Jupyter IPython**

Para comenzar a trabajar en esta unidad, presentaremos ***una herramienta muy interesante la cual le añade funcionalidades extras al modo interactivo incluido en python***, como resaltado de linea y autocompletado de datos: Jupyter IPython.

Para instalarlo seguiremos unos pasos sencillos.

Paso 1 - actualizamos pip

Python posee un repositorio de paquetes extras desarrollados por terceros, que le añaden funcionalidad a nuestras aplicaciones. Estos componentes pueden ser instalados y administrados mediante el gestor de paquetes pip, y antes de avanzar nos aseguraremos de poseer la ultima versión.

Opcion A

Si estamos en Windows, abrimos un cmd como administrador y ejecutamos.

```python
pip install --upgrade pip
```

Opcion B

Tambien podemos instalarlo descargando el archivo de instalacion desde:

https://pip.pypa.io/en/stable/installing/

> Esta opción es válida también para cuando pip no está instalado

## **2.- Números** 

Python soporta números enteros, de punto flotante o complejos, básicamente el interprete actúa como una calculadora, utilizando operadores de forma análoga a como lo hariamos en C, en donde tenemos la posibilidad de utilizar paréntesis puede alterar el resultado. Veamos un ejemplo

```pyth
valor1 = 5 - 2 * 6
valor2 = (5 - 2) * 6
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
```

Resultado:

```bash
-7
<class 'int'>
18
<class 'int'>
```



Como vemos ambos resultados son del tipo entero ya que los números utilizados son del tipo entero. Esto no se cumple cuando utilizamos el operador de división el cual siempre nos retorna un número flotante:

