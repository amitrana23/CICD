FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ACEest_Fitness_flask.py .
EXPOSE 5000
ENV APP_VERSION=v1.0.0
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "ACEest_Fitness_flask:create_app()"]
