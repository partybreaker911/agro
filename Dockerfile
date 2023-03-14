# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY ./entrypoint.sh .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Set environment variables for Django settings
ENV DJANGO_SETTINGS_MODULE=market.settings

# Run the command to start the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "market.wsgi"]