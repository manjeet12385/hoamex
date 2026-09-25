import os
from PIL import Image

image_dir = r"c:\Users\Divyanshi123456\Music\hoamex\images"

for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        filepath = os.path.join(image_dir, filename)
        try:
            file_size = os.path.getsize(filepath)
            # Only optimize if file size is > 100KB
            if file_size > 100 * 1024:
                img = Image.open(filepath)
                
                # Convert RGBA to RGB if saving as JPEG
                if filename.lower().endswith(('.jpg', '.jpeg')) and img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Resize if too large
                max_size = (1200, 1200)
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                if filename.lower().endswith(('.jpg', '.jpeg')):
                    img.save(filepath, "JPEG", optimize=True, quality=60)
                elif filename.lower().endswith('.png'):
                    img.save(filepath, "PNG", optimize=True)
                    
                new_size = os.path.getsize(filepath)
                print(f"Optimized {filename}: {file_size/1024:.1f}KB -> {new_size/1024:.1f}KB")
        except Exception as e:
            print(f"Error optimizing {filename}: {e}")
