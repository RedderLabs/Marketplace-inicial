# Plantillas: ficha de agente, transferencias y plan de 7 días

## Ficha de agente

Una por agente. Si un campo queda vacío, el agente probablemente sobra.

```markdown
### <N>. <Nombre del agente>

- **Propósito:** <una frase: qué problema resuelve y por qué no lo hace otro agente>
- **Inputs:** <qué recibe, de quién y en qué formato>
- **Outputs:** <qué entrega, a quién y en qué formato exacto>
- **Herramientas:** <solo las que necesita: lectura de archivos, web, CRM… Nada de más>
- **Modelo:** <Opus | Sonnet | Haiku> — <por qué>
- **Criterios de éxito:** <cómo se comprueba que lo hizo bien, medible>
- **Modos de fallo:** <qué suele salir mal y qué hace el sistema entonces>

**System prompt:**
<bloque de código con el prompt completo, siguiendo la plantilla de abajo>
```

## Plantilla de system prompt

Corto, concreto y con el formato de salida cerrado. Sin "eres el mejor experto del mundo".

```
<rol>
Eres <rol concreto> dentro de un sistema de <N> agentes que <objetivo del sistema>.
Tu único trabajo es <tarea>. No haces <lo que hacen los otros agentes>.
</rol>

<entrada>
Recibes <qué>, en este formato: <formato>.
Si falta <dato crítico>, no lo inventes: devuelve {"estado": "falta_info", "falta": [...]}.
</entrada>

<reglas>
- <regla del negocio del usuario>
- Usa solo los datos de la entrada y de <fuentes permitidas>. Si no sabes algo, dilo.
- No envías, publicas, borras ni pagas nada. Eso lo decide una persona.
</reglas>

<salida>
Devuelve exactamente esto, sin texto antes ni después:
<formato: JSON con campos fijos o markdown con secciones fijas>
</salida>

<ejemplo>
Entrada: <ejemplo corto real>
Salida: <salida esperada>
</ejemplo>
```

## Tabla de transferencias

| De | A | Qué entrega | Formato | Dónde se guarda | Si falla |
|---|---|---|---|---|---|
| <agente> | <agente o humano> | <contenido> | <JSON/markdown> | <carpeta, tabla, issue> | <reintento máx. N, luego avisa a la persona> |

Reglas: máximo 2 reintentos por paso; si un revisor rechaza 2 veces, para y pasa a la
persona con el motivo. Cada ejecución guarda su registro (entrada, salida, coste, tiempo).

## Plan de lanzamiento de 7 días

| Día | Qué | Hecho cuando |
|---|---|---|
| 1 | Recoger 5–10 casos reales y escribir cómo sería la salida perfecta de cada uno | Casos y salidas guardados |
| 2 | Construir solo el agente del cuello de botella; humano hace el resto | Funciona con 3 casos |
| 3 | Probarlo con todos los casos, ajustar el prompt (no las salidas) | ≥ 80 % aceptables sin editar |
| 4 | Añadir el segundo agente y la transferencia entre ambos | Flujo de 2 pasos de punta a punta |
| 5 | Añadir revisor o verificación y el punto de aprobación humana | Errores atrapados antes de la persona |
| 6 | Medición: registro de coste, tiempo y calidad por ejecución | Panel o tabla con datos reales |
| 7 | Uso real con supervisión; lista de fallos y siguiente mejora | Decisión: ampliar, ajustar o parar |

## Medición

| Métrica | Cómo se mide | Valor bueno (por defecto) |
|---|---|---|
| Calidad | % de salidas aprobadas sin editar | ≥ 80 % |
| Velocidad | Tiempo de punta a punta frente al proceso manual | ≥ 50 % menos |
| Consistencia | Mismo caso ejecutado 3 veces: ¿mismo resultado en lo importante? | 3 de 3 |
| Coste | Coste por ejecución (tokens × precio) y al mes | Dentro del presupuesto |
| ROI | (horas ahorradas × valor hora − coste mensual) / coste mensual | > 3 |
