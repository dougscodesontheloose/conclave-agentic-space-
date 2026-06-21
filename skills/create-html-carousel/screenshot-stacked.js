#!/usr/bin/env node
/**
 * Screenshot individual slides from a single index.html
 * containing multiple .slide divs stacked vertically.
 * Each .slide div is 1080x1080px — this script captures each one precisely.
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const HTML_FILE = path.resolve(process.argv[2]);
const OUTPUT_DIR = path.resolve(process.argv[3] || path.join(path.dirname(HTML_FILE), 'exports'));

async function screenshotSlides() {
    if (!fs.existsSync(HTML_FILE)) {
        console.error(`❌ HTML file not found: ${HTML_FILE}`);
        process.exit(1);
    }

    if (!fs.existsSync(OUTPUT_DIR)) {
        fs.mkdirSync(OUTPUT_DIR, { recursive: true });
        console.log(`📁 Created exports directory: ${OUTPUT_DIR}`);
    }

    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
        viewport: { width: 1080, height: 1080 },
        deviceScaleFactor: 2, // Retina crisp
    });
    const page = await context.newPage();

    await page.goto(`file://${HTML_FILE}`, { waitUntil: 'networkidle', timeout: 15000 });
    await page.waitForTimeout(800); // Extra wait for Google Fonts

    const slideCount = await page.$$eval('.slide', els => els.length);
    console.log(`\n🚀 Found ${slideCount} slides — capturing PNGs...\n`);

    for (let i = 0; i < slideCount; i++) {
        const slideNum = String(i + 1).padStart(2, '0');
        const outputPath = path.join(OUTPUT_DIR, `slide-${slideNum}.png`);

        // Scroll the slide into view and clip it exactly
        const box = await page.$eval(`.slide:nth-child(${i + 1})`, el => {
            el.scrollIntoView();
            const r = el.getBoundingClientRect();
            return { x: r.x, y: r.y, width: r.width, height: r.height };
        });

        // Use clip to capture only this slide area
        // Since body scrolls the whole list, get absolute position
        const absoluteY = await page.$eval(`.slide:nth-child(${i + 1})`, el => {
            const rect = el.getBoundingClientRect();
            return window.scrollY + rect.top;
        });

        await page.evaluate((y) => window.scrollTo(0, y), absoluteY);
        await page.waitForTimeout(100);

        await page.screenshot({
            path: outputPath,
            type: 'png',
            clip: { x: box.x < 0 ? 0 : box.x, y: 0, width: 1080, height: 1080 },
        });

        const sizeKB = Math.round(fs.statSync(outputPath).size / 1024);
        console.log(`  ✓ slide-${slideNum}.png (${sizeKB} KB)`);
    }

    await browser.close();
    console.log(`\n✨ Done! All PNGs saved to:\n   ${OUTPUT_DIR}\n`);
}

screenshotSlides().catch(err => {
    console.error('❌ Failed:', err.message);
    process.exit(1);
});
