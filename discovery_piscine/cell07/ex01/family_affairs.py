"""Family Affairs"""
def find_the_redheads(family_head: dict):
    """Find person with red head"""
    red_head = [person for person in family_head if family_head[person] == "red"]
    return red_head

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
