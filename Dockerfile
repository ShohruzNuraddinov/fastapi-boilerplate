FROM python:3.9-alpine

# Set the working directory
RUN mkdir -p /app
WORKDIR /app

# Install dependencies
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    linux-headers \
    musl-dev \
    postgresql-dev \
    python3-dev \
    py3-pip

COPY requirments.txt .

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

# Copy the application code
COPY . .

CMD ["entrypoint.sh"]