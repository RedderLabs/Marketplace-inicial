# Checklist de entrega

Marca cada punto. Si no aplica, di por qué. Si no se cumple, dilo en la entrega.

## Mensaje
- [ ] En la primera pantalla, sin hacer scroll, se entiende qué es y hay una llamada a la acción.
- [ ] Todo el texto está en `src/content.ts`. Lo que falte está marcado `[PENDIENTE]`.
- [ ] Ningún dato, precio, cliente o testimonio inventado.

## Movimiento
- [ ] Las escenas ocurren en el orden de la coreografía (comprueba los pares que importan:
      "X termina antes de que empiece Y").
- [ ] En cada carrusel con foco, la tarjeta del punto focal es siempre la nítida.
- [ ] Un solo bucle de animación. Ningún `setState` en cada frame.
- [ ] Con `prefers-reduced-motion`: sin scroll suavizado, escenas en su fotograma de reposo
      y secciones fijadas de una pantalla de alto.
- [ ] Probado con scroll lento de arriba abajo en un móvil real o emulado.

## Diseño responsive
- [ ] Sin scroll horizontal a 390, 768, 1280 y 1920 px.
- [ ] Cortes de imagen `d` y `m` correctos. Nada importante tapado por la cabecera.
- [ ] Menú móvil usable con teclado, con `aria-expanded` y el resto de la página `inert`.

## Rendimiento
- [ ] LCP < 2,5 s, INP < 200 ms y CLS < 0,1 en móvil.
- [ ] La imagen principal precargada con `fetchpriority="high"` y ≤ 200 KB en móvil.
- [ ] Imágenes en WebP o AVIF, con `width`, `height`, `loading="lazy"` fuera de la primera pantalla.
- [ ] Página completa ≤ 3 MB.
- [ ] `will-change` solo en lo que de verdad se mueve.

## Accesibilidad (WCAG 2.1 AA)
- [ ] Contraste 4,5:1 en texto normal, también sobre imágenes.
- [ ] Un `h1` y jerarquía de títulos correcta. Cada sección con `aria-labelledby`.
- [ ] Imágenes decorativas con `alt=""` y `aria-hidden`; las que informan, con `alt` útil.
- [ ] Foco visible en todo lo interactivo. Formularios con etiquetas visibles.

## Privacidad y legal (España / UE)
- [ ] Fuentes autoalojadas: ninguna petición a Google Fonts ni a otros servidores sin consentimiento.
- [ ] Imágenes y assets en el propio hosting. Ninguno enlazado de servidores ajenos.
- [ ] Licencia clara de cada imagen, fuente y vídeo.
- [ ] Si hay formulario: consentimiento, política de privacidad y destino real de los datos.
- [ ] Aviso legal y, si hay cookies no esenciales, banner de consentimiento.

## Revisión de diseño
- [ ] `/impeccable critique`, `audit` y `polish` ejecutados, sin problemas graves abiertos.
- [ ] `design:design-critique` y `design:accessibility-review` ejecutados.
- [ ] `/web-quality-skills:web-quality-audit` ejecutado sobre la web en marcha, con los resultados medidos anotados.
- [ ] `design-qa` ejecutado sobre la web en marcha. Marcas `[PENDIENTE]` buscadas a mano y comunicadas.
- [ ] "Pre-Delivery Checklist" de ui-ux-pro-max pasado.
- [ ] Una sola dirección y una sola skill de estilo. Sin librerías de animación que el usuario no haya pedido.
- [ ] `PRODUCT.md` y `DESIGN.md` coinciden con lo entregado. No existe `design-system/MASTER.md`.

## Seguridad
- [ ] Claude Security ejecutado al terminar cada parte, sin hallazgos graves abiertos ni falsas alarmas sin justificar.

## SEO
- [ ] `lang` correcto, `<title>` y `meta description` propios.
- [ ] Open Graph y Twitter Card con imagen de 1200×630.
- [ ] `robots.txt`, `sitemap.xml` y URL canónica.
- [ ] El texto está en el HTML, no dentro de imágenes ni de canvas.

## Código
- [ ] `tsc --noEmit` y `build` sin errores.
- [ ] Sin archivos ni dependencias que no se usen.
- [ ] Versiones exactas en `package.json` y `package-lock.json` en el repositorio.
