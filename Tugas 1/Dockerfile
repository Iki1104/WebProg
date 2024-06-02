FROM python:3.12.2

RUN mkdir app
WORKDIR /app

COPY requirement.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirement.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["index.py"]