FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    texlive-full \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-science \
    texlive-publishers \
    texlive-lang-english \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . . 