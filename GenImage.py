#ev=Σdict[pos_y,pos_x,words,R,G,B]

from PIL import Image

img = Image.open('')

pixels = img.load()

w, h = img.size

for i in range(w):#幅
    for j in range(h):#高さ
        pixels[i, j] = (0, 255, 0)#RGB
        pixel_value = img.getpixel((i, j))
        #print(str(pixel_value))

img.save('')
