# Psuedocode for Final Lab


#First Part:


User opens file, upon opening, program launches into: 

getData function ()

    if user enters "correct data"
        Proceed.

    else
        while loop that asks for information three more times
        "Please enter code edits in correct style, language, and data type:"

        if getData function () = False after three times of incorrect input:

            Break
            "Incorrect input. Program locked."

Close file - program is now unaccessible until authorized user unlocks it
Vehicle is disabled (this seems annoying, but is a safety measure).


#Second Part (after user enters "correct data"):

    
Strip code using .strip() method
Take out all characters deemed unncessary by program (replace method)
Have program compare entered code to in-program code (likely in a file)
If statement:
    If there are no matches for words or functions listed in the entered code...
    that compares to the computer code, then:
    "Incorrect input. Program locked. Please see authorized user to contine."
    At this point, only authorized users (like a dealership) could modify code


#Third Part

input('Please enter which function you would like to access.")

      User inputs: 'EGR_Valve_Data()'

input('Please enter access code 1057a.')

if car owner has access to the data, it will be listed in car manual. If not:

      'Incorrect input. Please locate dealership.'


