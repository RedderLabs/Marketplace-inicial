# Changelog — web-premium

## 2026-11-02 (4)
- Cambio: añade `web-quality-skills` y `design-qa` a la Fase 5, y las guías `copywriting` y `site-architecture` en `references/externas/`, sin sus scripts. Quedan documentadas las skills descartadas y por qué.
- Motivo: "aqui hay mas" y "haz lo que sea factible", sobre las skills propuestas de labgeeks y de `alirezarezvani/claude-skills`.
- Revisión: lectura estática, sin ejecutar nada. `skill-security-auditor` no se pudo ejecutar porque los permisos bloquearon el código externo.
- Prueba: pendiente de un caso real del usuario.

## 2026-11-02 (3)
- Cambio: `references/skills-diseno.md` pasa a reunir todas las skills de diseño premium disponibles, con qué usar en cada fase, cómo elegir un único estilo, qué manda si chocan y cuáles quedan fuera.
- Motivo: "el skill de web tenga todas las skill para un diseño premium".
- Prueba: pendiente de un caso real del usuario.

## 2026-11-02 (2)
- Cambio: integra `/impeccable` y `/ui-ux-pro-max:ui-ux-pro-max` en las fases del proceso. Añadido `references/skills-diseno.md`, con qué usar en cada fase, qué manda si chocan y qué hacer si falta alguna.
- Motivo: "para el skills de web-premium debe integrar las skills de /ui-ux-pro-max:ui-ux-pro-max y /impeccable".
- Prueba: pendiente de un caso real del usuario.

## 2026-11-02
- Cambio: al terminar cada parte del trabajo se comprueba con Claude Security (`/claude-security`) que no hay agujeros de seguridad. Añadido también al checklist de entrega y a la autorrevisión.
- Motivo: "cada vez que finalice una parte del trabajo estos deben usar Claude Security para comprobar que no hay agujeros de seguridad".
- Prueba: pendiente de un caso real del usuario.

## 2026-10-31
- Creada a partir del análisis del prompt de referencia SELENE.
- Incluye: proceso en 7 fases, motor de scroll probado (compila con TypeScript estricto y
  funciona en navegador con y sin movimiento reducido), catálogo de 10 patrones, checklist
  de entrega con RGPD y plantilla para analizar y crear prompts de un solo paso.
- Mejoras sobre SELENE: fotograma de reposo para movimiento reducido, regla de "primero leer,
  luego escribir", fuentes autoalojadas, versiones exactas y aviso de secretos al exportar.
