
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "dQw4w9WgXcQ"
transcript = YouTubeTranscriptApi.get_transcript(video_id)
for entry in transcript:
    print(f"[{entry['start']:.2f}s] {entry['text']}")
