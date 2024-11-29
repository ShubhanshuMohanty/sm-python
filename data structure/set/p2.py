sports1={"Sanoj", "Neha", "Dev", "Raj", "Shweta", "Hiral"}  
sports2={"Neha", "Shweta", "Hiral", "Arjun", "Ram", "Sahyog"} 
#Find total participants in the sports list 
Total_Ath=sports1|sports2 
print("Total participants:", Total_Ath) 
for s in Total_Ath: 
    print(s) 
    
#set Difference
New_sports1=sports1-sports2 
print("The new sports one list is:", New_sports1)