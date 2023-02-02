# from pytube import YouTube
from pytube import Playlist


youtube_clip_lists = [
    'https://www.youtube.com/playlist?list=PLB8yRZhf8IeqhdnP_lRZmdwIRcnJNlyIG',
    'https://www.youtube.com/playlist?list=PLB8yRZhf8Ieokcq5fFVNbZS2HNyI8tU21',
    'https://www.youtube.com/playlist?list=PLB8yRZhf8IeohHlULfhyEmfIN3iaweDVP',
    'https://www.youtube.com/playlist?list=PLB8yRZhf8IerOmiP387Op92g-WdYHWB5U',
    'https://www.youtube.com/playlist?list=PLB8yRZhf8Ieqb0BdabukbL3-_AOHy05ts',
    'https://www.youtube.com/playlist?list=PLB8yRZhf8IerXmiPj03KnQk50tsp4rbsI',

]

i = 1
for youtube_clip_list in youtube_clip_lists:
    clip_list = Playlist(youtube_clip_list)

    for video in clip_list.videos:
        mp4 = video.streams.filter(progressive=True, file_extension='mp4')
        target_video = mp4.order_by('resolution').desc().first()
        target_video.download('vedio/' + str(i))
    
    i = i + 1