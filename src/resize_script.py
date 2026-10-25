from PIL import Image
import boto3

s3 = boto3.client("s3")

def process_img(in_path,out_path):



    image = Image.open(in_path)

    image.thumbnail((400,400))

    image.save(out_path)



