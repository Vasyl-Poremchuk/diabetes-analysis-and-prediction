# Use the Python 3.10.5 slim-buster base image
FROM python:3.10.5-slim-buster

# Set the value of the `PYTHONUNBUFFERED` variable to 1
ENV PYTHONUNBUFFERED 1

# Set the current working directory to /app
WORKDIR /app

# Copy the file with the requirements to the /app directory
COPY ./requirements.txt /app/requirements.txt

# Install the package dependencies in the requirements file
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the . directory inside the /app directory
COPY . /app

# Configure the container to run in an executed manner
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
