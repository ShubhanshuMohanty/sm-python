#methods related to string 
text="helloWorld" 
text_upper=text.upper() 
print("The data in uppercase is", text_upper) 
text_lower=text.lower() 
print("The data in lowercase is", text_lower) 
name=" RajGopal" 
newname=name.strip() 
print("The data without space is", newname)
lspace=name.lstrip() 
print("The data without space is", lspace)
rspace=name.rstrip() 
print("The data without space is", rspace)

#str.replace (old, new): This method replaces all occurrences of the "old" substring with 
#the "new" substring in the string. 
sentence = "I like apples, and I like pineapple." 
new_sentence = sentence.replace("like", "love") 
print(new_sentence) 
# "I love apples, and I love pineapple."