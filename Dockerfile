FROM python:3-alpine
WORKDIR /bot
COPY . /bot
RUN apk --no-cache --allow-untrusted add -q build-base jpeg-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev harfbuzz-dev fribidi-dev libpng-dev giflib-dev openblas-dev;\
    pip install --no-cache-dir -r requirements.txt
CMD python main.py
