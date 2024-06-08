# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Copy entrypoint script into the container
COPY entrypoint.sh /code/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Define the entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]