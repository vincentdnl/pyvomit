from PIL import Image

def gen_palette (integer):
    base_hue = (integer % 7) * 32 - 1
    compl_hue = 255 - base_hue

    return { 
        0: (0, 0, 70),
        1: (0, 0, 130),
        2: (0, 0, 190),
        3: (0, 0, 220),

        4: (base_hue, 200, 200),
        6: (base_hue, 200, 160),
        5: (base_hue, 200, 100),

        7: (base_hue, 80, 200),
        8: (base_hue, 80, 130),

        9: (compl_hue, 200, 160),
        10: (compl_hue, 80, 130),
        }


def _vomit(bigint, img):
    pixels = img.load()
    int_to_clr = gen_palette(bigint)
    for j in range(img.size[1]):
        for i in range((img.size[0] + 1) // 2):
            pixels[i,j] = int_to_clr[bigint % 11]
            pixels[img.size[0] - i - 1,j] = int_to_clr[bigint % 11]
            bigint = bigint // 11
    if bigint > 0:
        raise ValueError('Integer too big')
    img = img.resize((img.size[0] * 5,img.size[1] * 5))

def pyvomit128(bigint, name):
    img = Image.new('HSV', (9, 8), "black")
    _vomit(bigint, img)
    img.convert('RGB').save(name)

def pyvomit64(bigint, name):
    img = Image.new('HSV', (7, 5), "black")
    _vomit(bigint, img)
    img.convert('RGB').save(name)

for i in range(6):
    pyvomit64(2**64 - 32, 'small{i}.png'.format(i=i))
