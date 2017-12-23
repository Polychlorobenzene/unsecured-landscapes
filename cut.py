from vidpy import Clip, Composition
import subprocess
from glob import glob
from os import makedirs, path, getcwd, listdir, remove
from random import shuffle

PATH = getcwd()
COMPOSITION_PATH = PATH + "./recorded_videos/"
COMPOSITION_DESTINATION = PATH + '/recorded_videos/recorded_videos_cut'
COMPOSITION_CROPPED_LEFT = PATH + '/recorded_videos/recorded_videos_cut/recorded_videos_cut_left'
COMPOSITION_CROPPED_RIGHT = PATH + '/recorded_videos/recorded_videos_cut/recorded_videos_cut_right'

canvas_width = 1280
canvas_height = 720

list_videos = glob('./recorded_videos/*.mp4')
# list_videos_cut = [f for f in listdir(COMPOSITION_DESTINATION) if path.isfile(path.join(COMPOSITION_DESTINATION, f)) and '.mp4' in f]


def cutme():
    for video in list_videos:
        name = path.basename(video).split(':')[0] + ".mp4"
        resized_path = path.join(COMPOSITION_DESTINATION, name)
        print("Resizing Videos")
        subprocess.call(['ffmpeg', '-i', video, '-vf', 'scale={}:{},setdar=16:9'.format(canvas_width, canvas_height), '-y', resized_path])


def cut_left():
    for video in list_videos:
        name = path.basename(video).split(':')[0] + ".mp4"
        resized_path = path.join(COMPOSITION_DESTINATION, name)
        print("Cutting Left")

        clip = Clip(resized_path)
        clip.fx('crop', {'left': 1280/2})
        Composition([clip]).save(path.join(COMPOSITION_CROPPED_LEFT, name))


def cut_right():
    for video in list_videos:
        name = path.basename(video).split(':')[0] + ".mp4"
        resized_path = path.join(COMPOSITION_DESTINATION, name)
        print("Cutting Right")

        clip = Clip(resized_path)
        clip.fx('crop', {'right': 1280/2})
        Composition([clip]).save(path.join(COMPOSITION_CROPPED_RIGHT, name))


def compose_right():
    list_videos_right = glob('./recorded_videos/recorded_videos_cut/recorded_videos_cut_right/*.mp4')
    clips_right = []

    for video in list_videos_right:
        clip_right = Clip(video)
        clips_right.append(clip_right)

    print("Composing Right Videos")
    shuffle(clips_right)

    # play videos on top of each other
    composition = Composition(clips_right, singletrack=True)
    composition.save(COMPOSITION_CROPPED_RIGHT + '/composition_right/videos_right.mp4')

cutme()
cut_left()
cut_right()
compose_right()
