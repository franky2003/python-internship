import re
text=input("Enter the email:")
f=open("content.txt","r")
def valid(text):
    pattern=("\w*.?@(?!yahoo|hotmail)\w*[.][coi][orn][mg]")
    re.findall(pattern,text)
    if re.findall(pattern,text)==[]:
        print("GMAIL INVALID")
    else:
        print(f.read())
    
valid(text)    

#Output
'''
Enter the email:dhoni66@gmail.com

  ________               .__.__    .__         ____   ____      .__  .__    .___
 /  _____/  _____ _____  |__|  |   |__| ______ \   \ /   /____  |  | |__| __| _/
/   \  ___ /     \\__  \ |  |  |   |  |/  ___/  \   Y   /\__  \ |  | |  |/ __ | 
\    \_\  \  Y Y  \/ __ \|  |  |__ |  |\___ \    \     /  / __ \|  |_|  / /_/ | 
 \______  /__|_|  (____  /__|____/ |__/____  >    \___/  (____  /____/__\____ | 
        \/      \/     \/                  \/                 \/             \/ 
'''