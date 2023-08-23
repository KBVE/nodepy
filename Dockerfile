# Base Image
FROM nikolaik/python-nodejs:latest as production


RUN apt update -y
RUN apt upgrade -y

RUN apt install ffmpeg curl -y

# Poetry 
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN pip install flask yt-dlp pocketbase requests appwrite
RUN npm install pm2 -g

WORKDIR /app
COPY package.json .
RUN yarn install

COPY poetry.lock pyproject.toml ./
#RUN poetry config virtualenv.create false
RUN poetry config virtualenvs.in-project false
#RUN poetry config install.user true
RUN poetry install -g

COPY . .

EXPOSE 5000

CMD ["pm2-runtime", "ecosystem.config.js"]
