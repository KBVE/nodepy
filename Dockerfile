# Base Image
FROM nikolaik/python-nodejs:latest as production


RUN apt update -y
RUN apt upgrade -y

RUN apt install ffmpeg -y
RUN pip install flask yt-dlp pocketbase requests appwrite
RUN npm install pm2 -g


WORKDIR /app
COPY package.json .
RUN yarn install

COPY . .

EXPOSE 5000

CMD ["pm2-runtime", "ecosystem.config.js"]
