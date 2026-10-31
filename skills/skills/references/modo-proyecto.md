# Modo proyecto

Convierte una conversación corta en una skill que haga que cualquier sesión trabaje en
este proyecto como si ya lo conociera. No describe a un "experto genérico": recoge
decisiones concretas de este proyecto y de este usuario.

Instalación, prueba y verificación final: secciones 4, 5 y 6 del `SKILL.md`.

## Paso 1 — Mira antes de preguntar

Si hay acceso a los archivos, revisa primero lo que exista para no preguntar lo que ya
se puede saber:

- Manifiestos: `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pubspec.yaml`, `composer.json`…
- Configuración: linters, formateadores, `tsconfig`, Docker, CI, `.env.example`.
- Estructura de carpetas y 2–3 archivos representativos para ver el estilo real.
- README, `CLAUDE.md`, `AGENTS.md` y skills que ya existan en `.claude/skills/`.

Resume en 3–5 líneas lo que has detectado y pide solo confirmación de eso.
Si no hay proyecto todavía, empieza directamente por la entrevista.

## Paso 2 — Entrevista adaptativa

Sigue el banco de preguntas de `preguntas.md`. Reglas:

- **Rondas de 3–4 preguntas como máximo.** Cada una con opciones y un valor por defecto
  recomendado, para que se pueda responder con "lo que recomiendes".
- **Ramifica según las respuestas.** App móvil → plataformas y offline. API →
  autenticación y versionado. Sin frontend → no preguntes por diseño.
- **No preguntes lo que ya sabes** por el Paso 1 o por respuestas anteriores.
- **Máximo 4 rondas.** Lo que quede sin responder usa el valor por defecto y se marca
  `(por defecto)`.
- Si el usuario dice "empieza ya" o "lo que veas", cierra la entrevista.

En la última ronda pregunta siempre: **"¿Qué te molesta que haga una IA cuando
programa contigo?"** Las respuestas se convierten en reglas explícitas.

## Paso 3 — Asignar rol

Elige la skill de rol que aporta el oficio profesional, con la tabla de `roles.md`.

1. **Un solo rol: el más completo que cubra todo el proyecto.** Nunca dos. Si el
   proyecto tiene varias partes (p. ej. una app con landing de marketing), elige el rol
   que abarca más, aquí `ingeniero-software`, y no añadas otro para la parte pequeña.
2. **Comprueba si está instalado** (`.claude/skills/`, `~/.claude/skills/` o la lista de
   skills disponibles de la sesión).
   - Si está: se enlaza desde la skill del proyecto.
   - Si no: avisa y ofrece instalarlo desde su repo de roles, crearlo ahora con la
     estructura de `roles.md`, o seguir sin rol.
3. **No repitas el rol.** La skill del proyecto solo añade lo propio del proyecto y las
   excepciones que el usuario haya pedido.

## Paso 4 — Propuesta

Antes de escribir nada, muestra:

1. **Nombre**: kebab-case con el nombre del proyecto (p. ej. `proyecto-colmenas`).
2. **Descripción**: debe nombrar el proyecto y sus palabras clave para activarse solo en él.
3. **Rol asignado** y si está instalado.
4. **Resumen** de las decisiones en una lista breve.

Pide confirmación en una sola pregunta. Si corrige algo, ajústalo sin repetir la entrevista.

## Paso 5 — Generación

Sigue `plantilla-skill.md`:

```
<nombre>/
├── SKILL.md              (reglas y proceso)
├── CHANGELOG.md
└── references/           (solo si hace falta)
    ├── arquitectura.md   (modelo de datos, módulos, API)
    ├── estilo.md         (convenciones de código con ejemplos bien/mal)
    └── diseno.md         (tokens, colores, tipografía, componentes)
```

- Imperativo y concreto: "Usa Zod para validar en el borde", no "se recomienda validar".
- Cada regla con su motivo en pocas palabras cuando no sea obvio.
- Ejemplos cortos de código bien y mal, sacados del estilo real del proyecto.
- Nada que el modelo ya haga bien por defecto. Solo lo propio de este proyecto.

## Paso 6 — Prueba

Pide una tarea pequeña y real del proyecto (p. ej. "añade un campo al formulario de
cosechas") y comprueba que la skill se activa y se respetan sus reglas. Sigue la
sección 5 del `SKILL.md`.

## Paso 7 — Actualización

Si el usuario pide actualizar la skill de un proyecto:

1. Lee la skill actual.
2. Pregunta solo qué ha cambiado, en una ronda.
3. Revisa las marcadas `(por defecto)` por si ya hay decisión.
4. Si el tipo de proyecto ha cambiado, revisa si el rol sigue siendo el adecuado.
5. Propón los cambios como diff y aplica tras confirmar (ver `bucle-aprendizaje.md`).
