from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def get_video(url):
    save_to = "./Videos"
    video_url = url
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(save_to)
    print(f"Video saved to {save_to}")

def get_mp3(url):
    save_to = "./Audio"
    video_url = url
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    video_path = f"{save_to}/{yt.title}.mp4"
    stream.download(save_to)
    print(f"Video saved to {video_path}")
    audio_path = f"{save_to}/{yt.title}.mp3"
    video_clip = VideoFileClip(video_path)
    video_clip.audio.write_audiofile(audio_path)
    video_clip.close()
    os.remove(video_path)
    print(f"Audio saved to {audio_path}")