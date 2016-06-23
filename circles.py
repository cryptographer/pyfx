from PIL import Image, ImageDraw

input_img = Image.open('input.jpg')
output_img = Image.new(
    'RGB',
    (input_img.width, input_img.height),
    color=(255, 255, 255))

drw = ImageDraw.Draw(output_img)
dia = 32

for x in range(0, input_img.width, dia):
    for y in range(0, input_img.height, dia):
        rgb = input_img.getpixel((x, y))
        drw.ellipse([(x, y), (x + dia, y + dia)], fill=rgb)

output_img.save('output.jpg')
