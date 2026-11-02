# Desarrollo guiado por especificaciones: ciclo y plantillas

La especificación es un documento versionado en el repositorio que dice qué debe hacer
el software y cómo se comprueba. El plan, las tareas, los tests y el código salen de ella.

## Dónde vive

```
specs/
├── producto.md              (Fase 1: propósito, alcance, requisitos no funcionales)
├── arquitectura.md          (Fase 2: componentes, datos, stack; enlaza contratos y ADR)
└── 001-recuperar-contrasena/
    ├── spec.md              (qué y por qué)
    ├── plan.md              (cómo)
    └── tareas.md            (pasos pequeños y comprobables)
```

- Si el proyecto ya usa otra estructura o herramienta (Spec Kit, Kiro, OpenSpec…), síguela.
- Las reglas permanentes del proyecto van en su skill o en `CLAUDE.md`. No las copies aquí.

## El ciclo

1. **Especificar.** Escribe `spec.md`: qué y por qué, sin tecnología. Marca cada duda con
   `[POR ACLARAR: …]` y pregúntala.
2. **Aprobar.** Muestra la especificación y espera confirmación. Una con marcas pendientes
   no está aprobada. Si el usuario pidió avanzar sin parar, elige la opción más razonable,
   márcala `(por defecto)` y menciónala en la entrega.
3. **Planificar.** Escribe `plan.md`: decisiones técnicas que cumplen los requisitos.
4. **Dividir.** Escribe `tareas.md`: cada tarea cita su requisito y dice cómo se comprueba.
5. **Construir.** Una tarea cada vez. Cada criterio de aceptación da al menos un test,
   escrito antes o junto al código, con el identificador en su nombre. Al acabar cada tarea,
   pasa Claude Security como indica `SKILL.md`, antes de empezar la siguiente.
6. **Verificar.** Comprueba requisito por requisito, no solo que los tests pasen.
7. **Mantener.** Marca la especificación como `implementada`. A partir de ahí describe lo
   que el software hace hoy.

## Cuando la realidad choca con la especificación

- **Falta un caso o la especificación está mal:** para, corrígela y luego cambia el código.
  Si altera lo acordado con el usuario, confírmalo antes.
- **Un test falla:** arregla el código. Solo se cambia el test si cambió el requisito, y
  entonces primero la especificación.
- **Un cambio posterior modifica el comportamiento:** especificación y código cambian en el
  mismo commit o PR.
- **El código hace algo que ningún requisito pide:** se añade a la especificación con el OK
  del usuario, o se quita.

## Código existente

- No especifiques toda la aplicación de golpe. Especifica solo lo que vas a tocar.
- Antes de cambiarlo, describe el comportamiento actual en `spec.md` y fíjalo con tests.
- Si el código contradice lo que el usuario cree que hace, no asumas cuál es el correcto:
  pregunta.

## Plantilla: spec.md

```markdown
# <Funcionalidad>

Estado: borrador | aprobada | implementada | sustituida por <NNN>

## Problema
Qué le pasa a quién y por qué merece resolverse.

## Fuera de alcance
Lo que esta especificación no hace, aunque parezca natural.

## Comportamiento actual
Solo si se modifica algo que ya existe.

## Requisitos
- **R-001** <Actor> puede <acción observable>.
  - CA-1: Dado <contexto>, cuando <acción>, entonces <resultado comprobable>.
  - CA-2: Dado <caso de error o límite>, cuando <acción>, entonces <resultado>.

## Requisitos no funcionales
Con números: tiempos, límites, retención, accesibilidad.

## Dudas
- [POR ACLARAR: <pregunta concreta>]
```

CA significa criterio de aceptación: la prueba que decide si el requisito se cumple. Se
escriben siempre los casos de error y límite, no solo el camino feliz.

## Plantilla: plan.md

```markdown
# Plan: <funcionalidad>

## Enfoque
Cómo se resuelve, en pocas frases, y qué módulos se tocan.

## Datos
Tablas, campos, índices y migraciones. Qué datos son sensibles.

## Contrato
Endpoints o eventos con entrada, salida y errores. Enlaza el archivo del contrato.

## Cómo se cubre cada requisito
| Requisito | Solución | Test |
|---|---|---|

## Riesgos y decisiones
Riesgos conocidos. ADR de lo que sea caro de revertir.
```

## Plantilla: tareas.md

```markdown
- [ ] T1 (R-001) <Cambio concreto>. Hecho cuando: <comprobación>.
- [ ] T2 (R-001, depende de T1) <Cambio concreto>. Hecho cuando: <comprobación>.
```

Cada tarea cabe en un cambio que se pueda revisar de una sentada y deja el proyecto
funcionando. Si no cita ningún requisito, sobra la tarea o falta el requisito.

## Ejemplos

### Bueno: funcionalidad nueva

```markdown
- **R-001** Quien ha olvidado su contraseña puede crear una nueva desde un enlace enviado
  a su correo.
  - CA-1: Dado un correo registrado, cuando pide recuperar la contraseña, entonces recibe
    un enlace de un solo uso que caduca en 30 minutos.
  - CA-2: Dado un correo no registrado, cuando pide recuperar la contraseña, entonces ve el
    mismo mensaje que en CA-1 y no se envía nada.
  - CA-3: Dado un enlace caducado o ya usado, cuando lo abre, entonces ve el motivo y puede
    pedir otro.
```

Funciona porque cada criterio se convierte en un test sin interpretar nada y porque no
dice cómo se guarda el enlace: eso lo decide el plan.

### Bueno: cambio pequeño en una especificación que ya existe

```diff
  - **R-004** Quien tiene un pedido sin enviar puede cancelarlo.
    - CA-1: Dado un pedido sin enviar, cuando lo cancela, entonces se reembolsa el importe.
+   - CA-2: Dado un pedido ya enviado, cuando intenta cancelarlo, entonces ve que ya no es
+     posible y cómo devolverlo.
```

Funciona porque añade solo lo que cambia, sin carpeta nueva ni plan: el nuevo criterio y
su test bastan.

### Malo

```markdown
La recuperación de contraseña debe ser rápida, segura y fácil de usar.
Usar Redis para guardar los tokens y SendGrid para el correo. El endpoint será
POST /api/v1/auth/reset.
```

Falla por tres motivos: "rápida", "segura" y "fácil" no se pueden comprobar, así que nadie
puede decir si está terminada; mezcla el qué con el cómo, atando la especificación a
decisiones técnicas que pertenecen al plan; y omite los casos que causan los problemas, como
el enlace caducado o el correo que no existe.
