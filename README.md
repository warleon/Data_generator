# Data_generator
Este simple programa te ayudara a completar encuestas para tu curso de estadisica.
Necesitas tener encuestas previas en tu "archivo.csv" ya que se basa en sus respuestas.

## Prerequisitos

- Tener el interprete de python3 instalado.
- Terner la libreria Pandas la cual se instala con el comando:
~~~
pip3 install pandas
~~~

## Como usarlo
1. En "dataGen.py" modifica las 2 variables 'eBase' con el nombre de tu "archivo.csv" y 'eGen' con el nombre del "gen.csv" que quieras obtener. Ambos nombres de archivo tienen que tener la terminacion .csv debido a las funciones de pandas que se estan usando.

2. En tu terminal ejecuta el comando:
~~~
python3 dataGen.py
~~~

## Aclaraciones
- Para generar archivo se escojera solo de las respuestas previas que tenga tu encuesta.
- si tus encuestas no tienen suficientes repuestas te recomiendo agregar todas las posibles respuesta de cada variable(pregunta).
