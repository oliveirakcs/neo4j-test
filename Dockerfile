FROM python:3.11

# Set environment variable to ensure Python output is unbuffered
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt requirements.txt

# Upgrade pip and install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the entire project directory to the working directory
COPY . /app

# Expose port for the application
EXPOSE 8008
EXPOSE 8009