import os
import shutil
import cv2 as cv


def tracker_results(VideoPath, mode=0):
    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    firstBbox = []

    # Capturing first frame
    vid = cv.VideoCapture(VideoPath)
    ret, img = vid.read()
    fHeight, fWidth = img.shape[:2]
    img = cv.resize(img, (fWidth // 2, fHeight // 2))

    bbox = cv.selectROI(img, False)
    cv.destroyWindow("ROI selector")
    firstBbox.append(bbox)

    val = 0
    while True:
        if (mode != 0):
            val = int(input("Enter A Tracker Type ::\n"
                            "[0] BOOSTING\n"
                            "[1] MIL\n"
                            "[2] KCF\n"
                            "[3] TLD\n"
                            "[4] MEDIANFLOW\n"
                            "[5] GOTURN\n"
                            "[6] MOSSE\n"
                            "[7] CSRT\n"
                            "==> "))

        tracker_type = tracker_types[val]

        if tracker_type == 'BOOSTING':
            tracker = cv.legacy.TrackerBoosting_create()
        elif tracker_type == 'MIL':
            tracker = cv.TrackerMIL_create()
        elif tracker_type == 'KCF':
            tracker = cv.TrackerKCF_create()
        elif tracker_type == 'TLD':
            tracker = cv.legacy.TrackerTLD_create()
        elif tracker_type == 'MEDIANFLOW':
            tracker = cv.legacy.TrackerMedianFlow_create()
        elif tracker_type == 'GOTURN':
            tracker = cv.TrackerGOTURN_create()
        elif tracker_type == 'MOSSE':
            tracker = cv.legacy.TrackerMOSSE_create()
        elif tracker_type == "CSRT":
            tracker = cv.TrackerCSRT_create()

        boxRet = tracker.init(img, firstBbox[0])

        while True:
            ret, frame = vid.read()

            if not ret:
                print("INFO :: Video has ended . . .")
                break

            frame = cv.resize(frame, (fWidth // 2, fHeight // 2))
            boxRet, bbox = tracker.update(frame)

            if (boxRet):
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            else:
                cv.putText(frame, "Tracking failure detected", (10, 55), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

            cv.putText(frame, tracker_type + " Tracker", (10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
            cv.imshow("Tracking", frame)

            k = cv.waitKey(1) & 0xff
            if k == 27: break

        if (mode != 0):
            vid.release()
            break

        if (val == 7):
            vid.release()
            break

        val += 1
        vid = cv.VideoCapture(VideoPath)
        cv.destroyAllWindows()

    vid.release()
    cv.destroyAllWindows()
    print("INFO :: End of trackers . . .")
    return firstBbox[0]


def create_directory():
    userName = os.getlogin()
    path = 'C:\\Users\\{}\\Desktop'.format(userName)
    os.chdir(path)
    if (os.path.exists(path + "\\label_results")):
        shutil.rmtree(path + "\\label_results")

    os.mkdir(path + "\\label_results")
    return path + "\\label_results"


def create_labels(path, img, name, bbox):
    h, w = img.shape[:2]

    x_center = int(bbox[0] + (bbox[2] / 2))
    y_center = int(bbox[1] + (bbox[3] / 2))
    l_width = int(bbox[2])
    l_height = int(bbox[3])

    x_center_norm = x_center / w
    y_center_norm = y_center / h
    width_norm = l_width / w
    height_norm = l_height / h

    f = open(path + "/" + name + ".txt", "a")
    f.write("0 {} {} {} {}".format(x_center_norm, y_center_norm, width_norm, height_norm))
    cv.imwrite(path + "/" + name + ".png", img)


def start_the_process(VideoPath, val, mode=1, bbox=None):
    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

    tracker_type = tracker_types[int(val)]

    if tracker_type == 'BOOSTING':
        tracker = cv.legacy.TrackerBoosting_create()
    elif tracker_type == 'MIL':
        tracker = cv.TrackerMIL_create()
    elif tracker_type == 'KCF':
        tracker = cv.TrackerKCF_create()
    elif tracker_type == 'TLD':
        tracker = cv.legacy.TrackerTLD_create()
    elif tracker_type == 'MEDIANFLOW':
        tracker = cv.legacy.TrackerMedianFlow_create()
    elif tracker_type == 'GOTURN':
        tracker = cv.TrackerGOTURN_create()
    elif tracker_type == 'MOSSE':
        tracker = cv.legacy.TrackerMOSSE_create()
    elif tracker_type == "CSRT":
        tracker = cv.TrackerCSRT_create()

    firstBbox = []
    vidPath = os.getcwd() + "\\" + VideoPath
    SavePath = create_directory()

    vid = cv.VideoCapture(vidPath)
    ret, img = vid.read()
    fHeight, fWidth = img.shape[:2]
    img = cv.resize(img, [fWidth // 2, fHeight // 2])

    if bbox is not None:
        firstBbox = [bbox]
    else:
        bbox = cv.selectROI(img, False)
        cv.destroyWindow("ROI selector")
        firstBbox.append(bbox)

    boxRet = tracker.init(img, firstBbox[0])

    cnt = 0
    while True:
        ret, frame = vid.read()
        if not ret:
            print("INFO :: Video has ended . . .")
            break

        frame = cv.resize(frame, (fWidth // 2, fHeight // 2))
        boxRet, bbox = tracker.update(frame)

        if boxRet:
            cnt += 1
            name = "img_{}".format(cnt)
            create_labels(SavePath, frame, name, bbox)

        k = cv.waitKey(1) & 0xff
        if k == 27: break

    vid.release()
    print("INFO :: Finished . . .")
