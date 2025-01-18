import yt_dlp

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=2o2d7Nr_SN8"

# Download options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # High-quality video and audio
    'outtmpl': './downloads/%(title)s.%(ext)s',  # File download path
    'merge_output_format': 'mp4',  # Output format after merging
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Ensure final format is mp4
    }]
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Downloading...")
        ydl.download([video_url])  # List me URL pass karte hain
        print("Download completed!")
except Exception as e:
    print("Error:", e)
