# Stack: dónde montar los agentes

Elige lo más simple que encaje con lo que el usuario ya usa. Si duda, empieza por la
primera fila que le sirva.

| Opción | Cuándo | Memoria y contexto |
|---|---|---|
| **Claude Code con subagentes** (`.claude/agents/*.md`) y skills | El usuario ya trabaja en Claude Code y el flujo lo lanza una persona | Archivos del repo (`docs/`, `CLAUDE.md`, JSON de estado); cada subagente lee solo lo que necesita |
| **Claude Code programado** (rutinas o tareas en la nube) | El flujo se repite con horario fijo y no necesita servidor propio | Igual que arriba, más el historial de cada ejecución |
| **n8n o Make + API de Claude** | El flujo empieza en otras apps (correo, formularios, CRM) y el usuario no programa | Tablas de la propia herramienta, Google Sheets o Airtable |
| **Claude Agent SDK** (Python o TypeScript) | Hace falta lógica propia, integraciones a medida o un producto | Base de datos (Postgres/SQLite) para estado; archivos para contexto. Construir con `ingeniero-software` |

## Reglas

- **Memoria** = lo que debe sobrevivir entre ejecuciones (casos procesados, decisiones,
  preferencias). Guárdala en un sitio que el usuario pueda leer y corregir.
- **Contexto** = lo que un agente lee al empezar. Lo mínimo: su system prompt, la entrada
  y las referencias fijas (tarifas, guía de estilo). Nunca el historial completo de todo.
- Claves y tokens en variables de entorno o en el gestor de secretos de la herramienta,
  nunca en prompts ni en archivos del repo.
- Registra cada ejecución: entrada, salida, modelo, tokens, coste y duración. Sin
  registro no hay medición.
