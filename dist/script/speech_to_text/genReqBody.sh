#!/bin/sh
# predict mnist
# $1 : image zip file name
# $2 : result file name
echo "-----" >> /home/acms/gcp/speech_to_text/genReqBody.sh.log
pwd >> /home/acms/gcp/speech_to_text/genReqBody.sh.log
echo $* >> /home/acms/gcp/speech_to_text/genReqBody.sh.log
ls -l >> /home/acms/gcp/speech_to_text/genReqBody.sh.log
ls -l $1 >> /home/acms/gcp/speech_to_text/genReqBody.sh.log
python $(dirname $0)/genReqBody.py $1 $2 >> /home/acms/gcp/speech_to_text/genReqBody.sh.log 2>&1
ls -l >> /home/acms/gcp/speech_to_text/genReqBody.sh.log
ls -l $2 >> /home/acms/gcp/speech_to_text/genReqBody.sh.log
exit 0


