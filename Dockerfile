# Use official slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Poetry
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy Poetry files first (better Docker caching)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies without creating virtualenvs (Docker prefers system install)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi


# Copy the rest of your app
COPY . /app

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "src/dv_classifier_app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
