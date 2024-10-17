import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Configuraciones básicas
image_size = (224, 224)  # Tamaño de las imágenes (ancho x alto)
batch_size = 32
num_classes = len(os.listdir("dataset"))  # Número de clases, basado en las carpetas en tu dataset

# Generador de imágenes con aumento de datos
train_datagen = ImageDataGenerator(
    rescale=1./255,           # Normalización
    rotation_range=20,        # Rotación aleatoria
    width_shift_range=0.2,    # Desplazamiento horizontal
    height_shift_range=0.2,   # Desplazamiento vertical
    shear_range=0.2,          # Corte aleatorio
    zoom_range=0.2,           # Zoom aleatorio
    horizontal_flip=True,     # Volteo horizontal
    fill_mode='nearest',      # Completar huecos con píxeles cercanos
    validation_split=0.2      # Separación para validación
)

# Cargar las imágenes de entrenamiento y validación
train_generator = train_datagen.flow_from_directory(
    'dataset',                # Ruta al dataset
    target_size=image_size,    # Tamaño de las imágenes
    batch_size=batch_size,
    class_mode='categorical',  # Salida categórica para clasificación
    subset='training'          # Subconjunto de entrenamiento
)

validation_generator = train_datagen.flow_from_directory(
    'dataset',
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'        # Subconjunto de validación
)

# Definir el modelo CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], 3)),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),  # Para evitar sobreajuste
    Dense(num_classes, activation='softmax')  # Capa final con el número de clases
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Mostrar un resumen del modelo
model.summary()
