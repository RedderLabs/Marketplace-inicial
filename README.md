# redder-roles

Skills de roles profesionales en español, de Redder Labs.

## Instalar en Claude Code

```
/plugin marketplace add RedderLabs/Marketplace-inicial
```

Todo de una vez:

```
/plugin install todo@redder-roles
```

O solo una categoría (`desarrollo`, `herramientas`…):

```
/plugin install desarrollo@redder-roles
```

No instales `todo` y una categoría a la vez, o tendrás las skills repetidas.

`web-premium` coordina además skills externas de diseño, que se instalan aparte. Las
imprescindibles son `impeccable` ([instrucciones](https://impeccable.style/docs/)) y `ui-ux-pro-max`:

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

La lista completa, y qué hace la skill si falta alguna, está en
`skills/web-premium/references/skills-diseno.md`.

## Añadir o quitar skills

1. Crea o borra la carpeta en `skills/`.
2. Pon su categoría en `categorias.json` (si no la tiene, solo entra en `todo`).
3. Ejecuta `python3 scripts/build-marketplace.py`.
4. Haz commit y push. Quien lo tenga instalado lo recibe con `/plugin marketplace update redder-roles`.
