FROM python:3

RUN pip install httpx beautifulsoup4 pydantic_settings

WORKDIR /opt
COPY ./app /opt/app

CMD ["python3" , "/opt/app/main.py"]