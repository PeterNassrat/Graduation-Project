# HAND REMOTE CONTROL

## Contents
<font size="4">
 
1. [Introduction](#introduction)
2. [Scope](#scope)
3. [Requirements](#requirements)
4. [Timeline](#timeline)
5. [Stakeholders](#stakeholders)
6. [Team](#team)
7. [Risk Management](#risk-management)
8. [Resources](#resources)
9. [Communication Plan](#communication-plan)
10. [Monitoring and Evaluation](#monitoring-and-evaluation)
11. [Lessons Learned](#lessons-learned)
12. [Closure Criteria](#closure-criteria)
13. [Appendices](#appendices)

</font>

## Introduction

<a id="introdution"></a>
<font size="4">
  
- **Overview:** <br> This project helps us control devices using hand remotely. <br> The purposed AI virtual mouse system can be used to overcome problems in the real world such as situations where there is no space to use a physical mouse and also for the COVID-19 situation, it is not safe to use the devices by touching them because it may result in a possible situation of the spread of the virus by touching the devices.
- **Objectives:** <br> The proposed AI virtual mouse can be used to overcome these problems since hand gestures and hand tip detection is used to control the PC mouse functions by using a webcam or a built-in camera. <br>
  **_Some applications_** **:** <br>
  - The COVID-19 situation, it is not safe to use the devices by touching them because it may result in a possible situation of spread of the virus by touching the devices, so it helps us to reduce the spread of the virus.
  - Smart homes, it controls in devices such as lights and thermostats through hand gestures for a seamless and convenient home automation experience.
  - Gaming and Entertainment, it enhances gaming experiences by allowing players to control characters, perform in-game actions and navigate virtual worlds using hand gestures.
- **Review on deep learning:** <br> Deep learning is a subfield of machine learning that involves training artificial neural networks to perform tasks without explicit programming. It relies on algorithms known as artificial neural networks, which are inspired by the structure and functioning of the human brain. These networks consist of interconnected layers of nodes (artificial neurons) that process and transform input data to produce an output. <br>
**Input layer:** Data enters through the input layer. <br>
**Hidden layers:** Hidden layers process and transport data to other layers. <br>
**Output layer:** The final result or prediction is made in the output layer. <br>
  
</font>

## Scope

<a id="scope"></a>
<font size="4">

Our goal is to control a laptop or desktop remotely using our hands – **_the left hand and the right hand_** – by connecting the **mouse** and the **keyboard** functions to an internal or external **camera**.

This kind of control is not very common in real life yet. It is still under development, and it is a research topic. That is why we chose it as our project. We want to make it possible and practical for real-life use. We also want to learn more about this technology and how to improve it and make it popular and helpful.

We are eager to learn and overcome the challenges that this technology may face because it is not well defined yet. But we are confident that we can contribute to this technology.

This technology can be useful for many purposes, such as **presentation** and **lecturing** and **personal use**. It can make controlling a laptop easier and more fun just by using our hands.

We will start by using two pretrained models that are built by Google developers.
- The first one is the [**Hand landmark detection**](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) model.
- The second one is the [**Gesture recognition**](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer) model.

*_We will respect the license agreement and use these models according to the terms and conditions_*.

The way that the hand control will work is that we will use one hand as a **mode selector** and the other hand as a **mode executor**. The modes that we will provide are:
- **Mouse pointer mode**
- ...

</font>

## Requirements

<a id="requirements"></a>
<font size="4">
 
- **Functional Requirements**:
    - **Hand Landmark Detection**:<br> The system must accurately detect and track the landmarks or key points on the user's hand, such as fingertips and palm.
    - **Tracking Consistency**:<br> The hand landmark detection should maintain consistent tracking, even during rapid hand movements or changes in hand orientation.
    - **Coordinate Mapping**:<br> The system must map the detected hand landmarks to screen coordinates for precise control of the mouse cursor.
    - **Mouse Movement**:<br> Translate the movements of detected hand landmarks into corresponding mouse movements on the screen.
    - **Click Detection**:<br> Identify gestures or hand configurations representing left-click, right-click, and other click actions.
    - **Drag and Drop**:<br> Implement the ability to perform drag-and-drop actions by recognizing specific hand movements.
    - **Real-time Responsiveness**:<br> Ensure real-time responsiveness in updating the mouse cursor based on changes in hand landmark positions.  
    - **Error Handling**:<br> Implement mechanisms to handle inaccuracies in hand landmark detection, providing feedback to the user when needed.
    - **User Interface Feedback**:<br> Provide visual feedback to indicate successful hand landmark detection and corresponding mouse actions.
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

<a id="timeline"></a>
![Timeline - Schedule](https://github.com/PeterNassrat/Graduation-Project/assets/93524169/e016356a-27cf-482b-bdd7-eb80ebdae0e3)
![Timeline - Diagram](https://github.com/PeterNassrat/Graduation-Project/assets/93524169/6581427c-38f4-40b6-b09d-3fa913fccb38)

<font size="4">

**_Phases_** **:**
1.	**Research:** <br>
Explore the project idea and its potential
2.	**Scope:** <br>
Outline the project goals, deliverables, and constraints
3.	**Plan:** <br>
Design a project schedule and budget
4.	**Prototype:** <br>
Build a mock-up of the project functionality
5.	**Presentation:** <br>
prepare a detailed demonstration of the project’s objectives, strategies, and outcomes, aimed at conveying its overall narrative and progress.
6.	**Environment:** <br>
Configure the development tools and platforms
7.	**Verification:** <br>
Check the development environment for errors or issues
8.	**Implementation:** <br>
Code each feature of the project as per the requirements
9.	**Testing:** <br>
Debug each feature and ensure its quality and performance
10.	**Evaluation:** <br>
Assess the whole project against the success criteria
11.	**Terms:** <br>
Define the legal and ethical aspects of the application
12.	**Deployment:** <br>
Launch the application to the intended users or customers
13.	**Guide:** <br>
Create a tutorial that teaches how to use the application

</font>

## Stakeholders

<a id="stakeholders"></a>
<font size="4">

- **Doctors:** <br>
It helps doctors in surgeries and examinations that require using a computer and makes it faster, as it helps them control their devices remotely.
- **Professors and Teaching Assistants:** <br>
It helps them control their devices remotely, making it easier to use them in lectures.
- **The Public:** <br>
People in daily use to control their laptops in an easier and more enjoyable way

</font>

## Team

<a id="team"></a>
<font size="4">

|Name|Role|Email|Phone Number|
|----|----|-----|------------|
|Kirolos Ayman|Project Manager|[kerls.ayman713@compit.aun.edu.eg](mailto:kerls.ayman713@compit.aun.edu.eg)|+201279583355|
|Marcos Shehata|Business Analyst|[morqos.shehata331@compit.aun.edu.eg](mailto:morqos.shehata331@compit.aun.edu.eg)|+201208017374|
|Marina Alashkar|Resource Manager|[marina.alashkar506@compit.aun.edu.eg](mailto:marina.alashkar506@compit.aun.edu.eg)|+201283906008|
|Marly Monsef|Quality Assurance (QA)|[Marly.monsef326@compit.aun.edu.eg](mailto:Marly.monsef326@compit.aun.edu.eg)|+201271453290|
|Mina Samir|Software Developer|[mina.20375830@compit.aun.edu.eg](mailto:mina.20375830@compit.aun.edu.eg)|+201225868088|
|Peter Nasrat|Software Architect|[Peter.20377281@compit.aun.edu.eg](mailto:Peter.20377281@compit.aun.edu.eg)|+201273770052|

</font>

## Risk Management

<a id="risk-management"></a>
<font size="4">

- **Errors in detection**:

  **_Solutions_**:
  - **Machine learning training**:<br> continuously train the gesture recognition model with diverse datasets to improve its ability to recognize different scenarios and reduce false positives or negatives.
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

## Resources

<a id="resources"></a>
<font size="4">
    
 - **Human Resources:**
 
   **_Software Developer_** **:**
   - **Role:** Develop software for hand landmark detection and mouse control.
   - **Responsibilities:** Code implementation, testing, and debugging.
            
 - **Skills and Expertise:**
   
   **_Software Development_** **:**
   - Proficiency in Python
   - Experience in computer vision and image processing. 

 - **Development Tools:**
   
   **_Computer Vision Libraries_** **:**
   - [**OpenCV (cv2):**](https://opencv.org/) <br>
   It provides tools for image and video processing, including functions for image manipulation, feature detection, and object tracking.

   - [**MediaPipe (mediapipe):**](https://developers.google.com/mediapipe) <br>
   MediaPipe is a library developed by Google that offers solutions for various perception tasks, including hand tracking.

   - [**Autopy (autopy):**](https://pypi.org/project/autopy/) <br>
   Autopy is a library for automating mouse and keyboard actions. It can be used to simulate mouse clicks, movements, and keyboard input.

 - **Equipment:**
   
   **_Sensors_** **:** <br>
   Laptop camera or External cameras for computers
     
</font>

## Communication Plan

<a id="communication-plan"></a>
<font size="4">

1. **Communication Group on WhatsApp:**
   - We created a group on the WhatsApp application as a quick means of communication.
   - Use the group to send any new amendments to the project, updates to our work plan, or changes in the date of the weekly meeting on the Google Meeting platform.
2. **Weekly Project Meeting:**
   - We hold a weekly meeting every Friday at 11 am.
   - The purpose of the meeting is to discuss what has been accomplished in the project and plan for additions in the upcoming week.

3. **GitHub Repository Updates:**
   - We upload all the additions and modifications we have made to GitHub.

</font>

## Monitoring and Evaluation

<a id="monitoring-and-evaluation"></a>
<font size="4">

1. **Project Milestones:**
   - We have defined clear project milestones and timeline.
   - We monitor progress toward these milestones regularly at our weekly meeting to ensure the project is on track.

2. **Track the Progress of Tasks:**
   - We track the progress of individual and group tasks through a task board on the Google Spreadsheet application.
   - Completed tasks are marked with a check mark in the sheet.
   - We update our task boards regularly and review completed, ongoing, and upcoming tasks.

3. **Key Performance Indicators (KPIs):**
   - We have identified key performance indicators aligning with project objectives, such as recognizing and identifying hand joints and responding to commands on their movements.
   - Regular evaluations of these KPIs are conducted to measure the overall success of the hand gesture mouse control project.

4. **Usage Tests:**
   - We conducted several hands-on code testing sessions to collect feedback on the hand gesture control system.
   - Use this feedback to make necessary adjustments and improvements.

5. **Document Review:**
   - We periodically update the project documentation, ensuring it is easily accessible and useful for all team members.

6. **Budget and Resource Management:**
   - We utilized our study laptops to work on the project, eliminating the need for additional budget spending.

7. **Training and Skills Development:**
   - We assessed the team's skill levels and identified areas that require training and development.
   - Team members are enhancing their skills related to the project, such as developing proficiency in writing code in Python and using GitHub.

</font>

## Lessons Learned

<a id="lessons-learned"></a>
<font size="4">

1. **User Feedback Importance:** <br> Understand the value of continuous user feedback throughout the development process. Users can provide insights into usability, identify potential issues, and suggest improvements.

2. **Iterative Development:** <br> Recognize the iterative nature of development for novel projects. Regularly test and refine the system based on user experiences and emerging challenges.

3. **Adaptability:** <br> Be prepared to adapt the hand control system to different user preferences and requirements. Flexibility in the design allows for a more inclusive and widely applicable product.

4. **Technical Challenges:** <br> Acknowledge and address technical challenges associated with computer vision, gesture recognition, and maintaining a stable connection between the hand control system and the target device.

5. **Security Measures:** <br> Emphasize the importance of robust security measures to prevent unauthorized access.

6. **Clear Documentation:** <br> Understand the significance of clear and comprehensive documentation for users, support teams, and potential future developers. Well-documented systems are easier to troubleshoot and maintain.

7. **Testing in Diverse Environments:** <br> Recognize the importance of testing the hand control system in diverse environments and conditions to ensure its reliability and performance under various scenarios.

8. **Scalability Considerations:** <br> Anticipate potential scalability issues and design the system with scalability in mind to accommodate future updates, improvements, or increased user demand.

9. **Ethical Considerations:** <br> Address ethical considerations related to privacy and data security, especially when dealing with camera-based systems that capture user gestures. Prioritize user consent and data protection in the development process.

</font>

## Closure Criteria

<a id="closure-criteria"></a>
<font size="4">

1. **Functionality:** <br> Ensure that the hand remote control system is capable of effectively controlling mouse functions on a laptop. Verify that the mode selector and mode executor hands work seamlessly together.

2. **Accuracy:** <br> The system should accurately interpret hand gestures and translate them into corresponding mouse actions without significant delays or errors.

3. **Compatibility:** <br> Confirm compatibility with common operating system Windows and various applications to ensure broad usability.

4. **Range:** <br> Determine the effective range of the hand control system to ensure it provides practical remote control capabilities.

5. **Reliability:** <br> Ensure the system is reliable and stable over extended usage periods, without frequent disconnections or malfunctions.

6. **Security:** <br> Implement security measures to prevent unauthorized access or control, ensuring the hand control system is secure against potential vulnerabilities.

7. **User Interface:** <br> Develop a user-friendly interface for configuring and customizing hand gestures, modes, and other settings.

8. **User Feedback:** <br> Gather user feedback to assess user satisfaction, identify potential improvements, and address any usability concerns.

9. **Documentation:** <br> Prepare comprehensive documentation, including user manuals and troubleshooting guides, to facilitate user understanding and support.

</font>

## Appendices

<a id="appendices"></a>
