#!/bin/sh
# predict mnist
# $1 : image file name
echo '-----' >> /home/acms/gcp/vision/genRequestBody2.sh.log
echo $1 >> /home/acms/gcp/vision/genRequestBody2.sh.log
file $1 >> /home/acms/gcp/vision/genRequestBody2.sh.log
echo -n '{"requests": [{"image": {"content": "'
base64 | tr -d '\n'
echo -n '"}, "features": [{"type": "LABEL_DETECTION", "maxResults": 10}]}]}'
exit 0

