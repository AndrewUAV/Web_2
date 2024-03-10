FROM python:3.11.8


ENV APP_HOME /app


WORKDIR $APP_HOME


COPY .. .

RUN pip install -e .
RUN pip install -r requirements.txt


EXPOSE 5000


ENTRYPOINT ["python", "app/__main__.py"]