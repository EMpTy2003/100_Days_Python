#Docstrings

def format_name(f_name,l_name):
    """ Take a First name and last name and for mat it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "Invalid Inputs"
    flname= f_name +" "+l_name
    name=flname.title()
    return f"Result: {name}"
print(format_name("mohamed","thoufeek"))

format_name()