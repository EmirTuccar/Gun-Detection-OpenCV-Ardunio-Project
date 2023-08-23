#include <Servo.h>

Servo servoMotor;

int servoPin = 9; // Pin connected to the servo motor

void setup() {
  servoMotor.attach(servoPin); // Attaches the servo motor to the specified pin
  servoMotor.write(90); // Initial position of the servo (facing forward)
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available()) {
    char input = Serial.read();
    if (input == '1') {
      servoMotor.write(45); // Rotate the servo motor to the left
    } 
    else if (input == '2') {
      servoMotor.write(77); // Rotate the servo motor to the right
    } 
    else if (input == '3') {
      servoMotor.write(90); // Center the servo motor (facing forward)
    } 
    else if (input == '4') {
      servoMotor.write(112); // Rotate the servo motor to the right
    } 
    else if (input == '5') {
      servoMotor.write(135);
    }
}
}
