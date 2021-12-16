FROM python:3.8

WORKDIR /juu_jarviis

# Install Dependencies of Miniconda
RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install miniconda3
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
#    && \
#    echo "conda create -n venv" >> ~/.bashrc && \
#    echo "conda activate venv" >> ~/.bashrc

COPY . .
COPY requirements.txt requirements.txt

CMD ["python", "manage.py", "runserver"]

ENV TZ=Asia/Seoul

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000