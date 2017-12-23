import requests
import subprocess
from ipvideos import cameras as places
import sys

## Code based on @cvalenzuela https://github.com/cvalenzuela/automating_video

# This function calls the next one
def get_one(ip, path, duration):
  ''' Download video from IP Camera'''
  IP = ip
  video_path = path + ip + '.mp4'
  record(IP, video_path, duration, False, '20')

# This function recors each video
def record(ip, outputname, duration='00:00:05', rtsp=True, fps='30'):
  ''' This function record the video  '''
  BASE_URL = 'http://' + ip
  MJPG_URL = BASE_URL + '/mjpg/video.mjpg'
  RTSP_URL = (BASE_URL + ':554/axis-media/media.amp').replace('http://', 'rtsp://')

  print('Recording video from', MJPG_URL)

  if rtsp:
    args = ['ffmpeg', '-i', RTSP_URL, '-vcodec', 'copy', '-acodec', 'copy', '-f', 'mp4', '-t', duration, '-y', outputname]
  else:
    args = ['ffmpeg', '-f', 'mjpeg', '-r', fps, '-i', MJPG_URL, '-t', duration, '-y', outputname]
  subprocess.call(args)

for place in places:
    for camera in places[place]:
        name = camera["place"]
        ip = camera["ip"]
        path = "./recorded_videos/" + name + ":" + ip
        print('The camera' + name + 'has the ip' +  'and is located in ' + place)

        get_one(ip, path, '00:00:05')

sys.exit()
