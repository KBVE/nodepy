from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload
import yt_dlp

#import sys
#import json

#data = sys.argv[1]
#jsonData = json.loads(data)

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

client = PocketBase('http://pocketbase:8090')

# This is just a throw away test account, does not work in production, you stupid memers.
admin_data = client.admins.auth_with_password("test@test.com", "pythonpython")

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

URLS = 'https://www.youtube.com/watch?v=BaW_jenozKc'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)

result = client.collection("apollo").create(
    {
        "music": FileUpload(error_code),
    })

print(f"{result}")