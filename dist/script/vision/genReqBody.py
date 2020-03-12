from base64 import b64encode
from os import makedirs
from os.path import join, basename, isdir
from sys import argv
import json
import requests
import zipfile

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
RESULTS_DIR = 'jsons'
if not isdir(RESULTS_DIR):
    makedirs(RESULTS_DIR)

def make_image_data_list(image_zip_filename):
    img_requests = []
    zip_file = zipfile.ZipFile(image_zip_filename, "r")
    for filename in zip_file.namelist():
        ctxt = b64encode(zip_file.read(filename)).decode()
        img_requests.append({
                'image': {'content': ctxt},
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10
                }]
        })
    zip_file.close()
    return img_requests

def make_image_data(image_zip_filename):
    imgdict = make_image_data_list(image_zip_filename)
    return json.dumps({"requests": imgdict }).encode()

if __name__ == '__main__':
    print('start')
    image_zip_filename, out_filename = argv[1:]
    print(image_zip_filename)
    print(out_filename)
    if not image_zip_filename or not out_filename:
        print("""Specify parameters collectly. $ python cvapi.py image.zip outfile""")
    else:
        image_data = make_image_data(image_zip_filename)
        body_file=open("body.json","wb")
        body_file.write(image_data)
        body_file.close()
        out_file=open(out_filename,"w")
        out_file.write("output_file=body.json\n")
        out_file.write("section=end\n")
        out_file.close()
    print('end')


