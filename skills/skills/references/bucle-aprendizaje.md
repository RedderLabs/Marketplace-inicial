# Modo mejora — bucle de aprendizaje

Cada corrección del usuario es una regla que falta en alguna skill. El objetivo es
que no tenga que hacer la misma corrección dos veces.

## Cuando el usuario corrige tu trabajo

1. **Pregúntate qué skill debería haberlo evitado.**
   - Si hay una, esa es la que se cambia.
   - Si no hay ninguna y la tarea se repite, propón crear una (modo biblioteca, un solo caso).
   - Si el usuario dice que es algo puntual ("solo esta vez"), no cambies nada.
2. **Propón el cambio exacto como diff**, en lenguaje claro antes del diff:

   ```diff
   ## Reglas
   - Usa un tono cercano.
   + Usa un tono cercano, pero sin emojis ni exclamaciones.
   + Motivo: corrección del 31/10 en el texto de la newsletter.
   ```

3. **Aplícalo solo después del OK del usuario.** Si dice que no, no insistas.
4. **Añade una entrada al `CHANGELOG.md`** de esa skill.
5. **Vuelve a ejecutar la skill** con el caso que provocó la corrección y comprueba que
   ahora sale bien.
6. Si con el cambio la skill empieza a hacer dos trabajos, propón dividirla.

## Formato del CHANGELOG.md

```markdown
# Changelog — <nombre-skill>

## 2026-10-31
- Cambio: <qué cambió, en una línea>.
- Motivo: <la corrección del usuario, en sus palabras si es posible>.
- Prueba: <caso con el que se comprobó> → correcto.

## 2026-10-29
- Creada a partir de la tarea "<tarea>" de la tabla de descubrimiento.
- Prueba: <caso real> → correcto tras 1 ajuste (<cuál>).
```

Lo más reciente, arriba.

## Para que funcione siempre

Una skill solo se carga cuando la tarea encaja con su descripción, así que una
corrección cualquiera no siempre la activa. Para que el bucle funcione en todas las
sesiones, el usuario debe añadir esta instrucción permanente:

- **Claude Code:** en `CLAUDE.md` del proyecto, o en `~/.claude/CLAUDE.md` para todos.
- **App de Claude:** en las preferencias o instrucciones personales del perfil.

```
Cuando corrija tu trabajo, antes de seguir pregúntate qué skill debería haberlo
evitado. Propón el cambio a esa skill como diff, usando la skill "skills" en modo
mejora, y no lo apliques sin mi OK. Anótalo en su CHANGELOG.md.
```
