from modules import *
import os, sys

application_path = os.path.dirname(sys.executable)

bbox = None
if __name__ == "__main__":
    os.system("cls")
    print("Please enter a video path")
    path = input(">> ")
    if (os.path.exists(path)):
        while True:
            os.system("cls")
            print("Welcome . . .")
            print("Please select one of the modes")
            print("[0] Exit \n"
                  "[1] Try Trackers \n"
                  "[2] Start Labeling")
            ans0 = input(">> ")
            if (ans0 == "0"):
                print("Exiting . . . ")
                break
            elif (ans0 == "1"):
                os.system("cls")
                print("Would you like to try all trackers or\n only selected one ?")
                print("[1] All Trakers\n"
                      "[2] Selected One")
                ans1 = input(">> ")
                if (ans1 == "1"):
                    bbox = tracker_results(path, 0)
                elif (ans1 == "2"):
                    bbox = tracker_results(path, 1)
            elif (ans0 == "2"):
                os.system("cls")
                print("Select a tracker :\n"
                      "[0] BOOSTING\n"
                      "[1] MIL\n"
                      "[2] KCF\n"
                      "[3] TLD\n"
                      "[4] MEDIANFLOW\n"
                      "[5] GOTURN\n"
                      "[6] MOSSE\n"
                      "[7] CSRT")
                tracker = input(">> ")
                if (bbox is None):
                    start_the_process(path, tracker, mode=0)
                else:
                    start_the_process(path, tracker, bbox=bbox)
    else:
        print("Video could not be found.")
        print("Exitinf the program . . .")
