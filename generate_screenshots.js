const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const sizes = {
    "6.7-inch": { width: 1290, height: 2796 },
    "6.5-inch": { width: 1284, height: 2778 },
    "5.5-inch": { width: 1242, height: 2208 }
};

const baseUrl = "file://" + path.resolve(__dirname, "appstore_gen.html");

if (!fs.existsSync("screenshots")) {
    fs.mkdirSync("screenshots");
}

(async () => {
    const browser = await chromium.launch();
    
    for (const [sizeName, dim] of Object.entries(sizes)) {
        const page = await browser.newPage({ viewport: dim });
        for (let i = 0; i < 4; i++) {
            await page.goto(`${baseUrl}?i=${i}`);
            await page.waitForLoadState('networkidle');
            await page.waitForTimeout(1000); // Wait for fonts/images
            
            const outputPath = path.join("screenshots", `${sizeName}_${i+1}.png`);
            await page.screenshot({ path: outputPath });
            console.log(`Generated ${outputPath}`);
        }
    }
    await browser.close();
})();