#include "ODriveCAN.h"
#include <due_can.h>
#include "OdriveDueCAN.hpp"
#include "shaperMaker.h"
#include "motorManager.hpp"
#include "switchesAndButtons.h"

/*
  This is the main script that calls the other scripts and starts the entire program 
  It begins by setting up the serial comunication and setting up the interupts for the limit switches
  It then initializes the ODrive objects and starts CAN communication 
  It will connect to each motor individually and will stop the program if it doesnt find one of the three motors through the heartbeats 
  Afterwards, it recieves messages from the GUi and acts 

  This script also starts the autocalibration procedure as some of the objects need to be defined before the crane could be calibrated


*/


bool isTrolley = true;
bool isSlew = true;
bool isHoist = true;


void setup() {
  Serial.begin(115200);
  
  // Wait for up to 3 seconds for the serial port to be opened on the PC side.
  // If no PC connects, continue anyway.
  for (int i = 0; i < 30 && !Serial; ++i) {
    delay(100);
  }
  delay(200);


  Serial.println("i,Starting ODriveCAN");

  // Register callbacks for the heartbeat and encoder feedback messages
  setupSwitches();
  odrv0.onFeedback(onFeedback, &odrv0_user_data);
  odrv0.onStatus(onHeartbeat, &odrv0_user_data);

  odrv1.onFeedback(onFeedback, &odrv1_user_data);
  odrv1.onStatus(onHeartbeat, &odrv1_user_data);

  odrv2.onFeedback(onFeedback, &odrv2_user_data);
  odrv2.onStatus(onHeartbeat, &odrv2_user_data);

  // Configure and initialize the CAN bus interface. This function depends on
  // your hardware and the CAN stack that you're using.

  if (!setupCan()) {
    Serial.println("i,CAN failed to initialize: reset required");
    while (true); // spin indefinitely
  }
  // moveFandB();
  Serial.println("i, Waiting for ODrive...");

  while ((!odrv0_user_data.received_heartbeat) & (isTrolley) ) {
    pumpEvents(can_intf);
    delay(100);
  }
  Serial.println("i, Found Slewing");

  while ((!odrv1_user_data.received_heartbeat) & (isSlew)){
    pumpEvents(can_intf);
    delay(100);
  }
  Serial.println("i, Found Trolley");

  while ((!odrv2_user_data.received_heartbeat) & isHoist) {
    pumpEvents(can_intf);
    delay(100);
  }
  Serial.println("i, found Hoisting");

  // request bus voltage and current (1sec timeout)
  Serial.println("i, attempting to read bus voltage and current");
  Get_Bus_Voltage_Current_msg_t vbus;
  Get_Error_msg_t myError;
  
  if (!odrv0.request(vbus, 1)) {
    Serial.println("i, vbus request failed! Please Reset");
    while (true); // spin indefinitely
  }

  // Serial.print("i, DC voltage [V]: ");
  // Serial.println(vbus.Bus_Voltage);
  // Serial.print("i, DC current [A]: ");
  // Serial.println(vbus.Bus_Current);

  Serial.println("i, Enabling closed loop control...");
  while ((odrv0_user_data.last_heartbeat.Axis_State != ODriveAxisState::AXIS_STATE_CLOSED_LOOP_CONTROL) & isTrolley){
    odrv0.clearErrors();
    delay(1);
    // odrv0.setControllerMode(0x2, 0x2);
    odrv0.setState(ODriveAxisState::AXIS_STATE_CLOSED_LOOP_CONTROL);

    // Pump events for 150ms. This delay is needed for two reasons;
    // 1. If there is an error condition, such as missing DC power, the ODrive might
    //    briefly attempt to enter CLOSED_LOOP_CONTROL state, so we can't rely
    //    on the first heartbeat response, so we want to receive at least two
    //    heartbeats (100ms default interval).
    // 2. If the bus is congested, the setState command won't get through
    //    immediately but can be delayed.
    for (int i = 0; i < 15; ++i) {
      delay(10);
      pumpEvents(can_intf);
    }

    // setPID();
    
  }


  Serial.println("i, Looking for slew heartbeat");
  while ((odrv1_user_data.last_heartbeat.Axis_State != ODriveAxisState::AXIS_STATE_CLOSED_LOOP_CONTROL) & isSlew){
    odrv1.clearErrors();
    delay(1);
    // odrv0.setControllerMode(0x2, 0x2);
    odrv1.setState(ODriveAxisState::AXIS_STATE_CLOSED_LOOP_CONTROL);
    for (int i = 0; i < 15; ++i) {
      delay(10);
      pumpEvents(can_intf);
    }
  }


  Serial.println("i, Looking for hoist heartbeat");
  while ((odrv2_user_data.last_heartbeat.Axis_State != ODriveAxisState::AXIS_STATE_CLOSED_LOOP_CONTROL) & isHoist){
    odrv2.clearErrors();
    delay(1);
    // odrv0.setControllerMode(0x2, 0x2);
    odrv2.setState(ODriveAxisState::AXIS_STATE_CLOSED_LOOP_CONTROL);
    for (int i = 0; i < 15; ++i) {
      delay(10);
      pumpEvents(can_intf);
    }
  }


  makeIden();
  Serial.println("i, ODrive running!");
  startTimer();
    
}


bool hasSent = false;
bool hasEnded = false;

int t0=0;
String myMsg = "";


const char TERMINATION_CHAR = '\n'; //This is how we know the message is finished being sent 
char rec_msg[175];
char* processed_msg[80];  // the max number of values we can have in the message 
int curMsgPos = 0;

int nummy = 0;
void loop() {
   pumpEvents(can_intf);
      // This is required on some platforms to handle incoming feedback CAN messages
  // put your main code here, to run repeatedly:
    while (Serial.available() > 0) {
      char receivedChar = Serial.read();
      if (receivedChar == TERMINATION_CHAR) {
 
        // Serial.println("DONE WOOO");
        processMessage();
        curMsgPos = 0;
        
      } else {
        // Append character to the message buffer
        rec_msg[curMsgPos] = receivedChar;
        curMsgPos += 1;
      }
    }
/*
    if (odrv0_user_data.received_feedback & odrv1_user_data.received_feedback & odrv2_user_data.received_feedback) {
      Get_Encoder_Estimates_msg_t feedback0 = odrv0_user_data.last_feedback;
      Get_Encoder_Estimates_msg_t feedback1 = odrv1_user_data.last_feedback;
      Get_Encoder_Estimates_msg_t feedback2 = odrv2_user_data.last_feedback;
      

      odrv0_user_data.received_feedback = false;
      odrv1_user_data.received_feedback = false;
      odrv2_user_data.received_feedback = false;

        // String myMsg = String(millis()) + "," + String(feedback0.Vel_Estimate) + "," + String(vMax*velo_motor_0);
        slewAngle = (-1*feedback1.Pos_Estimate*gearRatioSlew) - slew_cal;
        trolleyLen = (feedback0.Pos_Estimate*gearRatioTrolley) - trolley_cal;
        hoistHeight = (feedback2.Pos_Estimate*gearRatioHoist) - hoist_cal;

        String myMsg = "d," + String(millis()) + "," + String(feedback0.Vel_Estimate*gearRatioTrolley)+ "," + (float(velo_motor_0)*vMaxTrolley*0.001*gearRatioTrolley) + "," + String(trolleyLen) + "," + String(feedback1.Vel_Estimate*gearRatioSlew)+ "," + (float(velo_motor_1)*vMaxSlew*0.001*gearRatioSlew) + "," + String(slewAngle)+ "," + String(feedback2.Vel_Estimate*gearRatioHoist) + "," + (float(velo_motor_2)*vMaxHoist*0.001*gearRatioHoist) + "," + String(hoistHeight);
        Serial.println(myMsg);
    
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
  

  */
  // odrv0.clearErrors();


}

void splitString(char* data, char delimiter, char* outputArray[], int size) {
  // This function separates out the data inside the char array by commas into separate char arrays for each found comma
  int index = 0;
  // char* token = strtok(data, &delimiter);  // Get the first token
  char* token = strtok(data, ",");  // Get the first token
  while (token != NULL && index < size) {
    outputArray[index++] = token;  // Store the token in the output array
    // token = strtok(NULL, &delimiter);  // Get the next token
    token = strtok(NULL, ",");  // Get the next token
  }
}

void processMessage() {
  // This function interprets the received message from either the GUI or the handheld controller and does things based on the input

  // First to separate out the string
  // Serial.println("Received Message: ");
  // Serial.println(rec_msg);

  splitString(rec_msg, ',', processed_msg, curMsgPos);
  // Serial.println(processed_msg[1]);

  // Now to figure out what kind of message we have
  if (strcmp(processed_msg[0], "v") == 0) {
    Serial.print("Motor Trajectory Received: ");
    float v0 = atof(processed_msg[1]);
    float v1 = atof(processed_msg[2]);
    float v2 = atof(processed_msg[3]);

    


    
    // Assume t2, a2, and L2 are properly declared and defined elsewhere
    t2[0] = 0;
    a2_trolley[0] = v1 * 1000;

    unshaped_command_motor_0 = a2_trolley[0];
    a2_slew[0] = v0 * 1000;
    unshaped_command_motor_1 = a2_slew[0];
    a2_hoist[0] = v2 * 1000;
    unshaped_command_motor_2 = a2_hoist[0];
    L2 = 1;     
    // float v3 = atof(processed_msg[3]);

    convolveShaper();
    sendShapedCommand();

  }else if (strcmp(processed_msg[0], "a") == 0) {
    
    // Serial.println("Custom Ampliudes ");

    if(strcmp(processed_msg[1], "1")== 0){
      storeCustomShaper(c1_amp,processed_msg);
    } else{
      storeCustomShaper(c2_amp,processed_msg);
    }
    
  } else if(strcmp(processed_msg[0], "m") == 0){
      float m1 = atof(processed_msg[1]);
      float m2 = atof(processed_msg[2]);
      float m3 = atof(processed_msg[3]);
      set_motorVelocity(m1,m2,m3);
  } else if (strcmp(processed_msg[0], "b") == 0) {
    // Serial.println("Custom Times");
    if(strcmp(processed_msg[1], "1")== 0){
      storeCustomShaper(c1_time,processed_msg);
    } else{
      storeCustomShaper(c2_time,processed_msg);
    }
  } else if (strcmp(processed_msg[0], "c") == 0) {
    //Calibration command, if the second option is a, auto calibrate else manual calibrate
    if(strchr(processed_msg[1], 'a') != NULL){
      Serial.println("Begin auto cal");
      autoCalibrateMotorOffset();
    }else{
      //Means we are calibrating the crane's offsets
      float c1 = atof(processed_msg[1]);
      float c2 = atof(processed_msg[2]);
      float c3 = atof(processed_msg[3]);
      calbrateMotorOffsets(c1,c2,c3);

      Serial.print("Calibrating ");
      Serial.print(c1);
      Serial.print("  ,");
      Serial.print(c2);
      Serial.print("  ,");
      Serial.println(c3);
    }
  } else if(strcmp(processed_msg[0], "f") == 0){
    if (strcmp(processed_msg[1], "cl") == 0) {
      //message from the gui to clear the faults 
      Serial.println("Clearning the faults");
      clearFaults();
    } else if (strcmp(processed_msg[1], "e") == 0) {
      //message from the gui to clear the faults 
      Serial.println("f, 33554432,33554432, 33554432");
      digitalEstop = true;
    } 
  }else if (strcmp(processed_msg[0], "s") == 0) {
    if(isTraj){
      //if we are currently in trajectory mode, exit out of it 
      toggleTraj();
    }
    Serial.println("Changing Shapers");
    if (strcmp(processed_msg[1], "iden") == 0) {
      makeIden();
    } else if (strcmp(processed_msg[1], "zv") == 0) {
      makeZV();
    } else if (strcmp(processed_msg[1], "ei") == 0) {
      makeEI();
    } else if (strcmp(processed_msg[1], "u1") == 0) {
      Serial.println("User Shaper 1");
      makeCustomShaper(c1_time,c1_amp);
    } else if (strcmp(processed_msg[1], "u2") == 0) {
      Serial.println("User Shaper 2");
      makeCustomShaper(c2_time,c2_amp);
    } else if (strcmp(processed_msg[1], "traj") == 0) {
      toggleTraj();
      Serial.println("Trajectory Mode");
    }
    
  } else if (strcmp(processed_msg[0], "t") == 0) {
    // Serial.println("trajectory message");
    if (strcmp(processed_msg[1], "s") == 0){
      startTraj();
    } else if (strcmp(processed_msg[1], "e") == 0){
      stopTraj();
    } else {
      addTraj(atof(processed_msg[1]), atof(processed_msg[2]), atof(processed_msg[3]));
    }
  } else {
    Serial.println("Command not Recognized");
  }
}

void autoCalibrateMotorOffset(){
  /* This function is all about using limit switches on the trolley and slewing axis to programatically 
      comprehend the location of the crane. This should only have to be done at startup. Note that there are currently 
      NO SENSORS on the hoisting axis and that will need to be calibrated manually by measuring from the top pully to 
      the center of the bottom pulley. 
  */
  //initiates calibration of an axis
  isCal = false;
  //tell the axis to start moving 
  t2[0] = 0;
  a2_trolley[0] = -0.75 * 1000;
  a2_slew[0] = 0;
  a2_hoist[0] = 0;
  L2 = 1; 
  makeIden();
  convolveShaper();
  sendShapedCommand();

  while(!isCal){
    //Wait for the limit switch to be hit 
  }

  Serial.println("Hit limit switch");
  delay(100);
  Get_Encoder_Estimates_msg_t feedback0 = odrv0_user_data.last_feedback;
  // trolleyLen = (feedback0.Pos_Estimate*gearRatioTrolley) - trolley_cal;
  trolley_cal = feedback0.Pos_Estimate*gearRatioTrolley;
  //Move off the limit switch
  Serial.println("Moving Away");
   t2[0] = 0;
  a2_trolley[0] = 1.25 * 1000;
  a2_slew[0] = 0;
  a2_hoist[0] = 0;
  L2 = 1; 
  makeIden();
  convolveShaper();
  sendShapedCommand();
  while(!trolleyLimit1){
    //Wait for the limit switch to be released
  }
  delay(1000);
  a2_trolley[0] = -0.5 * 1000;
  convolveShaper();
  sendShapedCommand();
  

  
  Serial.println("Starting to Slew");
  isCal = false;
  a2_trolley[0] = 0;
  a2_slew[0] = -0.75 * 1000;
  a2_hoist[0] = 0;
  L2 = 1; 
  makeIden();
  convolveShaper();
  sendShapedCommand();
  while(!isCal){
    //Wait for the limit switch to be hit 
  }

  Serial.println("Hit limit switch");
  delay(100);
  Get_Encoder_Estimates_msg_t feedback1 = odrv1_user_data.last_feedback;
  // trolleyLen = (feedback0.Pos_Estimate*gearRatioTrolley) - trolley_cal;
  slew_cal = -1.0*feedback1.Pos_Estimate*gearRatioSlew-22.0;
  velo_motor_1 = 0;
  odrv1.setVelocity(float(velo_motor_1));
  Serial.println("Moving Away");
  a2_slew[0] = 0.5*1000;
  convolveShaper();
  sendShapedCommand();
  while(!slewLimit1){
    //Wait for the limit switch to be released
    Serial.println("Waiting to leave it");
    delay(50);
  }
  delay(1000);
  a2_slew[0] = -0.5 * 1000;
  convolveShaper();
  sendShapedCommand();

}
