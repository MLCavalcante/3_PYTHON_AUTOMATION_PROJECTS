#from pytube import YouTube
#from sys import argv


#link = argv[1] # Get the link from the command line argument // pega o input do link no terminal
#yt = YouTube(link) # Create a YouTube object // cria um objeto do youtube



#yd = yt.streams.get_highest_resolution() # Get the highest resolution stream // pega o video com a maior resolução
#yd.download('./Users/666/OneDrive/Área de Trabalho/vid>') # Download the video // baixa o video


#outra library para baixar videos do youtube: youtube_dl
import youtube_dl
import sys

link = sys.argv[1]  # Get the link from the command line argument

ydl_opts = {
    'outtmpl': './Users/666/OneDrive/Área de Trabalho/vid/%(title)s.%(ext)s',  # Set the output directory and filename template
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Set the video format
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])  # Download the video

