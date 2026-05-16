from pytube import YouTube

def download_with_pytube(url):
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print("Downloading...")
        
        # Get the highest resolution progressive stream (video + audio combined)
        # usually maxes out at 720p
        stream = yt.streams.get_highest_resolution()
        
        stream.download()
        print("Download completed!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_with_pytube(url)