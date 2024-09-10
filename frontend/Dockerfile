# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY frontend.py /app
COPY templates /app/templates

# Install any needed packages specified in requirements.txt
RUN pip install flask requests

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run frontend.py when the container launches
CMD ["python", "frontend.py"]
