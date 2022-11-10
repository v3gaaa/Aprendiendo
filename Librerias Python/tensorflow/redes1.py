#TENSORFLOW NOS AYUDA A CREAR REDES NEURONALES QUE PODEMOS ENTRENAR APARTIR DE CODIGO
#LAS REDES NEURONALES SON PROGRAMAS QUE TIENEN ENTRADAS Y SALIDAS PERO NO TIENEN LOGICA NI ALGORTIMO. POR ESO LAS ENTRENAMOS PARA QUE TOMEN DECISIONES


import tensorflow as tf
import numpy as np

celsius = np.array([-40,-10,0,8,15,22,38],dtype=float)
fahr = np.array([-40,14,32,46,59,72,100],dtype=float)

#USAREMOS EL FRAMEWORK KERAS QUE NOS AYUDA CON LA CODIFICACION DE REDES NEURONALES DE MANERA MAS SIMPLE

#Las capas densas tienen conexiones entre todas las nueronas de entrada y todas las de salida
capa =tf.keras.layer.Dense(units=1, input_shape =1) #units = 1 por que solo tiene una neurona de salida, input_shape[1] nos autoregistra la capa de entrada con 1 neurona

#Las capas