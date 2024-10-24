# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install opencv-python face-recognition matplotlib

# Run main.py when the container launches
CMD ["python", "main.py"]
