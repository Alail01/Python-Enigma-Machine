# Enigma-Machine

  This was created as a practice with the pyton language, and it not totally optimized nor is the code as pretty as possible. This is just a start to the Enigma Machine that was used within WW2. The rotors are as close to the WW2 as I could find. Any mistakes are mine, and mine alone. 
  
  Created by a German engineer, the Enigma Machine was used in the second world war to pass messages to the front line. There is nearly 159 qunintillion ways that the engima machine can be set. 

Basics on how it works:
  The type writer like structure is used the start the key press. Once a key is pressed, it goes to the plug board. The plug board then passes the new letter to the rotors, where is passes through the first one, into the second one, into the third, which then goes back on itself, going from three to two and back to one. Once through the rotor block, that new letter is passed back to the plug board, which then goes to the lights, to emit a light which is the new letter. 

Rotors: 
  In the one that was used in World War 2, there was five different rotors. Each one was different from the last, and each one can be used in what ever order. Three are used with the machine, and are set into position. The rotor can be placed in the machine starting with any letter on top. Each time a letter is passed between the rotors, the rotors shift one letter. Starting with the first positition rotor, it shifts each time the leter is passed through a rotor. The second rotor only shifts once after the first rotor has completed a full rotation, and the third only shifts once after the second makes a full rotation. So it would take 676 letters for the third rotor to move once, and 17576 letters for all three rotors to make a full rotation.
  Below is the reference that I used for the rotors: Found on https://en.wikipedia.org/wiki/Enigma_rotor_details (Yes I know Wikipedia...)
  
Rotor #	 \t ABCDEFGHIJKLMNOPQRSTUVWXYZ	  Date Introduced	   Model Name & Number
I	        JGDQOXUSCAMIFRVTPNEWKBLZYH	  7 February 1941	   German Railway (Rocket)
II	      NTZPSFBOKMWRCJDIVLAEYUXHGQ	  7 February 1941	   German Railway (Rocket)
III	      JVIUBHTCDYAKEQZPOSGXNRMWFL	  7 February 1941  	 German Railway (Rocket)
UKW	      QYHOGNECVPUZTFDJAXWMKISRBL	  7 February 1941	   German Railway (Rocket)
ETW	      QWERTZUIOASDFGHJKPYXCVBNML	  7 February 1941	   German Railway (Rocket)


Plug Board: 
  The plug board is what made this machine insane to break. Each letter is on the plug board, and there are ten wires that can be used. Each wire is connected from one letter to another. This would make the machine change the letter you used. So if a wire was from 'A' to 'G', each time the 'A' key was pressed, a 'G' would go through the rotors. Similarly, each time a 'G' was returned from the rotors, the 'A' light would come up. If there was no wire attached to the letter you pressed, or that got returned from the rotors, then that letter would be the same that was pressed, or returned. 
  
