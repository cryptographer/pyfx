#! /usr/bin/env python3
import argparse
from PIL import Image, ImageDraw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'source', help='source file')
    parser.add_argument(
        'algorithm', help='algorithm (triangles, circles)')
    parser.add_argument(
        '-s', '--size', default=32, type=int, help='element size')
    args = parser.parse_args()

    input_img = Image.open(args.source)
    output_img = Image.new(
        'RGB',
        (input_img.width, input_img.height),
        color=(255, 255, 255))

    drw = ImageDraw.Draw(output_img)
    algorithm = args.algorithm
    size = args.size

    if(algorithm == 'triangles'):
        for x in range(0, input_img.width, size):
            for y in range(0, input_img.height, size):
                rgb_one = input_img.getpixel((x, y))
                rgb_two = input_img.getpixel((x, y + 1))

                drw.polygon(
                    [(x, y), (x + size, y), (x + size/2, y + size)],
                    fill=rgb_one)
                drw.polygon(
                    [(x - size/2, y + size), (x, y), (x + size/2, y + size)],
                    fill=rgb_two)

                if (input_img.width - x) <= size:
                    drw.polygon(
                        [(x + size/2, y + size), (x + size, y), (x + 3*size/2, y + size)],
                        fill=rgb_two)
    elif(algorithm == 'circles'):
        for x in range(0, input_img.width, size):
            for y in range(0, input_img.height, size):
                rgb = input_img.getpixel((x, y))
                drw.ellipse([(x, y), (x + size, y + size)], fill=rgb)

    output_img.save('output.jpg')


if __name__ == "__main__":
    main()
