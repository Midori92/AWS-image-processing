from PIL import Image

image = Image.open("tests/test_img/in/hello_kitty_img.jpg")

image.thumbnail((400,400))

image.save("tests/test_img/out/hello_kitty_thumbnail.jpg")