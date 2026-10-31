# Motor de scroll y coreografía

Para webs cinematográficas. Es el patrón que usa SELENE, reescrito y probado: un solo
bucle de animación, cada escena calcula su progreso y escribe estilos directamente.

## Las cuatro reglas que lo sostienen todo

1. **Un solo bucle `requestAnimationFrame` para toda la página.** Lenis avanza primero y
   después cada escena se pinta. Nunca un segundo bucle ni una segunda librería de scroll.
2. **Nada de estado de React mientras se hace scroll.** Las escenas escriben `style`
   directamente sobre refs. React solo se usa para montar, y como mucho para cambios
   discretos (p. ej. "tramo 2 de 4"), nunca para valores continuos.
3. **Todo es aritmética sobre el progreso `p` (0–1).** Cada efecto es `lerp` + `span` +
   una curva. Sin GSAP ni librerías de animación: así cada número se puede leer y ajustar.
4. **Primero leer, luego escribir.** En cada frame, lee todas las posiciones que
   necesites y después escribe estilos. Si escribes un `transform` y luego llamas a
   `getBoundingClientRect()`, fuerzas al navegador a recalcular el diseño en cada frame
   (SELENE lo hace en su carrusel). Mejor: guarda las posiciones al cambiar el tamaño de la
   ventana y calcula el resto con aritmética.

## Archivos

Escríbelos antes que las secciones. Todas leen su progreso a través de ellos.

### `src/lib/math.ts`

```ts
/** Limita v entre min y max. */
export const clamp = (v: number, min = 0, max = 1) => Math.min(max, Math.max(min, v));

/** Interpola entre a y b según t (0–1). */
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

/** Dónde está v dentro del tramo [a, b], limitado a 0–1. Es la pieza básica de toda coreografía. */
export const span = (v: number, a: number, b: number) => clamp((v - a) / (b - a));

export const easeOut = (t: number) => 1 - Math.pow(1 - t, 3);
export const easeInOut = (t: number) => t * t * (3 - 2 * t);

/**
 * Progreso de una sección alta cuyo hijo es `position: sticky`:
 * 0 cuando su borde superior toca el de la pantalla, 1 justo antes de soltarse.
 */
export function stickyProgress(el: HTMLElement) {
  const rect = el.getBoundingClientRect();
  const vh = window.innerHeight;
  return {p: clamp(-rect.top / Math.max(1, rect.height - vh)), visible: rect.bottom > 0 && rect.top < vh};
}
```

### `src/lib/scroll.ts`

```ts
import Lenis from 'lenis';

/**
 * Un solo bucle requestAnimationFrame para toda la página.
 * Primero avanza Lenis y después cada escena lee su progreso y escribe estilos
 * directamente en el DOM. Nada pasa por el estado de React mientras se hace scroll.
 */

type Frame = (time: number) => void;

const frames = new Set<Frame>();
let lenis: Lenis | null = null;

export function startScroll(reducedMotion: boolean): () => void {
  // Con movimiento reducido no hay scroll suavizado: el navegador manda.
  lenis = reducedMotion ? null : new Lenis({lerp: 0.1, smoothWheel: true});
  let raf = 0;
  const tick = (time: number) => {
    lenis?.raf(time);
    frames.forEach((f) => f(time));
    raf = requestAnimationFrame(tick);
  };
  raf = requestAnimationFrame(tick);
  return () => {
    cancelAnimationFrame(raf);
    lenis?.destroy();
    lenis = null;
  };
}

export function onFrame(f: Frame): () => void {
  frames.add(f);
  return () => {
    frames.delete(f);
  };
}

/** Desplaza a un ancla (#seccion) o al principio (#top), con o sin Lenis. */
export function scrollToHash(hash: string) {
  const target = hash === '#top' ? 0 : document.querySelector<HTMLElement>(hash);
  if (target === null) return;
  if (lenis) lenis.scrollTo(target, {duration: 1.4});
  else if (typeof target === 'number') window.scrollTo({top: 0});
  else target.scrollIntoView();
  history.replaceState(null, '', hash === '#top' ? ' ' : hash);
}
```

### `src/hooks/useScene.ts`

```ts
import {useEffect, useRef, type RefObject} from 'react';
import {stickyProgress} from '../lib/math';
import {onFrame} from '../lib/scroll';

/**
 * Conecta una sección fijada al bucle de scroll. `render(p)` recibe el progreso
 * (0–1) y escribe estilos directamente. Solo se llama si la sección está en
 * pantalla y el progreso ha cambiado.
 *
 * Con movimiento reducido no se anima: se pinta una sola vez el fotograma de
 * reposo (`rest`), el instante que mejor resume la escena.
 */
export function useScene(
  ref: RefObject<HTMLElement | null>,
  render: (p: number) => void,
  {reduced = false, rest = 0.5}: {reduced?: boolean; rest?: number} = {},
) {
  const renderRef = useRef(render);
  renderRef.current = render;

  useEffect(() => {
    if (reduced) {
      renderRef.current(rest);
      return;
    }
    let last = -1;
    return onFrame(() => {
      const el = ref.current;
      if (!el) return;
      const {p, visible} = stickyProgress(el);
      if (!visible || Math.abs(p - last) < 1e-4) return;
      last = p;
      renderRef.current(p);
    });
  }, [ref, reduced, rest]);
}
```

### `src/hooks/useReducedMotion.ts`

```ts
import {useEffect, useState} from 'react';

const QUERY = '(prefers-reduced-motion: reduce)';

export function useReducedMotion() {
  const [reduced, setReduced] = useState(() => typeof window !== 'undefined' && window.matchMedia(QUERY).matches);
  useEffect(() => {
    const mq = window.matchMedia(QUERY);
    const update = () => setReduced(mq.matches);
    mq.addEventListener('change', update);
    return () => mq.removeEventListener('change', update);
  }, []);
  return reduced;
}
```

### `src/hooks/useReveals.ts` (apariciones suaves para secciones normales)

```ts
import {useEffect, useRef} from 'react';

/** Añade `.is-in` a cada `[data-reveal]` de la sección la primera vez que entra en pantalla. */
export function useReveals<T extends HTMLElement>() {
  const ref = useRef<T>(null);
  useEffect(() => {
    const root = ref.current;
    if (!root) return;
    const io = new IntersectionObserver(
      (entries) =>
        entries.forEach((e) => {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }),
      {rootMargin: '0px 0px -10% 0px'},
    );
    root.querySelectorAll('[data-reveal]').forEach((el) => io.observe(el));
    return () => io.disconnect();
  }, []);
  return ref;
}
```

CSS que lo acompaña:

```css
[data-reveal] {
  opacity: 0;
  transform: translate3d(0, 24px, 0);
  transition: opacity 1s cubic-bezier(0.2, 0.7, 0.1, 1), transform 1s cubic-bezier(0.2, 0.7, 0.1, 1);
}
[data-reveal].is-in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { [data-reveal] { transform: none; } }
body { overflow-x: clip; } /* red de seguridad contra el scroll horizontal */
```

### Arranque en `App.tsx`

```tsx
const reduced = useReducedMotion();
useEffect(() => startScroll(reduced), [reduced]);
```

Y en `main.tsx`, para que las escenas siempre empiecen arriba:

```ts
if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
```

## Plantilla de sección fijada

Una sección alta (`ALTO_SVH`) con un hijo `sticky` de una pantalla. Mientras la sección
pasa, el hijo se queda quieto y la escena avanza de 0 a 1.

```tsx
import {useRef} from 'react';
import {useReducedMotion} from '../hooks/useReducedMotion';
import {useScene} from '../hooks/useScene';
import {easeOut, lerp, span} from '../lib/math';

/**
 * Plantilla de sección fijada.
 *
 * Coreografía (p = progreso de la sección):
 *   0.00 – 0.30  el titular aparece y su espaciado se cierra
 *   0.20 – 0.70  la capa de fondo sube y se acerca
 *   0.80 – 1.00  todo sale hacia arriba y entrega a la sección siguiente
 *
 * Fotograma de reposo (movimiento reducido): 0.75, todo en su sitio.
 */
const ALTO_SVH = 300;

export function Escena() {
  const rootRef = useRef<HTMLElement>(null);
  const fondoRef = useRef<HTMLDivElement>(null);
  const tituloRef = useRef<HTMLHeadingElement>(null);
  const reduced = useReducedMotion();

  useScene(rootRef, (p) => {
    const salida = span(p, 0.8, 1);
    const entra = easeOut(span(p, 0, 0.3));
    const sube = easeOut(span(p, 0.2, 0.7));
    tituloRef.current!.style.opacity = String(entra * (1 - salida));
    tituloRef.current!.style.letterSpacing = `${lerp(0.4, 0.1, entra)}em`;
    fondoRef.current!.style.transform = `translate3d(0, ${lerp(20, 0, sube) - salida * 30}vh, 0) scale(${lerp(1.1, 1, sube)})`;
  }, {reduced, rest: 0.75});

  // Con movimiento reducido: el fotograma de reposo, quieto, y una sola pantalla de alto.
  return (
    <section ref={rootRef} aria-labelledby="escena-titulo" className="relative" style={{height: reduced ? '100svh' : `${ALTO_SVH}svh`}}>
      <div className="sticky top-0 h-[100svh] overflow-hidden">
        <div ref={fondoRef} className="absolute inset-0 will-change-transform" aria-hidden="true" />
        <h2 ref={tituloRef} id="escena-titulo" style={{opacity: 0}}>
          Titular
        </h2>
      </div>
    </section>
  );
}
```

## Coreografía

Antes de programar una escena, escribe su coreografía como comentario encima del
componente. Es el guion de la escena y el documento que se revisa con el cliente.

```
Coreografía (p = progreso de la sección):
  0.00 – 0.18  <qué pasa>                   [elemento]
  0.04 – 0.50  <qué pasa>                   [elemento]
  0.70 – 1.00  salida: entrega a la sección siguiente
Fotograma de reposo (movimiento reducido): <p>
```

Reglas:

- **Cada tramo tiene nombre y empieza y acaba en un número.** Los números van en
  constantes con comentario, no sueltos dentro del cálculo.
- **El orden importa y se comprueba.** Si una cosa tiene que terminar antes de que empiece
  otra (en SELENE, el polvo se despeja antes de que salga la Tierra), escríbelo como
  comprobación de calidad.
- **Como mucho 2–3 cosas a la vez.** Si todo se mueve, nada se ve.
- **Cada capa a su velocidad**: lo lejano se mueve poco y lo cercano mucho. Es lo que da
  profundidad sin 3D.
- **La salida entrega a la siguiente sección**: termina en el color de fondo de lo que
  viene después, para que no haya corte.
- **Alto de la sección: unos 80–100 svh por tramo principal.** SELENE usa 440 svh para cinco
  tramos. En móvil, si se hace largo, reduce el alto, no la coreografía.
- **Fotograma de reposo**: el instante que mejor resume la escena. Es lo que ve quien tiene
  activado el movimiento reducido, con la sección reducida a una pantalla de alto.
