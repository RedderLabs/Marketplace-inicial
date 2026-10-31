# Checklist de calidad antes de entregar

Marca cada punto. Si alguno no aplica, indica por qué. Si no se cumple, dilo en la entrega.

## Especificación
- [ ] La especificación está en el repositorio, aprobada y sin marcas `[POR ACLARAR]`.
- [ ] Cada requisito está comprobado con un test o una verificación manual anotada.
- [ ] Código y especificación coinciden: nada pedido sin hacer, nada hecho sin pedir.
- [ ] Las decisiones `(por defecto)` están comunicadas y la especificación marcada como `implementada`.

## Funcionalidad
- [ ] El flujo principal funciona de punta a punta.
- [ ] Todos los estados de UI existen: carga, vacío, error, éxito y sin conexión.
- [ ] Los formularios validan, muestran errores claros junto al campo y no pierden lo escrito.
- [ ] Las acciones destructivas piden confirmación o se pueden deshacer.

## Código
- [ ] Lint y comprobación de tipos sin errores ni avisos ignorados.
- [ ] Sin código muerto, `console.log` de depuración ni TODOs sin explicar.
- [ ] Nombres claros y estructura por dominio.
- [ ] Ningún secreto en el repositorio. Existe `.env.example`.

## Tests
- [ ] Tests unitarios de la lógica de negocio.
- [ ] Tests de integración de la API (casos correctos y de error).
- [ ] Al menos un test de extremo a extremo del flujo principal.
- [ ] Los tests pasan en CI, no solo en local.

## Seguridad
- [ ] Autenticación y autorización comprobadas en el servidor en cada endpoint.
- [ ] Entradas validadas con esquema. Consultas parametrizadas, sin SQL concatenado.
- [ ] Salida escapada para evitar XSS. Protección CSRF donde aplique.
- [ ] Contraseñas con hash robusto (argon2 o bcrypt). Tokens con caducidad.
- [ ] Cabeceras: CSP, HSTS, X-Content-Type-Options, Referrer-Policy.
- [ ] Límite de peticiones en login, registro y endpoints costosos.
- [ ] Dependencias sin vulnerabilidades conocidas graves.
- [ ] Datos personales: mínimos necesarios, cifrados donde toque, nunca en logs.

## Rendimiento
- [ ] Web: LCP < 2,5 s, INP < 200 ms y CLS < 0,1 en móvil.
- [ ] Imágenes en formato moderno, con dimensiones y carga diferida.
- [ ] Paquete JS dividido por rutas. Sin librerías enormes para tareas pequeñas.
- [ ] Consultas a BD sin N+1 y con índices.
- [ ] Listas largas paginadas o virtualizadas.

## Accesibilidad (WCAG 2.1 AA)
- [ ] Contraste suficiente (4,5:1 en texto normal).
- [ ] Todo usable con teclado y con foco visible.
- [ ] Etiquetas en formularios y textos alternativos en imágenes.
- [ ] Áreas táctiles de al menos 44×44 px en móvil.
- [ ] Respeta `prefers-reduced-motion` y el tamaño de letra del sistema.

## Operación
- [ ] CI con lint, tipos, tests y build.
- [ ] Despliegue reproducible y entornos separados.
- [ ] Copias de seguridad configuradas y restauración probada.
- [ ] Monitorización de errores y alerta de caída.
- [ ] README: qué es, arranque local, despliegue, decisiones (ADR) y dónde están las especificaciones.
