import os
from PIL import Image

INPUT_DIR = "input_images"
OUTPUT_DIR = "output_jpg"

os.makedirs(OUTPUT_DIR, exist_ok=True)

SUPPORTED_FORMATS = (".png", ".webp", ".tiff", ".bmp", ".jpeg", ".jpg")

def convert_to_jpg(input_path, output_path):
    with Image.open(input_path) as img:
        # Convert RGBA / P mode to RGB (JPG doesn't support alpha)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(
            output_path,
            "JPEG",
            quality=100,        # max quality
            subsampling=0,      # disable chroma subsampling
            optimize=True
        )

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(SUPPORTED_FORMATS):
        input_file = os.path.join(INPUT_DIR, filename)
        output_file = os.path.join(
            OUTPUT_DIR,
            os.path.splitext(filename)[0] + ".jpg"
        )

        convert_to_jpg(input_file, output_file)
        print(f"Converted: {filename}")

print("✅ All images converted successfully.")
