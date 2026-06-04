# Simulador de Memoria de Trabajo: Hipergrafos vs Grafos Binarios

Este proyecto es una simulación experimental bioinspirada desarrollada como núcleo práctico de la tesis de maestría titulada **"Representación hipergráfica para la preservación de relaciones N-arias en la memoria de trabajo de arquitecturas cognitivas bioinspiradas"**, realizada por **Juan Daniel Pedraza Díaz**. 

Esta investigación forma parte activa del proyecto de **Cuāyōllōtl**, dirigido por el **Dr. Félix Francisco Ramos Corchado**.

Su propósito central es comparar matemáticamente la eficiencia de retención cognitiva utilizando dos paradigmas de representación estructural: **Grafos Binarios** (tradicionales) y **Hipergrafos**.

---

## 🧠 1. Conceptos Base del Experimento

Para comprender la simulación a la perfección, primero debemos definir qué representan los términos clave que utilizamos:

### ¿Qué es el "Contexto"?
El contexto es el conjunto íntegro de elementos (entidades) que participan en una situación o evento de la vida real. Por ejemplo, en la situación *"Juan estudia Matemáticas con el Profesor en el Aula"*, el **contexto completo** está formado por: `{Juan, Matemáticas, Profesor, Aula}`. El objetivo de una memoria de trabajo eficiente es lograr recordar todas estas piezas al mismo tiempo, sin olvidar ninguna (sin fragmentarse).

### ¿Qué es un "Estímulo"?
El estímulo es la "chispa inicial" o la pista que desencadena el recuerdo. Imagina que te preguntan: *"¿Qué sabes de Juan?"*. En ese momento, **"Juan" es el estímulo**. 
En nuestro programa (`experiment.py`), forzamos esto explícitamente diciendo que todo siempre arranca desde el mismo punto: `stimulus = "Juan"`. A esta entidad le inyectamos artificialmente una energía matemática inicial de `1.0`. A partir de ahí, observamos si el sistema tiene la fuerza suficiente para recordar (activar) al resto del contexto (Matemáticas, Profesor, Aula).

---

## ⚙️ 2. El Motor de Activación Único (Rigor Científico)

Una decisión crucial de este simulador es que **ambos modelos (Grafos e Hipergrafos) son sometidos a exactamente el mismo Motor de Activación** (`activation_engine.py`). 

* **¿Qué implica esto?** Significa que el algoritmo que calcula cómo viaja la energía es ciego a si está usando un grafo binario o un hipergrafo. Se aplica la misma regla matemática para ambos.
* **¿Qué hubiese pasado si no fuera así?** Si hubiésemos escrito un algoritmo de activación especial para hipergrafos y otro distinto para grafos binarios, el experimento perdería validez. Cualquier diferencia en los resultados podría atribuirse a que un código estaba "mejor optimizado" que el otro. Al usar un motor único, garantizamos que la **única variable** responsable del éxito o fracaso es la estructura (topología) matemática que subyace a la representación.

---

## 🌊 3. ¿Cómo fluye la energía y qué es el "Efecto Abanico"?

Cuando decimos que *"la activación de la memoria fluye hacia los nodos conectados"*, nos referimos a cómo la energía inicial del estímulo (`1.0` en "Juan") viaja a través de la red (las líneas que unen las palabras) multiplicándose por un factor de pérdida de señal (el `decay` o decaimiento temporal).

Pero, **¿cómo se divide esta energía?** El programa utiliza un concepto real de la psicología cognitiva llamado **Efecto Abanico (Fan Effect)**: la fuerza de la señal que un nodo envía a sus vecinos se divide matemáticamente por el número de conexiones salientes que tiene. 

Aquí radica el corazón lógico del experimento:

#### En el Grafo Binario:
La regla estricta de un grafo binario es que **solo puede unir dos cosas a la vez**. Para representar que Juan, las Matemáticas, el Profesor y el Aula estaban juntos en un mismo evento, el grafo nos obliga a dibujar múltiples líneas independientes simulando pares: 
* Juan está conectado a Matemáticas.
* Juan está conectado al Profesor.
* Juan está conectado al Aula.

Esto causa que "Juan" termine teniendo **muchas conexiones independientes**. Según nuestro motor, si Juan tiene 4 conexiones (aristas), la energía de `1.0` que intenta enviar por cada hilo para despertar a sus vecinos **se divide entre 4 (`1.0 / 4`)**. Si aumenta la complejidad a 10 elementos, la energía se divide entre 10. *Consecuencia: La señal se vuelve tan débil que no logra despertar al resto del contexto.*

#### En el Hipergrafo:
Un hipergrafo no une pares; utiliza un "saco" (hiperarista) que envuelve a todo el grupo de elementos como un evento único e indivisible. 
"Juan" se conecta a **una sola hiperarista** (la escena en sí misma). Por tanto, cuando "Juan" dispara su energía, su número de conexiones (abanico) es **1**. 
La energía (`1.0 / 1`) viaja casi intacta hacia la hiperarista, y esta actúa como un difusor holístico que irradia toda esa energía de golpe al resto del contexto. *Consecuencia: La memoria no sufre penalización por complejidad.*

---

## 📚 4. Los Escenarios de Estudio (E1 a E4)

Para probar matemáticamente que el grafo binario colapsa ante la complejidad mientras que el hipergrafo la resiste, diseñamos 4 escenarios de prueba de **complejidad relacional creciente** (fenómeno conocido matemáticamente como "Aridad"). 

* **E1 (Aridad 2):** *"Juan estudia Matemáticas"*.
  * *Entidades:* `{Juan, Matemáticas}`.
  * *Por qué se usa:* Es el caso base de control. Una relación simple de par donde ambos modelos (Binario e Hipergrafo) deberían comportarse de manera muy similar y sin errores cognitivos.
* **E2 (Aridad 3):** *"Juan estudia Matemáticas con un Profesor"*.
  * *Entidades:* `{Juan, Matemáticas, Profesor}`.
  * *Por qué se usa:* Comienza a probar la capacidad del sistema de mantener unido un trinomio (sujeto-acción-compañía) sin que se pierda una de las partes al evocar el recuerdo.
* **E3 (Aridad 4):** *"Juan estudia Matemáticas con un Profesor en el Aula 5"*.
  * *Entidades:* `{Juan, Matemáticas, Profesor, Aula 5}`.
  * *Por qué se usa:* Introduce contexto espacial profundo. Aquí la red binaria se vuelve densa y el "Efecto Abanico" obliga a dividir la energía severamente, marcando el punto de quiebre donde la memoria convencional empieza a fallar.
* **E4 (Aridad 5 - El Caso Crítico y Límite Biológico):** *"Juan estudia Matemáticas con el Profesor García en el Aula 5 usando Álgebra Moderna"*.
  * *Entidades:* `{Juan, Matemáticas, Profesor García, Aula 5, Álgebra Moderna}`.
  * *Por qué se usa:* Este límite de 5 entidades no es arbitrario. La psicología cognitiva y las neurociencias (apoyándose en los estudios de Nelson Cowan sobre el límite de *4±1 chunks*) demuestran que la capacidad máxima de la memoria de trabajo humana ronda los 5 elementos de información simultáneos. Al forzar la aridad a 5, sometemos a la arquitectura a operar exactamente en el umbral biológico máximo del cerebro humano para observar si la representación hipergráfica resiste sin fragmentarse.

---

## 📊 5. Diccionario de Variables del Sistema

* **`decay` (Decaimiento):** Factor de pérdida temporal. Varía aleatoriamente entre `[0.85, 0.95]`. Simula que, biológicamente, una señal eléctrica no viaja perfectamente, sino que pierde entre el 5% y 15% de su fuerza.
* **`threshold` (Umbral = 0.5):** La activación mínima requerida para considerar que una palabra del contexto fue exitosamente recuperada ("recordada"). Si tras propagar la señal matemática, "Aula" termina con una energía de `0.49`, significa que no lograste recordarlo.
* **`seed` (Semilla = 42):** La semilla ancla la aleatoriedad. Si bien el `decay` es un número al azar en cada paso, usar una semilla fija hace que ese "azar" sea exactamente el mismo cada vez que aprietas Play. Esto permite que la tesis sea **100% reproducible** matemáticamente por otros investigadores.
* **`iterations` (100 iteraciones):** Se corre la simulación de cada escenario 100 veces. Al haber un decaimiento aleatorio (ruido), una sola ejecución podría dar resultados engañosos. Al hacerlo 100 veces, calculamos un **promedio estadístico robusto** que aplana el ruido e indica la verdadera tendencia estructural.

---

## 📈 6. Cómo Analizar los Resultados (Las Gráficas)

En la carpeta `outputs/` observarás gráficas de barras comparando el Grafo Binario (Azul) con el Hipergrafo (Naranja) a lo largo de 4 escenarios (E1 a E4). A medida que avanzamos hacia E4, **aumenta la aridad**, es decir, agregamos más entidades a la escena.

### Preservación Contextual y Precisión
* **Qué evaluar:** Estas barras indican qué tan bien se recordó el evento original. 
* **Lectura:** Notarás que en E1 y E2 (situaciones simples), la barra azul compite. Pero al llegar a **E3 y E4**, la barra azul se desploma drásticamente, mientras que la naranja (Hipergrafo) se mantiene alta e inmutable. 
* **Significado:** El modelo binario colapsa bajo el peso de la complejidad porque fragmenta las relaciones (el Efecto Abanico diluyó la energía). El Hipergrafo demuestra ser la estructura ideal para retener escenas multivariables complejas en la memoria de trabajo.

### Fragmentación
* **Qué evaluar:** Mide los fallos. El porcentaje de veces que la memoria se rompió y no pudo traer el recuerdo completo.
* **Lectura:** Aquí ocurre lo inverso; las barras azules suben velozmente al llegar a E4, demostrando una alta tasa de error cognitivo (fragmentación relacional). Las barras naranjas se mantienen casi en cero.

---

## 🚀 7. Instrucciones de Ejecución

Para replicar este experimento en cualquier computadora, sigue estos pasos:

1. **Abre una terminal** (Símbolo del sistema, PowerShell o Bash) y navega a la carpeta del proyecto.
2. **Instala las dependencias estadísticas** (Pandas y Matplotlib) ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecuta la simulación** corriendo el script principal:
   ```bash
   python main.py
   ```
Una vez que finalice, la terminal te confirmará la creación de la carpeta `outputs/`. Allí no solo encontrarás los datos crudos y las gráficas, sino también una tabla estadística preprocesada (`summary_stats.csv`) y un reporte de texto (`summary_report.txt`) diseñados para que copies los promedios directos a tu tesis.

---

## 📁 8. Estructura del Código Fuente

El código fue diseñado modularmente para mantener el rigor académico sin utilizar librerías de "Caja Negra" (Black Box) de Inteligencia Artificial.

```text
wm-hypergraph-thesis/
│
├── scenarios/
│   └── definitions.py          # Define las escenas (E1 a E4) y sus topologías.
│
├── src/
│   ├── entities/               # Clases base (Nodos).
│   ├── graph/                  # Matemáticas de Grafo Binario (fragmentación en pares).
│   ├── hypergraph/             # Matemáticas de Hipergrafo (agrupamiento en hiperaristas).
│   ├── memory/                 # El Motor de Activación y el 'Efecto Abanico'.
│   ├── metrics/                # Fórmulas de evaluación (Precisión, Fragmentación).
│   ├── simulation/             # Controlador lógico de las 100 iteraciones.
│   └── visualization/          # Generador visual de gráficas con Matplotlib.
│
├── main.py                     # Punto de entrada para iniciar la simulación.
└── requirements.txt            # Dependencias.
```
