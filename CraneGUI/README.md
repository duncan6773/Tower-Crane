# Folder Contents 

This folder contains files regarding the python GUI. The GUI was made utilizing the pyqt5 library and QT designer. 
There are multiple files with the .ui extension, they allow users to directly upload the file into designer and edit the gui files
Then the impComands.txt includes the information to change the .ui files into python files to be able to run in the code 

# What files does the GUI need
There are three critical files that the Gui needs to be able to run. The first is craneGui_main.py this is the main executable the user should run to create and bring up the GUi.
The next is the CraneGuiActions file. This includes the Crane Gui backend class which handles all the backend actions of the Crane GUi such as setting up commands, adding the photos 
to buttons and much much more. The final file is customDialoug.py. This script conatins the classes for any pop up menus for gui and is called upon by the crane Gui backend. 

## Recomendations for Changes
It is not reccomended to edit the craneGui_main.py file directly except for when converting a new layout file or adding in the code to setup the crane Gui backend
Instead, it is reccomended to add all functionality to the crane GUI backend as this is what should handle all events for the crane. Note that the backend and main script 
are actually doing multiple actions called threads in parallel and debugging the script with the built in python debugger might not always work. To help prevent debugging issues, 
it is helpfull to only have break points in functions that are on the same thread. For example, only have breakpoints on functions that are caused from buttons being pressed or the drop
down menu. Do not put a break point in the message callback function and the button functions. 
