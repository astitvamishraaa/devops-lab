# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files from current folder into container
COPY . .

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
