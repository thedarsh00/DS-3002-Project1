FROM python:3
WORKDIR /data
ADD . /data
RUN pip install -r requirements.txt
CMD ["script.py"]
ENTRYPOINT ["python3"]