import sys, asyncio
from playwright.async_api import async_playwright
async def main(html, out, w, h, sel=None):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width':w,'height':h})
        await pg.goto('file://'+html); await pg.wait_for_timeout(400)
        if sel:
            els = await pg.query_selector_all(sel)
            for i,e in enumerate(els): await e.screenshot(path=out.replace('%d',str(i+1)))
        else: await pg.screenshot(path=out)
        await b.close()
a=sys.argv; asyncio.run(main(a[1],a[2],int(a[3]),int(a[4]),a[5] if len(a)>5 else None))
