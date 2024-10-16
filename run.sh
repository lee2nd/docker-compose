rundocker stop at_tempview
docker rm -f at_tempview
docker run -t -d --restart always --name at_tempview -v /etc/localtime:/etc/localtime:ro -v /home/ivan/Program/AT_CODE_VIEW:/app at_image python at_tempview.py
