FROM --platform=linux/amd64 python:3.9-slim as build
# Use an official Python runtime as a parent image

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the Flask application using `flask run`
CMD ["flask", "run"]