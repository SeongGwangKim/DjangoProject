FROM python:3.8

WORKDIR /home/

RUN git clone https://github.com/SeongGwangKim/DjangoProject.git

WORKDIR /home/DjangoProject/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-e!pq+@p8be^5&#d&6it!la$0ezyfcu9qkjy$i$=4+x!ehs3t2@" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "main.wsgi", "--bind", "0.0.0.0:8000"]