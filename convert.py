import subprocess
from pathlib import Path

data_path = Path("resources")


def main():
    for path in data_path.glob("*.m4a"):
        output_path = data_path / path.stem
        output_path = str(output_path) + ".wav"
        command = "ffmpeg -i {} -vn -ac 1 -ar 44100 -acodec pcm_s16le -f wav {}".format(str(path), output_path)
        subprocess.call(command, shell=True)


if __name__ == '__main__':
    main()
