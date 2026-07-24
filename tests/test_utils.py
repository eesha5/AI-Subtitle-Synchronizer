from utils import get_file_paths

audio, subtitle, output = get_file_paths(
    r"C:\Users\Eesha\Videos\lecture.mp4"
)

print(audio)
print(subtitle)
print(output)