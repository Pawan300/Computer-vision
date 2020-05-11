import argparse
import time

import cv2
import simpleaudio as sa
import numpy as np

import imutils
from camera_use import Live_video
from central_tracking_algorithm import CentroidTracker
from invisible import Invisible


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--prototxt",
        required=True,
        help="path to Caffe 'deploy' prototxt file",
        default="/home/hackerearth/Documents/temp/demo_camera_use/object_detection/deploy.prototxt",
    )
    parser.add_argument(
        "-m",
        "--model",
        required=True,
        help="path to Caffe pre-trained model",
        default="/home/hackerearth/Documents/temp/demo_camera_use/object_detection/model.caffemodel",
    )
    parser.add_argument(
        "-c",
        "--confidence",
        type=float,
        default=0.5,
        help="minimum probability to filter weak detections",
    )
    parser.add_argument(
        "-d",
        "--output_data",
        help="path to store output file",
        default="/home/hackerearth/Documents/temp/demo_camera_use/Video/recording.avi",
    )

    args = vars(parser.parse_args())
    return args


def social_distance(object):
    distance = {}
    keys = list(object.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a = object[keys[i]]
            b = object[keys[j]]
            temp = np.linalg.norm(a - b)
            distance[keys[i], keys[j]] = temp

    return distance


def main():
    args = argument_parser()
    l = Live_video(args["output_data"])

    ct = CentroidTracker(args["confidence"])
    (H, W) = (None, None)

    print("[INFO] loading model...")
    net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

    print("[INFO] starting video stream...")

    while True:
        frame = l.record()

        if W is None or H is None:
            (H, W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 1.0, (W, H), (104, 117, 123))
        net.setInput(blob)
        detections = net.forward()
        rectangle = []
        for i in range(0, detections.shape[2]):
            if detections[0, 0, i, 2] > args["confidence"]:
                box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                rectangle.append(box.astype("int"))

                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 0), 2)

        objects = ct.update_object(rectangle)
        # print(objects)
        flag = 1
        if len(objects) > 1:
            distance = social_distance(objects)
            print(distance)
            for (objectID, centroid) in objects.items():
                for i in distance:
                    if objectID in i and distance[i] < 200:
                        cv2.putText(
                            frame,
                            "maintain distance",
                            (centroid[0] - 10, centroid[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0, 255, 0),
                            2,
                        )
                        wave_obj = sa.WaveObject.from_wave_file("/home/hackerearth/Downloads/Siren-SoundBible (mp3cut.net).wav")
                        play_obj = wave_obj.play()
                    #     print("dedwexwq")
                    #     flag =0
                    # else:
                    #     if flag==0:
                    #         print("adddawdqw")
                    #         play_obj.stop()

                cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

        frame = l.window(frame)
        l.save_video(frame)
        if cv2.waitKey(1) == ord("q"):
            break

    l.release()


if __name__ == "__main__":
    main()
