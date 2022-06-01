# EDA Tour de France

![](images/logo.png)

Históricamente, los tres países ganadores en el ciclismo han sido Francia, España e Italia. El objetivo de este EDA es analizar la evolución en el rendimiento de sus ciclistas en los últimos años. Para ello, vamos a visualizar los resultados que han obtenido entre los años 2015 y 2019 en la competición del Tour de France. 

## Obtener los datos

![](images/procycling.png)

Lo primero es obtener el tiempo de cada ciclista en la clasificación general. https://www.procyclingstats.com/ es la web con mayor cantidad de datos e información sobre competiciones de ciclismo profesional. En ella podemos realizar web scraping de una manera sencilla. En este caso lo haremos con la librería Selenium. 

![](images/tabla1.png)

## Limpiar los datos

Una vez obtenemos la clasificación, limpiamos los datos hasta quedarnos solo con los corredores que nos interesan así como con su tiempo. El ciclista ganador marca el tiempo record y la columna tiempo nos indica la diferencia añadida con la que terminan el resto de ciclistas. Algunos llegarán con segundos, otros con minutos y otros con horas de retraso. Este dato puede resultar incómodo a la hora de tratar con el, por lo que crearemos una nueva columna que nos convierta dicho tiempo a minutos.

![](images/tabla2.png)

## Representar los datos

Para representarlo, en el eje y tendremos los minutos, en orden descendente. Y en el eje x, los años que hemos analizado. 

![](images/tours.png)
