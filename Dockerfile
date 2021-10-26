FROM ninai/microns-base 
LABEL maintainer="Stelios Papadopoulos <spapadop@bcm.edu>"

RUN pip3 install \
        cloud-volume \
        caveclient \
        nglui \
        slackclient

WORKDIR /root
ARG CLOUDVOLUME_TOKEN
RUN mkdir -p .cloudvolume/secrets
RUN echo "{\"token\": \"${CLOUDVOLUME_TOKEN:-}\"}" > .cloudvolume/secrets/cave-secret.json

WORKDIR /src

# MICRONS PACKAGES
RUN git clone https://github.com/cajal/microns-materialization.git
RUN pip3 install -e /src/microns-materialization/python

# ALLEN INSTITUTE
RUN git clone -b phase3 --single-branch https://github.com/AllenInstitute/em_coregistration.git
RUN pip3 install -e /src/em_coregistration

# MISC PACKAGES
RUN pip3 install git+https://github.com/spapa013/wridgets.git

# CURRENT PACKAGE
COPY . /src/microns-coregistration
RUN pip install -e /src/microns-coregistration/python