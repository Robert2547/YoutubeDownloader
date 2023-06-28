from pytube import YouTube # for downloading youtube videos
from sys import argv # for command line arguments

link = argv[1] # get the link from the command line
yt = YouTube(link) # create a YouTube object

# print the title of the video
print("Title: ", yt.title)

# print the number of views of the video
print("Number of views: ", yt.views)

# print the length of the video
print("Length of video: ", yt.length, "seconds")

# download the video
yd = yt.streams.get_highest_resolution()
print("Downloading...")
yd.download()
print("Download completed!!")


