#The python dictionary deep dive
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving Items from dictionary
#print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."


#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"]="Poochi kaatu poochi"
#print(programming_dictionary)

#Loop Through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])