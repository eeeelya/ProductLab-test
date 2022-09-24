FROM python:3.10

WORKDIR /usr/src/app/

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="."

RUN pip install pipenv

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app/

RUN #chmod +x "/usr/src/app/entrypoint.sh"
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]