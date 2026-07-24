import os

def get_file_paths(video_path):
    filename = os.path.splitext(os.path.basename(video_path))[0]

    audio_path = f"data/audio/{filename}.wav"
    subtitle_path = f"data/subtitles/{filename}.srt"
    output_video = f"data/videos/{filename}_subtitled.mp4"

    return audio_path, subtitle_path, output_video