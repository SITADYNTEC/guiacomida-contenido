"""Renderiza un reel de plantillas/ y le monta la voz.

Uso:
  python3 scripts/render_reel.py plantillas/reel2.html voz.mp3 salida.mp4 [cortes_json]

Sin cortes_json, detecta las pausas de la voz y toma las más cercanas a los cortes
estimados que trae la plantilla (window.T). Con cortes_json (ej. "[0,4.2,6.2,...,26.7]")
usa esos tiempos tal cual: el último valor es la duración total del video.
"""
import sys, re, json, os, subprocess, shutil, tempfile

html, mp3, out = sys.argv[1:4]
manual = json.loads(sys.argv[4]) if len(sys.argv) > 4 else None
here = os.path.dirname(os.path.abspath(__file__))
html = os.path.abspath(html)

dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                            '-of', 'csv=p=0', mp3], capture_output=True, text=True).stdout)
if manual:
    T = manual
else:
    est = json.loads(re.search(r'window\.T\s*=\s*window\.T\s*\|\|\s*(\[[^\]]+\])', open(html).read()).group(1))
    log = subprocess.run(['ffmpeg', '-i', mp3, '-af', 'silencedetect=noise=-35dB:d=0.15', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    s = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', log)]
    e = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', log)]
    mids = [(a + b) / 2 for a, b in zip(s, e)]
    scale = dur / est[-1] if est[-1] else 1
    cuts = []
    for c in est[1:-1]:
        c *= scale
        cand = [m for m in mids if abs(m - c) < 1.2 and (not cuts or m > cuts[-1])]
        cuts.append(round(min(cand, key=lambda m: abs(m - c)) if cand else c, 2))
    T = [0] + cuts + [round(dur + 1.6, 2)]
print('Cortes:', T)

tmp = tempfile.mkdtemp()
subprocess.run(['python3', os.path.join(here, 'frames.py'), html, tmp, str(T[-1]), json.dumps(T)], check=True)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{tmp}/f%04d.jpg', '-i', mp3,
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '192k', '-af', 'adelay=150|150', '-movflags', '+faststart', out], check=True)
shutil.rmtree(tmp)
print('Listo:', out)
