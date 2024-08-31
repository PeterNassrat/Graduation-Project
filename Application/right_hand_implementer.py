import pyautogui
import numpy as np
from collections import deque
class right_hand_implementer:
	def __init__(self, gesture_svm_clf, image_width, image_height, right_hand_boundary, mode, gesture_history_size = 1, confidence_threshold = 0.9, action_tempo = 15, movement_smoothing_factor = 0.9):
		self._gesture_svm_clf = gesture_svm_clf
		self._right_hand_boundary = right_hand_boundary
		self._image_width = image_width
		self._image_height = image_height
		self._screen_width, self._screen_height = pyautogui.size()
		self._mode = mode
		self._gesture_history_size = gesture_history_size
		self._gesture_history = deque([])
		self._confidence_threshold = confidence_threshold
		self._action_tempo = action_tempo
		self._movement_smoothing_factor = movement_smoothing_factor
		self._left_mouse_down_flag = False
		self._right_mouse_down_flag = False
		self._current_iteration = 0
		self._last_left_click = 0
		self._last_right_click = 0
		pyautogui.PAUSE = 0
		pyautogui.FAILSAFE = False
		

	def implement(self, hand_landmarks):
		self._current_iteration += 1
		if len(hand_landmarks) == 21:
			gesture = self._get_gesture([hand_landmarks[2], hand_landmarks[3], hand_landmarks[4],
								hand_landmarks[10], hand_landmarks[11], hand_landmarks[12],
								hand_landmarks[14], hand_landmarks[15], hand_landmarks[16],
								hand_landmarks[18], hand_landmarks[19], hand_landmarks[20]], self._image_width, self._image_height)
			if len(self._gesture_history) == self._gesture_history_size:
				self._gesture_history.append(gesture)
				self._gesture_history.popleft()
				most_frequent_gesture = self._get_most_frequent_gesture()
				#print(most_frequent_gesture)	# for debug
				if most_frequent_gesture == 1:
					self._left_mouse_click()
				elif most_frequent_gesture == 2:
					self._right_mouse_click()
				elif most_frequent_gesture == 3:
					if self._mode.get() == 0:
						self._left_mouse_double_click()
					else:
						self._left_mouse_down()
				else:
					if self._left_mouse_down_flag:
						self._left_mouse_up()
			else:
				self._gesture_history.append(gesture)
			self._move_mouse_pointer(hand_landmarks[8])

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

	def _move_mouse_pointer(self, index_finger_tip):
		x = index_finger_tip[0] * self._image_width
		y = index_finger_tip[1] * self._image_height
		
		x = (x - self._right_hand_boundary[0][0]) / (self._right_hand_boundary[1][0] - self._right_hand_boundary[0][0]) * self._screen_width
		y = (y - self._right_hand_boundary[0][1]) / (self._right_hand_boundary[1][1] - self._right_hand_boundary[0][1]) * self._screen_height
		
		x_div = 10
		y_div = 6
		
		x = ((x // x_div) * x_div) + (x_div // 2)
		y = ((y // y_div) * y_div) + (y_div // 2)
		
		current_position = pyautogui.position()
		x = int(self._movement_smoothing_factor * current_position[0] + (1 - self._movement_smoothing_factor) * x)
		y = int(self._movement_smoothing_factor * current_position[1] + (1 - self._movement_smoothing_factor) * y)
		
		if pyautogui.onScreen(x, y):
			pyautogui.moveTo(x, y)
	
	def _left_mouse_down(self):
		if not self._left_mouse_down_flag and self._current_iteration > self._last_left_click + self._action_tempo:
			pyautogui.mouseDown()
			self._left_mouse_down_flag = True

	def _left_mouse_up(self):
		if self._left_mouse_down_flag:
			self._last_left_click = self._current_iteration
			pyautogui.mouseUp()
			self._left_mouse_down_flag = False
	
	def _left_mouse_click(self):
		if self._current_iteration > self._last_left_click + self._action_tempo:
			self._last_left_click = self._current_iteration
			pyautogui.click()
	
	def _right_mouse_click(self):
		if self._current_iteration > self._last_right_click + self._action_tempo:
			self._last_right_click = self._current_iteration
			pyautogui.click(button='right')

	def _left_mouse_double_click(self):
		if self._current_iteration > self._last_left_click + self._action_tempo:
			self._last_left_click = self._current_iteration
			pyautogui.click(clicks=2)

	def _get_most_frequent_gesture(self):
		frequency_list = [0, 0, 0, 0, 0]
		for gesture in self._gesture_history:
			frequency_list[gesture] += 1
		return frequency_list.index(max(frequency_list))
