import os
import argparse
from pytube import YouTube
from pydub import AudioSegment
from youtubesearchpython import VideosSearch
import re

DEFAULT_DEPTH_SCAN = 1
DEFAULT_OUTPUT_PATH_MP4 = 'mp4_output'
DEFAULT_OUTPUT_PATH_MP3 = 'mp3_output'
specific = False

def sanitize_filename(filename):
    # Remove invalid characters from filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def create_output_folder(output_path, folder_name):
    folder_name = sanitize_filename(folder_name)
    folder_path = os.path.join(output_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def search(query, depth_scan=DEFAULT_DEPTH_SCAN, output_path=DEFAULT_OUTPUT_PATH_MP4):
    videos_search = VideosSearch(query, limit=depth_scan)
    search_results = videos_search.result()['result']

    if not search_results:
        print(f"No videos found for the search query: {query}")
        return

    for video in search_results:
        video_url = f"https://www.youtube.com/watch?v={video['id']}"
        video_folder_name = sanitize_filename(video['title'])
        video_folder = create_output_folder(output_path, video_folder_name)
        download_video(video_url, video_folder)

def search_and_convert(query, depth_scan=DEFAULT_DEPTH_SCAN, output_path=DEFAULT_OUTPUT_PATH_MP3):
    videos_search = VideosSearch(query, limit=depth_scan)
    search_results = videos_search.result()['result']

    if not search_results:
        print(f"No videos found for the search query: {query}")
        return

    for video in search_results:
        video_url = f"https://www.youtube.com/watch?v={video['id']}"
        video_folder_name = sanitize_filename(video['title'])
        video_folder = create_output_folder(output_path, video_folder_name)
        download_and_convert(video_url, video_folder)

def download_and_convert(url, output_path, specific=False):
    download_video(url, output_path)

    # Convert the downloaded video to MP3 using pydub
    video_title = sanitize_filename(YouTube(url).title)
    video_path = os.path.join(output_path, f'{video_title}.mp4')
    audio_path_temp = os.path.join(output_path, 'temp_output.mp3')

    try:
        audio = AudioSegment.from_file(video_path, format="mp4")
        audio.export(audio_path_temp, format="mp3")
    except Exception as e:
        print(f"Error converting video to audio: {e}")
    finally:
        # Remove the downloaded MP4 file
        os.remove(video_path)

    if specific:
        # Create a folder with the video title
        folder_path = os.path.join(output_path, video_title)
        os.makedirs(folder_path, exist_ok=True)
        mp3_file_path = os.path.join(folder_path, f'{video_title}.mp3')

        # Check if the file with the same name already exists and override
        if os.path.exists(mp3_file_path):
            os.remove(mp3_file_path)

        os.rename(audio_path_temp, mp3_file_path)
    else:
        # Move the MP3 file to the output path
        mp3_file_path = os.path.join(output_path, f'{video_title}.mp3')

        # Check if the file with the same name already exists and override
        if os.path.exists(mp3_file_path):
            os.remove(mp3_file_path)

        os.rename(audio_path_temp, mp3_file_path)


def download_video(url, output_path):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_title = sanitize_filename(YouTube(url).title)
    video_file_path = os.path.join(output_path, f"{video_title}.mp4")

    # Check if the file with the same name already exists and override
    if os.path.exists(video_file_path):
        os.remove(video_file_path)

    video_stream.download(output_path, filename=f"{video_title}.mp4")

def main():
    parser = argparse.ArgumentParser(description='YouTube Video Downloader')
    parser.add_argument('--url', help='YouTube video URL')
    parser.add_argument('--search', help='Search YouTube videos and download them to MP4 format')
    parser.add_argument('--search-convert', help='Search YouTube videos and convert them to MP3 format')
    parser.add_argument('--depth-scan', type=int, default=DEFAULT_DEPTH_SCAN, help='Number of videos to pick from search results')
    
    args = parser.parse_args()

    if args.search:
        search(args.search, depth_scan=args.depth_scan, output_path=DEFAULT_OUTPUT_PATH_MP4)
        print(f"Download complete. Videos saved in separate folders under: {DEFAULT_OUTPUT_PATH_MP4}")

    elif args.search_convert:
        search_and_convert(args.search_convert, depth_scan=args.depth_scan, output_path=DEFAULT_OUTPUT_PATH_MP3)
        print(f"Download and conversion complete. Audio files saved in: {DEFAULT_OUTPUT_PATH_MP3}")

    elif args.url:
        specific = True
        download_and_convert(args.url, DEFAULT_OUTPUT_PATH_MP3, specific)
        print(f"Download and conversion complete. Audio file saved under: {DEFAULT_OUTPUT_PATH_MP3}")

if __name__ == '__main__':
    main()
