"""
Reference:
https://github.com/googleapis/google-cloud-python/tree/master/speech
"""

import argparse
from pathlib import Path
from pprint import pprint

from google.cloud import speech
from google.cloud.speech import enums, types

data_path = Path("resources")
if not data_path.exists():
    data_path.mkdir()


def write_transcript(input_file_path, response):
    transcript_file = "resources/trs_{}.txt".format(input_file_path.stem)
    with open(transcript_file, "w", encoding="utf-8") as f:
        for idx, result in enumerate(response.results):
            # The first alternative is the most likely one for this portion.
            f.write(str(idx))
            f.write("\n")
            f.write("transcript: ")
            f.write(result.alternatives[0].transcript)
            f.write("\n")
            f.write("confidence: ")
            f.write(str(result.alternatives[0].confidence))
            f.write("\n")
            f.write("words: [")
            for word in result.alternatives[0].words:
                f.write(word)
                f.write(", ")
            f.write("]\n")


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="gcs link or local file path")
    # support audio_encoding format url
    # https://cloud.google.com/speech-to-text/docs/encoding
    parser.add_argument("--audio_encoding", type=str,
                        help="audio encoding format\n"
                             "support audio encoding format: https://cloud.google.com/speech-to-text/docs/encoding\n"
                             "(default=FLAC)", default="FLAC")
    parser.add_argument("--hertz", type=int, help="sampling rate (default=44100)", default=44100)
    # support language_code url
    # https://cloud.google.com/speech-to-text/docs/languages
    parser.add_argument("--language_code", type=str,
                        help="want to transcript language code\n"
                             "support language_code: https://cloud.google.com/speech-to-text/docs/languages\n"
                             "(default=en-US)", default="en-US")
    _args = parser.parse_args()
    return _args


def is_support_audio_encoding(audio_config, input_config):
    for ac in audio_config:
        if ac.name.lower() == input_config.lower():
            return True
    return False


def main():
    args = get_arguments()
    gcs_prefix = "gs://"
    file_path = Path(args.path)
    if args.path.startswith(gcs_prefix):
        audio = types.RecognitionAudio(uri=args.path)
    else:
        if not file_path.exists():
            raise FileExistsError("{} not exist".format(file_path))
        else:
            with file_path.open("rb") as audio_file:
                content = audio_file.read()
                audio = types.RecognitionAudio(content=content)

    if not is_support_audio_encoding(enums.RecognitionConfig.AudioEncoding,
                                     args.audio_encoding):
        raise ValueError("{} is not supported audio_encoding".format(args.audio_encoding))
    client = speech.SpeechClient()
    encoding = args.audio_encoding
    sample_rate_hertz = args.hertz
    language_code = args.language_code

    config = types.RecognitionConfig(
        encoding=encoding.upper(),
        sample_rate_hertz=sample_rate_hertz,
        language_code=language_code)

    operation = client.long_running_recognize(config, audio)
    print('Waiting for operation to complete...')
    response = operation.result(timeout=360)
    pprint(response)
    write_transcript(file_path, response)


if __name__ == '__main__':
    main()
