# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask

# Make port 8080 available to the world outside this container
EXPOSE 8080

ENV FLASK_APP=example.py

# Run frontend.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
