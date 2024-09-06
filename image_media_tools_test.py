

import json
from geek_image_media_tools_util import ImageMediaTools

imageMediaTools = ImageMediaTools()
# Load JSON data
with open('blockchain_data.json', 'r') as f:
    data = json.load(f)

# Specify the path to your custom font file
font_path = 'Gotham-Rounded-Bold_21016.ttf'

# Create SVG for each main item
for key, value in data.items():
    if isinstance(value, list):
        # For lists, create separate SVGs for each item
        for i, item in enumerate(value):
            print('value ' + value)
            imageMediaTools.create_svg(f"{key}_{i + 1}", item, f"{key}_{i + 1}.svg", font_path)
    else:
        imageMediaTools.create_svg(key, value, f"{key}.svg", font_path)

print("SVG files have been created with custom font.")
