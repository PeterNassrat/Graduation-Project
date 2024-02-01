# HAND REMOTE CONTROL

## Introduction

- ### Overview
 
- ### Objectives

## Scope

<font size="4">

Our goal is to control a laptop or desktop remotely using our hands – **_the left hand and the right hand_** – by connecting the **mouse** and the **keyboard** functions to an internal or external **camera**.

This kind of control is not very common in real life yet. It is still under development, and it is a research topic. That is why we chose it as our project. We want to make it possible and practical for real-life use. We also want to learn more about this technology and how to improve it and make it popular and helpful.

We are eager to learn and overcome the challenges that this technology may face because it is not well defined yet. But we are confident that we can contribute to this technology.

This technology can be useful for many purposes, such as **presentation** and **lecturing** and **personal use**. It can make controlling a laptop easier and more fun just by using our hands.

We will start by using two pretrained models that are built by Google developers.
- The first one is the **Hand landmark detection** model.
- The second one is the **Gesture recognition** model.

*_We will respect the license agreement and use these models according to the terms and conditions_*.

The way that the hand control will work is that we will use one hand as a **mode selector** and the other hand as a **mode executor**. The modes that we will provide are:
- **Mouse pointer mode**
- ...

</font>

## Requirements

<font size="4">
 
- **Functional Requirements**:
    - **Hand Landmark Detection**:<br> The system must accurately detect and track the landmarks or key points on the user's hand, such as fingertips and palm.
    - **Tracking Consistency**:<br> The hand landmark detection should maintain consistent tracking, even during rapid hand movements or changes in hand orientation.
    - **Coordinate Mapping**:<br> The system must map the detected hand landmarks to screen coordinates for precise control of the mouse cursor.
    - **Mouse Movement**:<br> Translate the movements of detected hand landmarks into corresponding mouse movements on the screen.
    - **Click Detection**:<br> Identify gestures or hand configurations representing left-click, right-click, and other click actions.
    - **Drag and Drop**:<br> Implement the ability to perform drag-and-drop actions by recognizing specific hand movements.
    - **Scrolling**:<br> Allow users to scroll through documents or images using hand gestures.
    - **Tab Switching**:<br> The user should be able to switch between open tabs or applications on the computer using specific hand gestures.
    - **Real-time Responsiveness**:<br> Ensure real-time responsiveness in updating the mouse cursor based on changes in hand landmark positions.  
    - **Error Handling**:<br> Implement mechanisms to handle inaccuracies in hand landmark detection, providing feedback to the user when needed.
    - **User Interface Feedback**:<br> Provide visual or auditory feedback to indicate successful hand landmark detection and corresponding mouse actions.
- **Non-Functional Requirements**:
    - **Performance**:<br> The system must respond to changes in hand landmark positions within 100 milliseconds to provide a real-time user experience and the system should be able to process frames at a rate of up to 30 fps
    - **Accuracy**: <br>The hand landmark detection algorithm must achieve an accuracy rate of at least 95% in identifying key points on the user's hand.
    - **Scalability**: <br>The system should handle hand landmark detection for various hand sizes and shapes, ensuring scalability for a diverse user population.
    - **Usability**: <br>The user interface must be intuitive and user-friendly, allowing users to easily understand and control the mouse through hand gestures.
    - **Robustness**: <br>The system should operate robustly in various lighting conditions and environments without significant degradation in performance.
    - **Security**: <br>Implement encryption for any communication between the system and the computer to ensure the security and privacy of user hand data.
    - **Reliability**: <br>The system should maintain consistent and reliable hand landmark detection, minimizing errors and unexpected behavior.
    - **Compatibility**: <br>Ensure compatibility with a wide range of computer systems, operating systems, and hardware configurations.
    - **Maintainability**: <br>Design the system in a modular and maintainable way to facilitate future updates, improvements, and bug fixes.
    - **Portability**: <br>The system should be portable across different devices, allowing users to control the mouse through hand gestures on various platforms.
    - **Response Time**: <br>The mouse cursor should respond to hand movements without perceptible delay, providing a seamless and responsive user experience.
    - **Adaptability**: <br>The system must adapt to changes in hand landmark patterns caused by variations in hand positions, orientations, and gestures.

</font>
   
## Timeline

## Stakeholders

## Team

## Risk Management

<font size="4">

- **Errors in detection**:

  **_Solutions_**:
  - **Machine learning training**:<br> continuously train the AI model with diverse datasets to improve its ability to recognize different scenarios and reduce false positives or negatives.
  - **Regular maintenance**:<br> establish a routine for maintenance and calibration to ensure that sensors and components remain accurate over time.
  - **Testing and simulation**:<br> regularly test the system in controlled environments and simulate various scenarios to identify potential detection errors and refine the algorithms accordingly.

  By combining these strategies, you can enhance the reliability and safety of the AI remote control hand, reducing the impact of detection errors.
- **Misinterpretation of gestures**:<br> The system may misinterpret user gestures, leading to unintended actions.

  **_Solution_**:<br>
Conduct extensive testing with diverse user groups, refines gesture recognition algorithms.
- **Budget**:<br> The project might exceed budget constraints.

  **_Solution_**:<br>
conduct a detailed cost analysis, prioritize essential features and explore cost-effective alternatives without compromising safety.
- **User discomfort**:<br> Prolonged use of gesture control may lead to user discomfort.

  **_Solution_**:<br>
design comfort gestures, allow for breaks and provide alternative control methods to reduce physical stain.
- **Accessibility concerns**:<br> Users may have difficulty performing specific gestures due to physical limitations.

  **_Solution_**:<br>
provide alternative control options, such as voice commands or physical buttons.
- **Environmental interferences**:<br> External factors such as lighting conditions may affect gesture recognition accuracy.

  **_Solution_**:<br>
implement adaptive algorithms that adjust to varying environmental conditions and use sensors for context awareness. 

</font>

## Budget and Resources
- ### Resources 
    Human Resources:
    - ### Software Developer:

        Role: Develop software for hand landmark detection and mouse control.
        Responsibilities: Code implementation, testing, and debugging.
        
    Skills and Expertise:
    - ### Software Development:
        Proficiency in Python
        Experience in computer vision and image processing. 

    Development Tools:
    - ### Computer Vision Libraries:
        OpenCV (cv2) :
        It provides tools for image and video processing, including functions for image manipulation, feature detection, and object tracking.

        MediaPipe (mediapipe) :
        MediaPipe is a library developed by Google that offers solutions for various perception tasks, including hand tracking.

        Autopy (autopy):
        Autopy is a library for automating mouse and keyboard actions. It can be used to simulate mouse clicks, movements, and keyboard input.

    Equipment:
    - ### Sensors :
        Laptop camera OR External cameras for computers
    


## Communication Plan

## Monitoring and Evaluation

## Lessons Learned

## Closure Criteria

## Appendices
