from PIL import Image
import glob
import os

out_dir = '/opt/icons/'
print(os.getcwd())
os.chdir('images')

for image in glob.glob('ic_*'):
    im = Image.open(image)
    im2 = im.rotate(90).resize((128, 128)).convert("RGB")
    im2.save(os.path.join(out_dir, image), format='jpeg')




