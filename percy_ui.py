import os
import sys
from colorama import Fore, Style, init

# Initialize colorama for Windows
init()

def main():
    os.system("cls")  # Clears the screen
    os.system("title Percy - AI Assistant")  # Sets terminal title

    print(Fore.GREEN + """

<========================================================>
           
     :::::::::  :::::::::: :::::::::   ::::::::  :::   ::: 
     :+:    :+: :+:        :+:    :+: :+:    :+: :+:   :+:  
    +:+    +:+ +:+        +:+    +:+ +:+         +:+ +:+    
   +#++:++#+  +#++:++#   +#++:++#:  +#+          +#++:      
  +#+        +#+        +#+    +#+ +#+           +#+        
 #+#        #+#        #+#    #+# #+#    #+#    #+#         
###        ########## ###    ###  ########     ###             
  
<========================================================>
    """, Style.RESET_ALL)
    
    while True:
        user_input = input(Fore.GREEN + "Percy> " + Style.RESET_ALL)  # Green input prompt
        if user_input.lower() == "exit":
            print(Fore.GREEN + "Goodbye Sir!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
