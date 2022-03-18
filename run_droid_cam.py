import os

os.system("sudo modprobe v4l2loopback")
# os.system("droidcam & ffplay /dev/video2")
# os.system("droidcam & ffplay /dev/video1")
os.system("droidcam & ffplay /dev/video0")
os.system("droidcam")
