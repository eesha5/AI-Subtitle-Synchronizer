import subprocess

def burn_subtitles(video, subtitle, output):
    """
    Burns subtitles into a video using FFmpeg.

    Parameters:
        video (str): Path to the input video.
        subtitle (str): Path to the .srt subtitle file.
        output (str): Path where the output video will be saved.
    """

    command = [
        "ffmpeg",
        "-y",                       # Overwrite output file if it already exists
        "-i", video,                # Input video
        "-vf", f"subtitles={subtitle}",  # Subtitle filter
        output                      # Output video
    ]

    subprocess.run(command)

    print("✓ Video with subtitles created!")