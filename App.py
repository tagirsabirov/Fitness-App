import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()
pTime = 0
cap = cv2.VideoCapture(0)

while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)
    results = pose.process (imgRGB)
    print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText (img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow ("image", img)
    cv2.waitKey (1)

cap.release()
cv2.destroyAllWindows()