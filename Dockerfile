# pull the python image
FROM tensorflow/tensorflow:latest

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy everything to the image
COPY . .

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["api.py"]