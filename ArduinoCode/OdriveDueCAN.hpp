#pragma once
#include "ODriveCAN.h"
#include <due_can.h>


// CAN bus baudrate. Make sure this matches for every device on the bus
#define CAN_BAUDRATE 1000000

// ODrive node_id for odrv0
// #define ODRV0_NODE_ID 0
byte trolleyNodeID = 0;
byte slewingNodeID =  1;
byte hoistingNodeID = 2;
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
Motor PID Gains 
  Note not currently used
*/

float trolley_vel_int_gain = 0.375;
float trolley_pos_gain = 27.0;
float trolley_vel_gain = 0.75;

float slew_vel_int_gain = 20.0;
float slew_pos_gain = 52.0;
float slew_vel_gain = 0.837;


////////////////////////////////////////////////////////////////////////////////////////////////////////////
using CanMsg = CAN_FRAME;
CANRaw& can_intf = Can0; // the can bus we are using 

static bool sendMsg(CANRaw& can_intf, uint32_t id, uint8_t length, const uint8_t* data) {
    /* 
      DO NOT TOUCH!! This function is the building block for all comunication to the ODRIVES and any CAN Device
      Small mistakes in this function can prevent the crane and Estop from functioning properly. 
    */
    CAN_FRAME teensy_msg;
    teensy_msg.id =  id & 0x1fffffff;
    teensy_msg.extended = (bool)(id & 0x80000000);
    teensy_msg.rtr = !data;
    teensy_msg.length = length;
    
    if (data) {
        memcpy(teensy_msg.data.byte, data, length);
    }

    return (can_intf.sendFrame(teensy_msg) > 0);
}

void onReceive(const CAN_FRAME& msg, ODriveCAN& odrive) {
  /*
    How to process the incoming message frames
  */
    odrive.onReceive(msg.id | (msg.extended ? 0x80000000 : 0), msg.length, msg.data.byte);
}

void pumpEvents(CANRaw& can_intf) {
  /*
    pumpEvents is required for some CAN systems and built in support is required for ODRIVE 
    However our system does not need to pumpp events itself so it is left empty 
  */
    // can_intf.events();
}


/////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
  Not a function but setting up the data structures for the Arduino to be able to process messages from the odrive
*/
CREATE_CAN_INTF_WRAPPER(CANRaw)


struct ODriveUserData {
  Heartbeat_msg_t last_heartbeat;
  bool received_heartbeat = false;
  Get_Encoder_Estimates_msg_t last_feedback;
  bool received_feedback = false;
};

// Keep some application-specific user data for every ODrive.
ODriveUserData odrv0_user_data;
ODriveUserData odrv1_user_data;
ODriveUserData odrv2_user_data;

// ODriveCAN odrv0(wrap_can_intf(can_intf), ODRV0_NODE_ID); // Standard CAN message ID
ODriveCAN odrv0(wrap_can_intf(can_intf), trolleyNodeID);
ODriveCAN odrv1(wrap_can_intf(can_intf), slewingNodeID);
ODriveCAN odrv2(wrap_can_intf(can_intf), hoistingNodeID);

ODriveCAN* odrives[] = {&odrv0, &odrv1, &odrv2}; // Make sure all ODriveCAN instances are accounted for here

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////



// Called every time a Heartbeat message arrives from the ODrive
void onHeartbeat(Heartbeat_msg_t& msg, void* user_data) {
  // Serial.println("Heart beat?");
  ODriveUserData* odrv_user_data = static_cast<ODriveUserData*>(user_data);
  odrv_user_data->last_heartbeat = msg;
  odrv_user_data->received_heartbeat = true;
}

// Called every time a feedback message arrives from the ODrive
void onFeedback(Get_Encoder_Estimates_msg_t& msg, void* user_data) {
  ODriveUserData* odrv_user_data = static_cast<ODriveUserData*>(user_data);
  odrv_user_data->last_feedback = msg;
  odrv_user_data->received_feedback = true;
}



// Called for every message that arrives on the CAN bus
void onCanMessage(CanMsg* msg) {
  // Serial.println("New MSG");
  for (auto odrive: odrives) {
    onReceive(*msg, *odrive);
  }
}


bool setupCan() {
  /*
    Initializing CAN communication with the DUE CAN library
  */
  can_intf.begin(CAN_BAUDRATE);
  // can_intf.set_baudrate(CAN_BAUDRATE);
  
  // can_intf.setRXFilter(ODRV0_NODE_ID, 0, 0, true);
    for (int filter = 0; filter < 3; filter++) {
    Can0.setRXFilter(filter, 0, 0, true);
  }
  for (int filter = 3; filter < 15; filter++) {
    Can0.setRXFilter(filter, 0, 0, false);
  }
  can_intf.setGeneralCallback(onCanMessage);
  return true;
}

// void setPID(){
  /*
    A function to change the PID gains of the controllers. Deemed Un needed but leaving here incase 
    it is needed in the future
  */
//   byte velIntBytes[4];
//   byte velGBytes[4];
//   byte posGBytes[4];
//   byte gain_msg[8];

//   CAN_FRAME canMsg;

//   byte currNode[8];
//   //For trolley 
//   // memcpy(currNode,&trolleyNodeID);

//   //Message for trolley 
//   canMsg.id = (trolleyNodeID<<8) | 0x1b;
//   memcpy(gain_msg, &trolley_vel_int_gain, 4);
//   memcpy(gain_msg+4, &trolley_vel_gain, 4);
//   sendMsg(can_intf,canMsg.id,8,gain_msg);
//   delay(100);
//   canMsg.id = (trolleyNodeID<<8) | 0x1a;
//   memcpy(gain_msg, &trolley_pos_gain,4);
//   sendMsg(can_intf,canMsg.id,8,gain_msg);
//   sendMsg(can_intf,canMsg.id,4,gain_msg);

//   //Message for slew 
//   canMsg.id = (slewingNodeID<<8) | 0x1b;
//   memcpy(gain_msg, &slew_vel_int_gain, 4);
//   memcpy(gain_msg+4, &slew_vel_gain, 4);
//   sendMsg(can_intf,canMsg.id,8,gain_msg);
//   delay(100);
//   canMsg.id = (slewingNodeID<<8) | 0x1a;
//   memcpy(gain_msg, &slew_pos_gain,4);
//   sendMsg(can_intf,canMsg.id,8,gain_msg);
//   sendMsg(can_intf,canMsg.id,4,gain_msg);

// }


