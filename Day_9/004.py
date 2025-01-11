#Nesting Lists and Dictionaries
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
    
################################################################################

#Nesting
capitals = {
    "France":"Paris",
    "Germany" : "Berlin",
}

#Nesting a List in Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
    "France" :{"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visited": 12},
    "Germany" :{"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "days_spent" : 22},
}

#Nesting a dictionary in a list

travel_log = [
    {
        "country":"France", 
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visited": 12
    },
    {
        "country":"Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visited" : 22
    },
]