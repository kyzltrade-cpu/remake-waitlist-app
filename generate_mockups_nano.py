import os
import sys
from PIL import Image
import io

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai is not installed. Please run with: uv run --with google-genai,Pillow python3 generate_mockups_nano.py")
    sys.exit(1)

# Initialize the Gemini/Google client
client = genai.Client()

mockups = [
    {
        "filename": "mockup-scanner.jpg",
        "target_w": 588,
        "target_h": 1280,
        "prompt": "An elegant, high-fidelity App Store screenshot mockup for a luxury beauty app. A realistic, front-facing matte black iPhone 15 Pro frame centered on a solid matte light pink (#FFE6EC) background. Above the phone, a clean, bold title in an elegant serif typeface reads: 'IS YOUR MAKEUP SAFE?'. Inside the iPhone screen, an active barcode scanner is shown. The camera view is sharp, displaying the back of a luxury cosmetic cream bottle (Rhode/Chanel style). A crisp, flat solid rose-gold reticle outlines the barcode, with a thin solid pink horizontal laser line. The app's bottom panel is a solid flat charcoal-black (#1C1C1C) card with neat, white geometric sans-serif text reading 'Align Barcode'. No messy 3D glass, no translucent layers, no gradient blobs, 100% flat professional graphic design."
    },
    {
        "filename": "mockup-analysis-1.jpg",
        "target_w": 652,
        "target_h": 1280,
        "prompt": "A high-end App Store screenshot mockup of a beauty product analysis screen. A realistic, front-facing matte black iPhone 15 Pro frame centered on a solid matte light pink (#FFE6EC) background. Inside the iPhone screen, a clean white interface presents a skincare formula analysis for a trending makeup product. In the upper half is a flat, solid dark charcoal circular score ring showing a low score of '24/100' in a bold, crisp sans-serif font. Below the score, a flat, solid red warning banner displays 'NOT ACNE SAFE' in stark white typography. Underneath is a neat, high-contrast list of ingredients with small warning icons: 'Bismuth Oxychloride - Irritant Risk' and 'Synthetic Fragrance - Allergen' in minimalist black text. Flat vector style, clean alignment, absolutely no frosted glass, no transparency, no slop."
    },
    {
        "filename": "mockup-analysis-2.jpg",
        "target_w": 652,
        "target_h": 1280,
        "prompt": "A premium App Store screenshot mockup for a cosmetic rating app showing a side-by-side comparison screen. A realistic, front-facing matte black iPhone 15 Pro frame centered on a solid matte light pink (#FFE6EC) background. Inside the iPhone screen, the app displays a product comparison. On the left half, a column with a dark-red card at the top reads 'PORE CLOGGING' in clean white typography, showing a toxic product with comedogenic ratings. On the right half, a column with a clean white card reads 'CLEAN ALTERNATIVE' in black typography, displaying a safe organic replacement with '100% SAFE' badge. Minimalist, professional UI comparing ingredients side-by-side, 100% flat design, zero glass, zero blur, zero gradient blobs."
    },
    {
        "filename": "mockup-analysis-3.jpg",
        "target_w": 652,
        "target_h": 1280,
        "prompt": "A luxury beauty App Store screenshot mockup for an AI face-scanning app. A realistic, front-facing matte black iPhone 15 Pro frame centered on a solid matte light pink (#FFE6EC) background. Inside the iPhone screen, the app displays a computer-vision shade-matching analysis. It shows a close-up photo of a woman's cheek with clean skin, overlaid with a solid rose-gold badge that reads '98% SHADE MATCH'. Below, a flat solid black (#1C1C1C) card recommends the exact product match: 'Fenty Beauty Pro Filt'r - Shade 145N' in crisp, clean white sans-serif typography. Flat luxury branding, solid backgrounds, extremely clean layout, zero 3D glass, zero reflections, zero slop."
    }
]

def generate_mockup(item):
    filename = item["filename"]
    target_w = item["target_w"]
    target_h = item["target_h"]
    prompt = item["prompt"]
    
    print(f"\nGenerating {filename} with Imagen 4.0...")
    print(f"Prompt: {prompt[:100]}...")
    
    response = client.models.generate_images(
        model="imagen-4.0-generate-001",
        prompt=prompt,
        config=types.GenerateImagesConfig(
            numberOfImages=1,
            aspectRatio="9:16",
            outputMimeType="image/jpeg"
        )
    )
    
    if not response.generated_images:
        raise Exception(f"Failed to generate image for {filename}")
        
    image_bytes = response.generated_images[0].image.image_bytes
    img = Image.open(io.BytesIO(image_bytes))
    
    print(f"Original generated size: {img.size}")
    
    # Resize keeping aspect ratio 9:16, but matching target_h (1280)
    # 9:16 scaled to height 1280 has width: 1280 * 9 / 16 = 720
    scaled_w = 720
    scaled_h = 1280
    
    print(f"Resizing to temporary size: ({scaled_w}, {scaled_h})")
    resized_img = img.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)
    
    # Center-crop to target width
    left = (scaled_w - target_w) // 2
    right = left + target_w
    top = 0
    bottom = target_h
    
    print(f"Center cropping to final size: ({target_w}, {target_h})")
    final_img = resized_img.crop((left, top, right, bottom))
    
    # Save image
    output_dir = "/Users/kyzl/remake-waitlist-app"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    final_img.save(output_path, "JPEG", quality=95)
    print(f"Successfully saved to {output_path}")

def main():
    print("Starting App Store Mockup Generation via Google GenAI (Imagen 4.0)...")
    for item in mockups:
        generate_mockup(item)
    print("\nAll 4 mockups successfully generated and saved!")

if __name__ == "__main__":
    main()
