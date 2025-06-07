
# 🧪 Generador de Tests en PyQt5

Aplicación de escritorio **Python + PyQt5** para crear, organizar y realizar tests interactivos.  
Ideal para docentes, estudiantes, opositores o cualquier persona que quiera gestionar cuestionarios y ver su evolución gráfica.

---

## 🚀 Características Principales

- 📂 Organización por secciones/asignaturas y tests en archivos `.json`
- ✅ Tests interactivos con revisión de respuestas y revisión visual final
- 📊 Estadísticas automáticas de rendimiento, evolución diaria y por tipo (¡con gráficos!)
- 📈 Gráficas de puntuación y barras comparativas con línea de tendencia y colores por nota
- 📋 Tabla de resultados por examen (colores según porcentaje)
- 🧠 Examen aleatorio de 20 preguntas por sección/asignatura
- 🔀 Examen de 40 preguntas por mitad de temas (primera/segunda mitad)
- 📝 Añadir tests o secciones personalizados fácilmente
- 📤 Exportar resultados a CSV desde la propia app
- 🖼 Fondo de menú configurable y visualmente atractivo
- 👆 Multi-idioma y preparado para ampliar funcionalidades

---

## 🖼 Fondo Visual del Menú

Pantalla principal con fondo personalizado, elegante y con espacio central claro para menús legibles:

![Fondo de menú](fondo.png)

---

## 📸 Interfaz Visual

### 1. Menú principal y navegación

Desde aquí accedes a las secciones, puedes crear nuevas y gestionar tus tests:

![Menú principal](Menu_main.png)

---

### 2. Selección de sección

Escoge la sección/asignatura desde el desplegable para cargar sus tests:

![Selección de sección](Select_Subject%20.png)

---

### 3. Selección de test

Elige el test que quieras realizar:

![Selección de tema/test](Select_Issue%20.png)

---

### 4. Iniciar un test

Haz clic en "Hacer Test" para comenzar con las preguntas:

![Iniciar test](Make_Test.png)

---

### 5. Examen aleatorio de 20 preguntas

Ahora puedes lanzar un examen aleatorio SOLO de la sección/asignatura seleccionada:

![Examen aleatorio](20_Question_Random.png)

---

### 6. Examen de 40 preguntas (primera y segunda mitad)

Puedes lanzar un examen solo de la 1ª o 2ª mitad de temas para practicar por bloques:

**Primera mitad:**  
![Examen 40 primera mitad](40_Question_Random_Middle_1.png)

**Segunda mitad:**  
![Examen 40 segunda mitad](40_Question_Random_Middle_2.png)

---

### 7. Crear nueva sección

Organiza tus tests creando nuevas secciones:

![Nueva sección](Create_New_Section.png)

---

### 8. Añadir un test

Agrega tests en formato `.json` en la sección actual:

![Añadir test](Add_Test.png)

---

### 9. Resultados y revisión visual

Consulta los resultados y revisa todas las respuestas, viendo correctas y falladas:

![Correctas](Corrects.png)  
![Preguntas](Questions.png)  
![Resultados](Results.png)

---

### 10. Estadísticas

Consulta los resultados acumulados y evolución gráfica de tus tests:

**Panel clásico:**  
![Estadísticas](Statistics.png)

---

## 📊 Estadísticas Visuales Mejoradas

- **Tabla de resultados diaria y por tipo, coloreada según nota:**
- **Gráficas de evolución temporal** con línea de tendencia.
- **Gráficas de barras** por tipo de test.
- **Exporta todo a CSV** con un solo clic.

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
fondo.png
...
```

---

## 💬 Formato del archivo `.json`

Cada test sigue este esquema:

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

## 🛠 Requisitos

- Python 3.7 o superior
- PyQt5
- python-docx (opcional si usas `.docx`)
- matplotlib y numpy (para estadísticas avanzadas)

```bash
pip install pyqt5 python-docx matplotlib numpy
```

---

## 🧩 ¿Cómo empezar?

1. Clona el repositorio.
2. Ejecuta el archivo `Test_Generator.py`
3. Añade tus propios tests o usa los de ejemplo.
4. Haz un test, revisa las estadísticas y exporta los resultados.

---

## ✨ Novedades y ampliaciones

- Fondo visual con `fondo.png` personalizable y espacio central difuminado
- Estadísticas por fecha y tipo de test (gráficas embebidas con colores por nota)
- Exportación directa de resultados a CSV
- Tabla de resultados diaria visual
- Modos: 20 aleatorias por sección, 40 por mitad de temas, revisión gráfica
- Preparado para integración futura en web o APK

---

## 📬 Contribuciones

¡Se agradecen sugerencias, correcciones y mejoras!  
Puedes abrir issues o pull requests.

---

## 📄 Licencia

MIT.

---

> 📚 Aplicación diseñada con fines educativos para facilitar la evaluación autodidacta y reforzar el aprendizaje con estadísticas visuales.
