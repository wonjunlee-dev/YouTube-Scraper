FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    curl \
    unzip \
    gnupg \
    && apt-get clean

ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="${PATH}:/usr/bin/chromium"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/docker-cmd ./scripts/
RUN chmod +x ./scripts/docker-cmd

COPY . .

ENV PORT=8080

CMD ["./scripts/docker-cmd"]