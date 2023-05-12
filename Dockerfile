# pull official base image
FROM jupyter/datascience-notebook

# I need to pin this image
# FROM jupyter/datascience-notebook:f3079808ca8c


# set working directory
WORKDIR /home/jovyan/work

# install python dependencies
RUN pip install --upgrade pip
COPY ./src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD jupyter lab --ip=0.0.0.0 --allow-root --no-browser
