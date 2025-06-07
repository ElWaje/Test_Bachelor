
# 🧪 Generador de Tests en PyQt5

Aplicación de escritorio **Python + PyQt5** para crear, organizar y realizar tests interactivos.  
Ahora con estadísticas visuales, fondo personalizado y nuevos modos de examen.  
Ideal para docentes, estudiantes, opositores o cualquier persona que quiera gestionar cuestionarios y ver su evolución gráfica.

---

## 🚀 Características Principales

- 📂 Organización por secciones y archivos `.json`
- ✅ Realización de tests con respuestas interactivas y revisión al final
- 📊 Estadísticas automáticas de rendimiento, evolución diaria y por tipo
- 📈 Gráficas de puntuación y barras comparativas (con línea de tendencia)
- 📋 Tabla de resultados por examen, coloreada según nota
- 🧠 Examen aleatorio de 20 preguntas por sección/asignatura
- 🔀 Examen de 40 preguntas por mitad de temas (primera/segunda)
- 📝 Añadir tests o secciones personalizados fácilmente
- 📤 Exportar resultados a CSV
- 🖼 Fondo de menú configurable, visual y elegante (ver abajo)

---

## 🖼 Fondo Visual de Menú

Pantalla principal con fondo personalizado para que los menús sean fáciles de leer y la experiencia más pro:

![Fondo de menú](fondo.png)

---

## 📸 Capturas de la Interfaz

### Examen 40 preguntas (primera mitad)
![Examen 40 primera mitad](40_Question_Random_Middle_1.png)

### Examen 40 preguntas (segunda mitad)
![Examen 40 segunda mitad](40_Question_Random_Middle_2.png)

### Preguntas correctas y resultados
![Correctas](Corrects.png)
![Preguntas](Questions.png)
![Resultados](Results.png)

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
```

---

## 💬 Formato de archivo `.json`

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
2. Asegúrate de tener Python 3.7+ y dependencias instaladas:
   ```bash
   pip install pyqt5 python-docx matplotlib numpy
   ```
3. Ejecuta `Test_Generator.py`
4. Añade tus propios tests (o usa los de ejemplo).
5. ¡Haz un test, revisa las estadísticas y exporta resultados!

---

## ✨ Novedades 2025

- Fondo visual con `fondo.png` personalizable
- Estadísticas por fecha y tipo de test (con gráficos)
- Exportación directa a CSV
- Tabla visual con color por nota
- Modos avanzados: 20 aleatorias, 40 por mitad de temas
- Revisión de respuestas correctas vs. seleccionadas

---

## 📬 Contribuciones

¡Sugerencias, correcciones y mejoras son bienvenidas!  
Abre issues o pull requests.

---

## 📄 Licencia

MIT.

---

> 💡 *Este programa es para fines educativos, refuerzo y autoevaluación. Si fallas, ¡la culpa es del bot!*
