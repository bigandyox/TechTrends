FROM python:3.8
LABEL maintainer="Andrew Simpson"
LABEL course="nd064"
LABEL provider="Udacity"

EXPOSE 3111

COPY ./techtrends /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python init_db.py

CMD ["python", "app.py"]