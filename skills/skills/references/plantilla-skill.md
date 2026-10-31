# Plantilla de la skill generada

Rellena solo las secciones con contenido real. Borra las que no apliquen.

```markdown
---
name: <nombre-proyecto>
description: Contexto, reglas y convenciones del proyecto <Nombre> (<qué es en pocas palabras>). Úsala siempre que se trabaje en el código, el diseño o la arquitectura de <Nombre>, o se mencione <palabras clave del proyecto>.
---

# <Nombre>

<Una frase: qué es y para quién.> Fase: <prototipo | producción>.

## Rol
- Aplica la skill `<rol>` para el proceso, los estándares y el checklist. Es el único rol de este proyecto.
- Excepciones a ese rol en este proyecto: <p. ej. "sin tests e2e mientras sea prototipo">.
- Si una regla de este proyecto choca con el rol, manda este proyecto.

## Stack
- <Framework / lenguaje / versión>
- <Base de datos> · <Hosting> · <Gestor de paquetes>

## Estructura
<Árbol corto de carpetas principales y qué va en cada una.>

## Reglas del proyecto
1. <Regla concreta en imperativo.> <Motivo breve si no es obvio.>
2. ...

## Forma de trabajar conmigo
- Autonomía: <avanza y resume | pregunta antes de X>
- Nunca: <manías del usuario convertidas en reglas>
- Siempre: <lo que quiere que haga siempre>
- Commits: <convención y si puede hacerlos>
- Pide aprobación explícita antes de: `git push`, desplegar, borrar datos o archivos,
  publicar, enviar mensajes o hacer pagos.
- Secretos: nunca en el código ni en esta skill. Están en <variables de entorno>.
- Si no sabes algo del proyecto, pregunta. No lo inventes.

## Estilo de código
<2–4 reglas + un ejemplo corto bien / mal. Lo largo, en references/estilo.md>

## Glosario
- **<término>**: <significado en este proyecto>

## Reglas de negocio
- <Lo que no se puede romper>

## Antes de terminar una tarea
- [ ] <comando de lint / tipos / tests del proyecto>
- [ ] <comprobación propia del proyecto>

## Pendiente de decidir
- <Valores marcados (por defecto) que el usuario debe revisar>
```

Y en la misma carpeta, `CHANGELOG.md` con la primera entrada (formato en
`bucle-aprendizaje.md`).

## Ejemplo de descripción buena y mala

- Mala: "Ayuda con desarrollo web." → se activa en cualquier proyecto y pisa a otras skills.
- Buena: "Contexto y reglas del proyecto Colmenas (PWA para apicultores: colmenas,
  cosechas, libro REGA). Úsala siempre que se trabaje en el código o diseño de
  Colmenas o se mencionen colmenas, apiarios o el libro de explotación."
