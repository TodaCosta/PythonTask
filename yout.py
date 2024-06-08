# import pytube
# from pytube import YouTube
#
# youtube_video_url = "https://www.youtube.com/watch?v=BbII9GhLkxs&ab_channel=egoroff_channel"
# try:
#     yt_obj = YouTube(youtube_video_url)
#     filters =yt_obj.streams.filter(progressive=True, file_extension='mp4')
#     filters.get_highest_resolution().download()
#     print('Видео загрузилось')
# except Exception as e:
#     print(e)

from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=2rbVNTw8ajc&ab_channel=egoroff_channel').streams[0].download()



