#!/usr/bin/python3

import argparse
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description='Injects text into a lossless image')
    parser.add_argument('image', help="the file name of the image into which you want inject text")
    parser.add_argument('textfile', help="the name of a file containing text to inject into the image")
    parser.add_argument('output', help="the file name and extension of the output image to write")
    args = parser.parse_args()

    im = Image.open(args.image)
    # Get a list pixels as an ordered triple (R, G, B).
    pixels = list(im.getdata())
    # Flatten Pixels to a 1-dimensional array of bytes.
    pixel_bytes = [b for triple in pixels for b in triple]



    # Read the contents of the text file as an array of bytes.
    text_bytes = []
    with open(args.textfile, 'r') as text_file:
        text_bytes = bytearray(map(ord, text_file.read()))

    difference_bytes = subtract_bytes(pixel_bytes, text_bytes, padding=ord(' '))

    # Transform an array of bytes into a list of (R,G,B) tuples.
    mode = 'RGB'
    depth = len(mode)
    output_data = list(zip(*[iter(difference_bytes)] * depth))
    output_image = Image.new(mode, im.size, "black")
    output_pixels = output_image.load()

    # Write the data to the pixels object
    for i in range(len(output_data)):
        row,col = index2d(i,im.size)
        output_pixels[col,row] = output_data[i]

    output_image.save(args.output)



def subtract_bytes(listA, listB, padding=0):
    length_difference = len(listA) - len(listB)
    if length_difference < 0:
        return False

    # In case listB is too small, append padding values to ensure they are the same size..
    listB.extend([padding] * length_difference)

    # Return a list of the difference for each element as unsigned bytes.
    return [(a - b) % 2**8 for a, b in zip(listA, listB)]


# Returns 2-dimensional coordinates given index and size
def index2d(index, size):
    width, height = size
    col = index % width
    row = (index - col) / width
    return row, col

main()
