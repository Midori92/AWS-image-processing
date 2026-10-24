from PIL import Image




def process_img(in_path,out_path):

    image = Image.open(in_path)

    image.thumbnail((400,400))

    image.save(out_path)



in_val = "tests/test_img/in/hello_kitty_img.jpg"
out_val = "tests/test_img/out/hello_kitty_thumbnail2.jpg"
process_img(in_val,out_val)