# Bulk Image to JPG Converter (Python)

A simple Python script to convert multiple images into high-quality JPG format without noticeable quality loss.  
Supports common formats like PNG, WEBP, TIFF, BMP, and JPEG.

This tool is ideal for batch processing images while keeping file size reasonable and image quality as high as possible.

---

## Features

- Batch converts multiple images to JPG
- Preserves maximum image quality
- Automatically handles alpha transparency
- Simple folder-based workflow
- Fast and lightweight (uses Pillow)

---

## Supported Input Formats

- PNG
- WEBP
- TIFF
- BMP
- JPEG / JPG

---

## Requirements

- Python 3.7+
- Pillow (PIL)

Install dependency:

```bash
pip install pillow
````

---

## Project Structure

```
project/
├── input_images/    # Place images to be converted here
├── output_jpg/      # Converted JPG images will be saved here
├── convert.py       # Conversion script
└── README.md
```

---

## How to Use

1. Place all source images inside the `input_images` folder.
2. Run the script:

```bash
python convert.py
```

3. Converted JPG images will appear in the `output_jpg` folder.

---

## How Quality Is Preserved

The script saves images using:

* `quality=100`
* `subsampling=0`
* `optimize=True`

This produces the highest possible JPG quality.
Note that **JPG is a lossy format**, so 100% lossless conversion is not possible, but visual quality loss is minimized.

---

## Notes

* Images with transparency (PNG/WebP) are automatically converted to RGB.
* Original filenames are preserved.
* Existing files in the output folder may be overwritten.

---

## Customization Ideas

You can easily extend this script to:

* Resize images during conversion
* Process subfolders recursively
* Preserve EXIF metadata
* Convert to other formats
* Add a GUI interface

---

## License

MIT License – free to use, modify, and distribute.
