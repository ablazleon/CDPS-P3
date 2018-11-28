import sys
import os

# It is configured S1, to have connectivity in this scenario

if len(sys.argv) == 1:
    sys.exit("You have not introduced as an aditional parameter the web name")
s1 = sys.argv
print("The name of your tab is:" + sys.argv[1])
os.system("xterm -rv -sb -rightbar -fa monospace -fs 10 -title 's1' -e 'sudo virsh console s1'")


print("In the new terminal")