#!/usr/bin/python3

import argparse
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description='Writes the difference in pixel data of two lossless images to standard output')
    parser.add_argument('subtractor', help="the file name of the image from which you are subtracting pixel data")
    parser.add_argument('subtractend', help="the file name of a image which whose pixel data is being subtracted")
    args = parser.parse_args()

    imgA = Image.open(args.subtractor)
    # Get a list pixels as an ordered triple (R, G, B).
    pixelsA = list(imgA.getdata())
    # Flatten Pixels to a 1-dimensional array of bytes.
    pixel_bytesA = [b for triple in pixelsA for b in triple]

    imgB = Image.open(args.subtractend)
    # Get a list pixels as an ordered triple (R, G, B).
    pixelsB = list(imgB.getdata())
    # Flatten Pixels to a 1-dimensional array of bytes.
    pixel_bytesB = [b for triple in pixelsB for b in triple]

    # Subtract the bytes, thereby retrieving the hidden text
    difference_bytes = subtract_bytes(pixel_bytesA, pixel_bytesB, ord(' '))

    # convert each byte to a character,
    # convert the array to a string,
    # strip trailing whitespace,
    # and write to stdout
    print(''.join(map(chr,difference_bytes)).strip())


def subtract_bytes(listA, listB, padding=0):
    length_difference = len(listA) - len(listB)
    if length_difference < 0:
        return False

    # In case listB is too small, append padding values to ensure they are the same size..
    listB.extend([padding] * length_difference)

    # Return a lexiist of the difference for each element as unsigned bytes.
    return [(a - b) % 2**8 for a, b in zip(listA, listB)]

main()
