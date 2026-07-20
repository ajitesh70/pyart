FROM python:3.11-slim
WORKDIR /app

# Copy the wheels produced by the CI `test` job (downloaded into wheelhouse)
COPY wheelhouse/ /wheels/
COPY requirements.txt .

# Install from the offline wheelhouse only — no network access.
RUN pip install --no-index --find-links=/wheels -r requirements.txt

# Copy application files
COPY . .

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
