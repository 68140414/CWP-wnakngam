"""Your Namebook"""
def array_of_names(persons: dict):
    """Change Dict to array of names"""
    name_arr = [f"{name.capitalize()} {persons[name].capitalize()}" for name in persons]
    return name_arr

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
