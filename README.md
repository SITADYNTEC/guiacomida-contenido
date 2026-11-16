# GuiaComida · contenido de redes

Contenido de Instagram **@guiacomida** (marca **GuiaComida** en Metricool, `blogId 8155473`). El repositorio es **público** porque Metricool lee los archivos desde `raw.githubusercontent.com`. Aquí solo va contenido que se va a publicar.

- Guía de producción (fuente de verdad para la tarea automática): [`GUIA.md`](GUIA.md)
- Calendario: [`calendario.md`](calendario.md) · Formatos usados: [`formatos_usados.md`](formatos_usados.md)
- Plantillas y marca: `plantillas/` (Fraunces + Albert Sans, colores del sitio guiacomida.com)
- Piezas finales: `publicar/AAAA-MM-DD_semanaN/`
- Scripts de render: `scripts/` (`shot.py` posts/historias, `frames.py` + `render_reel.py` reels, `sheet.py` hojas de contacto). Requieren Chrome y Playwright.

## Flujo semanal

1. **Miércoles 11:12 (CDMX):** la tarea programada "Contenido semanal GuiaComida" produce la semana siguiente, la sube aquí y crea **borradores** en Metricool.
2. **Jueves o viernes:** el equipo revisa los borradores en Metricool y programa cada uno. Lo que no se programa, no se publica.
3. Las historias con stickers (encuestas, preguntas) se suben a mano desde `publicar/`.

## Render

```bash
python3 scripts/shot.py "$PWD/plantillas/post_lanzamiento.html" "publicar/.../post1_%d.png" 1080 1350 .slide
python3 scripts/render_reel.py plantillas/reel_vitrina.html musica.mp3 publicar/.../reel1.mp4 "[0,2.29,...,20.57]"
```
