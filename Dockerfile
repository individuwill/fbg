FROM alpine:3.8

RUN apk add --update --no-cache \
  python3 \
  py3-gunicorn \
  && rm -rf /var/cache/apk/*

WORKDIR /app

COPY app /app

EXPOSE 80

ENV username user
ENV password pass

CMD ["gunicorn", "-b", "0.0.0.0:80", "web:app"]

RUN python3 -m pip install -r requirements.txt
