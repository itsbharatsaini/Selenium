FROM python

RUN apt-get update
RUN apt-get install wget -y

# Set the Chrome repo.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Install Chrome.
RUN apt-get update && apt-get -y install google-chrome-stable

WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt

# CMD ["python3", "main.py"]
#docker run --entrypoint "demo.py" pylenium