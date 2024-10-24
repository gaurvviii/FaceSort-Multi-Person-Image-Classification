# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv venv

# Install Python dependencies
RUN ./venv/bin/pip install --upgrade pip
RUN ./venv/bin/pip install tensorflow numpy scikit-learn opencv-python matplotlib

# Set the environment variable to use the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Command to run the main script
CMD ["python", "main.py"]
