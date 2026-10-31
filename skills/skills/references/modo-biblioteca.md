# Modo biblioteca

Encuentra las tareas que el usuario repite, convierte cada una en una skill probada y
sigue mejorándolas cada vez que te corrija.

Instalación, prueba y verificación final: secciones 4, 5 y 6 del `SKILL.md`.

## Paso 1 — Busca patrones antes de preguntar

Revisa lo que tengas a tu alcance, sin pedir permiso para leer:

- **Proyecto:** `CLAUDE.md`, `AGENTS.md`, README, skills que ya existan, scripts de
  `package.json` o `Makefile`, y el historial de git (`git log --oneline -100`) para ver
  qué tipos de cambio se repiten.
- **Conversaciones anteriores**, si tienes acceso al historial: peticiones parecidas,
  correcciones repetidas, instrucciones que el usuario pega una y otra vez.
- **Skills ya instaladas:** si una tarea ya tiene skill, se mejora esa en vez de crear otra.

## Paso 2 — Entrevista

**Máximo 6 preguntas, de una en una.** Espera la respuesta antes de la siguiente.
Sáltate las que ya sepas por el Paso 1.

1. ¿A qué te dedicas y en qué estás trabajando ahora?
2. ¿Para qué usas Claude cada semana? Dime las tareas, aunque sean pequeñas.
3. ¿Qué instrucciones le repites a Claude una y otra vez?
4. ¿Qué resultados siempre tienes que arreglar, y qué les cambias?
5. ¿Cómo es tu tono al escribir? Si puedes, pega un texto tuyo.
6. ¿Hay algo que Claude nunca deba hacer en tu trabajo?

Para cada tarea, intenta saber cuántas veces a la semana la haces y cuánto tardas. Lo
necesitarás al final para calcular las horas ahorradas.

## Paso 3 — Resumen y confirmación

Resume todo en esta tabla:

| Tarea | Frecuencia | Qué siempre corrijo | Prioridad (1–5) |
|---|---|---|---|
| … | 3 veces/semana, ~20 min | … | 5 |

Debajo, en una línea, lo que hayas deducido del tono del usuario.
**No continúes hasta que el usuario confirme la tabla.** Si cambia algo, actualízala y
vuelve a pedir confirmación.

## Paso 4 — Construcción

Para las **5 tareas de mayor prioridad**:

1. Si ya hay una skill que la cubre, mejórala (propón el diff y aplica tras el OK).
2. Si no, crea `.claude/skills/<nombre>/` con `SKILL.md` y `CHANGELOG.md` según
   `plantilla-tarea.md`. En la app de Claude, entrega un zip por skill.
3. Si la tarea es un oficio completo (p. ej. "programar apps", "escribir guiones"), no
   la conviertas en skill de tarea: asigna o crea un rol con `roles.md`.
4. Si una tarea envía, publica, elimina o paga algo, la skill debe pedir aprobación
   explícita antes de ese paso.

## Paso 5 — Prueba

Ejecuta cada skill en un caso real de la tabla, como dice la sección 5 del `SKILL.md`.
Muestra los cinco resultados con las dos columnas "Con la skill" y "A mano". Corrige
las skills, no las salidas.

## Paso 6 — Cierre

1. Haz la verificación final (sección 6 del `SKILL.md`) y termina con
   **PRÓXIMAS 3 HABILIDADES POR CONSTRUIR**.
2. Explica en dos líneas cómo activar el bucle de aprendizaje (ver
   `bucle-aprendizaje.md`, apartado "Para que funcione siempre").
