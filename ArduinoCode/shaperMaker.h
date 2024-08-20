#pragma once
#include "motorManager.hpp"

/*
  Date:     7/15/2024
  Author:   Will Duncan

  This script is here to do everything involving shapers. It includes the code to make the built in shapers
  how to convolve shapers, and loading the shapers into the motor buffer




*/


//User inputted Shaper
int t1[20]; //times are in miliseconds 
int a1[20]; //decimal *1000. it is cut off after 3 decimal places to save space 
int L1 = 4;
//User Commands  
int t2[4];
int a2_trolley[4];
int a2_slew[4];
int a2_hoist[4];

//Custom shapers 
int c1_amp[20];
int c1_time[20];

int c2_time[20];
int c2_amp[20];


int L2 = 1; //The commads to the motors should all be the same. If there isnt a command for a motor, make it zero
//Making the convolved trajectory
int t3[80];

//Total Shaped Command 
int a3_trolley[80];
int a3_slew[80];
int a3_hoist[80];



void convolveShaper(){
  //This is a function that convolves two shapers defined by t1,a1 and t2,a2
  //
  //for each element in L1
  for(int i = 0 ; i < L1 ; i++){
    //For each element in L2 
    for(int j = 0; j<L2 ; j++ ){

      t3[i*L2+j] = t1[i] + t2[j];
      a3_trolley[i*L2+j] = a1[i] * a2_trolley[j]/1000;
      a3_slew[i*L2+j] = a1[i] * a2_slew[j]/1000;
      a3_hoist[i*L2+j] = a1[i] * a2_hoist[j]/1000;


      // Serial.println(a3[i*L1+j]);
    }
  }

}

void makeZV(){
  //Makes the shaper given in Z1 to be a zv
  int damp = 0;
  float k = exp(-1.0* damp * 3.14159 /(sqrt(1.0-(damp*damp))));
  float cable_len = hoistHeight/1000;

  a1[0] = (1.0/(1.0+k))*1000;
  a1[1] = (k/(1.0+k))*1000;

  t1[0] = 0;
  t1[1] = (0.5 * 2*PI*sqrt(cable_len/g))*1000;

  L1 = 2; //Redefining the length of the array 
}

void makeEI(){
  //TOOO double check the math here 
  float damp = 0.0f;
  float k = exp(-1* damp * 3.14159 /(sqrt(1-(damp*damp))));
  float cable_len = hoistHeight/1000;
  float vtol = 0.05;
  float td = 2*PI*sqrt(cable_len/g);
  a1[0] = 0.25*(1+vtol)*1000;
  a1[1] = 0.5*(1-vtol) *1000;
  a1[2] = 0.25*(1+vtol)*1000;
  t1[0] = 0;
  t1[1] = 0.5*(td)*1000;
  t1[2] = (td)*1000;
  L1 = 3;
}

void makeIden(){
  /*
    This shaper is essentially saying there is no shaper. Whatever your input is, is what will be sent to the motor
  */
  a1[0] = 1000;
  t1[0] = 0;
  L1 = 1;
}

void makeCustomShaper(){
  //TODO Delete
  a1[0] = 0.069*1000;
  a1[1] = 0.124*1000;
  a1[2] = 0.125*1000;
  a1[3] = 0.069 *1000; 
  a1[4] = 0.226 *1000;
  a1[5] = 0.069 *1000;
  a1[6] = 0.125 *1000;  
  a1[7] = 0.124 *1000;  
  a1[8] = 0.069*1000;
   
  t1[0] = 0;
  t1[0] = 0.5825 *1000;   
  t1[0] = 1.0276 *1000;
  t1[0] = 1.1651*1000;  
  t1[0] = 1.6101*1000;
  t1[0] = 2.0552*1000;
  t1[0] = 2.1927 *1000;
  t1[0] = 2.6377 *1000; 
  t1[0] = 3.2203*1000;
                          
  L1 = 9;


}

void sendShapedCommand(){
  /*
    THis function is what sends the convolved shaper into the motor buffer
  */

  int L3 = L1*L2; //Figure out how many commands we need to add
  int startTime = curMotorVeloPos; //figuring out what the start time is 
  // Serial.print("L3 is");
  // Serial.println(L3);
  for (int i = 0; i < L3; i++ ){
    //For each shaped command in the shaper 
    int newidx = ((t3[i])/motorTimerPeriod)+curMotorVeloPos+10; //plus 15 to give a buffer incase 
    newidx = wrapMotorIDX(newidx);
    motor0V[newidx] = motor0V[newidx] + a3_trolley[i]; 
    motor1V[newidx] = motor1V[newidx] + a3_slew[i];
    motor2V[newidx] = motor2V[newidx] + a3_hoist[i];
    
  }
}

void storeCustomShaper(int custArray[] , char* myMsg[]){

 for(int i = 0; i< 20; i++ ){
  custArray[i] = atoi(myMsg[i+2]); //We need to ignore the first two entries of the array as they are the letter and the shaper number
 }

}

void makeCustomShaper(int custTimes[], int custAmps[] ){
  for(int i = 0; i < 20; i++){
    a1[i] = custAmps[i];
    t1[i] = custTimes[i];
  }
  L1 = 20;
}


