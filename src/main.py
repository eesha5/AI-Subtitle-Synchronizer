from pathlib import Path
import sys

from utils import get_file_paths
from extract_audio import extract_audio
from transcribe import transcribe
from burn_subtitles import burn_subtitles


print("=" * 50)
print("        AI Subtitle Synchronizer")
print("=" * 50)

# Ask user for video path
video = input("\nEnter the path of the video: ").strip()

# Check if the file exists
if not Path(video).is_file():
    print("\n❌ Error: Video file not found.")
    print("Please enter a valid video path.")
    sys.exit()

# Generate all required file paths
audio, subtitle, output = get_file_paths(video)

print("\nGenerated file paths:")
print(f"Audio    : {audio}")
print(f"Subtitle : {subtitle}")
print(f"Output   : {output}")

print("\nStep 1: Extracting audio...")
extract_audio(video, audio)

print("\nStep 2: Transcribing...")
transcribe(audio, subtitle)

print("\nStep 3: Burning subtitles...")
burn_subtitles(video, subtitle, output)

print("\n" + "=" * 50)
print("✅ Done!")
print("=" * 50)

print("\nOutput video:")
print(output)