FROM python:2.7-alpine

RUN apk add --no-cache \
        libc-dev \
        linux-headers \
        tar \
        gcc

RUN mkdir /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY . /code/
COPY config/ /etc

RUN rm -rf public/*

WORKDIR /code

# add python path
ENV PYTHONPATH=/code:$PATH

ADD https://releases.hashicorp.com/consul-template/0.18.3/consul-template_0.18.3_linux_amd64.tgz /consul-template.tgz
RUN tar -xaf /consul-template.tgz && mv consul-template /bin/

VOLUME /var/log /etc

EXPOSE 8028

CMD ["consul-template", "--config", "/etc/perseus.hcl"]
