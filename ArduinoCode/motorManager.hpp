#include "variant.h"
#include "USB/USBAPI.h"
#include "sam3xa/include/sam3x8e.h"
#pragma once
#include <DueTimer.h>
#include "OdriveDueCAN.hpp"
#include "switchesAndButtons.h"
#include "shaperMaker.h"
/*
  Date:     8/5/2024
  Author:   Will Duncan
          This is a script that manages the velocity commands beign sent to the motor. Note that all the motors should be mad/ defined in the 
          OdriveDueCAN.hpp folder at once otherwise they wont get initialized properly. This script contains the motor command buffer which is read 
          every motorTimerPeriod and sends updated velocitied to the odrive motors. This script also includes information on the timer utilized when 
          setting up that update function as well as what the timer does every period.  

*/

#define motorTimerPeriod 5 //in ms bridge crane is roughly 49ms   
#define motorCommandLen 10*1000 //the length time in s     that stores the velocities of the motor
#define g 9.81

volatile int motor0V[motorCommandLen/ motorTimerPeriod]; //time we want it to last in ms * timer
volatile int motor1V[motorCommandLen/motorTimerPeriod]; //time we want it to last in ms * timer
volatile int motor2V[motorCommandLen/motorTimerPeriod]; //time we want it to last in ms * timer



volatile int curMotorVeloPos = 0;  

//The current Motor Velocity commanded Shaped
volatile int velo_motor_0 = 0;
volatile int velo_motor_1 = 0;
volatile int velo_motor_2 = 0;

int unshaped_command_motor_0 = 0;
int unshaped_command_motor_1 = 0;
int unshaped_command_motor_2 = 0;

///////////////////////////////////////////////
//Encoder Read data. 
volatile float slewAngle = 0.0;
volatile float hoistHeight = 0.0;
volatile float trolleyLen = 0.0;

volatile float slewVelo = 0.0;
volatile float hoistVelo = 0.0;
volatile float trolleyVelo = 0.0;
///////////////////////////////////////////////


//Software limits
int slewMin = 30;
int slewMax = 350;

int hoistMin = 100;
int hoistMax = 1400;

volatile bool isTraj = false;



float vMaxTrolley = 15.0;
float vMaxSlew = 9.0;
float vMaxHoist = 2.0;

float gearRatioSlew = 360.0 / 100.0;
float gearRatioHoist = 0.5*119.69;
float gearRatioTrolley = 1.0 * 25.4/7;




bool digitalEstop = false; // This bool represents the Estop stent by the Gui or the hand held controller 
volatile bool isCal = true; //Has the motor hit a limit switch since boot up/ cal. Note this is used in the auto calibration 
float slew_cal = 0;
float trolley_cal = 0;
float hoist_cal = 0;


float craneInnerRad = 250.0f;
// Timer ISR
//TODO make it send velo commands 
void timerISR() {
  /*
    This is the main timer interupt that handles taking in the values from the motor buffers and updating the motor velocity
  */

     //Check to see if we are bigger than the array 
    if (curMotorVeloPos >=(motorCommandLen/ motorTimerPeriod)){
      curMotorVeloPos = 0; //Reset it back to zero 
    }

  //Check is we are e stoppedv
  if(Estop || digitalEstop){
    isCal = true;
    //This means that the estop is pressed 
    if(velo_motor_0 != 0){
      velo_motor_0 = 0;
      odrv0.setVelocity(float(velo_motor_0));
    }
    if(velo_motor_1 != 0){
      velo_motor_1 = 0;
      odrv1.setVelocity(float(velo_motor_1));
    }
    if(velo_motor_2 != 0){
      velo_motor_2 = 0;
      odrv2.setVelocity(float(velo_motor_2));
    }
    // Serial.println("ESTOPED");
    if(!digitalEstop){
    Serial.println("f, 33554432,33554432, 33554432");
    digitalEstop = true;
    }
  } else{
    ////////////////////////////////////////////////////////////////////////////
    //If we are not estoped, we check to see if it has hit a certain limit switch and is still moving in that direction
    if(trolleyLimit1&(velo_motor_0<0)){
        odrv0.setVelocity(0);
        Serial.println("i, trolleyLimit 1");
        isCal = true;
    }else if(trolleyLimit2 &(velo_motor_0>0)){
        odrv0.setVelocity(0);
        Serial.println("i, trolleyLimit 2");
        // Serial.println(velo_motor_0);
        isCal = true;
    }


    if((motor0V[curMotorVeloPos] != 0) ){
      velo_motor_0 = velo_motor_0 + motor0V[curMotorVeloPos];
      
      if( (trolleyLimit1) & (velo_motor_0 < 0 ) ){
        // Serial.println("trolleyLimit1");
        odrv0.setVelocity(0);
      } else if(trolleyLimit2 & (velo_motor_0 > 0 )) {
        // Serial.println("trolleyLimit2");
        odrv0.setVelocity(0);
      } else {
        // Serial.println("i,Velo Sent");
        odrv0.setVelocity(float(velo_motor_0)*vMaxTrolley*0.001,0.78);
       
      }

     
    }

    // Note from the odrives reference from clockwise is positve on this axis but we need to reverse that
    if((slewLimit1||((slewAngle<slewMin)&isCal))&(velo_motor_1>0)){
      //If the slew limit switch or software limit when not calibrating is hit
      Serial.println("i,Slew Limit1");
      
      odrv1.setVelocity(0);
      isCal = true;

    } else if((slewLimit2 ||((slewAngle>slewMax)&isCal))&(velo_motor_1<0)){
        
        odrv1.setVelocity(0);
        Serial.println("i,Slew Limit2 ");
        // Serial.print(slewLimit2);
        // Serial.print(',');
        // Serial.print((slewAngle>slewMax)&isCal);
        // Serial.print(',');
        // Serial.print(slewAngle);
        // Serial.print(',');
        // Serial.println(slewMax);
        isCal = true;
    }

    if((motor1V[curMotorVeloPos] != 0) ){
      //Note it is -1 times the velocity to rotate the coordinate system to match expectations
      velo_motor_1 = velo_motor_1 + -1.0* motor1V[curMotorVeloPos];
      
      //Limit switch checks
      if( (((slewAngle<slewMin)& isCal )|| slewLimit1)& (velo_motor_1 > 0) ){

        Serial.println("i, Slew Soft min");
        
        odrv1.setVelocity(0);
        isCal = true;
      } else if((((slewAngle>slewMax)& isCal)||slewLimit2) & (velo_motor_1 < 0 )) {
      
        odrv1.setVelocity(0);
        Serial.println("i,Slew Soft max");
        isCal = true;
      } else {
        odrv1.setVelocity(float(velo_motor_1)*vMaxSlew*0.001);
       
      }
    }

    //& (hoistHeight >= hoistMin) & (hoistHeight <= hoistMax)
    if((hoistHeight <= hoistMin) & (velo_motor_2 <= 0)){
            odrv2.setVelocity(0.0f);
            Serial.println("i, Hoist Lim Min");

    }else if((hoistHeight >= hoistMax)&(velo_motor_2 >= 0)){
            odrv2.setVelocity(0.0f);
            Serial.println("i, Hoist Lim Max");
    }

    if((motor2V[curMotorVeloPos] != 0)  ){
          // Serial.println("Trying to move");
          velo_motor_2 = velo_motor_2 + motor2V[curMotorVeloPos];
          
          if((hoistHeight <= hoistMin) & (velo_motor_2 < 0)){
              odrv2.setVelocity(0.0f);
              // Serial.println("i, Hoist Lim Min");
              // Serial.println(velo_motor_2);
          }else if((hoistHeight >= hoistMax)&(velo_motor_2 > 0)){
              odrv2.setVelocity(0.0f);
              // Serial.println("i, Hoist Lim Max");
          } else{
            odrv2.setVelocity(float(velo_motor_2)*vMaxHoist*0.001);
          }
    }



     
    }
    
  motor0V[curMotorVeloPos] = 0;
  motor1V[curMotorVeloPos] = 0;
  motor2V[curMotorVeloPos] = 0;
  curMotorVeloPos = curMotorVeloPos + 1;
}

void trajISR(){
  //Needed because this directly sets speeds not impulses 
  
     //Check to see if we are bigger than the array 
    if (curMotorVeloPos >=(motorCommandLen/ motorTimerPeriod)){
      curMotorVeloPos = 0; //Reset it back to zero 
      Timer3.stop();
    }

  //Check is we are e stoppedv
  if(Estop){
    //This means that the estop is pressed 
    if(velo_motor_0 != 0){
      velo_motor_0 = 0;
      odrv0.setVelocity(float(velo_motor_0));
    }
    if(velo_motor_1 != 0){
      velo_motor_1 = 0;
      odrv1.setVelocity(float(velo_motor_1));
    }
    if(velo_motor_2 != 0){
      velo_motor_2 = 0;
      odrv2.setVelocity(float(velo_motor_2));
    }
    Serial.println("f, 33554432,33554432, 33554432");
    Timer3.stop();
    digitalEstop = true;

  } else{

    if(trolleyLimit1&(velo_motor_0<0)){
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);

        Timer3.stop();
        digitalEstop = true;

    } else if(trolleyLimit2 &(velo_motor_0>0)){
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);
        Timer3.stop();
        digitalEstop = true;
    }
      velo_motor_0 = motor0V[curMotorVeloPos];
      
      if( trolleyLimit1 & (velo_motor_0 < 0 ) ){
        Serial.println("Limit Switch");
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);
        Timer3.stop();
      } else if(trolleyLimit2 & (velo_motor_0 > 0 )) {
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);
        Timer3.stop();
      } else {
        odrv0.setVelocity(float(velo_motor_0)*vMaxTrolley*0.001);
        // Serial.println(float(velo_motor_0)*vMax*0.001);
      }

     

      velo_motor_1 = motor1V[curMotorVeloPos];
      
      if( slewLimit1 & (velo_motor_1 < 0 ) ){
        Serial.println("Limit Switch");
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);
        Timer3.stop();
      } else if(slewLimit2 & (velo_motor_1 > 0 )) {
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);
        Timer3.stop();
      } else {
        //Need to flip the coordinate system 
        odrv1.setVelocity(-1*float(velo_motor_1)*vMaxSlew*0.001);
       
      }
          
      velo_motor_2 = motor2V[curMotorVeloPos];
      
      if( (velo_motor_2 < 0 ) &(hoistHeight < hoistMin)){
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);
        Timer3.stop();
      } else if((velo_motor_2 > 0 )&(hoistHeight > hoistMax)) {
        odrv0.setVelocity(0);
        odrv1.setVelocity(0);
        odrv2.setVelocity(0);
        Timer3.stop();
      } else {
        // Serial.println("Velo Sent");
        // odrv1.setVelocity(3.0*float(velo_motor_0)*vMax*0.001);
        odrv2.setVelocity(float(velo_motor_2)*vMaxHoist*0.001);
      
      }




     
    }
    
  // motor0V[curMotorVeloPos] = 0;
  // motor1V[curMotorVeloPos] = 0;
  // motor2V[curMotorVeloPos] = 0;
  curMotorVeloPos = curMotorVeloPos + 1;

}

void gatherDataISR(){
  //Timer Interupt Service Routine to send data to the gui laptop

  if (odrv0_user_data.received_feedback & odrv1_user_data.received_feedback & odrv2_user_data.received_feedback) {
      Get_Encoder_Estimates_msg_t feedback0 = odrv0_user_data.last_feedback;
      Get_Encoder_Estimates_msg_t feedback1 = odrv1_user_data.last_feedback;
      Get_Encoder_Estimates_msg_t feedback2 = odrv2_user_data.last_feedback;
      

      odrv0_user_data.received_feedback = false;
      odrv1_user_data.received_feedback = false;
      odrv2_user_data.received_feedback = false;

        // String myMsg = String(millis()) + "," + String(feedback0.Vel_Estimate) + "," + String(vMax*velo_motor_0);
        slewAngle = (-1*feedback1.Pos_Estimate*gearRatioSlew) - slew_cal;
        trolleyLen = ((feedback0.Pos_Estimate*gearRatioTrolley) - trolley_cal) + craneInnerRad;
        hoistHeight = (feedback2.Pos_Estimate*gearRatioHoist) - hoist_cal;

        slewVelo = feedback1.Vel_Estimate*gearRatioSlew;
        hoistVelo = feedback2.Vel_Estimate*gearRatioHoist;
        trolleyVelo = feedback0.Vel_Estimate*gearRatioTrolley;

        String myMsg = "d," + String(millis()) + "," + String(trolleyVelo)+ "," + (float(velo_motor_0)*vMaxTrolley*0.001*gearRatioTrolley);
        myMsg = myMsg  + "," + String(trolleyLen) + "," + String(slewVelo)+ "," + (float(velo_motor_1)*vMaxSlew*0.001*gearRatioSlew) + "," + String(slewAngle);
        myMsg = myMsg  + "," + String(hoistVelo) + "," + (float(velo_motor_2)*vMaxHoist*0.001*gearRatioHoist) + "," + String(hoistHeight) + "," + String(unshaped_command_motor_0) + "," + String(unshaped_command_motor_1) + "," + String(unshaped_command_motor_2);
        Serial.println(myMsg);
        // Serial.println("Data Sent");
    
  } else {
      //If the motors havent fully sent the next update yet or is not moving
        String myMsg = "d," + String(millis()) + "," + String(trolleyVelo)+ "," + (float(velo_motor_0)*vMaxTrolley*0.001*gearRatioTrolley);
        myMsg = myMsg  + "," + String(trolleyLen) + "," + String(slewVelo)+ "," + (float(velo_motor_1)*vMaxSlew*0.001*gearRatioSlew) + "," + String(slewAngle);
        myMsg = myMsg  + "," + String(hoistVelo) + "," + (float(velo_motor_2)*vMaxHoist*0.001*gearRatioHoist) + "," + String(hoistHeight) + "," + String(unshaped_command_motor_0) + "," + String(unshaped_command_motor_1) + "," + String(unshaped_command_motor_2);
        Serial.println(myMsg);
        // Serial.println("Data Sent");
  }
  
  //Maybe make it check every few cycles 
  Get_Error_msg_t myError0;
  Get_Error_msg_t myError1;
  Get_Error_msg_t myError2;
  odrv0.request(myError0,2);
  odrv1.request(myError1,2);
  odrv2.request(myError2,2);
  

  if((myError0.Active_Errors!= 0)||(myError1.Active_Errors!= 0)||(myError2.Active_Errors!= 0)){
    //If a fault has occured, tell the laptop
    Serial.print("f, "); //Fault flag
    Serial.print(myError0.Disarm_Reason);//Error code
    Serial.print(",");
    Serial.print(myError1.Disarm_Reason);
    Serial.print(",");
    Serial.println(myError2.Disarm_Reason);
  }
  

}

void startTimer(){
  // Set up Timer interupt. Note this is a seperate script so in some debugging cases, we dont have to be connected to the odrive for it to work 
  Timer3.attachInterrupt(timerISR); // Attach ISR to Timer 3
  Timer4.attachInterrupt(gatherDataISR);
  
  Timer3.setPeriod(motorTimerPeriod*1000); // Start Timer 3 with motorTimerPeriod. Note the input to this function is in micro seconds
  Timer4.setPeriod(10*1000); // Start Timer 4. Note the input to this function is in micro seconds

  Timer3.start();
  Timer4.start();
  //Setting the timer interupt priority to 3 
  NVIC_SetPriority(TC3_IRQn,3);
  NVIC_SetPriority(TC4_IRQn,3);
  //CAN messages need to be a higher priority than the timer because CAN is needed in the timer interupts 
  NVIC_SetPriority(CAN0_IRQn,0);
}

int wrapMotorIDX(int idx){
  /*Takes in a motor index is makes sure it is within the array bounds. If not, it wraps it back around 
    to the begining of the array */
    while(idx>=(motorCommandLen/ motorTimerPeriod)){
      idx = idx-(motorCommandLen/ motorTimerPeriod);
    }
    return idx;
}

void clearVeloBuffer(){
  //clears the motor velocity buffers. Needed when the user enters trajectory mode
  for(int i = 0; i <(motorCommandLen/ motorTimerPeriod); i++ ){
    motor0V[i] = 0;
    motor1V[i] = 0;
    motor2V[i] = 0;
  }
    curMotorVeloPos = 0;
}

void toggleTraj(){
  //Toggles on or off the trajectory mode. It handles changing the motor interupts and clearing the motor buffers as needed 


  //Need to check if we are in trajectory mode 

    if(isTraj){
      //Exiting out of trajectory mode 
      Serial.println("Exiting Trajecotry");
      Serial.println(curMotorVeloPos);
      clearVeloBuffer();
      // Serial.print("Traj pos recieved: ");
      // Serial.print(curMotorVeloPos);
      startTimer();
      isTraj = false;
      

    } else {
      isTraj = true;
      Serial.println("Entering Trajecotry");
      Timer3.stop();
      Timer3.setPeriod(50*1000);
      Timer3.attachInterrupt(trajISR);
      curMotorVeloPos = 0;
      // Timer3.start();
      // 
    }
}

void addTraj(float v0, float v1, float v2){
  /*
    THis function adds the input trajectory into the motor buffer. It is run for every line in the excel sheet 
    If the excel sheet is longer than the buffer, it will start to overwrite the begining and will warn user 
  */


  //Notes that the trajectory sheet is in percents but we need it to be 10^3
  motor0V[curMotorVeloPos] = (int) (v0 * 10);
  motor1V[curMotorVeloPos] = (int) (v1 * 10);
  motor2V[curMotorVeloPos] = (int) (v2 * 10);
  curMotorVeloPos = curMotorVeloPos + 1;
  
  if(curMotorVeloPos >=motorCommandLen/ motorTimerPeriod){
    curMotorVeloPos = 0;
    Serial.println("Maxed Out Buffer");
  }

}

void startTraj(){
  /*
    Starts the trajecctory timer 
  */
  Serial.println("Trajectory Starting");
  curMotorVeloPos = 0;
  Timer3.start();
}

void stopTraj(){
  /*
    Stops the trajectory timer and stops all motors 
  */
  // Serial.println("Trajectory Stopped");
  Timer3.stop();
  odrv0.setVelocity(0.0);
  odrv1.setVelocity(0.0);
  odrv2.setVelocity(0.0);
  Serial.println("Trajectory Stopped");

}

void calbrateMotorOffsets(float c1, float c2, float c3){
  //Changes the motor offsets so that the measurements match what is expected. If 
  // the input value is less than zero, then we ignore the entry, but the calibration 
  //values can be negative 

  if(c1 >= 0 ){
    slew_cal = (slew_cal+ slewAngle) - c1;
  }

  if(c2 >= 0 ){
    trolley_cal = (trolley_cal+ trolleyLen)-c2;
  }

  if(c3 >= 0 ){
    hoist_cal = (hoist_cal+ hoistHeight)-c3;
  }

  Serial.print("Calibrating ");
    Serial.print(slewAngle-slew_cal);
    Serial.print("  ,");
    Serial.print(trolleyLen - trolley_cal);
    Serial.print("  ,");
    Serial.println(hoistHeight - hoist_cal);
}

void clearFaults(){
  //Sends the message to the odrive to clear current faults
  odrv0.clearErrors();
  delay(10);
  odrv1.clearErrors();
  delay(10);
  odrv2.clearErrors();
  delay(10);
  digitalEstop = false;
}

void set_motorVelocity(float v0,float v1,float v2){
/*
  Hard sets the motor velocities. Note this is not reccomended as it can throw off
  shaping and the timer isrs
    v0: Trolley velocity 
    v1: slewing 
    v2: hoisting 
*/
  velo_motor_0 = int(v0*1000);
  velo_motor_1 = int(v1*1000);
  velo_motor_2 = int(v2*1000);
  odrv0.setVelocity(float(velo_motor_0)*vMaxTrolley*0.001,0.78);
  odrv1.setVelocity(float(velo_motor_1)*vMaxSlew*0.001);
  odrv2.setVelocity(float(velo_motor_2)*vMaxHoist*0.001);


}