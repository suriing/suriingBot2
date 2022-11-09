from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

ascii_characters_by_surface = (
    '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
)


def main():
    image = Image.open("image.png")
    # you can first resize the image if needed
    # image = image.resize((width, height))
    ascii_art = convert_to_ascii_art(image)
    save_as_text(ascii_art)


def image_to_ascii(file, max_width=128, max_height=128):
    image = Image.open(file).convert("RGB")
    resize_ratio = max(int(image.width / max_width), int(image.height / max_height))
    resize_img = image.resize(
        (int(image.width / resize_ratio), int(image.height / resize_ratio))
    )
    # resize_img = image.resize((int(image.width / resize_ratio), int(image.height / resize_ratio)), Image.Resampling.BOX)
    # image = image.resize((width, height))
    ascii_art = convert_to_ascii_art(resize_img)
    return ascii_art


def convert_to_ascii_art(image):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ""
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convert_pixel_to_character(px)
        ascii_art.append(line)
    return ascii_art


def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


def save_as_text(ascii_art):
    with open("image.txt", "w", encoding='utf-8') as file:
        for line in ascii_art:
            file.write(line)
            file.write("\n")
        file.close()


def getSize(txt, font):
    testImg = Image.new("RGB", (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textbbox((0, 0), txt, font)


def text_to_img(file, fontsize=11, ratio=2.14, colortheme="light"):
    fontname = "src/consola.ttf"
    text = ""
    with open(file, "r", encoding='utf-8') as f:
        for line in f.readlines():
            text += line
    if colortheme == "dark":
        colorText = "white"
        colorOutline = "black"
        colorBackground = "black"
    else:
        colorText = "black"
        colorOutline = "white"
        colorBackground = "white"
    font = ImageFont.truetype(fontname, fontsize)
    # width, height = getSize(text, font)
    left, top, right, bottom = getSize(text, font)
    width = abs(right - left)
    height = abs(bottom - top)
    img = Image.new("RGB", (width + 4, height + 4), colorBackground)
    d = ImageDraw.Draw(img)
    d.text((2, 2), text, fill=colorText, font=font)
    d.rectangle((0, 0, width + 3, height + 3), outline=colorOutline)
    img = img.resize((int(img.width), int(img.height / ratio)), Image.Resampling.BOX)
    return img


if __name__ == "__main__":
    main()
