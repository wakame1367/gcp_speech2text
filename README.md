# gcp_speech2text
This repository is **GCP Speech2Text API Python Sample**

## Before you start

**Setup Project** and **export GOOGLE_APPLICATION_CREDENTIALS**, **Install Cloud SDK**
[Cloud Speech-to-Text API - QuickStart](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)

## Installing

Use [Github - pipenv](https://github.com/pypa/pipenv)

```
git clone https://github.com/wakamezake/gcp_speech2text.git
pipenv install
```

## How to use

```
python cli.py  path/to/file or gcs://path/to/file
```

```
usage: cli.py [-h] [--audio_encoding AUDIO_ENCODING] [--hertz HERTZ]
              [--language_code LANGUAGE_CODE]
              path

positional arguments:
  path                  gcs link or local file path

optional arguments:
  -h, --help            show this help message and exit
  --audio_encoding AUDIO_ENCODING
                        audio encoding format support audio encoding format:
                        https://cloud.google.com/speech-to-text/docs/encoding
                        (default=FLAC)
  --hertz HERTZ         sampling rate (default=44100)
  --language_code LANGUAGE_CODE
                        want to transcript language code support
                        language_code: https://cloud.google.com/speech-to-
                        text/docs/languages (default=en-US)
```