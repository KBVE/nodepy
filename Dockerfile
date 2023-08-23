# Base Image
FROM nikolaik/python-nodejs:latest as production


RUN apt update -y
RUN apt upgrade -y

RUN apt install ffmpeg curl -y

RUN npm install pm2 -g


# Poetry 
RUN curl -sSL https://install.python-poetry.org | python3 -


WORKDIR /app
COPY package.json .
RUN yarn install


RUN pip install flask yt-dlp pocketbase requests appwrite

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project false
RUN poetry install

COPY . .

EXPOSE 5000

CMD ["pm2-runtime", "ecosystem.config.js"]
