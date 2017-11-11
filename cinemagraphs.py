# Project 3: Cinemagraphs
# Alejandrina Patron Lopez
# apl7@gatech.edu
# GT ID 903075226
# Sana Ajani
# sajani@gatech.edu
# GT ID 903072587

from moviepy.editor import *
import moviepy.video.tools.drawing as dw
import cv2

def convertMask(mask):
    h = mask.shape[0]
    w = mask.shape[1]
    for y in range(h):
        for x in range(w):
            if mask[y, x] < 30:
                mask[y, x] = 0
            else:
                mask[y, x] = 1
    return mask

fountainVid = (VideoFileClip("fountain.mp4").subclip(2, 22).resize(.5))
fountainMask = cv2.imread("fountain.jpg", cv2.IMREAD_GRAYSCALE)
fountainMask = convertMask(fountainMask)
fountainSnapshot = (fountainVid.to_ImageClip().set_duration(fountainVid.duration).set_mask(ImageClip(fountainMask, ismask=True)))
composition = CompositeVideoClip([fountainVid,fountainSnapshot]).speedx(1)
composition.write_gif('fountainGif.gif', fps=25)
fountainVid.write_gif('fountainOrig.gif', fps=25)

metroVid = (VideoFileClip("metro.mp4").subclip(9, 17.5).resize(.5))
metroMask = cv2.imread("metroMask3.jpg", cv2.IMREAD_GRAYSCALE)
metroMask = convertMask(metroMask)
metroSnapshot = (metroVid.to_ImageClip().set_duration(metroVid.duration).set_mask(ImageClip(metroMask, ismask=True)))
metroComposition = CompositeVideoClip([metroVid,metroSnapshot]).speedx(1)
metroComposition.write_gif('metroGif.gif', fps=25)
metroVid.write_gif('metroOrig.gif', fps=25)

bubblesVid = (VideoFileClip("bubbles.mp4").subclip(26, 33).resize(.5))
bubblesMask = cv2.imread("bubblesMask7.jpg", cv2.IMREAD_GRAYSCALE)
bubblesMask = convertMask(bubblesMask)
bubblesSnapshot = (bubblesVid.to_ImageClip().set_duration(bubblesVid.duration).set_mask(ImageClip(bubblesMask, ismask=True)))
bubblesComposition = CompositeVideoClip([bubblesVid,bubblesSnapshot]).speedx(1)
bubblesComposition.write_gif('bubblesGif.gif', fps=25)
bubblesVid.write_gif('bubblesOrig.gif', fps=25)
