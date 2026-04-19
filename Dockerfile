# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxfixes3 \
    libxrender1 \
    libxtst6 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    fonts-noto-color-emoji \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project directory to the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install

# Create reports directory
RUN mkdir -p reports

# Set environment variables for headless testing
ENV PYTHONUNBUFFERED=1
ENV HEADLESS=true
ENV CI=true

# Run the test_frontpage.py script in headless mode with HTML report
CMD ["python", "-m", "pytest", "python-scripts/test_frontpage.py", "-v", "--tb=short", "--html=reports/test_report.html", "--self-contained-html"]
