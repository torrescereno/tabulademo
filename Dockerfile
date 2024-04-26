# Usa una imagen base de OpenJDK
FROM openjdk:11

# Instala Python
RUN apt-get update && apt-get install -y python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en el contenedor
WORKDIR /code

# Copia el archivo de requisitos primero para aprovechar la cache de Docker
COPY ./requirements.txt /code/requirements.txt

# Instala las dependencias de Python
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia el resto de la aplicación
COPY ./app /code/app

# Comando para correr la aplicación usando uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

