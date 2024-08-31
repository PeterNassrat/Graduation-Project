import cv2
import threading
import time
import pickle
from term_flag import term_flag
from right_hand_implementer import right_hand_implementer
from helper import draw_image
from left_hand_implementer import left_hand_implementer
from mode import mode
from helper import reformat_hands_info
import mediapipe as mp
from helper import notify_in_thread
import tkinter as tk
from helper import get_connected_cameras
import warnings
from helper import get_resource_path

def run(boundary_size, selected_camera, start_button):
	try:
		start_button.config(state=tk.DISABLED)
		t_flag = term_flag()
		boundary_size = [int(boundary_size.split('x')[0]), int(boundary_size.split('x')[1])]
		if selected_camera == 'No Cameras':
			raise Exception('There is no connected camera!')
		camera_id = int(selected_camera.split()[-1].strip('()'))
		rh_boundary = None
		lh_implementer = None
		rh_implementer = None
		lh_gesture_clf = None
		rh_gesture_clf = None
		lh_gesture_clf_path = get_resource_path('left_hand_gesture_svm_clf.pkl')
		rh_gesture_clf_path = get_resource_path('right_hand_gesture_svm_clf.pkl')
		with open(lh_gesture_clf_path, 'rb') as f:
			lh_gesture_clf = pickle.load(f)
		with open(rh_gesture_clf_path, 'rb') as f:
			rh_gesture_clf = pickle.load(f)
		rh_mode = mode()
		scroll_speed = 20
		start_time = time.time()

		mp_hands = mp.solutions.hands
		hands = mp_hands.Hands(static_image_mode=False,
					max_num_hands=2,
					min_detection_confidence=0.5,
					min_tracking_confidence=0.5)
		cap = cv2.VideoCapture(camera_id)
		try:
			while cap.isOpened() and not t_flag.get_flag():
				success, image = cap.read()
				if not success:
					continue

				image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

				image.flags.writeable = False
				results = hands.process(image)

				image.flags.writeable = True
				image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

				hands_info = []

				if results.multi_hand_landmarks:
					for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
						hand_label = 1 if handedness.classification[0].label == 'Right' else 0
						hands_info.append(hand_label)

						for landmark in hand_landmarks.landmark:
							hands_info.append(landmark.x)
							hands_info.append(landmark.y)

				hands_info = reformat_hands_info(hands_info)
				left_hand_landmarks = hands_info[0]
				right_hand_landmarks = hands_info[1]

				if rh_boundary == None:
					rh_boundary = [[(image.shape[1] // 2 - boundary_size[0] // 2), (image.shape[0] // 2 - boundary_size[1] // 2)], [(image.shape[1] // 2 + boundary_size[0] // 2), (image.shape[0] // 2 + boundary_size[1] // 2)]]
				if lh_implementer == None:
					lh_implementer = left_hand_implementer(lh_gesture_clf, image.shape[1], image.shape[0], rh_mode, t_flag, scroll_speed)
				if rh_implementer == None:
					rh_implementer = right_hand_implementer(rh_gesture_clf, image.shape[1], image.shape[0], rh_boundary, rh_mode)

				lh_implementer.implement(left_hand_landmarks)
				rh_implementer.implement(right_hand_landmarks)

				fps = 30
				div = time.time() - start_time
				if div != 0.0:
					fps = round(1.0 / div)
				start_time = time.time()

				draw_image(image, image.shape[1], image.shape[0], hands_info, rh_boundary, fps)

				cv2.imshow('Hand Remote Control Cpu', image)
				if cv2.waitKey(1) & 0xFF == 27:
					break
		except Exception as e:
			notify_in_thread("Error", f"{e}")
			#print(f'Error: {e}')
		finally:
			hands.close()
			cap.release()
			cv2.destroyAllWindows()
	except Exception as e:
		notify_in_thread("Error", f"{e}")
		#print(f'Error: {e}')
	finally:
		start_button.config(state=tk.NORMAL)
		notify_in_thread("Note", "Session end")

def start(boundary_size, selected_camera, start_button):
	start_thread = threading.Thread(target=run, args=(boundary_size, selected_camera, start_button,))
	start_thread.start()
	#start_thread.join()

def main():
	try:
		warnings.filterwarnings("ignore")
		root = tk.Tk()
		root.title("Hand Remote Control")
		root.geometry("680x480")
		root.configure(bg='#2c3e50')

		label_frame_size = tk.Label(root, text="Right Hand Boundary:", font=('Calibri', 14), bg='#2c3e50', fg='white')
		label_frame_size.place(x=100, y=100)
		frame_size = tk.StringVar(root)
		frame_size.set("200x150")
		sizes = ["100x75", "200x150", "300x225"]
		operation_menu1 = tk.OptionMenu(root, frame_size, *sizes)
		operation_menu1.config(font=('Calibri', 12), bg='#ecf0f1', fg='#2c3e50', width=15)
		operation_menu1["menu"].config(font=('Calibri', 12), bg='#ecf0f1', fg='#2c3e50')
		operation_menu1.place(x=350, y=100)

		camera_ids = get_connected_cameras()
		camera_options = [f"Camera {i+1} (ID: {i})" for i in camera_ids]

		label_camera = tk.Label(root, text="Camera:", font=('Calibri', 14), bg='#2c3e50', fg='white')
		label_camera.place(x=100, y=200)

		default_camera = tk.StringVar(root)
		if camera_options:
			default_camera.set(camera_options[0])
		else:
			default_camera.set("No Cameras")

		operation_menu2 = tk.OptionMenu(root, default_camera, *camera_options)
		operation_menu2.config(font=('Calibri', 12), bg='#ecf0f1', fg='#2c3e50', width=25)
		operation_menu2["menu"].config(font=('Calibri', 12), bg='#ecf0f1', fg='#2c3e50')
		operation_menu2.place(x=250, y=200)

		start_button = tk.Button(root, text="START", width=32, height=1, font=('Calibri', 16), fg="white", bg="#16a085", bd=0, command=lambda: start(frame_size.get(), default_camera.get(), start_button))
		start_button.place(x=100, y=300)
		
		root.mainloop()
	except Exception as e:
		notify_in_thread("Error", f"{e}")
		#print(f'Error: {e}')

if __name__ == '__main__':
	main()