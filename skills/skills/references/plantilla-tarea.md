# Plantilla de skill de tarea (modo biblioteca)

Una skill por tarea. Corta y enfocada en un solo trabajo.

```markdown
---
name: <nombre-tarea>
description: <Qué produce, en una frase>. Úsala cuando <situaciones y palabras exactas que usa el usuario>. No la uses para <lo que hace otra skill parecida>.
---

# <Nombre de la tarea>

<Una frase: qué entrega y para quién.>

## Antes de empezar
Necesitas: <datos de entrada>. Si falta algo, pregunta. No lo inventes.

## Pasos
1. …
2. …
3. <Si envía, publica, elimina o paga:> Pide aprobación explícita antes de <acción>.

## Reglas
- <Regla del usuario, en imperativo.> <Motivo si no es obvio.>
- …

## Ejemplos

### Bien — <caso 1>
<Entrada breve> → <salida breve>

### Bien — <caso 2, distinto del primero>
<Entrada breve> → <salida breve>

### Mal — y por qué
<Salida incorrecta>
Por qué es malo: <qué regla rompe y qué habría corregido el usuario>.

## Antes de entregar
- [ ] <comprobación 1>
- [ ] <comprobación 2>
```

Y en la misma carpeta, `CHANGELOG.md` con la primera entrada (formato en
`bucle-aprendizaje.md`).

## Ejemplo de descripción buena y mala

- Mala: "Ayuda a escribir textos." → demasiado vaga, se activa con cualquier cosa.
- Buena: "Redacta la nota de prensa de un lanzamiento de Redder Labs a partir de las
  notas del producto. Úsala cuando el usuario diga 'nota de prensa', 'comunicado' o
  'enviar a medios'. No la uses para posts de redes sociales."

## Ejemplo de "mal ejemplo" útil

> **Mal:** "¡¡Estamos súper emocionados de anunciar nuestra increíble app!! 🚀🚀"
> Por qué es malo: el usuario siempre quita los emojis y las exclamaciones, y
> "increíble" no dice nada. Una nota de prensa empieza por el dato: qué es, para quién
> y desde cuándo está disponible.

Un mal ejemplo enseña cuando muestra **el error que el usuario corrige de verdad**, no
un error inventado que nadie cometería.
