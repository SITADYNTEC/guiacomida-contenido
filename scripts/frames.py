import sys, asyncio, json
from playwright.async_api import async_playwright
async def main(html, outdir, times, T=None):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width':1080,'height':1920})
        if T: await pg.add_init_script(f'window.T={json.dumps(T)}')
        await pg.goto('file://'+html); await pg.wait_for_timeout(500)
        st = await pg.query_selector('#stage')
        for i,t in enumerate(times):
            await pg.evaluate(f'render({t})')
            await st.screenshot(path=f'{outdir}/f{i:04d}.jpg', type='jpeg', quality=92)
        await b.close()
html,outdir,mode=sys.argv[1:4]
T=json.loads(sys.argv[4]) if len(sys.argv)>4 else None
if mode.startswith('['): times=json.loads(mode)
elif mode=='preview': times=[3.9,7.5,9.6,11.4,13.0,15.0,18.8,22.2,24.4,27.0]
else:
    fps=30; dur=float(mode); times=[i/fps for i in range(int(dur*fps))]
asyncio.run(main(html,outdir,times,T))
