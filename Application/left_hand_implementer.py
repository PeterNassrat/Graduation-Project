from collections import deque
import numpy as np
from helper import notify_in_thread
import pyautogui

class left_hand_implementer:
	def __init__(self, gesture_svm_clf, image_width, image_height, mode, term_flag, scroll_speed, gesture_history_size = 5, confidence_threshold = 0.8, action_tempo = 15):
		self._gesture_svm_clf = gesture_svm_clf
		self._image_width = image_width
		self._image_height = image_height
		self._mode = mode
		self._change_mode = False
		self._term_flag = term_flag
		self._scroll_speed = scroll_speed
		self._gesture_history_size = gesture_history_size
		self._gesture_history = deque([])
		self._confidence_threshold = confidence_threshold
		self._action_tempo = action_tempo
		self._current_iteration=0
		self._last_scroll_up=0
		self._last_scroll_down=0
		self._last_zoom_in=0
		self._last_zoom_out=0
		self._last_left_arrow_press = 0
		self._last_right_arrow_press = 0
		pyautogui.PAUSE = 0
		#pyautogui.FAILSAFE = False

	def implement(self, hand_landmarks):
		self._current_iteration+=1
		if len(hand_landmarks) == 21:
			gesture = self._get_gesture(hand_landmarks, self._image_width, self._image_height)
			if len(self._gesture_history) == self._gesture_history_size:
				self._gesture_history.append(gesture)
				self._gesture_history.popleft()
				most_frequent_gesture = self._get_most_frequent_gesture()
				if most_frequent_gesture == 1:
					#if self._current_iteration > self._last_scroll_up + self._action_tempo:
						#self._last_scroll_up = self._current_iteration
					pyautogui.scroll(self._scroll_speed)
				elif most_frequent_gesture == 2:
					if self._current_iteration > self._last_right_arrow_press + self._action_tempo:
						self._last_right_arrow_press = self._current_iteration
						pyautogui.press('right')
				elif most_frequent_gesture == 3:
					if self._current_iteration > self._last_zoom_in + self._action_tempo:
						self._last_zoom_in = self._current_iteration
						pyautogui.hotkey('ctrl', '+')
				elif most_frequent_gesture == 4:
					if self._change_mode:
						if self._mode.get() != 0:
							#print('Click mode')	# for debug
							self._change_mode = False
							self._mode.change(0)
							notify_in_thread("Mode", "Click mode")
				elif most_frequent_gesture == 5:
					if self._current_iteration > self._last_zoom_out + self._action_tempo:
						self._last_zoom_out = self._current_iteration
						pyautogui.hotkey('ctrl', '-')
				elif most_frequent_gesture == 6:
					if not self._change_mode:
						self._change_mode = True
				elif most_frequent_gesture == 7:
					if self._change_mode:
						if self._mode.get() != 1:
							#print('Drag drop mode')	# for debug
							self._change_mode = False
							self._mode.change(1)
							notify_in_thread("Mode", "Drag drop mode")
				elif most_frequent_gesture == 8:
					if self._current_iteration > self._last_left_arrow_press + self._action_tempo:
						self._last_left_arrow_press = self._current_iteration
						pyautogui.press('left')
				elif most_frequent_gesture == 9:
					#if self._current_iteration > self._last_scroll_down + self._action_tempo:
						#self._last_scroll_down = self._current_iteration
					pyautogui.scroll(-self._scroll_speed)
				elif most_frequent_gesture == 10:
					if self._change_mode:
						self._term_flag.switch()
			else:
				self._gesture_history.append(gesture)

	def _get_gesture(self, hand_landmarks, image_width, image_height):
		x_min = y_min = float('inf')
		x_max = y_max = float('-inf')
		for lm in hand_landmarks:
			cx, cy = int((1.0-lm[0]) * image_width), int(lm[1] * image_height)
			x_min = min(x_min, cx)
			y_min = min(y_min, cy)
			x_max = max(x_max, cx)
			y_max = max(y_max, cy)

		normalized_landmarks_on_hand_region = []
		for lm in hand_landmarks:
			cx, cy = int((1.0 - lm[0]) * image_width), int(lm[1] * image_height)
			if x_max - x_min != 0 and y_max - y_min != 0:
				relative_x = (cx - x_min) / (x_max - x_min)
				relative_y = (cy - y_min) / (y_max - y_min)
				normalized_landmarks_on_hand_region.extend([relative_x, relative_y])

		normalized_landmarks_on_hand_region = np.array(normalized_landmarks_on_hand_region).reshape(1, -1)
		gesture = self._gesture_svm_clf.predict(normalized_landmarks_on_hand_region)
		confidence_scores = self._gesture_svm_clf.predict_proba(normalized_landmarks_on_hand_region)
		max_confidence_score = np.max(confidence_scores)
		if max_confidence_score > self._confidence_threshold:
			return gesture[0]+1
		return 0
	
	def _get_most_frequent_gesture(self):
		frequency_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for gesture in self._gesture_history:
			frequency_list[gesture] += 1
		return frequency_list.index(max(frequency_list))
