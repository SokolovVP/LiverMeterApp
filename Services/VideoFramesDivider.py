from typing import overload
import cv2
from os import path


class VideoFramesDivider:

    @staticmethod
    @overload
    def divide_video_into_frames(file_path: str) -> list:
        if not path.exists(file_path):
            raise Exception("File doesn't exist")

        video_capture = cv2.VideoCapture(file_path)

        if not video_capture.isOpened():
            raise Exception("File is not a video")

        frames = []
        while True:
            res, frame = video_capture.read()

            if res:
                frames.append(frame)
            else:
                break

        video_capture.release()

        return frames

    @staticmethod
    def divide_video_into_frames(video_capture: cv2.VideoCapture) -> list:
        if not video_capture.isOpened():
            raise Exception("File is not a video")

        frames = []
        while True:
            res, frame = video_capture.read()

            if res:
                frames.append(frame)
            else:
                break

        video_capture.release()

        return frames


