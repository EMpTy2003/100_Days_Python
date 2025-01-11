#Functions with outputs - Multiple Return values

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "Invalid Inputs"
    flname= f_name +" "+l_name
    name=flname.title()
    return f"Result: {name}"
print(format_name("mohamed","thoufeek"))

    