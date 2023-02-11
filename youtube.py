from pytube import YouTube


link = input("Enter link on video: ")
typeOfVideo = input("Enter type of downloads 'mp3' or 'mp4'").lower()

if typeOfVideo == "mp4":
    quality = input("Enter level quality 'l'-lowest or 'h-highest': ").lower()
    def downloadVideo():
        videoUrl = link
        yt = YouTube(videoUrl)
        try:
            if quality == "h":
                videoDwH = yt.streams.get_highest_resolution()
                videoDwH.download()
            else:
                videoDwL = yt.streams.get_lowest_resolution()
                videoDwL.download()
        except Exception as error:
            print(error)
        print("Loading is complete")
    downloadVideo()
else:
    def downloadAudio():
        videoUrl = link
        yt = YouTube(videoUrl)
        name = f"{yt.streams[0].title}.mp3"
        yt.streams.filter(only_audio=True).first().download(filename=name)

    downloadAudio()




