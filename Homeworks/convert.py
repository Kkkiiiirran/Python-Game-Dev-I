import os
import cairosvg

root_folder = r'C:\Users\Kiranpreet Kaur\OneDrive\Documents\JetLearn\Python Game Dev - I'  # Change to your root folder

for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith('.svg'):
            svg_path = os.path.join(dirpath, filename)
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(dirpath, png_filename)

            print(f"Converting {svg_path} → {png_path}")
            try:
                cairosvg.svg2png(url=svg_path, write_to=png_path)
            except Exception as e:
                print(f"Failed to convert {svg_path}: {e}")

print("✅ All SVGs have been converted to PNGs where possible.")
