# Base Image
FROM nikolaik/python-nodejs:latest as production

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


RUN apt update -y
RUN apt upgrade -y

RUN apt install ffmpeg curl -y

RUN npm install pm2 -g


# Poetry 
RUN curl -sSL https://install.python-poetry.org | python3 -



WORKDIR /app
COPY package.json .
RUN yarn install

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh



RUN pip install flask yt-dlp pocketbase requests appwrite

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

EXPOSE 5000

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["pm2-runtime", "ecosystem.config.js"]
