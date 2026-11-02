# Probar la skill web-premium

Guía para comprobar con una web de ejemplo que la skill funciona antes de usarla con un cliente.
Una prueba completa puede durar bastante y consume de tu uso normal.

## 1. Requisitos

- Claude Code con un plan de pago o acceso a la API.
- Git y Python 3 disponible como `python3`.
- Las skills de diseño de `references/skills-diseno.md`. Las imprescindibles son `impeccable`
  ([instrucciones](https://impeccable.style/docs/)) y `ui-ux-pro-max`.
- Claude Security. En el plan Pro, activa también Dynamic workflows en `/config`.

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
/plugin install claude-security@claude-plugins-official
/plugin marketplace add addyosmani/web-quality-skills
/plugin install web-quality-skills@addy-web-quality-skills
/plugin marketplace add alirezarezvani/claude-skills
/plugin install design-qa@claude-code-skills
```

`design-qa` necesita además Node 18 o superior.

## 2. Instalar la versión a probar

**Si el cambio ya está en `main`:**

```
/plugin marketplace update redder-roles
/plugin update desarrollo@redder-roles
```

Si `redder-roles` no está añadido, usa antes `/plugin marketplace add RedderLabs/Marketplace-inicial`
y después `/plugin install desarrollo@redder-roles`.

**Si todavía está en la rama `web-premium-equipo-diseno`:**

```
/plugin marketplace remove redder-roles
/plugin marketplace add RedderLabs/Marketplace-inicial#web-premium-equipo-diseno
/plugin install desarrollo@redder-roles
```

Quitar el marketplace desinstala sus plugins y borra sus datos. Al terminar, repite estos comandos
sin `#web-premium-equipo-diseno` para volver a `main`.

Reinicia Claude Code después de instalar.

## 3. Preparar la prueba

Usa una carpeta vacía, fuera de este repositorio:

```
mkdir prueba-web-premium
cd prueba-web-premium
git init
claude
```

## 4. Lanzar la prueba

**Invoca la skill con su nombre completo, `/desarrollo:web-premium`.** Si tienes otra copia en
`~/.claude/skills/web-premium`, `/web-premium` puede abrir esa y estarías probando otra cosa.

Pega este encargo. El negocio es inventado:

```
/desarrollo:web-premium Quiero una landing para Horno Alba, una panadería artesana de
Valencia. La acción principal es reservar pan para el fin de semana. Tono cálido y cuidado,
nivel de movimiento sobrio, solo en español, con tres secciones: portada, nuestro pan y
reservas. Sin textos ni fotos todavía. El formulario enviará los datos por correo y aún no
hay hosting. No despliegues nada.
```

## 5. Qué comprobar

Marca cada punto mientras avanza. Un fallo significa que hay que corregir la skill, no la web.

| Momento | Debe ocurrir |
|---|---|
| Arranque | Lee `references/skills-diseno.md` y avisa de las skills que falten. |
| Fase 0 | No vuelve a preguntar lo que ya dice el encargo y crea `PRODUCT.md`. |
| Fase 1 | Entrega concepto, momento y mapa de secciones, y **se detiene hasta tu OK**. |
| Fase 2 | Nombra una sola skill de estilo, explica por qué y crea `DESIGN.md`. |
| Fase 3 | Si no hay herramienta de imágenes, lo dice y sigue sin maquetas. |
| Fase 4 | Todo el texto está en `src/content.ts`, y lo que falta está marcado `[PENDIENTE]`. |
| Cada parte | Lanza Claude Security, o te pide que escribas el comando, antes de seguir con la siguiente. |
| Fase 5 | Ejecuta las revisiones de diseño, mide con `web-quality-skills`, comprueba con `design-qa`, pasa el checklist y dice qué no se cumple. |
| Entrega | Indica qué skills o revisiones faltaron y **no despliega nada**. |

Al terminar, ejecuta esto en la carpeta de la prueba:

```
grep -rnE "fonts\.googleapis|picsum\.photos|images\.unsplash" src index.html
grep -nE '"(gsap|motion|framer-motion|three)"' package.json
grep -n "CLAUDE-SECURITY" .gitignore
ls design-system
```

| Comando | Resultado correcto |
|---|---|
| Primer `grep` | Sin resultados: nada de fuentes o imágenes enlazadas. |
| Segundo `grep` | Sin resultados: nada de librerías de animación. |
| Tercer `grep` | Muestra una línea: el informe de seguridad no se sube al repositorio. |
| `ls design-system` | Error porque no existe: el diseño solo está en `DESIGN.md`. |

Para comprobar a ojo: abre la web a 390 y 1280 px. No debe haber scroll horizontal, y se debe
entender qué es y cómo reservar sin hacer scroll.

## 6. Anotar el resultado

Si algo falla, corrige la skill y repite la prueba desde el principio. Cuando pase, sustituye en
`CHANGELOG.md` la línea "Prueba: pendiente" por la fecha, el caso probado y el resultado.

## Problemas conocidos

- **Windows:** si `scripts` de `ui-ux-pro-max` es un archivo y no una carpeta, la búsqueda falla.
  Usa `src/ui-ux-pro-max/scripts/search.py` desde la raíz de ese plugin.
- **Propuestas de `ui-ux-pro-max`:** pueden no encajar con el negocio. Descartarlas es lo correcto.
- **Claude Security:** no está documentado que un agente pueda lanzarlo por su cuenta. Si te pide
  que escribas el comando, también es un resultado válido.
