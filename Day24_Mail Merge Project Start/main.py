#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# use the readlines() method to get all names as  a list
# loop through the list, and create a new file of element.txt where you replace each [name] with the element
# # take the [name] invitation as a string in the beginning
# # replace [name] with the loop element after it has been stripped of the \n

with open("./Input/Letters/starting_letter.txt") as invitation:
    default_invitation = invitation.read()

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for name in name_list:
        current_name = name.strip()
        named_invitaion = default_invitation.replace("[name]", current_name)

        with open(f"./Output/ReadyToSend/{current_name}.txt", "w") as output:
            output.write(named_invitaion)
