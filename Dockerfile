FROM python:3.6.5
WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/app.ini"]