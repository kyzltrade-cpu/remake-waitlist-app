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
        "prompt": "A premium, high-fidelity mobile app UI screenshot on an iPhone screen, showcasing an active barcode scanner feature for skincare. The camera viewfinder occupies the upper portion, displaying a crisp, detailed view of the back of a luxury pink-and-white cosmetic cream tube. A glowing rose-gold neon rectangle outlines the barcode, with a thin pink scanning laser line active across it. The app's bottom menu is a frosted glass (glassmorphism) panel with the text 'Align Barcode' in a clean geometric sans-serif font. The background is a soft pastel pink (#FFD1E3) and warm ivory studio setup. No random messy graphics, very clean design."
    },
    {
        "filename": "mockup-analysis-1.jpg",
        "target_w": 652,
        "target_h": 1280,
        "prompt": "A luxury mobile app UI screenshot on an iPhone screen, presenting a skincare ingredient analysis. In the center is a beautifully animated pink circular score ring displaying a low score of '28' in a bold, charcoal-grey sans-serif font. Below the score, an elegant red alert card highlights 'TOXIC INGREDIENTS DETECTED' in clear white text. Underneath is a perfectly styled list with bullet points: 'Bismuth Oxychloride - Irritant Risk' and 'Fragrance/Parfum - Allergen' in modern, minimalist typography. The overall color scheme is pastel pink (#FFD1E3), deep red, and soft cream, looking extremely professional and clean."
    },
    {
        "filename": "mockup-analysis-2.jpg",
        "target_w": 652,
        "target_h": 1280,
        "prompt": "A sleek cosmetic app UI design screenshot on an iPhone screen, displaying a skin barrier and acne-safe rating page. At the top of the interface, a prominent warning card displays 'NOT ACNE SAFE' in bold white typography on a sharp crimson red background. Below is a beautifully detailed list of comedogenic ingredients with rating badges, such as 'Ethylhexyl Palmitate - Rating: 4/5' in elegant sans-serif typography. Glassmorphic containers, pastel pink and warm ivory layout. The interface is clean, uncluttered, with pixel-perfect alignment."
    },
    {
        "filename": "mockup-analysis-3.jpg",
        "target_w": 652,
        "target_h": 1280,
        "prompt": "A luxury mobile app UI screenshot on an iPhone screen, presenting a shade-matching feature for makeup. It shows a close-up photo of a woman's cheek with subtle, elegant color swatches, overlaid with a glowing pink ring that reads '98% SHADE MATCH' in a bold serif font. Below, a glassmorphic card recommends the exact makeup shade: 'Fenty Beauty Pro Filt'r 145N' in modern, clean typography. The background is a warm ivory and pastel pink marble, accented with delicate gold details, embodying a premium, high-converting cosmetic aesthetic."
    }
]

def generate_mockup(item):
    filename = item["filename"]
    target_w = item["target_w"]
    target_h = item["target_h"]
    prompt = item["prompt"]
    
    print(f"\nGenerating {filename} with Nano Banana (Imagen 4.0)...")
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
    output_path = os.path.join("/Users/kyzl/remake-waitlist-app", filename)
    final_img.save(output_path, "JPEG", quality=95)
    print(f"Successfully saved to {output_path}")

def main():
    print("Starting App Store Mockup Generation via Google GenAI (Nano Banana)...")
    for item in mockups:
        generate_mockup(item)
    print("\nAll 4 mockups successfully generated and saved!")

if __name__ == "__main__":
    main()
