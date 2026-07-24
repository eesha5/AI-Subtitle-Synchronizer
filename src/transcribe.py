import whisper

model = whisper.load_model("base")

def transcribe(audio_file, subtitle_file):

    print("Transcribing...")

    result = model.transcribe(
        audio_file,
        word_timestamps=False
    )

    def format_timestamp(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)

        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

    with open(subtitle_file, "w", encoding="utf-8") as file:

        for i, segment in enumerate(result["segments"], start=1):

            file.write(f"{i}\n")
            file.write(
                f"{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n"
            )
            file.write(segment["text"].strip() + "\n\n")

    print("✓ Subtitle file created")