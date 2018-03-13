FROM ubuntu:xenial
RUN apt-get update && apt-get install -y python3 python3-pip redis-server mongodb
ENV PYTHONIOENCODING UTF-8
RUN /bin/bash -c "pip3 install --upgrade pip setuptools \
    && pip3 install redis pymongo"
WORKDIR /home/code
VOLUME /home/code   
CMD /bin/bash
