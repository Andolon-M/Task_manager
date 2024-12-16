1. Estructura del Proyecto
Usaremos un diseño modular, separando la lógica de la aplicación, el manejo de datos y la interfaz:

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
│   ├── gui_view.py       # (Opcional) Interfaz gráfica.
├── utils/
│   ├── __init__.py       # Inicialización del módulo.
│   ├── file_manager.py   # Manejo de exportación/importación de tareas.
├── requirements.txt      # Dependencias del proyecto.
└── README.md             # Documentación del proyecto.
```




2. Instalación de Dependencias
Primero, asegurémonos de tener SQLAlchemy instalado. Además, instalaremos otras herramientas necesarias si usamos interfaces gráficas.

```
pip install sqlalchemy
```

