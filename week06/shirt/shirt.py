from PIL import Image, ImageOps
import os
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid input - Path.")
    elif not format_check(sys.argv[1]) and format_check(sys.argv[2]):
        sys.exit("Invalid Input")
    elif not format_same(sys.argv[1], sys.argv[2]):
        sys.exit("Input and ouput have different extensions.")

    else:
        overlay_image(sys.argv[1], sys.argv[2])


def format_check(input_file):
    valid_formats = ["jpg", "jpeg", "png"]
    _, ext = input_file.split(".", maxsplit=1)

    # If the format isn't valid, return False
    if ext in valid_formats:
        return True
    else:
        return False


def format_same(input_file, output_file):
    _, ext = input_file.split(".", maxsplit=1)

    # If the format isn't valid, return False
    if output_file.endswith(ext):
        return True
    else:
        return False


def overlay_image(input_file, output_file):
    shirt = Image.open("shirt.png")
    photo = Image.open(input_file)

    a, b = shirt.size
    photo = ImageOps.fit(photo, (a, b))

    photo.paste(shirt, shirt)
    photo.save(output_file)


if __name__ == "__main__":
    main()
