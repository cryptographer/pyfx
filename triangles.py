from PIL import Image, ImageDraw


def main():
    input_img = Image.open('input.jpg')
    output_img = Image.new(
        'RGB',
        (input_img.width, input_img.height),
        color=(255, 255, 255))

    drw = ImageDraw.Draw(output_img)
    side = 32

    for x in range(0, input_img.width, side):
        for y in range(0, input_img.height, side):
            rgb_one = input_img.getpixel((x, y))
            rgb_two = input_img.getpixel((x, y + 1))

            drw.polygon(
                [(x, y), (x + side, y), (x + side/2, y + side)],
                fill=rgb_one)
            drw.polygon(
                [(x - side/2, y + side), (x, y), (x + side/2, y + side)],
                fill=rgb_two)

            if (input_img.width - x) <= side:
                drw.polygon(
                    [(x + side/2, y + side), (x + side, y), (x + 3*side/2, y + side)],
                    fill=rgb_two)

    output_img.save('output.jpg')


if __name__ == "__main__":
    main()
