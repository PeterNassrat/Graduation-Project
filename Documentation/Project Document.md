# REMOTE CONTROL HAND GESTURES

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
- ### Functional Requirements: 
    - ### Hand Landmark Detection: 
        The system must accurately detect and track the landmarks or key points on the user's hand, such as fingertips and palm.
    - ### Tracking Consistency:

        The hand landmark detection should maintain consistent tracking, even during rapid hand movements or changes in hand orientation.
    - ### Coordinate Mapping:
        The system must map the detected hand landmarks to screen coordinates for precise control of the mouse cursor.
    - ### Mouse Movement:
        Translate the movements of detected hand landmarks into corresponding mouse movements on the screen.
    - ### Click Detection:
        Identify gestures or hand configurations representing left-click, right-click, and other click actions.
    - ### Drag and Drop:
        Implement the ability to perform drag-and-drop actions by recognizing specific hand movements.
    - ### Scrolling:
        Allow users to scroll through documents or images using hand gestures.
    - ### Tab Switching:
        The user should be able to switch between open tabs or applications on the computer using specific hand gestures.
    - ### Real-time Responsiveness:

        Ensure real-time responsiveness in updating the mouse cursor based on changes in hand landmark positions.  
    - ### Error Handling:
        Implement mechanisms to handle inaccuracies in hand landmark detection, providing feedback to the user when needed.
    - ### User Interface Feedback:
        Provide visual or auditory feedback to indicate successful hand landmark detection and corresponding mouse actions.
    #
- ### Non-Functional Requirements: 
    - ### Performance:
        The system must respond to changes in hand landmark positions within 100 milliseconds to provide a real-time user experience and
        the system should be able to process frames at a rate of up to 30 fps
    - ### Accuracy:
        he hand landmark detection algorithm must achieve an accuracy rate of at least 95% in identifying key points on the user's hand.
    - ### Scalability:
        The system should handle hand landmark detection for various hand sizes and shapes, ensuring scalability for a diverse user population.
    - ### Usability:
        The user interface must be intuitive and user-friendly, allowing users to easily understand and control the mouse through hand gestures.s
    - ### Robustness:
        The system should operate robustly in various lighting conditions and environments without significant degradation in performance.
    - ### Security:
        Implement encryption for any communication between the system and the computer to ensure the security and privacy of user hand data.
    - ### Reliability:

        The system should maintain consistent and reliable hand landmark detection, minimizing errors and unexpected behavior.
    - ### Compatibility:

        Ensure compatibility with a wide range of computer systems, operating systems, and hardware configurations.
    - ### Maintainability:

        Design the system in a modular and maintainable way to facilitate future updates, improvements, and bug fixes.
    - ### Portability:

        The system should be portable across different devices, allowing users to control the mouse through hand gestures on various platforms.
    - ### Response Time:

        The mouse cursor should respond to hand movements without perceptible delay, providing a seamless and responsive user experience.
    - ### Adaptability:

        The system must adapt to changes in hand landmark patterns caused by variations in hand positions, orientations, and gestures.
    
## Timeline

## Stakeholders

## Team

## Risk Management

## Budget and Resources

## Communication Plan

## Monitoring and Evaluation

## Lessons Learned

## Closure Criteria

## Appendices
