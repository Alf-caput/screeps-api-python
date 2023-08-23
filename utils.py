import base64
import gzip
import json


def gz_to_dict(data_with_gz_prefix):
    # Remove prefix "gz:" retain value in base64
    value_base64 = data_with_gz_prefix[3:]

    # Decode base64 value
    compressed_data = base64.b64decode(value_base64)

    # Decompress gzip value
    decompressed_data = gzip.decompress(compressed_data)

    # Load data into dictionary
    return json.loads(decompressed_data)
