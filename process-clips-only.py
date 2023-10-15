from moviepy.editor import VideoFileClip
import re
import os

def time_to_seconds(time_str):
    m, s, f = re.split(r'[:.]', time_str)
    seconds = int(m) * 60 + float(s) + float(f)
    return seconds

def seconds_to_time(seconds):
    m = int(seconds) // 60
    s = seconds % 60
    f = seconds - int(seconds)
    return f"{m:02d}:{s:02.1f}"

def extract_clips(video_file, clips):
    # Create a "Clips" folder if it doesn't exist
    if not os.path.exists("Clips"):
        os.makedirs("Clips")

    for clip in clips:
        start_time, end_time, clip_name = clip
        start_seconds = time_to_seconds(start_time)
        end_seconds = time_to_seconds(end_time)
        output_file = os.path.join("Clips", f"{clip_name}.mp4")
        
        try:
            clip = VideoFileClip(video_file).subclip(start_seconds, end_seconds)
            clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
            print(f"Saved {clip_name} from {start_time} to {end_time}")
        except Exception as e:
            print(f"Failed to extract {clip_name}: {str(e)}")

if __name__ == "__main__":
    input_video_file = "SEO_Masterclass.mp4"
    
    clips = [
        ("03:25.7", "04:07.8", "who-am-i"),
        ("04:42.4", "09:14.9", "my-rule-for-marketing-success"),
        ("09:29.3", "11:42.4", "on-site-seo"),
        ("11:59.2", "13:47.4", "understanding-the-seo-game"),
        ("13:47.4", "16:47.0", "off-site-seo"),
        ("16:52.4", "19:54.5", "programmatic-seo"),
        ("19:54.5", "21:29.1", "google-images-seo"),
        ("21:29.6", "36:10.9", "ai-automation-for-content"),
        ("25:03.4", "28:20.1", "competitor-content-spying"),
        ("28:20.8", "30:39.6", "how-many-articles-do-i-need"),
        ("30:39.6", "32:31.4", "how-many-backlinks-do-i-need"),
    ]
    
    extract_clips(input_video_file, clips)
