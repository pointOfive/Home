FROM debian:buster-slim
# Following https://hackernoon.com/running-docker-on-aws-ec2-83a14b780c56
# I created an "Amazon Linux AMI (HVM), SSH Volume Type" instance
# which is a RHEL/fedora OS, but debian is close enough to that these days
# so we just use the debian base

# here we set any environmental variables we'll need
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

# here we do any initial installs we'll need to use
RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion && \
    apt-get clean

# here we set our location inside the container
# and then we copy everything from our current directory
# over to that location inside the container
WORKDIR /usr/src/app
COPY . .

# we'll later ALSO use the volume flag "-v /home/ec2-user:/usr/src/app"
# to persist changes made to the directory while in the container

# this installs everything we'll need for python/bokeh
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    conda config --add channels conda-forge && \
    conda env create --file environment.yaml
# the most interesting thing here is "environment.yaml"
# which defines a py3 conda environment as well as
# everything we'll need to run our bokeh server

# finally the container is started and we execute
CMD [ "/bin/bash" ]
# which spawns a shell and drops us into it
# here we'll be able to run our bokeh server

