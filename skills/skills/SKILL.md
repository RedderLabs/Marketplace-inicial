---
name: skills
description: Crea, prueba y mejora skills a partir de entrevistas, para no tener que explicar lo mismo dos veces. Modo proyecto — al empezar un proyecto de programación genera una skill con su stack, reglas y rol. Modo biblioteca — detecta las tareas que el usuario repite y convierte las 5 principales en skills probadas. Modo mejora — cuando el usuario corrige un resultado, propone el cambio a la skill que debería haberlo evitado. Úsala cuando diga "configura el proyecto", "crea una skill", "convierte esto en una skill", "siempre te repito lo mismo", "mejora la skill" o corrija algo que una skill debería haber evitado.
---

# skills — crear, probar y mejorar skills

Objetivo: que el usuario nunca tenga que explicarle lo mismo dos veces a una IA.
Lo consigues guardando sus decisiones, reglas y correcciones en skills cortas,
probadas y que mejoran con cada corrección.

## 1. Elige el modo

| Situación | Modo | Lee antes de empezar |
|---|---|---|
| Empieza o configura un proyecto concreto | proyecto | `references/modo-proyecto.md` |
| Quiere convertir sus tareas repetitivas en skills | biblioteca | `references/modo-biblioteca.md` |
| Corrige un resultado o pide mejorar una skill | mejora | `references/bucle-aprendizaje.md` |

Si no está claro, haz una sola pregunta para decidir. Lee siempre el archivo del modo
antes de empezar y sigue también las reglas comunes de abajo.

## 2. Barreras de seguridad (siempre)

- **Ninguna skill puede enviar, publicar, eliminar o pagar nada sin aprobación explícita
  del usuario en ese momento.** Publicar incluye `git push`, desplegar, subir a una tienda,
  publicar en redes o mandar un correo. Si la tarea lo implica, la skill lleva un paso
  "Pide aprobación antes de…" justo antes de esa acción.
- **Nunca pongas contraseñas, claves API, tokens ni datos personales dentro de una skill.**
  Si hace falta una clave, la skill nombra la variable de entorno donde está, no su valor.
- **Si no sabes algo del trabajo del usuario, pregunta. No inventes** reglas, datos,
  nombres ni preferencias. Lo que no esté confirmado se marca `(por defecto)`.
- **Lenguaje plano, sin jerga**, tanto al hablar con el usuario como al escribir las skills.
  Si un término técnico es inevitable, explícalo en pocas palabras la primera vez.

## 3. Cómo se escribe una skill

- Frontmatter solo con `name` (kebab-case, igual que la carpeta) y `description`.
- La `description` dice **exactamente cuándo usarla**, con las palabras que el usuario
  usa de verdad. Si se parece a otra skill, añade cuándo **no** usarla.
- **Una skill, un solo trabajo.** Si hace dos cosas, divídela.
- Dentro: pasos en orden, reglas del usuario, **2 ejemplos buenos y 1 malo explicando
  por qué es malo** (plantillas en `references/plantilla-tarea.md` y
  `references/plantilla-skill.md`).
- Corta: cuanto menos, mejor; nunca más de 300 líneas. Plantillas o scripts en la
  misma carpeta **solo si de verdad hacen falta**.
- Cada carpeta lleva un `CHANGELOG.md`. La primera entrada se escribe al crearla.

## 4. Dónde se instala

- **Con acceso a los archivos del proyecto (Claude Code u otra herramienta de terminal):**
  `.claude/skills/<nombre>/` dentro del proyecto. Si el usuario la quiere para todos sus
  proyectos, `~/.claude/skills/<nombre>/`. Se carga en la siguiente sesión.
- **En la app de Claude:** genera la carpeta, empaquétala en `<nombre>.zip` (la carpeta en
  la raíz del zip) y entrégala. Se sube en los ajustes de skills.
- **Otra herramienta compatible con SKILL.md:** la carpeta donde esa herramienta lea las
  skills, o el zip si no lo sabes.
- Si ya existe una skill con ese nombre, no la sobrescribas: propón los cambios como en
  el modo mejora.

## 5. Prueba antes de dar nada por bueno

Cada skill nueva o modificada se prueba con **un caso real** del usuario:

1. Ejecuta la skill con ese caso.
2. Muestra el resultado junto a lo que el usuario habría hecho a mano (pídele un ejemplo
   suyo anterior o pregúntale qué habría hecho). Formato: dos columnas,
   "Con la skill" y "A mano".
3. Si hay que corregir algo, **corrige la skill, no la salida**, y vuelve a ejecutarla.
4. Anota la prueba y su resultado en el `CHANGELOG.md`.

## 6. Verificación final

Al terminar una sesión en la que se hayan creado skills (no en un cambio pequeño),
desafía tu propio trabajo y arregla lo que encuentres:

1. **¿Qué dos skills se solapan?** Fusiónalas o separa sus descripciones.
2. **¿Qué descripción es demasiado vaga para activarse bien?** Reescríbela con las palabras
   exactas que usa el usuario.
3. **¿Qué sigue explicando el usuario a mano?** Añádelo a una skill o apúntalo como candidata.
4. Comprobación técnica: `name` igual que la carpeta, frontmatter solo con `name` y
   `description`, sin secretos, `CHANGELOG.md` presente y enlaces a `references/` válidos.

Termina siempre con una sección titulada exactamente **PRÓXIMAS 3 HABILIDADES POR
CONSTRUIR**, ordenadas por horas ahorradas por semana. Para cada una: qué haría, cuántas
horas ahorra y cómo lo has calculado (veces por semana × minutos por vez).
