#include "wiring_constants.h"
   #pragma once

/*  
    Date:     7/15/2024
    Author:   Will Duncan


    This sccript should hopefully set up all the limit switches and buttons for the crane. Each pin on the arduino 
    is defined first. The limit switches should be connected driectly to ground and are an open circuit until pressed. 
    (Note it is standard to make it an open circuit so that when the button fails, the system wont be in danger).
    Because of this, we need to make sure the pullup resistor on the pin is enabled to protect the arduino from short circuiting 
    Then we are going to attach interupts to all the pins to make them flip their flags when pressed on depressed 


    //TODO make the Estop button instantly stop the motors from moving instead of waiting for the velocity of the motor to update
*/

const int t1Pin = 48; // Trolley pin 1
const int t2Pin = 52; // Trolley limit switch 2 
const int EstopPin = 53; //Pin for the estop

const int s1Pin = 47; 
const int s2Pin = 46; 

//Need to make flags for when the buttons are pressed
volatile bool trolleyLimit1 = false;
volatile bool trolleyLimit2 = false;
volatile bool slewLimit1 = false;
volatile bool slewLimit2 = false;
volatile bool Estop = false;



void t1ISR() {
  // This function will be called when the interrupt occurs
  if (digitalRead(t1Pin) == HIGH) {
    // Serial.println("Limit switch pressed!");
    // delay(100);
    trolleyLimit1 = true;
    // Add your code here to handle the limit switch being pressed
  } else if (digitalRead(t1Pin) == LOW){
    trolleyLimit1 = false;
  }
}


void t2ISR() {
  // This function will be called when the interrupt occurs
  if (digitalRead(t2Pin) == HIGH) {
    // Serial.println("Limit switch pressed!");
    // delay(100);
    trolleyLimit2 = true;
    // Add your code here to handle the limit switch being pressed
  } else if (digitalRead(t2Pin) == LOW) {
    trolleyLimit2 = false;
  }
}

void s1ISR() {
  // This function will be called when the interrupt occurs
  if (digitalRead(s1Pin) == HIGH) {
    // Serial.println("Limit switch pressed!");
    // delay(100);
    slewLimit1 = true;
    // Add your code here to handle the limit switch being pressed
  } else if (digitalRead(s1Pin) == LOW) {
    slewLimit1 = false;
  }
}

void s2ISR() {
  // This function will be called when the interrupt occurs
  if (digitalRead(s2Pin) == HIGH) {
    // Serial.println("Limit switch pressed!");
    // delay(100);
    slewLimit2 = true;
    // Add your code here to handle the limit switch being pressed
  } else if (digitalRead(s2Pin) == LOW) {
    slewLimit2 = false;
  }
}
void eStopISR(){
    if (digitalRead(EstopPin) == HIGH) {
    // Serial.println("Limit switch pressed!");
    // delay(100);
    Estop = true;
    // Add your code here to handle the limit switch being pressed
  } else {
    Estop = false;
  }
}


void setupSwitches() {  
  pinMode(t1Pin, INPUT_PULLUP); // Enable internal pull-up resistor
  pinMode(t2Pin, INPUT_PULLUP); // Enable internal pull-up resistor
  pinMode(s1Pin, INPUT_PULLUP); // Enable internal pull-up resistor
  pinMode(s2Pin, INPUT_PULLUP); // Enable internal pull-up resistor
  pinMode(EstopPin, INPUT_PULLUP); // Enable internal pull-up resistor

  //Interupt will change the flag in the code 
  attachInterrupt(digitalPinToInterrupt(t1Pin), t1ISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(t2Pin), t2ISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(s1Pin), s1ISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(s2Pin), s2ISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(EstopPin), eStopISR, CHANGE);

  NVIC_SetPriority(PIOA_IRQn, 3);
  // Attach the interrupt handler function to the pin

}
