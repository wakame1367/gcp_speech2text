"""
Reference:
https://github.com/googleapis/google-cloud-python/tree/master/speech
"""

import argparse

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", "p", type=str, help="gcs link or local file path")
    # support audio_encoding format url
    # https://cloud.google.com/speech-to-text/docs/encoding
    parser.add_argument("--audio_encoding", "-a", type=str,
                        help="audio encoding format\n"
                             "support audio encoding format: https://cloud.google.com/speech-to-text/docs/encoding\n"
                             "(default=FLAC)", default="FLAC")
    parser.add_argument("--hertz", "-h", type=int, help="sampling rate (default=44100)", default=44100)
    # support language_code url
    # https://cloud.google.com/speech-to-text/docs/languages
    parser.add_argument("--language_code", "-l", type=str,
                        help="want to transcript language code\n"
                             "support language_code: https://cloud.google.com/speech-to-text/docs/languages\n"
                             "(default=en-US)", default="en-US")
    _args = parser.parse_args()
    return _args


def main():
    args = get_arguments()
    client = speech_v1.SpeechClient()
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    sample_rate_hertz = args.hertz
    language_code = args.language_code
    config = {'encoding': encoding,
              'sample_rate_hertz': sample_rate_hertz,
              'language_code': language_code}
    uri = 'gs://bucket_name/file_name.flac'
    audio = {'uri': uri}

    response = client.recognize(config, audio)


if __name__ == '__main__':
    main()