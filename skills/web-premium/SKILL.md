---
name: web-premium
description: Diseña y construye webs de presentación de alto nivel — landings, webs corporativas, portfolios, lanzamientos y webs con narrativa por scroll (capas en parallax, trazados SVG que se dibujan, secciones fijadas, coreografía) — y puede exportarlas como prompt de un solo paso. Úsala cuando el usuario pida una web, landing, portfolio, "web tipo Awwwards", "web con efectos de scroll", o quiera analizar o crear un prompt de web como SELENE. No es para aplicaciones con usuarios, datos o backend (eso es ingeniero-software).
---

# Web premium

Trabajas como el estudio que cobra +10.000 € por una web: lo que se paga no son los
efectos, es que la web tenga **una idea**, la cuente bien y funcione perfecta en
cualquier móvil.

Principios:

- **Un momento, no diez efectos.** Cada web tiene una escena que la gente recuerda
  (en SELENE: la Tierra saliendo por el horizonte de la Luna). Todo lo demás la sirve.
- **El movimiento cuenta algo.** Si un efecto no explica ni emociona, se quita.
- **Espectacular y rápida a la vez.** Si hay que elegir, gana la rapidez.
- **Todo el texto en un solo archivo de contenido**, nunca repartido por los componentes.

## Fase 0 — Brief

Pregunta lo que falte, como máximo 5 cosas a la vez y con un valor recomendado:

1. Qué presenta, para quién y cuál es la acción principal (reservar, comprar, contactar).
2. Tono y 2–3 webs de referencia que le gusten.
3. Nivel de movimiento: **sobria** (apariciones suaves) o **cinematográfica**
   (secciones fijadas con coreografía). [sobria si es un negocio local o hay mucho texto]
4. Idiomas y qué contenido existe ya (textos, fotos, logotipo).
5. Formulario: ¿adónde van los datos? (correo, CRM, backend propio).
6. Hosting y dominio.

Si el usuario trae un prompt o una web de referencia, ve antes a
**"Partir de un prompt de referencia"**.

## Fase 1 — Concepto

Entrega y espera el OK antes de construir:

1. **Concepto en una frase** y el **momento** de la web.
2. **Mapa de secciones** en una tabla: sección | qué cuenta | patrón | llamada a la acción.
   Los patrones están en `references/patrones-cinematicos.md`.
3. Si es cinematográfica: la **coreografía** de cada sección fijada, en tramos de
   scroll (formato en `references/motor-scroll.md`, apartado Coreografía).

## Fase 2 — Sistema de diseño

- Tokens en un bloque `@theme` (Tailwind v4) o variables CSS: colores, tipografía,
  escala con `clamp()`, radios y curvas de animación. Nada de valores sueltos.
- **Tres papeles tipográficos**: display (titulares, con carácter), texto (lectura) y
  mono (datos, etiquetas). Contraste comprobado: 4,5:1 en texto normal.
- **Fuentes autoalojadas** (archivos `woff2` en el proyecto). En webs para Europa no
  enlaces Google Fonts directamente: envía la IP del visitante a Google sin consentimiento
  y un tribunal alemán ya lo declaró contrario al RGPD.

## Fase 3 — Imágenes y assets

- Plan de imágenes: qué, tamaño, formato y corte para escritorio (`d`) y móvil (`m`).
- Capas para parallax: **cortadas de una sola imagen** para que encajen (cómo hacerlo en
  `references/patrones-cinematicos.md`).
- Imágenes propias, generadas para el proyecto o con licencia clara. **Nunca enlaces
  imágenes de otro servidor**: todo va en `public/` y se sirve desde el hosting del cliente.
- Peso objetivo: imagen principal ≤ 200 KB en móvil y página completa ≤ 3 MB.
  Formato WebP o AVIF.

## Fase 4 — Construcción

Stack por defecto:

- **Una sola página con mucha interacción:** Vite + React + TypeScript estricto + Tailwind v4,
  y Lenis solo si es cinematográfica. Sin GSAP ni librerías de animación: cada efecto es
  aritmética sobre el progreso del scroll.
- **Varias páginas y mucho contenido:** Astro + Tailwind v4, con islas interactivas solo
  donde haga falta.

Orden de trabajo:

1. `src/content.ts` con todo el texto (los textos que no te hayan dado, márcalos como
   `[PENDIENTE]`; no inventes datos, precios ni testimonios).
2. Tokens y CSS base.
3. El motor de scroll (`references/motor-scroll.md`) **antes** que las secciones.
4. Secciones de arriba abajo, cada una probada en móvil al terminarla.
5. Versión con movimiento reducido de cada sección.
6. SEO: título, descripción, Open Graph, `lang` correcto, `robots.txt` y `sitemap.xml`.

## Fase 5 — Control de calidad

Pasa `references/checklist-entrega.md` completo. Lo innegociable:

- Sin scroll horizontal a 390, 768, 1280 y 1920 px.
- Las escenas ocurren en el orden de la coreografía.
- Core Web Vitals en verde en móvil y WCAG 2.1 AA.
- Funciona con `prefers-reduced-motion`.

## Fase 6 — Entrega

- README: cómo arrancarla, cómo cambiar textos (solo `content.ts`) e imágenes, y cómo desplegar.
- **Pide aprobación explícita antes de desplegar o publicar.** Nunca pongas claves en el código.
- Opcional: **exportar la web como prompt de un solo paso** (formato SELENE) con
  `scripts/exportar-prompt.py`. Instrucciones en `references/plantilla-prompt.md`.

## Partir de un prompt de referencia

Cuando el usuario trae un prompt como SELENE o una web que le gusta:

1. **Analízalo** con la plantilla de análisis de `references/plantilla-prompt.md`:
   concepto y momento, qué partes sostienen todo, coreografía (saca la tabla de tramos),
   patrones usados, stack, origen y licencia de los assets, comprobaciones e incoherencias.
2. **No lo copies para un cliente.** Las imágenes, el texto y el diseño son de su autor.
   Lo reutilizable es el **método**: el motor, los patrones y la forma de coreografiar.
3. **Para crear una web nueva a partir de él:** concepto nuevo → momento nuevo → elige
   patrones del catálogo → coreografía nueva → mismo motor → imágenes propias.

## Errores de amateur que evitas

- Efectos sin historia, o todos a la vez.
- Secciones fijadas eternas: en móvil, más de ~100 svh por escena cansa.
- Actualizar estado de React en cada frame de scroll.
- Leer posiciones (`getBoundingClientRect`) después de escribir estilos en el mismo frame.
- Una primera pantalla sin mensaje ni llamada a la acción.
- Texto dentro de imágenes (no se traduce, no se indexa, no se lee con lector de pantalla).
- Google Fonts enlazadas en webs europeas. Imágenes enlazadas de otro servidor.
- Formularios sin destino real o sin aviso de privacidad.
- Olvidar `prefers-reduced-motion` o el scroll horizontal accidental en móvil.

## Autorrevisión final

1. ¿Se entiende qué es y qué hacer en los primeros 5 segundos, incluso sin hacer scroll?
2. ¿El momento de la web funciona en un móvil de gama media?
3. ¿He pasado el checklist completo? ¿Qué no cumple y por qué?
4. ¿Hay algún texto, dato o imagen inventado que el cliente no haya confirmado? Márcalo.
