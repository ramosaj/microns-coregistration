FROM ninai/microns-base 
# TODO: add to dockerhub/at-docker
# FROM microns-base
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

# ALLEN INSTITUTE
RUN git clone -b phase3 --single-branch https://github.com/AllenInstitute/em_coregistration.git
RUN pip3 install -e /src/em_coregistration

# MISC PACKAGES
RUN pip3 install git+https://github.com/spapa013/wridgets.git

# CURRENT PACKAGE
# TODO: torch rebuilds partially after edit, consider improving docker caching (e.g. maybe with requirements.txt install in separate step)
COPY . /src/microns-coregistration
RUN pip install -e /src/microns-coregistration/python/microns-coregistration
RUN pip install -e /src/microns-coregistration/python/microns-coregistration-config