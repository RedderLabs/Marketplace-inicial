# Arquitectura: patrones y criterios de elección

## Elegir según el problema, no según la moda

| Necesidad | Opción por defecto | Cuándo cambiarla |
|---|---|---|
| App web con SEO y contenido | Framework con renderizado en servidor (p. ej. Next.js, Nuxt, SvelteKit, Astro) | App 100 % privada tras login → SPA basta |
| App web privada / dashboard | SPA o framework full-stack | — |
| App móvil sencilla o sin presupuesto para dos equipos | PWA | Necesitas notificaciones fiables en iOS, Bluetooth, segundo plano o tiendas → nativa o multiplataforma |
| App móvil multiplataforma | React Native / Expo o Flutter | Rendimiento gráfico extremo o APIs muy nativas → Swift/Kotlin |
| Base de datos | PostgreSQL | Datos claramente de documentos sin relaciones, o necesidad offline local → SQLite / IndexedDB con sincronización |
| Backend | Monolito modular | Equipos separados o partes con escalado muy distinto → servicios |
| Tareas largas | Cola de trabajos simple | — |
| Tiempo real | WebSockets o SSE | Pocas actualizaciones → polling |
| Autenticación | Proveedor probado o librería madura | Nunca implementes criptografía o sesiones desde cero |

## Monolito modular

Organiza por dominio, no por tipo técnico:

```
src/
├── modules/
│   ├── usuarios/     (rutas, servicio, repositorio, esquemas, tests)
│   ├── pedidos/
│   └── pagos/
├── shared/           (utilidades, tipos comunes, cliente de BD)
└── app/              (arranque, middleware, configuración)
```

Regla: un módulo solo accede a otro a través de su servicio público, nunca a sus tablas.
Así, si algún día hace falta separarlo, el corte ya está hecho.

## Offline-first (PWA y móvil)

- Guarda localmente lo que el usuario crea y sincroniza después.
- Cada registro con identificador generado en cliente (UUID) y marca de tiempo.
- Define la estrategia de conflictos antes de programar: último en escribir gana,
  fusión por campo o resolución manual.
- Muestra siempre el estado: guardado, pendiente de sincronizar, error.

## Modelo de datos

- Claves primarias UUID o ULID si hay sincronización o datos expuestos en URLs.
- `created_at` y `updated_at` en todas las tablas.
- Borrado lógico solo cuando haya motivo (auditoría, papelera). Si no, borrado real
  para cumplir con el RGPD.
- Índices para cada consulta frecuente. Revisa los planes de consulta lentos.
- Datos sensibles identificados desde el inicio: cifrado, acceso y retención.

## Plantilla de ADR (registro de decisión de arquitectura)

```
# ADR-001: <decisión>

Fecha: AAAA-MM-DD
Estado: propuesta | aceptada | sustituida por ADR-00X

## Contexto
Qué problema hay y qué restricciones lo condicionan.

## Decisión
Qué se ha decidido, en una o dos frases.

## Alternativas consideradas
- Opción A: por qué no.
- Opción B: por qué no.

## Consecuencias
Qué se gana, qué se pierde y qué habrá que vigilar.
```
