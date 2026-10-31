# Banco de preguntas

Elige de aquí según lo que falte. No hagas todas: ramifica. Entre corchetes, el valor
por defecto recomendado.

## Ronda 1 — Qué es (siempre)

1. ¿Qué vas a construir, en una frase, y para quién?
2. Tipo de proyecto: web/SaaS · PWA · app móvil · API/backend · CLI/script ·
   librería · juego · extensión · automatización/bots · otro
3. ¿Proyecto nuevo o existente? Si existe, ¿qué parte te preocupa más?
4. ¿Es un prototipo para validar o algo que irá a producción? [prototipo]

## Ronda 2 — Stack (ramificada)

**Web / SaaS / PWA**
- Framework [Next.js con TypeScript] · Estilos [Tailwind] · Componentes [shadcn/ui]
- ¿Renderizado en servidor o SPA? [servidor si hay SEO]
- ¿Necesita funcionar sin conexión? [no]

**App móvil**
- Plataformas [iOS y Android] · Tecnología [Expo/React Native] o Flutter o nativa
- ¿Offline, notificaciones push, cámara, ubicación, Bluetooth?

**API / backend**
- Lenguaje y framework [Node + Hono/Fastify, o Python + FastAPI]
- Estilo de API [REST] · Autenticación [sesiones o JWT con proveedor] · ¿Versionado?

**CLI / scripts / automatización**
- Lenguaje [Python o TypeScript] · ¿Se distribuye a otros o solo uso propio?

**Comunes**
- Base de datos [PostgreSQL; SQLite si es pequeño o local]
- Hosting / despliegue [Docker en servidor propio o plataforma gestionada]
- Gestor de paquetes [el que ya use el proyecto]

## Ronda 3 — Forma de trabajar

- Nivel de tests: ninguno (prototipo) · lógica de negocio [recomendado] · completo con e2e
- Estilo de código: ¿hay convenciones de nombres, idioma de los comentarios y de
  variables? [código en inglés, comentarios en español]
- Commits: ¿convención? [Conventional Commits] · ¿la IA puede hacer commits sola? [no]
- Cuánta autonomía: pregunta antes de cada cambio · avanza y resume al final [avanza y resume]
- ¿Diseño visual ya definido? (marca, colores, tipografía, referencias) [no]
- Privacidad y normativa: ¿datos personales, RGPD, cifrado? [RGPD básico si hay usuarios]

## Ronda 4 — Dominio y manías (siempre la última)

- Palabras propias del proyecto y qué significan (glosario corto).
- Reglas de negocio que no se pueden romper.
- **¿Qué te molesta que haga una IA cuando programa contigo?**
  Ejemplos para ayudar a responder: añadir dependencias sin preguntar, reescribir
  archivos enteros para un cambio pequeño, dejar `console.log`, inventar APIs,
  explicaciones largas, cambiar el estilo existente, no ejecutar los tests.
- ¿Algo que siempre quieras que haga? (p. ej. "ejecuta el lint antes de terminar").

## Cómo convertir respuestas en reglas

| Respuesta | Regla en la skill |
|---|---|
| "Odio que añada dependencias" | "No añadas dependencias sin preguntar. Propón la alternativa sin dependencia primero." |
| "Prototipo" | "Prioriza que funcione de punta a punta. Tests solo de la lógica crítica." |
| "Avanza y resume" | "No pidas confirmación para cambios dentro del alcance. Resume al final qué cambió." |
| "Código en inglés, comentarios en español" | Regla literal + ejemplo de función bien escrita. |
