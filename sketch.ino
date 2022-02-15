// ---------------------------------------------------------------- //
// Arduino Ultrasoninc Sensor HC-SR04
// Re-writed by Arbi Abdul Jabbaar
// Using Arduino IDE 1.8.7
// Using HC-SR04 Module
// Modified for CS50 Final Project by Navjot Saroa
// Tested on 15/02/2021
// ---------------------------------------------------------------- //


// Changes made to original code:
// 1. Added an inPin variable to use potentiometer (required for another part of the project).
// 2. Contents of void loop() are not in an if conditional, only need to collect data when inPin reads HIGH.

#define echoPin 2
#define trigPin 3
#define inPin 4

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement


void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
}
void loop() {
  // Clears the trigPin condition
  if (digitalRead(inPin) == HIGH) {
    digitalWrite(trigPin, HIGH);
    digitalWrite(trigPin, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    // Calculating the distance
    distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
    // Displays the distance on the Serial Monitor
    Serial.print(distance);
  };
}




