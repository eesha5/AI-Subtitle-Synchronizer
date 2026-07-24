# Synchronization Pipeline

# Normalize Whisper text
# Normalize subtitle text
# Merge nearby Whisper segments
# Find best subtitle match
# Apply confidence threshold
# Calculate offsets
# Remove outliers
# Estimate drift
# Correct subtitle timings.
# Save corrected subtitles
def merge_segments(segments, gap_threshold=1.0):
    """
   Algorithm:

1. Create an empty list to store merged Whisper segments.

2. Start with the first Whisper segment.

3. Calculate the time gap between the current segment and the next adjacent Whisper segment.

4. If the gap is smaller than the threshold:
      Merge the text.
      Update the end timestamp.

5. Otherwise:
      Save the current merged segment.
      Move to the next segment.

6. Repeat until all Whisper segments have been processed.

7. Return the list of merged Whisper segments.



    Merge consecutive Whisper segments if the time gap between them
    is less than the specified threshold.

    Parameters:
        segments (list): List of Whisper segment dictionaries.
        gap_threshold (float): Maximum allowed gap (seconds).

    Returns:
        list: New list containing merged Whisper segments.
    """