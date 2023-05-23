# Entrega Final IA
## Andrés Arango

### Presentación Básica del proyecto

##### La Fórmula 1 es la categoría más prestigiosa y de mayor nivel en el automovilismo de carreras. Se trata de un campeonato mundial de carreras de monoplazas, donde compiten equipos y pilotos de élite a bordo de vehículos de altas prestaciones y tecnología avanzada.

##### En la Fórmula 1, los monoplazas son diseñados y construidos por los equipos, siguiendo estrictas regulaciones técnicas establecidas por la Federación Internacional de Automovilismo (FIA). Estos vehículos son aerodinámicos y cuentan con motores potentes y sofisticados sistemas electrónicos. Además, están equipados con neumáticos de alto rendimiento que les permiten alcanzar velocidades extremadamente altas.

##### El campeonato de Fórmula 1 se compone de varias carreras, llamadas Grandes Premios, que se llevan a cabo en circuitos permanentes y urbanos alrededor del mundo. Cada temporada consta de múltiples carreras que se desarrollan en diferentes países.

##### Los equipos compiten tanto por el campeonato de constructores, que se otorga al equipo con más puntos acumulados durante la temporada, como por el campeonato de pilotos, que se concede al piloto que haya obtenido la mayor cantidad de puntos.

##### La Fórmula 1 es conocida por su intensidad y competitividad, con adelantamientos emocionantes, estrategias de carrera elaboradas y una constante búsqueda de la innovación tecnológica. Es seguida por millones de aficionados en todo el mundo y cuenta con una larga historia llena de leyendas y rivalidades entre pilotos y equipos.

##### A lo largo de los años surgen debates acerca de que piloto fue el que finalizó en que posición o que pilo según su equipo o nacionalidad podría obtener cierta cantidad de puntos en determinada carrera. 

## Los objetivos de este proyecto fueron:

+ Crear una aplicación web para poder predecir un piloto dependiendo de una serie de resultados, este puede ser un resultado pasado o  para un resultado a futuro 

+ Crear una aplicación web para poder predecir los puntos obtenidos por un piloto dependiendo de unos ajustes, este puede ser un resultado pasado o para un resultado a futuro 

## Documentación del archivo

### Features 

+ RacerId: Identificador de carrera, dentro de él sitio web se encuentra un índice con el nombre de la carrera y el código que se debe utilizar 

+ DriverId: Identifador de piloto, dentro de el sitio web se encuentra un índice con el nombre del piiloto y el código que se debe utilizar, este es exclusivo para la búsqueda de puntos 

+ ConstructorId: Identificador de constructor, dentro de él sitio web se encuentra un índice con el nombre de los constructores y el código que se debe utilizar

+ Grid: Valor en el que se almacena la posición de salida para el gran premio, se recomienda que el número ingresado esté dentro del rango de 1-20 porque para la mayoria de tuplas dentro de la base de datos están para las temporadas a partir del 2019 y este es el número de pilotos que participaron en esta temporada, adicionalmente, este es el número de pilotos que hay en la actual temporada, lo que para hacer predicciones se ajusta mejor para los resultados

+ Finish: Valor en el que se almacena la posición en la que finaliza la carrera, se recomienda que el número ingresado esté dentro del rango de 1-20, esto por las mismas razones del feature de Grid

+ Points: Valor en el que se almacenan los puntos obtenidos por el piloto en la carrera, estos se recomienda ingresar en el rango de 1-25, que son los puntos que se otorgan en la mayoría de carreras dento de la base de datos. Este es exclusivo del modelo para hallar/predecir el piloto 

+ laps: Valor en el que se almacenan las vueltas del gran premio, en caso de que tener dudas se puede ver en el índice de grandes premios

+ time_taken_in_millisec: Valor en el que se almacena el tiempo en el que se demora en hacer su vuelta rápida, se usan milisegundos por las mínimas diferencias que se presentan en el momento de hacer la vuelta más rápida de carrera

+ fastestLap: Vuelta en la que realiza la vuelta más rápida de carrera

+ max_speed: Velocidad máxima alcanzada en carrera

+ statusId: Status en que finalizó el gran premio, debido a la limpieza de datos el valor recomendado es 0, que según el índice es el de que finalizó la carrera

+ year: Año en el que se realiza la carrera

+ Age: Edad del piloto, se puede encontrar en el índice 

+ Nationality: Nacionalidad del piloto, se puede encontrar en el índice de nacionalidades 

#### Nota: En caso de desconocer el valor para la predicción se recomienda dejar la casilla en 0 para la búsqueda o predicción 
