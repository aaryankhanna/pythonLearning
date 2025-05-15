import os
import plistlib
import re
from PIL import Image
# ========== CONFIG ========== #
plist_file = 'TableCommonElements.plist'  # Your plist file
png_file = 'TableCommonElements.png'    # Your sprite sheet image
output_folder = 'output_sprites'  # Where to save extracted images
# ============================ #
# Helper to parse rect strings like '{{205,177},{138,68}}'
def parse_texture_rect(rect_str):
    nums = list(map(int, re.findall(r'\d+', rect_str)))
    return nums[0], nums[1], nums[2], nums[3]  # x, y, width, height
# Load the .plist data
with open(plist_file, 'rb') as f:
    plist_data = plistlib.load(f)
frames = plist_data['frames']
sprite_sheet = Image.open(png_file)
# Create output directory
os.makedirs(output_folder, exist_ok=True)
# Extract and save each frame
for frame_name, frame_info in frames.items():
    rect = frame_info.get('textureRect')
    rotated = frame_info.get('textureRotated', False)
    x, y, w, h = parse_texture_rect(rect)
    box = (x, y, x + w, y + h)
    sprite = sprite_sheet.crop(box)
    if rotated:
        sprite = sprite.rotate(90, expand=True)
    # Clean file name and save
    clean_name = frame_name.replace('/', '_')
    save_path = os.path.join(output_folder, clean_name)
    sprite.save(save_path)
print(f':white_tick: Extracted {len(frames)} sprites to ‘{output_folder}’')