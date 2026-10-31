# Prompts de un solo paso: analizar y crear

Un prompt de un solo paso (como SELENE) es un documento que cualquier IA de código puede
seguir para construir una web completa en una carpeta vacía. Sirve para dos cosas:
**aprender** de webs ajenas y **empaquetar** las tuyas (como plantilla, para venderla o
para rehacerla en otro proyecto).

## A. Plantilla de análisis

Cuando el usuario trae un prompt de referencia, responde estas preguntas:

1. **Concepto y momento.** ¿Qué es la web en una frase? ¿Cuál es la escena que se recuerda?
2. **Qué sostiene todo.** Las 2–4 decisiones que no se pueden tocar sin romperla
   (en SELENE: un solo bucle de scroll, capas cortadas de un render, trazado ligado al progreso).
3. **Coreografía.** Saca la tabla de tramos de cada escena (están en los comentarios y en
   los números de `span(p, a, b)`).
4. **Patrones usados**, con su número en `patrones-cinematicos.md`.
5. **Sistema de diseño.** Colores, fuentes y sus papeles, escala tipográfica.
6. **Stack y dependencias.** ¿Son exactas? (`^1.3.11` no es una versión exacta: sin
   `package-lock.json`, la reconstrucción no es idéntica aunque el prompt lo prometa).
7. **Assets.** ¿De dónde salen? ¿Con qué licencia? ¿Se pueden usar en un proyecto de cliente?
8. **Comprobaciones** que el prompt exige al terminar.
9. **Incoherencias y restos de plantilla.** Archivos que no se usan, comentarios que hablan
   de cosas que no existen, notas que no coinciden con el código. Indican que el prompt sale
   de un generador y que hay que limpiarlo antes de reutilizarlo.
10. **Problemas para usarlo en España/UE.** Fuentes enlazadas a Google, formularios sin
    consentimiento, textos en otro idioma.

Termina con: qué reutilizar (método), qué no (imágenes, textos, marca) y 2–3 ideas de webs
nuevas que usen el mismo método con otro momento.

## B. Estructura de un prompt nuevo

Usa estas secciones, en este orden. El orden importa: primero el porqué, después el qué.

```markdown
# <NOMBRE> — <frase de la web>

> Prompt de un solo paso para una IA de código. Pégalo entero en una carpeta vacía.

## Qué es este proyecto
<Un párrafo que cuenta la web como la vería un visitante: el momento, las secciones,
las fuentes y por qué.>

## Cómo funciona la página — léelo antes de tocar ningún número
<Las 2–4 decisiones que sostienen todo, con su motivo.>

Comprobaciones antes de darlo por terminado: <sin scroll horizontal a 390, 768, 1280 y
1920; el orden de las escenas que importa; etc.>

## Reglas
- Escribe cada archivo tal cual. No "mejores" textos, colores, tiempos ni medidas.
- No cambies librerías ni añadas archivos.
- Mantén todos los atributos de accesibilidad y las ramas de movimiento reducido.
- Mantén los comentarios: explican por qué cada número vale lo que vale.

## Stack (obligatorio)
<Lista + package.json con versiones exactas.>

## Assets
<Cómo obtenerlos: carpeta incluida o descarga única al principio. Nunca enlazados desde
la web final.>

## Pasos
1. Crear el proyecto y borrar lo que genere el asistente.
2. package.json e instalación.
3. Assets.
4. Configuración, CSS y content.ts.
5. lib/ y hooks/ antes que los componentes.
6. Componentes.
7. Releer "Cómo funciona" antes de tocar alturas o tramos.
8. Probar: scroll lento de arriba abajo, lint y build limpios.

## File: `<ruta>`
<contenido exacto de cada archivo>

## Notas de diseño (contexto, no instrucciones)
<Por qué se tomó cada decisión llamativa. Qué hay que cambiar antes de publicar.>
```

## C. Exportar una web hecha con esta skill

1. Escribe la cabecera (todo hasta "Pasos", incluido) en `PROMPT-cabecera.md` en la raíz del
   proyecto, siguiendo la estructura B.
2. Ejecuta desde la carpeta de la skill:

   ```bash
   python3 scripts/exportar-prompt.py <carpeta-del-proyecto> PROMPT.md
   ```

   El script añade una sección `## File:` por cada archivo del proyecto (HTML, configuración,
   `src/`), con el bloque de código en el lenguaje correcto, y las notas de diseño si
   existe `PROMPT-notas.md`. Ignora `node_modules`, `dist`, `public/`, el lockfile y archivos binarios.
3. Revisa el resultado: que no haya claves, correos personales ni URLs privadas.
4. Los assets de `public/` no van en el prompt: empaquétalos en un zip y explica en la
   sección Assets cómo obtenerlos.
