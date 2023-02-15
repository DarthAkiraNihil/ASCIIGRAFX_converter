from core.scripts.carver import carver
from core.scripts.handler import conventers
import os
import sys
import subprocess
import shutil

SAVING_FRAMES_PER_SECOND = 30
COMPRESSION = 10


def main():
    video_file = sys.argv[1]
    carver(video_file, SAVING_FRAMES_PER_SECOND)
    conventers(COMPRESSION)
    subprocess.check_output(["C:\\Users\\EgrZver\\Documents\\ffmpeg-5.1.2-full_build\\bin\\ffmpeg.exe", "-framerate", str(SAVING_FRAMES_PER_SECOND), "-i", f"{os.getcwd()}/processed/%07d.jpg", f"{video_file}-processed.mp4"])
    shutil.rmtree("not_processed/")
    shutil.rmtree('processed/')
    
    


if __name__ == "__main__":
    main()
