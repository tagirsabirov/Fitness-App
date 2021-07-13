import cv2
import mediapipe as mp
import time
import numpy as np

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()
pTime = 0
cap = cv2.VideoCapture(0)
mp_holistic = mp.solutions.holistic
joint_list = [[16, 14, 12], [15, 13, 11]]
counter = 0
j = 1

while True:
	succes, img = cap.read()
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results = pose.process(imgRGB)

	if results.pose_landmarks:
		mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

	cTime = time.time()
	fps = 1/(cTime - pTime)
	pTime = cTime
	cv2.putText (img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
	cv2.putText (img, str(int(counter)), (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
	cv2.imshow ("image", img)
	cv2.waitKey (1)

	if results.pose_landmarks:
		a = np.array([results.pose_landmarks.landmark[16].x, results.pose_landmarks.landmark[16].y])
		b = np.array([results.pose_landmarks.landmark[14].x, results.pose_landmarks.landmark[14].y])
		c = np.array([results.pose_landmarks.landmark[12].x, results.pose_landmarks.landmark[12].y])
		d = np.array([results.pose_landmarks.landmark[15].x, results.pose_landmarks.landmark[15].y])
		e = np.array([results.pose_landmarks.landmark[13].x, results.pose_landmarks.landmark[13].y])
		f = np.array([results.pose_landmarks.landmark[11].x, results.pose_landmarks.landmark[11].y])

		radian1 = np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
		radian2 = np.arctan2(f[1] - e[1], f[0]-e[0]) - np.arctan2(d[1]-e[1], d[0]-e[0])
		angle1 = np.abs(radian1*180.0/np.pi)
		angle2 = np.abs(radian2*180.0/np.pi)
		if angle1 > 180.0:
			angle1 = 360-angle1
		if angle2 > 180.0:
			angle2 = 360-angle2
		if angle1 > 140 and angle2 > 140:
			j = 1
		if angle1 < 110 and angle2 < 110 and j == 1:
			counter += 1
			j = 0

cap.release()
cv2.destroyAllWindows()