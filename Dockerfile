# Use an official Python runtime as a parent image
FROM python:3.8

# Install poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the dependency files
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-root

# Install GLPK solver
RUN apt-get update && apt-get install -y glpk-utils

# Copy the rest of the application
COPY . /app

# Command to run your Python script or application using Pyomo and GLPK
CMD ["poetry", "run", "python", "app.py"]
