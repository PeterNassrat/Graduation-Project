import cv2
from plyer import notification
import threading
import sys
import os

def reformat_hands_info(hands_info):
	try:
		formatted_hands_info = [[], []]
		hands_info_len = len(hands_info)

		if hands_info_len > 0:
			handedness_idx = int(hands_info[0])
			for i in range(1, 43, 2):
				formatted_hands_info[handedness_idx].append([hands_info[i], hands_info[i+1]])
		if hands_info_len > 43:
			handedness_idx = int(hands_info[43])
			for i in range(44, 86, 2):
				formatted_hands_info[handedness_idx].append([hands_info[i], hands_info[i+1]])
	except Exception:
		#notify_in_thread("Error", f"{e}")
		#print(f'Error: {e}')
		return [[], []]
	return formatted_hands_info
	
def draw_image(image, image_width, image_height, multi_hand_landmarks, right_hand_boundary, fps):
	for hand_landmarks in multi_hand_landmarks:
		for landmark in hand_landmarks:
			landmark_x = int(landmark[0] * image_width)
			landmark_y = int(landmark[1] * image_height)
			cv2.circle(image, (landmark_x, landmark_y), 5, (255, 0, 0), -1)
	cv2.rectangle(image, right_hand_boundary[0], right_hand_boundary[1], (0, 0, 255), 2)
	cv2.putText(image, str(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

def show_notification(title, message, timeout=1):
	notification.notify(
		title=title,
		message=message,
		app_name='Hand Remote Control',
		timeout=timeout  # Timeout in seconds
	)

def notify_in_thread(title, message, timeout=1):
    notification_thread = threading.Thread(target=show_notification, args=(title, message, timeout))
    notification_thread.start()

def get_connected_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def get_resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
	
    return os.path.join(base_path, relative_path)