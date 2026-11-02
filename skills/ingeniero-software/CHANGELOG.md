# Changelog — ingeniero-software

## 2026-11-02
- Cambio: al terminar cada parte del trabajo se comprueba con Claude Security (`/claude-security`) que no hay agujeros de seguridad. Añadido también al checklist, al ciclo de especificaciones y a la autorrevisión.
- Motivo: "cada vez que finalice una parte del trabajo estos deben usar Claude Security para comprobar que no hay agujeros de seguridad".
- Prueba: pendiente de un caso real del usuario.

## 2026-10-31 (2)
- Cambio: el desarrollo pasa a estar guiado por especificaciones (especificación → plan → tareas → tests y código → verificación), proporcional al tamaño del encargo. Añadido `references/spec-driven.md` y una sección de especificación en el checklist.
- Motivo: "la skill de ingeniero debe contemplar esta forma de desarrollar Spec-Driven Development".
- Prueba: pendiente de un caso real del usuario.

## 2026-10-31
- Cambio: la Fase 5 pide aprobación explícita antes de desplegar, hacer push, borrar datos o tocar pagos, y prohíbe secretos en el código.
- Motivo: barreras de seguridad comunes a todas las skills.

## 2026-10-30
- Creada: ingeniero sénior de apps y web en 5 fases, con `references/arquitectura.md` y `references/checklist-calidad.md`.
