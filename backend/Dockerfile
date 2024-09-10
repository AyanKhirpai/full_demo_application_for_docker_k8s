# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY backend.py /app

# Install any needed packages specified in requirements.txt
RUN pip install flask

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Run backend.py when the container launches
CMD ["python", "backend.py"]
