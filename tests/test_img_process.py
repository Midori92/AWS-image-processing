
from PIL import Image
from src.resize_script import process_img


def test_resize_image(tmp_path):
    input_path = tmp_path / "input.jpg"
    output_path = tmp_path / "thumbnail.jpg"

    # 1. Create a sample image before processing it
    Image.new("RGB", (800, 600), color="red").save(input_path)

    process_img(input_path, output_path)

    
    assert output_path.exists()

    with Image.open(output_path) as image:
        assert image.width <= 400
        assert image.height <= 400
