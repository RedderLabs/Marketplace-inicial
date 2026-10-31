# Catálogo de patrones

Piezas para montar webs. Cada una: qué es, cuándo usarla, cómo se hace y qué vigilar.
Una web cinematográfica usa **un patrón estrella** (el momento) y 2–4 de apoyo. Todos se
apoyan en el motor de `motor-scroll.md`.

## 1. Escena por capas (parallax de un solo render)

**Qué es:** 4–6 imágenes apiladas y fijadas, cada una movida a su velocidad por el scroll.
Da sensación de profundidad sin 3D ni vídeo. Es el momento de SELENE.
**Cuándo:** un lugar o un producto que se puede "atravesar": paisaje, edificio, interior,
un objeto que se desmonta.
**Cómo:**

1. Genera o fotografía **una sola imagen** con todos los planos.
2. Recorta cada plano en su propia capa con máscara (cielo, objeto principal, plano medio,
   marco, figura, suelo) y rellena lo que queda detrás de cada objeto.
3. Exporta todas las capas al **mismo tamaño de lienzo**, una versión horizontal (`d`, p. ej.
   2688×1520) y otra vertical para móvil (`m`), en WebP. Mismo tamaño = siguen encajando.
4. Todas con el mismo `object-fit: cover` y `object-position`, y `<picture>` para elegir `d` o `m`.
5. Precarga solo la capa del fondo con `fetchpriority="high"`: es la imagen principal (LCP).
6. La capa más cercana lleva debajo un bloque del color de fondo de la página: cuando
   sube, llena la pantalla y entrega a la siguiente sección sin corte.

**Vigila:** el peso total (6 capas × 2 cortes) y que la escena no dure más de lo que aguanta
el móvil.

## 2. Velo o partículas sobre la lente

**Qué es:** un `<canvas>` 2D con motas que se despejan al empezar el scroll. Invita a bajar.
**Cómo:** canvas con `devicePixelRatio` limitado a 2, aleatorio con semilla (siempre igual),
deja de dibujar cuando su opacidad llega a 0. Con movimiento reducido, motas quietas.
**Vigila:** no taparlo todo sin mensaje. Encima del velo tiene que leerse qué es la web.

## 3. Titular que se enfoca

**Qué es:** el titular aparece con el espaciado entre letras abierto y desenfocado, y se
cierra hasta quedar nítido.
**Cómo:** `letterSpacing = lerp(0.6, 0.24, t)` y `filter: blur((1 - t) * 10px)`. Quita el
`filter` al llegar a 1, porque es caro de pintar.
**Vigila:** compensa el espaciado de la última letra con `margin-right` negativo para que
el titular quede centrado.

## 4. Telemetría ligada al scroll

**Qué es:** cifras en las esquinas (reloj, grados, kilómetros) que cambian con el progreso.
Da sensación de instrumento.
**Cómo:** `textContent` calculado desde `p`, tipografía mono con `tabular-nums` para que
los números no bailen, y `aria-hidden` porque es decoración.
**Vigila:** que las cifras signifiquen algo de la historia, no números al azar.

## 5. Trazado SVG que se dibuja con el scroll

**Qué es:** un recorrido (ruta, proceso, línea de tiempo) que se va dibujando por tramos,
con un objeto que viaja por el tramo activo y un contador que sube.
**Cómo:**

- Cada tramo es un `<path>` con `pathLength={1}`, `strokeDasharray="1 1"` y
  `strokeDashoffset = 1 - k`.
- Debajo, el recorrido completo en discontinuo y muy tenue: el visitante ve adónde va.
- El objeto viajero usa `path.getPointAtLength(path.getTotalLength() * k)`.
- El texto del tramo activo cambia con `setState` **solo cuando cambia el tramo**, nunca en
  cada frame, dentro de un bloque con `aria-live="polite"`.

**Cuándo:** procesos de un servicio, la historia de una empresa, un viaje o una entrega.

## 6. Carrusel horizontal fijado con foco

**Qué es:** la sección se fija y una fila de tarjetas se desliza de lado con el scroll. La
tarjeta más cercana a un punto focal está nítida y el resto se apaga.
**Cómo:** desplaza la fila con `translate3d`. Para el foco, calcula la posición de cada
tarjeta con su `offsetLeft` (guardado al cambiar el tamaño) menos el desplazamiento
actual, en vez de pedir `getBoundingClientRect()` después de mover la fila.
**Cuándo:** casos de éxito, fases, galería de proyectos, menú de un restaurante.
**Vigila:** en móvil, las tarjetas a un 70 % del ancho para que se vea que hay más.

## 7. Dato convertido en decoración

**Qué es:** el adorno de una tarjeta muestra un dato real. En SELENE, cada misión dibuja
un anillo de órbita por cada semana de duración.
**Cuándo:** planes, precios o productos que se comparan.
**Vigila:** que el dato también esté escrito; el dibujo es un apoyo.

## 8. Cuenta atrás

**Cómo:** un `setInterval` de 1 s en un hook propio, números con `tabular-nums`.
**Vigila:** no anuncies cada segundo a los lectores de pantalla: `aria-live="off"` y una
etiqueta con la fecha completa.

## 9. Formulario

- **Sin backend (`mailto:`):** solo para conceptos o webs personales. Abre el correo del
  visitante con el mensaje redactado.
- **Web de cliente real:** envío a un backend o servicio de formularios, validación en el
  servidor, casilla de consentimiento y enlace a la política de privacidad (RGPD).
- Siempre: etiquetas visibles, errores junto al campo y un mensaje de estado con `role="status"`.

## 10. Cierre que rima con el inicio

**Qué es:** el final recuerda al principio (en SELENE, un brillo de Tierra asomando bajo el
formulario). Cierra la historia y devuelve al momento.

## Qué patrón usar como momento

| Tipo de web | Momento recomendado |
|---|---|
| Turismo, hotel, inmobiliaria, arquitectura | Escena por capas |
| Producto físico o tecnológico | Escena por capas (producto que se separa) o trazado |
| Servicio con proceso (agencia, logística, salud) | Trazado SVG que se dibuja |
| Portfolio, estudio creativo | Carrusel fijado con foco |
| Evento o lanzamiento | Velo + titular que se enfoca + cuenta atrás |
