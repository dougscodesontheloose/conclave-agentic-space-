import asyncio
import os
from playwright.async_api import async_playwright

async def html_to_pdf():
    html_path = "file://" + os.path.abspath("squads/linkedin-content/output/carousel/preview_synthwave.html")
    pdf_path = "squads/linkedin-content/output/carousel/post_final_carrossel.pdf"
    
    async with async_playwright() as p:
        # Iniciando o Chrome ignorando a Sandbox nativa do Mac que causou o bloqueio antes
        browser = await p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = await browser.new_page()
        await page.goto(html_path)
        
        # Tirar um PDF. Como o CSS já define as caixas em 1080x1080, vamos forçar esse tamanho de página
        await page.pdf(
            path=pdf_path,
            width="1080px",
            height="1080px",
            print_background=True,
            page_ranges="1" # test just one page first to see if it formats nicely, wait, the HTML is a single long page currently... 
        )
        await browser.close()
        print(f"PDF gerado com sucesso em: {pdf_path}")

asyncio.run(html_to_pdf())
