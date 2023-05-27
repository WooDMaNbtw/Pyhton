import moviepy.editor
from pathlib import Path


def main(source, name):
    print(name, source)
    video = moviepy.editor.VideoFileClip(fr"{source}")
    audio = video.audio
    audio.write_audiofile(f"{name}.mp3")



if __name__ == '__main__':
    source = input("Input path of the video: ")
    video_file = Path(source)
    main(video_file, video_file.stem)