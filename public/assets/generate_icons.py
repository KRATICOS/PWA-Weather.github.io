from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import os

# Define the resolutions (10 different sizes starting from 16x16)
resolutions = [
    (16, 16),
    (32, 32),
    (64, 64),
    (128, 128),
    (256, 256),
    (512, 512),
    (1024, 1024),
    (2048, 2048),
    (4096, 4096),
    (8192, 8192),
]

# Path to the iconoh.svg file
svg_path = os.path.join(os.path.dirname(__file__), 'iconoh.svg')

# Convert SVG to PNG using svglib
print(f"Converting {svg_path} to PNG...")
renderer = svg2rlg(svg_path)
if renderer is None:
    raise ValueError("Failed to parse SVG file")

# Render to PIL Image
img = renderPM.drawToPIL(renderer)

# Create directory for output if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), 'icons')
os.makedirs(output_dir, exist_ok=True)

# Generate images at different resolutions
for i, (width, height) in enumerate(resolutions, 1):
    print(f"Generating image {i}/10: {width}x{height}")
    
    # Resize the image
    resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    # Save as PNG
    output_path = os.path.join(output_dir, f'iconoh_{width}x{height}.png')
    resized_img.save(output_path, 'PNG')
    print(f"Saved: {output_path}")

print("Done! Generated 10 images at different resolutions.")