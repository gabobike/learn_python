Temas de esta Unidad 

1. Introduccion a Modulos
2. Diseño de Modulos
3. Releer Modulos
4. Sympy

## 1- Introduccion a Modulos

El término módulo corresponde a un archivo de python, cada archivo es un módulo y los módulos pueden importar otros módulos para utilizar los nombres que estos definen. 

Los módulos también pueden corresponder a extensiones de código de otros lenguajes como C, Java, o C# e incluso a directorios en la importación de paquetes.

Para importar los módulos se utiliza:

- Import: Para  importar  todo  el  módulo.  Import  asigna  un  objeto  módulo  a  un nombre, ya que el módulo en sí también es considerado un objeto.
- from: Se  utiliza  para  importar  un  nombre  específico, from asigna uno o más nombres a objetos con el mismo nombre en otro modulo

En los modulos definimos nombres conocidos como atributos que pueden ser referenciados externamente y de los cuales podemos utilizar sus herramientas.

## Estructura de un programa.

En un nivel básico python consiste de una serie de declaraciones dentro de un archivo principal  que  puede  utilizar  o  no  otros  módulos  complementarios.  El  archivo  principal posee  el  control  del flujo  del  programa,  este  es  el  archivo  que  se  ejecuta  al  lanzar  el programa.

## Módulos por defecto (Standard Library)

Cada  distribución de  Python  viene  con  un  número  de  módulos  por  defecto,  en  las distribuciones actuales de python ya han superado los 200.

## Importar un atributo.

Tomemos dos archivos **main.py** y **modulo1.py**, en donde main.py es el archivo de nivel más alto y el otro conforma un módulo.

main.py

```python
import modulo 1

modulo1.imprimir("mensaje a imprimir")
```

modulo1.py

```python
def imprimir(mensaje):
	print(mensaje)
```

Nos retorna:

Mensaje a imprimir

**Nota:** El módulo a importar se importa sin agregar la extension del archivo.

## ¿Cómo funciona la importación?

Durante  la  ejecución  del  programa  se  producen  tres  pasos  la  primera  vez  que  un programa importa un archivo.

1. Encuentra el archivo.
2. Lo compila a código de bit(si es necesario).
3. Ejecutar el codigo del modulo para construir los objetos que define.

Las posteriores importaciones acceden simplemente a la memoria. Python almacena los módulos en una tabla llamada sys.modules y chequea ahí al inicio de una operación de importación. Si el módulo no se encuentra, se ejecutan los tres pasos previos.

Para ver el contenido podemos simplemente modificar el código anterior:

a/main.py

```python
import modulo1
import sys

modulo1.imprimir("mensaje a imprimir")
print(sys.modules)
```

El cual nos retorna:

un mensaje 

**Nota:** Se ha limitado el mensaje retornado para facilitar la comprensión.

**¿Dónde se guarda el código de bit?**

Hasta la versión 3.1 se guardaba en archivos con extensión .pyc dentro del directorio en el  cual  se  encontraba  el  módulo.  Luego  de  la  versión  3.2  se  crea  un  directorio __pycache__ dentro del directorio en donde se encuentra el módulo y dentro se ubican los archivos .pyc. El nombre del archivo incluye el nombre de la versión de python que le da origen, así el archivo models.py  puede convertirse en models.cpython-37.pyc

**¿En que path se buscan los módulos?** 

Los módulos se buscan en los siguientes lugares según el orden que se presenta:

1. El directorio del programa.
2. Los directorios del PYTHONPATH si existe. Recordar que en este caso podemos ver todas las rutas importando el módulo “sys” y ejecutando la línea: print(sys.path).
3. Direcciones de librerías Standard en la máquina.
4. El directorio site-packages de extensiones de terceros.

**Import vs. From módulo import ***

Al usar “from módulo import *” en lugar de un nombre específico, obtenemos copias de todos los nombres asignados en el nivel más alto del módulo referenciado. Técnicamente tanto import como from invocan la misma operación de importación, la operación from * agrega un paso extra en el cual se copia todos los nombres en el módulo importado. En esencia  combina  un  namespace  dentro  del  otro  de  forma  de  que  la  segunda  opción requiere menos tipeo de código. 

**La importación se da una sola vez.**

Tanto  “import”  como  “from”  se  cargan  y  ejecutan  solo  la  primera  vez,  dado  que  la importación es algo costoso desde el punto de vista computacional. Las importaciones posteriores solamente hacen referencia a los objetos ya importados de cada módulo.

Tomemos un ejemplo, si ejecutamos **b/main.py**

```python
import modulo2  
print(modulo2.color)  
modulo2.color = "verde   
import modulo2 
print(modulo2.color) 
import modulo2  
print(modulo2.color) 
```

**b/modulo2.py**

```python
print(‘hola’) 
color = 1 
```

Nos retorna:  

**Cambiando objetos mutables en los módulos.**



