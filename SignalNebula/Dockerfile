FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python", "-m", "signalnebula.cli", "analyze", "data/sample_signal.csv"]
