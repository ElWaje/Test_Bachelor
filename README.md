
# 🧪 Generador de Tests en PyQt5

Este proyecto es una aplicación de escritorio construida con **Python** y **PyQt5** que permite crear, organizar y realizar tests interactivos de forma visual. Está diseñado para docentes, estudiantes o cualquier persona que necesite gestionar cuestionarios organizados por secciones y temas.

---

## 🚀 Características Principales

- 📂 Organización por secciones y archivos `.json`
- ✅ Realización de tests con respuestas interactivas
- 📊 Estadísticas automáticas de rendimiento
- 🧠 Examen aleatorio de 20 preguntas
- 📝 Posibilidad de añadir nuevos tests o secciones

---

## 📸 Interfaz Visual

### 1. Pantalla principal
Desde aquí se accede a las secciones y tests disponibles:

![Menú principal](Menu_main.png)

---

### 2. Selección de sección
Selecciona la sección desde el desplegable para cargar sus tests:

![Selección de sección](Select_Subject%20.png)

---

### 3. Selección del test
Una vez seleccionada la sección, escoge el test específico:

![Selección de tema/test](Select_Issue%20.png)

---

### 4. Iniciar un test
Haz clic en "Hacer Test" para comenzar con las preguntas:

![Iniciar test](Make_Test.png)

---

### 5. Examen aleatorio de 20 preguntas
Puedes optar por un test mixto aleatorio de cualquier sección:

![Examen aleatorio](20_Question_Random.png)

---

### 6. Crear nueva sección
Crea una sección personalizada para organizar mejor los tests:

![Nueva sección](Create_New_Section.png)

---

### 7. Añadir un test
Agrega nuevos tests en formato `.json` a la sección actual:

![Añadir test](Add_Test.png)

---

### 8. Ver estadísticas
Consulta los resultados acumulados de tus tests:

![Estadísticas](Statistics.png)

---

## 🛠 Requisitos

- Python 3.7 o superior
- PyQt5
- python-docx (opcional si usas `.docx` como fuente)

```bash
pip install pyqt5 python-docx
```

---

## 📁 Estructura del proyecto

```
tests_json/
│
├── Sección1/
│   ├── Test1.json
│   └── Test2.json
├── Sección2/
│   └── Test3.json
results.json
Test_Generator.py
```

---

## 💬 Formato del archivo `.json`

Cada archivo de test debe tener la siguiente estructura:

```json
[
  {
    "question": "¿Cuál es la capital de España?",
    "options": {
      "A": "Madrid",
      "B": "Barcelona",
      "C": "Valencia",
      "D": "Sevilla"
    },
    "answer": "A"
  }
]
```

---

## 🧩 ¿Cómo empezar?

1. Clona el repositorio.
2. Ejecuta el archivo `Test_Generator.py`.
3. Añade tus propios tests o usa los de ejemplo.
4. ¡Haz un test y mejora tus conocimientos!

---

## 📬 Contribuciones

¡Se agradecen las sugerencias, correcciones y mejoras! Puedes abrir issues o enviar pull requests para contribuir al proyecto.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

> 📚 Aplicación diseñada con fines educativos para facilitar la evaluación autodidacta y reforzar el aprendizaje con estadísticas visuales.
