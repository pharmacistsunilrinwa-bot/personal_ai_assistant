# Use the official Python lightweight image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the logs.
ENV PYTHONUNBUFFERED True

# Set local code path as working directory.
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install system dependencies if any are needed (none for our simple requirements, but keeping it lean).
# Copy local requirements and install python packages.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files.
COPY . ./

# Expose port 8080 (standard for Cloud Run).
EXPOSE 8080

# Run the web service on container startup.
# Cloud Run sets the PORT environment variable automatically.
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
