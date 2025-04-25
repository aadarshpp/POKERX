# importing vlc module
import vlc

# importing time module
import time

def playvideo(videopath, length=5):
    # creating vlc media player object
    media_player = vlc.MediaPlayer()

    media_player.toggle_fullscreen()

    # media object
    media = vlc.Media(videopath)

    # setting media to the media player
    media_player.set_media(media)

    # setting audio track
    media_player.audio_set_track(1)


    # setting volume
    media_player.audio_set_volume(80)

    # start playing video
    media_player.play()

    # wait so the video can be played for 5 seconds
    # irrespective for length of video
    time.sleep(length)
    
# video = r"C:\Users\Aadarsh\Videos\Edits\CSM_ig.edit.L.mp4"
# playvideo(video, type=1)
    
    