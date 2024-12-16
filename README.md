# Task Manager

## Descripción

**Task Manager** es una aplicación desarrollada en Python para gestionar tareas diarias. Los usuarios pueden agregar, listar, completar, eliminar tareas y exportarlas en formato JSON. La aplicación cuenta con dos interfaces disponibles: una interfaz de línea de comandos (CLI) y una interfaz gráfica (GUI) utilizando Tkinter. Además, se conecta a una base de datos PostgreSQL para persistencia de datos.

---

## Características

1. **Agregar Tareas**: Permite a los usuarios agregar nuevas tareas con un título y una descripción.
2. **Listar Tareas**: Muestra todas las tareas con su estado (pendiente o completada).
3. **Completar Tareas**: Permite marcar una tarea como completada.
4. **Eliminar Tareas**: Permite eliminar todas las tareas completadas.
5. **Exportar Tareas**: Exporta todas las tareas a un archivo JSON.
6. **Interfaz Dual**:
   - **CLI**: Para usuarios que prefieren la línea de comandos.
   - **GUI**: Interfaz gráfica amigable desarrollada con Tkinter.
7. **Conexión a PostgreSQL**: Almacena las tareas en una base de datos PostgreSQL para garantizar la persistencia.

---

## Dependencias

El proyecto utiliza las siguientes dependencias:

- **Python 3.8+**
- **Tkinter** (incluido con Python)
- **SQLAlchemy** (para la gestión de la base de datos)
- **psycopg2** (para la conexión con PostgreSQL)

Instalarlas con:

```bash
pip install -r requirements.txt
```

Contenido del archivo `requirements.txt`:

```
sqlalchemy
tk
psycopg2
```

---

## Estructura del Proyecto 

```
task_manager/
├── app.py                # Punto de entrada principal.
├── models/
│   ├── __init__.py       # Inicialización del módulo.
│   ├── database.py       # Configuración de la base de datos (SQLAlchemy).
│   ├── task.py           # Modelo para las tareas.
├── controllers/
│   ├── __init__.py       # Inicialización del módulo.
│   ├── task_controller.py # Controladores para la lógica de tareas.
├── views/
│   ├── __init__.py       # Inicialización del módulo.
│   ├── cli_view.py       # Interfaz de línea de comandos.
│   ├── gui_view.py       # Interfaz gráfica.
├── utils/
│   ├── __init__.py       # Inicialización del módulo.
│   ├── file_manager.py   # Manejo de exportación/importación de tareas.
├── requirements.txt      # Dependencias del proyecto.
└── README.md             # Documentación del proyecto.
```

---

## Configuración y Ejecución

### 1. Clonar el Repositorio

Clona el repositorio a tu máquina local:

```bash
git clone https://github.com/Andolon-M/Task_manager.git
cd task_manager
```

### 2. Configurar la Base de Datos

Asegúrate de tener un servidor posgres sql y colocar la url de coneccion en el archivo models/database.py

### 3. Instalar Dependencias

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación

- Para la interfaz de línea de comandos (CLI):

  ```bash
  python app.py
  ```

  Selecciona la opción `1` en el menú.

- Para la interfaz gráfica (GUI):

  ```bash
  python app.py
  ```

  Selecciona la opción `2` en el menú.

---

## Uso

### Interfaz de Línea de Comandos (CLI)

1. Agregar Tarea: Ingresa el título y descripción.
2. Listar Tareas: Muestra todas las tareas.
3. Completar Tarea: Proporciona el ID de la tarea.
4. Eliminar Tareas Completadas: Limpia las tareas completadas.
5. Exportar Tareas: Genera un archivo `tasks.json` en la carpeta del proyecto.

### Interfaz Gráfica (GUI)

- Usa los botones para agregar, completar, eliminar tareas o exportarlas.

---

## Exportar Tareas

El archivo `tasks.json` se genera en la raíz del proyecto con la estructura:

```json
[
  {
    "id": 1,
    "title": "Sample Task",
    "description": "This is a sample task.",
    "completed": false
  }
]
```

---




