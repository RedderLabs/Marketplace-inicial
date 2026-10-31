# Roles: qué skill de oficio asignar

## Regla: un solo rol, el más completo

Cada proyecto lleva **un único rol**: el más completo que cubra todo el proyecto.
Nunca se combinan dos roles. Si el proyecto mezcla partes, manda el rol que abarca más.

## Tabla de asignación

| Tipo de proyecto | Rol |
|---|---|
| Full-stack, SaaS, PWA (aunque tenga landing o web pública) | `ingeniero-software` |
| App móvil | `ingeniero-software` |
| API, backend, microservicio | `ingeniero-software` |
| CLI, scripts, automatización, bots | `ingeniero-software` |
| Librería o paquete | `ingeniero-software` |
| Juego | `ingeniero-software` |
| Solo web corporativa, landing, portfolio o tienda pequeña, sin aplicación detrás | `web-premium` |
| Guion, cortometraje, serie | `guionista` |
| Novela, relato | `novelista` |
| Análisis financiero, modelos, presupuestos | `analista-financiero` |

Si el proyecto no encaja en ninguna fila, elige el rol más completo de los que haya y
díselo al usuario, o propón crear uno nuevo.

## Si hay que crear un rol que no existe

Crea una carpeta `<rol>/` con un `SKILL.md` que siga esta estructura, sin presentarse
como "experto de prestigio", sino codificando cómo trabaja ese profesional:

```markdown
---
name: <rol>
description: <Qué hace este rol y cuándo usarlo, con palabras clave reales. Sin solaparse con otros roles.>
---

# <Rol>

<Dos o tres principios que guían sus decisiones.>

## Preguntas de arranque
## Proceso por fases (con entregable en cada fase)
## Estándares y checklist de calidad
## Errores de amateur que evita
## Autorrevisión final
```

- Menos de 300 líneas; lo extenso a `references/`.
- Los roles regulados (finanzas, legal, salud) se plantean como analista o asistente.
- Instálalo donde se instalan las skills (ver Paso 6) y añádelo a la tabla de arriba
  si el usuario mantiene un repositorio de roles.
