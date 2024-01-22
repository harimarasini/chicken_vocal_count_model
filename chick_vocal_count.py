# -*- coding: utf-8 -*-
"""chick_vocal_count.ipynb


pip install pydub



from pydub import AudioSegment

def count_chicken_vocalizations(audio_file_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Set a threshold for volume (adjust as needed)
    threshold = -30

    # Segment duration in milliseconds
    segment_duration = 500  # 500 milliseconds (0.5 seconds)

    # Count the number of vocalizations in each segment
    vocalizations = 0

    for i in range(0, len(audio), segment_duration):
        segment = audio[i:i + segment_duration]
        if segment.dBFS > threshold:
            vocalizations += 1

    # Print the total count
    print("Number of chicken vocalizations:", vocalizations)

if __name__ == "__main__":
    # Replace 'your_audio_file.wav' with the path to your audio file
    count_chicken_vocalizations('chickd3p1.wav')

