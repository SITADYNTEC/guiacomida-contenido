# GuiaComida · Guía de producción semanal (para la tarea automática)

La tarea corre cada **miércoles** y deja lista la semana que empieza el lunes siguiente: **2 reels, 3 posts, 2 historias de apoyo programables y 1–2 historias manuales**. Nunca publica: solo crea **borradores** en Metricool. El equipo los revisa y los programa el jueves o viernes.

Todo vive en el repositorio público **`SITADYNTEC/guiacomida-contenido`** (scripts de render en `scripts/`, plantillas en `plantillas/`, piezas en `publicar/`). Es independiente del repositorio de Dyntec: no lo clones ni lo modifiques.

## 0. Qué es GuiaComida (para escribir bien)

- Directorio mexicano de comida artesanal y hecha en casa: panaderías de masa madre, repostería por encargo, cocinas ocultas, comida casera, tamales, salsas, etc. Lo opera Dyntec.
- Cada negocio tiene su **vitrina** (página pública `guiacomida.com/<negocio>`) con menú, fotos y precios, y recibe **pedidos directo por WhatsApp, sin comisiones**.
- En su panel lleva **costos de recetas, márgenes, inventario y merma**.
- Precio: **$199 al mes o $1,990 al año (precio fundador)**. Prueba normal: 14 días.
- **Audiencia de las redes: emprendedores de comida** (cocineros, panaderos, reposteros, negocios pequeños, muchos desde casa). Les hablamos de tú, como alguien del gremio. Los consumidores no son el objetivo de estas piezas.

## 1. Qué producir

1. Abre `calendario.md` y ubica la fila cuyo lunes es el próximo lunes.
2. Produce todas las piezas `pendiente` de esa fila. Las `listo` ya están en `publicar/` y solo se suben como borrador.
3. Carpeta de salida: `publicar/AAAA-MM-DD_semanaN/` (fecha del lunes).
4. Nombres: `post1_N.png` (carrusel), `post2_*.png`, `post3_*.png`, `reelN_<tema>.mp4`, `historia_*.png`, voces y JSON de palabras en `voces/`.

## 2. Oferta y CTA (revisar cada semana)

- **Oferta vigente: Cortesía de bienvenida `bienvenida2026`: 1 mes gratis, sin tarjeta, límite de 100 cuentas nuevas.**
  - Link: `guiacomida.com/bienvenida2026`. En Instagram el texto de la publicación no tiene links clicables: el CTA es **"Link en el perfil"** y se escribe la dirección completa como texto.
  - Al terminar el mes, el negocio elige su plan y paga con Mercado Pago; sus datos se conservan. Dilo así, sin letra chica escondida.
  - Usa "Solo 100 lugares", nunca un número de lugares restantes (no lo podemos verificar desde aquí).
- **Si el equipo marca aquí `CORTESÍA AGOTADA`**, cambia la oferta a: "Prueba 14 días gratis en guiacomida.com/registro" y "Precio fundador $199/mes".
- Estado actual: **CORTESÍA ACTIVA**.

## 3. Reglas de contenido (obligatorias)

- Negocios de ejemplo siempre **ficticios** y marcados como "Ejemplo" en la pieza ("Panadería La Espiga", "Repostería Miel y Canela"…). Nunca nombres, fotos, vitrinas ni datos de negocios reales registrados en GuiaComida, salvo que el equipo mande un caso con permiso por escrito.
- Nada de testimonios inventados ni citas atribuidas a personas. Si el equipo manda un testimonio real con permiso, va con nombre de pila y giro.
- No prometer lo que el producto no hace: no hay app de delivery, no cobramos por el negocio, no hay repartidores, no prometemos "más ventas garantizadas". Sí: vitrina, pedidos por WhatsApp sin comisión, costos y márgenes, inventario y merma, estadísticas de visitas.
- Al comparar con apps de delivery, no des porcentajes de comisión de otras marcas ni las nombres. Basta con "sin comisión por pedido" y "el cliente es tuyo".
- Fotos IA de comida o cocinas: genéricas, sin logos ni rostros reconocibles, y nunca presentadas como un negocio real.
- Tono: cálido, directo, de tú, español de México, frases cortas. Orgullo por el oficio ("tu receta", "tu sazón", "tu horno"). Cero tecnicismos: "vitrina", "link", "pedidos", "cuánto ganas".
- Hashtags (4–6): #GuiaComida #EmprendedoresMexicanos #ComidaCasera + del tema (#Repostería #PanArtesanal #MasaMadre #NegocioDeComida #HechoEnMéxico).

## 4. Sistema de variedad (obligatorio)

Códigos de formato (los mismos que usa Dyntec, adaptados a comida). Regla: **ningún formato se repite en las 2 semanas anteriores**; revisa y actualiza `formatos_usados.md`.

| Código | Reel adaptado a GuiaComida |
|---|---|
| R1 | Texto cinético al ritmo de la música (ej. "Haces el mejor pan de tu colonia… pero nadie lo encuentra") |
| R2 | POV / humor: "POV: son las 11 p.m. y sigues contestando '¿cuánto cuesta?'" |
| R3 | Antes/después en pantalla dividida: pedidos por DM caóticos vs. vitrina + WhatsApp ordenado |
| R4 | Producto en acción: vitrina, panel de costos, inventario (mockups con datos ficticios) |
| R5 | Explicativo: "Así costeas un pastel paso a paso" (máx. 1 cada 4 semanas) |
| R6 | Lluvia de notificaciones: "¿precio?", "¿menú?", "¿hasta cuándo?" y silencio cuando llega la vitrina |
| R7 | Top 3: "3 errores al ponerle precio a tu pan", "3 fotos que venden" |
| R8 | Quiz: "¿Cuánto le ganas a este pastel? A/B/C" |
| R9 | Emprendedor a cámara: solo si el equipo sube un video real con permiso |
| R10 | Escena IA: cocina casera genérica (Veo Lite) + interfaz superpuesta |

| Código | Post adaptado |
|---|---|
| P1 | Carrusel educativo (fondo variable). Máx. 1 cada 2 semanas |
| P2 | Mito vs. realidad ("Necesito página web cara" ✗) |
| P3 | Tarjeta de frase fuerte de GuiaComida (nunca atribuida a una persona) |
| P4 | Checklist para guardar |
| P5 | Foto editorial IA de comida mexicana artesanal + titular en plantilla |
| P6 | Infografía de un proceso (de la receta al pedido) |
| P7 | Comparativa: "Vender por DM" vs. "Vender con vitrina" |
| P8 | Carrusel quiz "desliza para ver la respuesta" (ej. ¿cuánto cobrar?) |
| P9 | Meme propio en 2 paneles ilustrados (sin personajes con derechos) |
| P10 | Ficha de ejemplo: negocio ficticio, reto, cómo usa GuiaComida, resultado ilustrativo marcado como ejemplo |

Diseño:
- Rota 5 fondos: crema `#FBF6EE`, barro `#C75D38`, tinta `#241B12`, arena `#FBF1DC` y verde `#3C6B47`. Nunca dos piezas seguidas con el mismo fondo dominante.
- Títulos en **Fraunces** (cursiva para la palabra clave), textos en **Albert Sans** (`plantillas/brand.css`, fuentes en `plantillas/assets/fonts/`, licencia OFL).
- Marca: wordmark de texto `.wm` (`<span class="wm"><i>G</i><b>Guia</b><span>Comida</span></span>`). Si existe `plantillas/assets/logo.png`, úsalo en su lugar.
- Sin emojis dentro de las imágenes (el render no tiene fuente de emoji); en el texto de la publicación sí puedes usar 1–3.
- Reels: gancho en el primer segundo, corte cada 1–2 s, nada estático más de 1.5 s. **1 de cada 2 reels sin voz** (texto + música). Subtítulos palabra por palabra en los reels con voz, sin tapar los últimos 300 px (zona de la interfaz de Instagram).
- Referencias en `plantillas/`: `post_lanzamiento.html` (carrusel), `post_frase.html` (P3), `post_checklist.html` (P4), `historias.html`, `reel_vitrina.html` (R1 sin voz), `reel_mes_gratis.html` (R4 con voz y subtítulos) con el motor `reel_gc.js`. Para formatos nuevos puedes usar Remotion + video-shotcraft (ver §4b); guarda el proyecto en `remotion/`.

## 4b. Herramientas: modelos de imagen y recetas de video

### Modelos de imagen (vía ElevenLabs)
| Uso | Modelo | Créditos aprox. |
|---|---|---|
| Foto editorial realista de comida o cocinas (P5), escenas base para clips | `gpt-image-2.5-sunburst` (default) o `flux-3-image` | 190 · 290 |
| Imagen "héroe" de máxima calidad o personaje/escena que debe repetirse igual en varias láminas (con imágenes de referencia) | `gemini-3-pro-image` (Nano Banana Pro) | 1,220 · solo si no hay otro gasto IA esa semana |
| Ilustración vectorial, íconos, memes propios en 2 paneles (P9), infografías (P6) | `recraft-v4.1` · `recraft-v4.1-pro-vector` | 240 |
| Póster tipográfico o imagen donde el texto es parte del diseño | `ideogram-4.5` (revisar ortografía letra por letra; el texto final se pone en plantilla si sale mal) | 360 |
| Fotos de producto o pantallas en contexto (tablet en mostrador, celular en mano) | `flux-3-image` o `bytedance-seedream-5-pro` | ~290 |
| Quitar fondo / ampliar resolución | `birefnet-v2-bg-removal` · `topaz-image-upscale-v2` | bajo |

Reglas: `generations_count` 1 (máximo 2 si el post depende de la imagen); relación 4:5 para posts y 9:16 para historias; nada de marcas, logos ni rostros reconocibles; personas genéricas y diversas de México (de preferencia manos y comida, sin rostros); en el texto de la publicación no se dice que una foto IA es un cliente real.

### Remotion + video-shotcraft
Skills: `remotion:remotion-best-practices` (leer antes de escribir código Remotion), `remotion:remotion-captions` (subtítulos; tiempos con Scribe) y `video-shotcraft:video-shotcraft` en modo de una toma (elegir una tarjeta de `references/shots/<categoría>/`, leerla completa y adaptar su demo; copiar componentes de `assets/lib/`, no importarlos). Si los skills no aparecen en la sesión, instala `remotion` con npm o usa el motor HTML `reel_gc.js`, y anótalo en el resumen. Efectos de sonido: solo los de video-shotcraft con licencia registrada en `ATTRIBUTION.md` o generados con ElevenLabs SFX. Música: nunca las pistas de video-shotcraft.

**Recetas sugeridas por formato** (tarjetas de video-shotcraft; rota para no repetir):
| Formato | Tomas sugeridas |
|---|---|
| R1 texto cinético | typography: `flying-words`, `cel-flash-stomp`, `lead-word-zoom-assemble`, `split-flap-title`, `scramble`, `gradient-word-sweep`, `type-rhythm-sync` + rhythm: `beat-cut-moves`, `trailer-grammar-moves` |
| R2 POV / R10 escena IA | Clip Veo Lite en `<Video>` con effects `duotone()` (barro/crema), `vignette()`, `chromaticAberration()`, `lightLeak()`; transitions: `white-flash-logo-simplify-cut`, `circle-match-iris` |
| R3 pantalla dividida | data: `before-after-slider-scrub`; rhythm: `quad-split-parallel-scenes`, `speed-ramp-freeze` |
| R4 producto 2.5D | camera: `cursor-flyover`, `depth-layer-moves`, `crash-zoom-punch`, `steep-tilt-glide`; interaction: `ai-stream-response`, `command-palette-summon`, `type-and-filter` |
| R5 explicativo | ui-entrance: `integration-hub-map`, `draw-svg-trace`; effects: `scan-bracket-sweep`, `fui-hud-moves` |
| R6 lluvia de notificaciones | ui-entrance: `card-stack`, `list-stack-press`, `deck-deal-flyin`; effects: `impact-feedback`; rhythm: `rhythm-interrupt-moves` |
| R7 top 3 | typography: `countdown-arc-scatter`; data: `odometer-digit-roll`, `counter-confetti`, `gauge-readout-moves` |
| R8 quiz | interaction: `chip-grid-single-select-blackout`, `picker-carousel-feature-cycle`, `segmented-thumb-hero` |
| Aperturas (rotar) | opening: `brand-ink-open`, `text-as-mask`, `letterspace-materialize`, `orbit-ring-title-open`, `fracture` |
| Cierres (rotar) | outro: `logo-shrink-wordmark-lockup`, `ui-to-brand-morph`, `grain-dissolve`, `ui-strip-away-outro` |

## 5. Voz, música e imágenes (ElevenLabs)

- **Voz de marca: Liza – Natural Mexican Creator `kl7d390GatBPfqhRTyAl`**, modelo `eleven_v4`, `generations_count` 1. (Distinta de las voces de Dyntec a propósito.)
- Guion de 20–30 s (55–80 palabras), con "…" entre escenas.
- Subtítulos: transcribe la voz con Scribe (`creative_transcribe_audio` conectado al nodo de la voz; cuesta 0 créditos sobre una voz propia) y usa los tiempos por palabra (`window.W` en la plantilla, sumando 0.15 s por el retraso que mete `render_reel.py`).
- Música: reutiliza las pistas de `plantillas/audio/` (`musica_acustica_105bpm.mp3`, instrumental, ElevenLabs Music). Genera una nueva solo cada 2–3 semanas para variar (~900 créditos). Nunca uses pistas de video-shotcraft.
- Mezcla en reels con voz: música al 13 % bajo la voz y normaliza el MP4 final con `loudnorm=I=-14:TP=-1.5`.
- Imágenes IA según la tabla de §4b (`gpt-image-2.5-sunburst` por defecto), 4:5 para posts y 9:16 para historias, `generations_count` 1.
- Descarga cada archivo en cuanto termine (los enlaces caducan en horas).

### Presupuesto (cuenta compartida con Dyntec, plan Starter 40,000 créditos/mes, se renueva el día 3)
- **Tope: ~4,000 créditos por semana.** Referencia: voz ~400, pista de música ~900, imagen 190–360, clip Veo Lite ~2,400.
- Máximo por semana: 1 voz, 4 imágenes IA, 1 pista de música nueva **o** 1 clip Veo Lite (no ambos).
- Al empezar revisa `account_get_usage`. Si quedan menos de 8,000 créditos antes de la renovación, produce solo con voz y plantillas, sin imágenes ni video IA. Corre `estimate_only` antes de música o video.

## 6. Subir y crear borradores

1. `git add`, commit y `git push` a `main`. Metricool toma los archivos de `https://raw.githubusercontent.com/SITADYNTEC/guiacomida-contenido/main/<ruta>`.
2. Metricool, marca **GuiaComida `blogId 8155473`**, zona `America/Mexico_City`, plan Starter. **Nunca uses el blogId 8136891 (es Dyntec).** Llama `getBrandSettings` al empezar y publica en todas las redes conectadas de la marca (hoy: Instagram @guiacomida). Si aparece Facebook o TikTok conectado, agrégalo (reels a TikTok; en Facebook avisa que hay que desactivar el compartido automático para no duplicar).
3. Revisa con `getScheduledPosts` (blogId 8155473) que no exista ya un borrador ese día.
4. Un borrador por pieza (`"draft": true`), en el día y hora del calendario:
   - Reel: `instagramData.type = "REEL"`, `isAiGenerated: true` si lleva voz, música o imágenes IA.
   - Post/carrusel: `type = "POST"`, imágenes en orden.
   - Historias de apoyo: `type = "STORY"`, sin texto, una imagen 1080×1920. Las de encuesta, preguntas o quiz **no** van a Metricool: quedan en `publicar/` para subirlas a mano con su sticker.
5. Texto: gancho de 1 línea + 1–2 líneas de valor + CTA de la oferta vigente ("Link en el perfil 👉 guiacomida.com/bienvenida2026") + hashtags.

## 7. Cierre

- Marca `listo` en `calendario.md` y registra formatos en `formatos_usados.md`. Commit y push.
- Resumen corto al equipo: piezas, formato, día y hora, enlace al Planificador (`https://app.metricool.com/planner/calendar?blogId=8155473`), historias manuales con su enlace en GitHub, créditos gastados y restantes. Recuerda: **programar los borradores antes del lunes**.
- Si algo falla, deja lo que sí quedó, explica qué faltó y no repitas generaciones pagadas.
