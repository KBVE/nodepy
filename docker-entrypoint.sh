#!/bin/sh

set -e

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

# You can put other setup logic here


# SQLITE PATCH
wget https://www.sqlite.org/2023/sqlite-autoconf-3420000.tar.gz \
tar xvfz sqlite-autoconf-3420000.tar.gz \
mv sqlite-autoconf-3420000 /usr/local/share/sqlite3  \
cd /usr/local/share/sqlite3 \
./configure \
make -j 1 \ 
make install \
cd /opt/pysetup/


# Evaluating passed command:
exec "$@"