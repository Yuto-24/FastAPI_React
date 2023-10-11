FROM node:18.16.0-bullseye

# 環境変数 proxy設定
ENV http_proxy=http://proxy.otsuka-shokai.co.jp:8080
ENV https_proxy=http://proxy.otsuka-shokai.co.jp:8080
ENV TZ=Asia/Tokyo

RUN apt-get -y update && \
    apt install -y git && \
    apt install -y wget && \
    apt install -y curl

# Python のインストール
WORKDIR /root/
RUN wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tar.xz \
    && tar xvf Python-3.9.13.tar.xz \
    && cd Python-3.9.13 \
    && ./configure --enable-optimizations \
    && make \
    && make install
RUN rm Python-3.9.13.tar.xz

# pip のダウンロード
WORKDIR /root/Python-3.9.13
RUN ln -fs /root/Python-3.9.13/python /usr/bin/python
# RUN apt-get install -y --no-install-recommends python3-pip
# RUN pip3 install --upgrade pip
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python
RUN rm -rf /var/lib/apt/lists/*

# python 3.9.13 インストール後にライブラリをインストール.
WORKDIR /temp
ADD ./requirements.txt /temp
RUN pip install --proxy="http://proxy.otsuka-shokai.co.jp:8080/" --upgrade pip
RUN pip install --proxy="http://proxy.otsuka-shokai.co.jp:8080/" -r requirements.txt

RUN export http_proxy=http://proxy.otsuka-shokai.co.jp:8080 \
    && export https_proxy=http://proxy.otsuka-shokai.co.jp:8080 \
    && jupyter notebook --generate-config

RUN export LC_ALL=C.UTF-8

# エイリアスの追加
RUN echo "alias ll='ls -al'" >> ~/.bashrc && \
    echo "alias python='python3'" >> ~/.bashrc && \
    echo "alias pip='pip3'" >> ~/.bashrc && \
    echo "source ~/.bashrc" > ~/.bash_profile

# コンテナログイン時のディレクトリ指定
WORKDIR /projects/
CMD [ "\bin\bash" ]
