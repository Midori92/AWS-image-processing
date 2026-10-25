from PIL import Image

from src.resize_script import process_img


def test_resize_image():
    input_path = "tests/test_img/in/hello_kitty_img.jpg"
    output_path = "tests/test_img/out/hello_kitty_thumbnail.jpg"

    process_img(input_path, output_path)

    image = Image.open(output_path)

    assert image.width <= 400
    assert image.height <= 400