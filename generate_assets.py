import os
import subprocess
from PIL import Image
import zipfile

def run_node_generation():
    print("Running Node.js Playwright screenshot generator...")
    result = subprocess.run(["node", "generate_screenshots.js"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error during Node.js generation:")
        print(result.stderr)
        raise Exception("Node screenshot generation failed.")
    print("Node.js generation complete.")
    print(result.stdout)

def convert_png_to_jpg():
    print("Converting generated PNGs to JPEGs...")
    png_dir = "screenshots"
    jpg_dir = "screenshots_jpeg"
    
    if not os.path.exists(jpg_dir):
        os.makedirs(jpg_dir)
        
    for filename in os.listdir(png_dir):
        if filename.endswith(".png"):
            png_path = os.path.join(png_dir, filename)
            jpg_name = filename.replace(".png", ".jpg")
            jpg_path = os.path.join(jpg_dir, jpg_name)
            
            with Image.open(png_path) as img:
                # Convert RGBA to RGB since JPEG doesn't support alpha channel
                rgb_img = img.convert("RGB")
                rgb_img.save(jpg_path, "JPEG", quality=90)
                print(f"Converted {png_path} -> {jpg_path}")

def zip_assets():
    print("Creating ZIP file of all screenshots...")
    zip_path = "appstore_screenshots_all.zip"
    
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
        # Add PNG screenshots
        png_dir = "screenshots"
        for filename in os.listdir(png_dir):
            if filename.endswith(".png"):
                filepath = os.path.join(png_dir, filename)
                zip_file.write(filepath, os.path.join("PNG", filename))
                
        # Add JPEG screenshots
        jpg_dir = "screenshots_jpeg"
        for filename in os.listdir(jpg_dir):
            if filename.endswith(".jpg"):
                filepath = os.path.join(jpg_dir, filename)
                zip_file.write(filepath, os.path.join("JPEG", filename))
                
    print(f"Created zip archive: {zip_path}")
    print(f"Size of ZIP: {os.path.getsize(zip_path) / 1024:.2f} KB")

if __name__ == "__main__":
    run_node_generation()
    convert_png_to_jpg()
    zip_assets()
