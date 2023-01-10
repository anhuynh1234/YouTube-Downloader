from pytube import YouTube
import math
import os

def save(url, path):
    ytobject = YouTube(url)
    title = ytobject.title
    author = ytobject.author
    length = ytobject.length
    ytobject_stream = ytobject.streams.get_highest_resolution()
    try:
        ytobject.check_availability()
    except:
        print("Video not available, try again.")
        quit()
    print("Downloading " + title + " " + "from " + author + ' (' + str(math.floor(length/60)) + ':' + str(length%60) + ') ...')
    
    # if len(path) > 0:
    #     try:
    #         os.path.exists()
    #     except:
    #         print("Path not valid or exists.") 

    try: 
        ytobject_stream.download(path)
    except:
        print("Error - could not download.")

    print("Done")        



if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    path = input("Enter the path to download video (Current directory if left empty): ")
    save(url, path)