
import os
import tempfile
from urllib.parse import unquote_plus

import boto3
from src.resize_script import process_img

s3 = boto3.client("s3")


def lambda_handler(event, context):
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])

        # Only process files uploaded to input/
        if not key.startswith("input/"):
            continue

        filename = os.path.basename(key)

        # Lambda can write temporary files to /tmp
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = os.path.join(temp_dir, filename)
            output_path = os.path.join(
                temp_dir, f"thumbnail-{filename}"
            )

            # Download the original image from S3
            s3.download_file(bucket, key, input_path)

            # Reuse your existing Python function
            process_img(input_path, output_path)

            # Upload the thumbnail to output/
            output_key = f"output/thumbnail-{filename}"
            s3.upload_file(output_path, bucket, output_key)

    return {"statusCode": 200, "body": "Image processing complete"}
