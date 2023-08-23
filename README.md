# Gun-Detection-OpenCVArdunio-Project

Real-time Gun Detection and Localization System using Computer Vision and Arduino

Objective:

The project aims to develop an intelligent surveillance system that uses computer vision
for real-time detection of guns and facial recognition, complemented by a mechanical component
that physically points towards the detected threat.

Project Overview:

This innovative project integrates two major aspects - computer vision and mechanical manipulation
using an Arduino-controlled servo motor. The computer vision part involves detecting guns and faces
in each field of view. The servo motor integration offers a physical response to the detected threats,
making the system more interactive and responsive.
The display screen is divided into 9 parts, each corresponding to a different servo motor angle. Thus,
when a gun is detected in a specific part, the servo motor adjusts its angle to point towards that
region.
System had to design to divide the camera angle to the 9 parts because we had to gain from fps value
of live camera. When I increase the angle parts(for example with for loop to detect all angles) system
starts to be lagging so I decide to divide it.

Technical Details:

Face and Gun Detection: The system employs a color-coded scheme to represent the detection
status. The rectangles drawn around detected faces remain green under normal circumstances.
However, the detection of a gun changes the rectangle color to red, indicating a potential threat. This
allows users to easily identify when a firearm is present in the field of view.
For gun and face detection part haar-cascade classifiers were used to training part.
Servo Motor Control: Upon detecting a gun, the system triggers the Arduino-controlled servo motor.
The screen is segmented into nine parts, each associated with a specific angle of the servo motor.
Depending on which segment the firearm is detected, the servo motor adjusts its direction to point
towards the threat.

Applications:

The system can be used in various surveillance and security applications, including public spaces like
shopping malls, transportation hubs, schools, and more. The servo motor's physical response could
also be utilized to control other security measures, such as alarms, automatic door locks, or
emergency call systems, to further enhance the system's practicality.

Conclusion:

The project demonstrates an effective combination of computer vision and Arduino programming.
Despite its simplicity, it provides a proof of concept for a more advanced system capable of real-time
threat detection and localization. The practical implications for such a system are vast and, with
future enhancements, it can become a staple in safety and security systems.
