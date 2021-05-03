import cv2
import argparse


class Live_video:

    def __init__(self, output_path):
        self.frame = None
        self.check = None
        self.video = cv2.VideoCapture(0)
        self.output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (600, 600))

    def record(self):
        self.check, self.frame = self.video.read()

        return self.frame

    def release(self):
        self.video.release()
        cv2.destroyAllWindows()

    def save_video(self, frame):
        self.output.write(frame)


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--output_path", required=True, help="path to store data")

    args = vars(parser.parse_args())
    return args


def main():
    args = argument_parser()
    l = Live_video(args["output_path"])

    while True:
        frame = l.record()
        print(frame)
        cv2.namedWindow("Live_video", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live_video", 600, 600)
        frame = cv2.putText(frame, "Press q to quit...", (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Live_video", frame)
        l.save_video(frame)
        if cv2.waitKey(1) == ord("q"):
            break

    l.release()


if __name__ == '__main__':
    main()
