import sys
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def clip_video(input_filename, start_time, end_time, output_filename):
    start_time = convert_time(start_time)
    end_time = convert_time(end_time)
    
    ffmpeg_extract_subclip(input_filename, start_time, end_time, targetname=output_filename)
    
def convert_time(time_str):
    parts = time_str.split(':')
    minutes = int(parts[0])
    
    parts = parts[1].split('.')
    seconds = int(parts[0])
    fraction = int(parts[1])
    
    return 60 * minutes + seconds + fraction / 10.0

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 clip.py [filename.mp4] [start time] [end time]")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    start_time = sys.argv[2]
    end_time = sys.argv[3]
    output_filename = f"{input_filename.split('.')[0]}-clipped.mp4"
    
    clip_video(input_filename, start_time, end_time, output_filename)
    print(f"Video clipped and saved as {output_filename}")
