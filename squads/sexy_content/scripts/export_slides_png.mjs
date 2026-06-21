#!/usr/bin/env node
/**
 * Exporta cada slide de um HTML de preview para PNGs individuais (1080x1080).
 * Usa Playwright com o Chromium bundled.
 * Uso: node export_slides_png.mjs <caminho_do_html> [pasta_saida]
 */

import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const htmlFile = process.argv[2] || path.resolve(__dirname, '../output/carousel/preview_v5_brutalist.html');
const outputDir = process.argv[3] || path.resolve(path.dirname(htmlFile));

const fileUrl = `file://${path.resolve(htmlFile)}`;

async function exportSlides() {
  console.log(`📂 Abrindo: ${fileUrl}`);
  
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.setViewportSize({ width: 1200, height: 1200 });
  await page.goto(fileUrl, { waitUntil: 'networkidle', timeout: 30000 });
  
  // Esperar fonts
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(2000);

  const slideCount = await page.$$eval('.slide', slides => slides.length);
  console.log(`🎨 ${slideCount} slides encontrados.`);

  for (let i = 0; i < slideCount; i++) {
    const slideId = `slide-${i + 1}`;
    
    // Remove a escala de preview e isola o slide
    await page.evaluate((id) => {
      const el = document.getElementById(id);
      if (el) {
        el.style.transform = 'none';
        el.style.margin = '0';
        el.style.position = 'absolute';
        el.style.top = '0';
        el.style.left = '0';
        el.style.zIndex = '9999';
      }
      document.querySelectorAll('.slide').forEach(s => {
        if (s.id !== id) s.style.display = 'none';
      });
    }, slideId);

    await page.setViewportSize({ width: 1080, height: 1080 });
    await page.waitForTimeout(500);

    const filename = `slide-${String(i + 1).padStart(2, '0')}.png`;
    const filepath = path.join(outputDir, filename);
    
    await page.screenshot({
      path: filepath,
      clip: { x: 0, y: 0, width: 1080, height: 1080 },
    });

    console.log(`  ✅ ${filename}`);

    // Restaura
    await page.evaluate(() => {
      document.querySelectorAll('.slide').forEach(s => {
        s.style.display = '';
        s.style.transform = '';
        s.style.margin = '';
        s.style.position = '';
        s.style.top = '';
        s.style.left = '';
        s.style.zIndex = '';
      });
    });
  }

  await browser.close();
  console.log(`\n🎉 ${slideCount} slides exportados para ${outputDir}`);
}

exportSlides().catch(err => {
  console.error('❌ Erro:', err.message);
  process.exit(1);
});
