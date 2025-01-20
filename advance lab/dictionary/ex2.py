# Q.2) You have a list of email addresses and you want to extract the domain part (the after '@') from each email address.

email=["sm@gamail.com","sp@gamail.com","om@gama.in","nk@somaiya.in"]
domain=[i.split("@")[1] for i in email]
# dm=[i.split("@")[10] for i in email]
print(domain)
