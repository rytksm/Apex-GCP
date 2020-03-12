from base64 import b64encode
from os import makedirs
from os.path import join, basename, isdir, isfile
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
RESULTS_DIR = 'jsons'
if not isdir(RESULTS_DIR):
    makedirs(RESULTS_DIR)

def make_image_data_list(image_filenames):
    img_requests = []
    for imgname in image_filenames:
        if isfile(imgname):
            with open(imgname, 'rb') as f:
                ctxt = b64encode(f.read()).decode()
                img_requests.append({
                        'image': {'content': ctxt},
                        'features': [{
                            'type': 'LABEL_DETECTION',
                            'maxResults': 5
                        }]
                })
    return img_requests

def make_image_data(image_filenames):
    imgdict = make_image_data_list(image_filenames)
    return json.dumps({"requests": imgdict }).encode()

def request_ocr(api_key, image_filenames):
    response = requests.post(ENDPOINT_URL,
                            data=make_image_data(image_filenames),
                            params={'key': api_key},
                            headers={'Content-Type': 'application/json'})
    return response

if __name__ == '__main__':
    api_key, image_filenames = argv[1:]
    if not api_key or not image_filenames:
        print("""$ python cvapi.py api_key image.jpg""")
    else:
        response = request_ocr(api_key, image_filenames)
        if response.status_code != 200 or response.json().get('error'):
            print(response.text)
        else:
            for idx, resp in enumerate(response.json()['responses']):
                imgname = image_filenames[idx]
                jpath = join(RESULTS_DIR, basename(imgname) + '.json')
                print (json.dumps(resp, indent=2))


