FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2023.3.1
RUN pip install tensorflow==1.13.1
RUN pip install pandas==1.3.5
RUN pip install PyYAML==6.0.1
RUN pip install Keras==2.0.6
RUN pip install h5py==2.10.0

WORKDIR /repo
COPY . /repo
