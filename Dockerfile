FROM python:3.8
LABEL maintainer="Andrew Simpson"
LABEL course="nd064"
LABEL provider="Udacity"

EXPOSE 3111

COPY . /app
WORKDIR /app
RUN pip install -r /app/techtrends/requirements.txt

CMD ["python", "/app/techtrends/init_db.py", "/app/techtrends/app.py"]