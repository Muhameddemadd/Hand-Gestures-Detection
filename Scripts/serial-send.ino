#include <AccelStepper.h>
#include <Servo.h>

Servo myservo;

// Define two steppers and the pins they will use
AccelStepper stepper1(AccelStepper::DRIVER, 2, 3);
AccelStepper stepper2(AccelStepper::DRIVER, 4, 5);


int pos1 = 0;
int incomingByte; 


void setup()
{ 
  Serial.begin(115200);
  stepper1.setMaxSpeed(4000);
  stepper1.setAcceleration(3000);
  stepper2.setMaxSpeed(4000);
  stepper2.setAcceleration(3000);
  myservo.attach(9);
  myservo.write(0);

 
}

void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
      if (incomingByte == 'L') {
         for (int i = 0; i <= 100; i++) {
          stepper1.setSpeed(-2500);
          stepper1.run();
          delay(0.1);
         }
      }
    
      if (incomingByte == 'H') {
         for (int i = 0; i <= 100; i++) {
          stepper1.setSpeed(2500);
          stepper1.run();
          delay(0.1);
         }}

      if (incomingByte == 'R') {
         for (int i = 0; i <= 100; i++) {
          stepper2.setSpeed(-700);
          stepper2.run();
          delay(0.1);
         }}

      if (incomingByte == 'T') {
         for (int i = 0; i <= 100; i++) {
          stepper2.setSpeed(700);
          stepper2.run();
          delay(0.1);
         }}

      if (incomingByte == 'O') {
        myservo.write(180);
         }

      if (incomingByte == 'C') {
        myservo.write(0);
         }

  
      }
   }













