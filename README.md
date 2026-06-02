# YGOSearch

YGOSearch es una aplicación web para buscar y consultar cartas de Yu-Gi-Oh!.

El proyecto permite realizar búsquedas de cartas, visualizar información básica de cada una y consultar detalles como nombre, tipo, descripción, atributos o imágenes.

## Índice

- [Descripción](#descripción)
- [Funcionalidades principales](#funcionalidades-principales)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Modelo funcional](#modelo-funcional)
- [Configuración](#configuración)
- [Ejecución del proyecto](#ejecución-del-proyecto)
- [Uso de la aplicación](#uso-de-la-aplicación)
- [Capturas](#capturas)
- [Posibles mejoras](#posibles-mejoras)

## Descripción

YGOSearch es una aplicación orientada a la búsqueda de cartas de Yu-Gi-Oh!.

La aplicación permite consultar cartas a partir de un buscador y mostrar los resultados de forma visual. Cada resultado contiene información relevante de la carta, como su nombre, imagen, tipo y descripción.

El proyecto está planteado como una aplicación sencilla para practicar el consumo de datos externos, la creación de una interfaz de búsqueda y la presentación de resultados al usuario.

## Funcionalidades principales

- Búsqueda de cartas por nombre.
- Visualización de resultados.
- Consulta de información básica de cada carta.
- Visualización de imágenes de las cartas.
- Presentación ordenada de los datos obtenidos.
- Manejo básico de resultados vacíos o errores de búsqueda.

## Tecnologías utilizadas

- HTML
- CSS
- JavaScript
- API externa de cartas de Yu-Gi-Oh!

## Estructura del proyecto

Ejemplo de estructura general del proyecto:

```text
YGOSearch
├── index.html
├── css
│   └── style.css
├── js
│   └── script.js
└── assets
    └── ...
```

La estructura puede variar según la organización final del proyecto.

## Modelo funcional

El funcionamiento básico de la aplicación es el siguiente:

1. El usuario introduce el nombre de una carta en el buscador.
2. La aplicación realiza una consulta a una API externa.
3. Se reciben los datos de las cartas encontradas.
4. La aplicación muestra los resultados en pantalla.
5. El usuario puede consultar la información de cada carta.

## Datos mostrados

La aplicación puede mostrar información como:

```text
Nombre de la carta
Tipo de carta
Descripción
Atributo
Nivel o rango
Ataque
Defensa
Imagen
```

Los campos disponibles dependen de la información recibida desde la API utilizada.

## Configuración

No es necesaria una configuración compleja para ejecutar el proyecto.

En caso de utilizar una API externa, la URL de consulta se encuentra normalmente dentro del archivo JavaScript principal.

Ejemplo:

```javascript
const API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php";
```

## Ejecución del proyecto

Para clonar el repositorio:

```bash
git clone https://github.com/l-rivas-v95/YGOSearch.git
```

Entrar en la carpeta del proyecto:

```bash
cd YGOSearch
```

Abrir el archivo principal en el navegador:

```text
index.html
```

También puede ejecutarse con una extensión como Live Server en Visual Studio Code.

## Uso de la aplicación

Ejemplo de uso básico:

```text
1. Abrir la aplicación en el navegador.
2. Escribir el nombre de una carta.
3. Pulsar el botón de búsqueda.
4. Revisar los resultados mostrados.
5. Consultar la información de la carta deseada.
```

Ejemplo de búsqueda:

```text
Dark Magician
Blue-Eyes White Dragon
Kuriboh
Exodia
```

## Capturas

Pendiente de añadir capturas de la aplicación.

Capturas recomendadas:

```text
- Pantalla principal
- Buscador
- Resultados de búsqueda
- Detalle de una carta
- Mensaje cuando no hay resultados
```

## Posibles mejoras

- Añadir filtros por tipo de carta.
- Añadir filtros por atributo.
- Añadir filtros por raza o arquetipo.
- Añadir ordenación de resultados.
- Mejorar la visualización en dispositivos móviles.
- Añadir paginación o carga progresiva.
- Añadir favoritos.
- Guardar búsquedas recientes.
- Mostrar mensajes de error más claros.
- Añadir una pantalla de detalle para cada carta.
- Mejorar el diseño visual de las cartas.
