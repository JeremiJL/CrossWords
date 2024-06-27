FROM python:3.11
LABEL authors="Jeremi Lipniacki"

WORKDIR /cross_words

COPY requirements.txt /cross_words
RUN pip3 install -r requirements.txt

COPY . /cross_words

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]