This folder should hold the most up to date code for the Arduino running the tower crane software. At this current time it is an arduino due running the code 
however there is the possibility that it will swap over to the Teensy. If you need to swap over to the teensy microcontroller or to another arduino. I will leave some
instructions and tips to help users. First though is the scripts used on the arduino and what they do on a high level

Tower Crane Master Arduino:
  This is the main script for the arduino. This imports the other scripts and has the main for loop. It also calls the functions to setup the switches, timers, and         handles the serial comunication with GUI. 
  
Odrive Due CAN:
  This is a custom made function to allow the arduino due to communicate with the odrive motors over CAN. Normally this is provided by ODRIVE, but they do not support  
  Arduino DUE, so I had to custom make this 
  
Motor Manager:
  This is the script that handles vlocity updates to the motor, the command buffers and storage for the trajectory.
  
Shaper Maker:
  This script contains the functions for making the pre made shapers as well as convolving the incoming commands with the desired shaper 
  
Switches and Buttons:
  This script handles setting up the buttons and the corresponding interupts.




--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


If you need to swap the code over the Teensy, there are a few main things you need to do:

1st: 
  The arduino due has a custom timer library to handle timer interupts that is specific to the microcontroller. This means any functions that is being used to setup
  the timerISR and the trajISR. Basically anywhere you see Timer3, you will need to replace this with an appropriate function for the teensy. At this current time that
  would effect the startTimer, startTraj, and endTraj functions in the motor manager script
  
2nd:
  Odrive did not have the libraries to support the arduino due code and I needed to make a custom one called OdriveDueCAN. This code will not work with the Teensy, but 
  Odrive does have code to support CAN on the Teensy with examples. This means that you will need to change the import to be the correct script and everything else should
  work out automatically
  
3rd:
  The arduino due utilizes the NVIC C++ library to change the priority of the interupt to allow certain interupts to be classified as more important than other interupts.
  I do not know/ think the Teensy supports this structure. You will need to replace the lines with NVIC_SetPriority with the cooresponding method for the teensy. You can 
  see an example of where this is used in the setupt switches function is switchesAndButtons
