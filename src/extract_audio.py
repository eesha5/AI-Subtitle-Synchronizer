import subprocess

def extract_audio(input_video, output_audio):

    command = [
        "ffmpeg",
        "-y",
        "-i", input_video,
        "-vn",
        "-ar", "16000",
        "-ac", "1",
        output_audio
    ]

    subprocess.run(command)

    print("✓ Audio extracted")