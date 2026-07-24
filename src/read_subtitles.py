import pysrt

# Open the subtitle file
subs = pysrt.open("data/subtitles/sample.srt")

# Print every subtitle
for sub in subs:
    print("Subtitle Number :", sub.index)
    print("Start Time      :", sub.start)
    print("End Time        :", sub.end)
    print("Subtitle Text   :", sub.text)
    print("-" * 40)