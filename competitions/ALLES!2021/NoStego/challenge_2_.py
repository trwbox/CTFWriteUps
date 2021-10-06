from PIL import Image
import sys

di_values = [358, 504, 406, 48, 6, 232, 438, 32, 422, 472, 214, 16, 70, 200, 246, 0, 486, 440, 22, 496, 134, 168, 54, 480, 38, 408, 342, 464, 198, 136, 374, 219]
dj_values = [412, 294, 20, 150, 12, 454, 388, 438, 124, 358, 244, 470, 236, 6, 100, 246, 348, 422, 468, 278, 460, 70, 324, 54, 60, 486, 180, 86, 172, 134, 36, 29]

if len(sys.argv) != 3:
    print("Usage: %s [infile] [outfile]" % sys.argv[0])
    sys.exit(1)

image = Image.open(sys.argv[1]).convert("F")
width, height = image.size
result = Image.new("F", (width, height))

ROUNDS = 32

for i in range(width):
    for j in range(height):
        value = 0
        for k in range(ROUNDS):
            value += image.getpixel(((i - di_values[k]) % width, (j - dj_values[k] + (i - di_values[k]) * width) % height))
        result.putpixel((i, j), value / ROUNDS)

result = result.convert("RGB")
result.save(sys.argv[2])
print("Done")

