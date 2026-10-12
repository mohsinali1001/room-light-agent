
def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Bright":
        return "Turn Light OFF"
    elif percept == "Very Bright":
        return "Turn Light OFF"
    else:
        return "Leave Light As Is"


percept_sequence = ["Dark", "Dim", "Bright", "Dark", "Very Bright"]

print("Percept\t\t\tAction")

for percept in percept_sequence:
    action = room_light_agent(percept)
    print(percept, "\t\t", action)

def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Bright":
        return "Turn Light OFF"
    elif percept == "Very Bright":
        return "Turn Light OFF"
    else:
        return "Leave Light As Is"


percept_sequence = ["Dark", "Dim", "Bright", "Dark", "Very Bright"]

print("Percept\t\t\tAction")

for percept in percept_sequence:
    action = room_light_agent(percept)
    print(percept, "\t\t", action)
