FROM python:3.7.5
WORKDIR /app
COPY ./ ./
RUN pip install pipenv && pipenv install --system
EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/app.ini"]