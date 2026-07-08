FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install PlatformIO
RUN pip install --no-cache-dir platformio

# Set working directory
WORKDIR /workspace

# Copy platformio.ini first for dependency caching
COPY platformio.ini .

# Install PlatformIO dependencies (platforms, packages, libraries)
RUN pio pkg install

# Copy the rest of the project
COPY . .

# Default command: build the project
CMD ["pio", "run"]
