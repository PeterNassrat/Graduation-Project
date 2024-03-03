# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 01:58:09 2024

@author: peter
"""
import cv2
#import win32gui
import mediapipe as mp
#import autopy
import tkinter as tk
import mouse
import time

def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

p_time = 0

imgHeight = 270     # The static height of the image
imgWidth = 480      # The static width of the image

dispHeight = 135    # The static height of the virtual display inside the image
dispWidth = 240     # The static width of the virtual display inside the image

screenWidth, screenHeight = get_screen_size()
print(screenWidth, screenHeight)

topLeft = (dispWidth - 80, (imgHeight - dispHeight) // 2 - 20)
bottomRight = (topLeft[0] + dispWidth, topLeft[1] + dispHeight)


#hlms = None

#print(topLeft)
#print(bottomRight)
#print(type(bottomRight[0]))

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
videoCapture = cv2.VideoCapture(0)
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = 'C:/Users/peter/Spyder Projects/Graduation Project 2024/gesture_recognizer.task'
'''
def smooth_move(start_pos, end_pos, duration=0.015  , steps=1):
    delta_x = end_pos[0] - start_pos[0]
    delta_y = end_pos[1] - start_pos[1]
    
    for step in range(steps):
        t = (step + 1) / steps
        x = start_pos[0] + t * delta_x
        y = start_pos[1] + t * delta_y
        autopy.mouse.move(x, y)
        time.sleep(duration / steps)
'''

def mouse_move(result, handMode, handExec):
    #autopy.mouse.toggle(False)
    IFT = result.hand_landmarks[handExec][8]
    rx, ry = IFT.x, IFT.y
    rx = (int)(rx * imgWidth)
    ry = (int)(ry * imgHeight)
    #print(rx, ry)
    if rx >= topLeft[0] and rx <= bottomRight[0] and ry >= topLeft[1] and ry <= bottomRight[1]:
        rx = (int)((rx - topLeft[0]) / dispWidth * screenWidth)
        ry = (int)((ry - topLeft[1]) / dispHeight * screenHeight)
        print(rx, ry)
        if rx >= 0 and rx < screenWidth and ry >= 0 and ry < screenHeight:
            mouse.move(rx, ry, absolute=True, duration=0)
            
def mouse_pointer_track(result, handMode, handExec):
    if result.gestures[handMode][0].category_name == 'Pointing_Up':
        mouse_move(result, handMode, handExec)
    elif result.gestures[handMode][0].category_name == 'Closed_Fist':
        #autopy.mouse.toggle(True)
        mouse.click('left')
        mouse_move(result, handMode, handExec)
    #else:
        #autopy.mouse.toggle(False)
        
                
def mouse_pointer(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    #global hlms
    #hlms = result.hand_landmarks
    if len(result.handedness) == 2:
        if result.handedness[0][0].display_name == 'Right':
            mouse_pointer_track(result, 0, 1)
        elif result.handedness[1][0].display_name == 'Right':
            mouse_pointer_track(result, 1, 0)

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    num_hands=2,
    result_callback=mouse_pointer)

try:
    while True:
        success, image = videoCapture.read()
        if not success:
            continue
        image = cv2.resize(image, (imgWidth, imgHeight))
        image = cv2.flip(image, 1)
        
        rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgbImage)
        timestamp_ms = (int)(round(videoCapture.get(cv2.CAP_PROP_POS_MSEC)))
        #print("Frame timestamp (ms):", timestamp_ms)
        with GestureRecognizer.create_from_options(options) as recognizer:
            recognizer.recognize_async(mp_image, timestamp_ms)
        
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        cv2.putText(image, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        
        cv2.rectangle(image, topLeft, bottomRight, (255, 255, 0), 1)
        cv2.imshow("Camera Video", image)
        cv2.moveWindow("Camera Video", 0, 0)
        #hwnd = win32gui.FindWindow(None, "Camera Video")
        #win32gui.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    videoCapture.release()
    cv2.destroyAllWindows()