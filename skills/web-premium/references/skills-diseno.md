# Skills de diseño premium

`web-premium` dirige el proceso y usa estas skills como su equipo de especialistas. Invócalas:
no copies su contenido aquí ni lo resumas de memoria, porque se actualizan por su cuenta.

**Todas están disponibles, pero no todas a la vez.** En cada fase carga solo las indicadas: algunas
superan las 1.000 líneas y varias se contradicen entre sí. Una web premium tiene una sola dirección.

## El equipo

| Papel | Skill | Qué aporta |
|---|---|---|
| Dirección | `impeccable` | Decide la dirección visual y hace la revisión final de oficio. |
| Dirección | `frontend-design` | Asunto concreto y un único elemento memorable. |
| Dirección | `design-taste-frontend` | Lectura del brief, patrones de landing y control contra lo genérico. |
| Datos | `ui-ux-pro-max:ui-ux-pro-max` | Estilos, paletas, fuentes y normas de experiencia de usuario. |
| Estilo | `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `gpt-taste` | Lenguajes visuales; se elige **uno**. |
| Imagen | `imagegen-frontend-web`, `image-to-code` | Maquetas por sección y paso de imagen a código. |
| Marca | `brandkit` | Logotipo e identidad cuando el cliente no tiene. |
| Web existente | `redesign-existing-projects` | Auditoría y mejora sin rehacer desde cero. |
| Especialistas | `design:design-critique`, `design:accessibility-review`, `design:ux-copy`, `design:design-system`, `design:design-handoff` | Crítica, accesibilidad, textos de interfaz, sistema y traspaso. |
| Investigación | `design:user-research`, `design:research-synthesis` | Solo si hay que investigar o existen datos reales de usuarios. |
| Medición | `web-quality-skills:*` | Lighthouse, Core Web Vitals, rendimiento, accesibilidad, SEO y buenas prácticas, medidos. |
| Comprobación final | `design-qa` | Revisa la web ya renderizada: controles que no hacen nada, estados, foco, contraste y 320 px. |
| Guías | `references/externas/copywriting/GUIA.md`, `references/externas/site-architecture/GUIA.md` | Textos de venta por sección y estructura de páginas y URL. Se leen, no se invocan. |

## Qué usar en cada fase

| Fase | Siempre | Solo si hace falta |
|---|---|---|
| 0. Brief | `/impeccable init` guarda el producto en `PRODUCT.md`. | `redesign-existing-projects` si ya hay web. `brandkit` si no hay marca. `design:user-research` o `design:research-synthesis`. |
| 1. Concepto | `--design-system` de `ui-ux-pro-max` para contrastar con el sector. `frontend-design` y la lectura del brief de `design-taste-frontend`. `/impeccable shape <web>` decide la dirección. | La guía `site-architecture` si la web tiene varias páginas. |
| 2. Sistema de diseño | La skill de estilo elegida. `DESIGN.md` con la dirección aprobada. | `--domain color` y `--domain typography`. `design:design-system`. |
| 3. Imágenes | Los criterios de la Fase 3 de `SKILL.md`. | `imagegen-frontend-web` para maquetas por sección, si hay herramienta de generar imágenes. |
| 4. Construcción | Los mínimos de oficio de `impeccable`. Los patrones de `design-taste-frontend`. | `image-to-code` si se parte de maquetas. `/impeccable animate` u `overdrive` si el momento lo necesita. La guía `copywriting` para los textos de venta y `design:ux-copy` para botones y mensajes. `--domain ux` para dudas. |
| 5. Calidad | `/impeccable critique`, `audit` y `polish`. `design:design-critique`. `design:accessibility-review`. El "Pre-Delivery Checklist" de `ui-ux-pro-max`. `/web-quality-skills:web-quality-audit`, con `core-web-vitals` y `seo`. `design-qa` sobre la web en marcha. | — |
| 6. Entrega | `/impeccable document` si `DESIGN.md` no refleja lo entregado. | `design:design-handoff` si otro equipo seguirá con la web. |

Modo de `impeccable` según la página: landing, corporativa o lanzamiento son **Persuade**;
portfolio o galería, **Experience**; artículos o documentación, **Read**. No lances `/impeccable`
sin argumento: solo muestra un menú.

## Cómo elegir el estilo

Elige uno a partir del brief y de la dirección aprobada, nunca al azar:

| Web | Estilo |
|---|---|
| Lujo, inmobiliaria, agencia, tecnología premium | `high-end-visual-design` |
| Editorial, sobria, con mucho texto | `minimalist-ui` |
| Portfolio o marca técnica de carácter crudo, muchos datos | `industrial-brutalist-ui` |
| Lanzamiento o web cinematográfica | `gpt-taste`, solo para composición |

## Búsquedas de ui-ux-pro-max

- Usa el `scripts/search.py` de esa skill, siempre **sin `--persist`**. Si en Windows `scripts`
  es un archivo y no una carpeta, usa `src/ui-ux-pro-max/scripts/search.py` desde la raíz del plugin.
- Revisa cada resultado antes de usarlo. Descarta lo que no encaje con el negocio o la dirección,
  y cualquier estilo que el propio resultado marque con rendimiento o accesibilidad dudosos.

## Cómo encajan con el proceso

- **No repitas preguntas.** Pasa a cada skill lo que el usuario ya respondió.
- **Una sola fuente de verdad.** El producto va en `PRODUCT.md` y el diseño en `DESIGN.md`. No
  crees `design-system/MASTER.md`, porque competiría con ellos.
- **El OK de la Fase 1 sigue siendo obligatorio.** Muestra el mapa de secciones y la coreografía
  junto al brief de `shape`, y espera la aprobación antes de construir.

## Si dos instrucciones chocan

Manda lo primero de esta lista:

1. Lo que haya pedido el usuario en el brief, incluida su marca.
2. Las reglas de `web-premium`: RGPD, rendimiento, accesibilidad, motor de scroll y datos sin inventar.
3. La dirección y los criterios de `impeccable`.
4. La skill de estilo elegida.
5. El resto de skills y las recomendaciones de `ui-ux-pro-max`.

Choques que ya se conocen:

| Situación | Qué hacer |
|---|---|
| Piden GSAP, Motion o Three.js (`gpt-taste`, `design-taste-frontend`, `impeccable overdrive`) | Coge la idea y hazla con `references/motor-scroll.md`. Solo se añade la librería si el usuario la pide. |
| `design-taste-frontend` propone Next.js o shadcn/ui | El stack es el de la Fase 4, salvo que el brief diga otro. |
| `gpt-taste` o `high-end-visual-design` piden sortear el diseño | No se sortea, y no se simula ningún script de Python. Decide el brief. |
| Piden `picsum.photos` o Unsplash enlazado | Nunca en la entrega. Las imágenes son propias o con licencia clara, en `public/`. |
| `ui-ux-pro-max` propone enlaces a Google Fonts | Pueden servir si la licencia lo permite, pero descargadas y autoalojadas. |
| Una skill prohíbe una fuente que usa la marca del cliente (Inter, Roboto…) | Manda la marca. |
| `ui-ux-pro-max` dice que su único stack es React Native | No se aplica. |
| `ui-ux-pro-max` pide animar 150–300 ms y solo 1 o 2 elementos | Vale para botones y microinteracciones. Las escenas de scroll siguen su coreografía. |
| `design-taste-frontend` prohíbe dibujar SVG a mano | Vale para iconos. Los trazados narrativos sí se dibujan. |
| Piden logotipos de clientes, testimonios o cifras de ejemplo | Solo con datos confirmados. Lo que falte se marca `[PENDIENTE]`. |
| Las skills de imagen exigen generar imágenes y no hay herramienta para ello | Sáltalas, sigue con la dirección aprobada y dilo en la entrega. |
| Los ejemplos de `web-quality-skills` usan valoraciones (`AggregateRating`), Google Fonts o Next.js | Son solo ejemplos. Valoraciones únicamente si son reales y visibles en la página; fuentes autoalojadas; el stack es el de la Fase 4. |
| `web-quality-skills` y `design-qa` miden WCAG 2.2 | El mínimo sigue siendo 2.1 AA. Corrige lo que incumpla 2.1 AA y anota aparte lo que solo afecte a 2.2. |
| `design-qa` no detecta las marcas `[PENDIENTE]` | Búscalas a mano en `src/` antes de dar la web por terminada, y comunica las que queden. |
| `design-qa` necesita Playwright | Instálalo solo como dependencia de desarrollo. Si no se puede, usa su alternativa desde la consola del navegador y dilo en la entrega. |
| `copywriting` pide `.claude/product-marketing-context.md` | Usa `PRODUCT.md` y el brief. |
| `copywriting` pide puntuar titulares con su script | No se copió: solo acepta inglés y premia palabras de urgencia. Elige con sus principios. |
| `copywriting` propone urgencia, escasez o pruebas sociales | Solo si son ciertas y las confirma el cliente. Sin pruebas reales, marca `[PENDIENTE]`; no las inventes. |
| `site-architecture` propone silos o un análisis con `sitemap_analyzer.py` | Los silos, solo en webs con mucho contenido. El script no se copió. |

## Cuáles se quedan fuera

- `stitch-design-taste`: solo si el usuario trabaja con Google Stitch. Su `DESIGN.md` no sustituye al del proyecto.
- `design-taste-frontend-v1`: versión antigua de `design-taste-frontend`.
- `imagegen-frontend-mobile`: es para apps móviles.
- `kakulex-design` y `brand-guidelines`: son las marcas de Kakulex y de Anthropic.
- `theme-factory`: temas prefabricados, lo contrario de una dirección propia.
- `a11y-audit`: su documentación describe opciones que su script no tiene y no analiza archivos `.astro`.
- `seo-audit`, `schema-markup` y `meta-tags-optimizer`: los cubre `web-quality-skills:seo`. Instalarlas añadiría muchas skills más.
- `page-cro` y `form-cro`: dan por buenas pruebas sociales sin verificar, proponen ventanas emergentes y enriquecer formularios con terceros sin consentimiento.
- `local-seo-manager`: pensada para reparaciones en EE. UU., con afirmaciones comerciales fijas en sus scripts y riesgo de páginas de relleno.
- `epic-design`: carga GSAP desde un servidor externo.
- `webapp-testing`: `design-qa` ya cubre esta revisión, y sus scripts ejecutan comandos y escriben fuera del proyecto.

## Si falta alguna

Comprueba cuáles están disponibles antes de la Fase 0.

- **Imprescindibles: `impeccable` y `ui-ux-pro-max`.** Si falta alguna, dile al usuario cómo
  instalarla y deja que elija entre instalarla o seguir sin ella.
  - `ui-ux-pro-max`: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` y después
    `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`. Sus búsquedas necesitan Python 3.
  - `impeccable`: instrucciones en https://impeccable.style/docs/
- **El resto:** sigue sin ella y sustitúyela por los criterios de las demás. Las dos de medición se
  instalan así:
  - `web-quality-skills`: `/plugin marketplace add addyosmani/web-quality-skills` y después
    `/plugin install web-quality-skills@addy-web-quality-skills`.
  - `design-qa`: `/plugin marketplace add alirezarezvani/claude-skills` y después
    `/plugin install design-qa@claude-code-skills`. Necesita Python y Node 18 o superior.

Se revisaron leyéndolas, sin ejecutarlas, en los commits `afa8da9` (`web-quality-skills`) y `e4a1dc3`
(`design-qa`). Al instalarlas se recibe la última versión, que puede ser distinta.

Indica en la entrega qué skills y revisiones faltaron. **Nunca des por hecha una revisión que no
se ha ejecutado.**
