def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Bright":
        return "Turn Light OFF"
    else:
        return "Leave Light As Is"


percept_sequence = ["Dark", "Dim", "Bright", "Dark"]

print("Percept\t\tAction")

for percept in percept_sequence:
    action = room_light_agent(percept)
    print(percept, "\t", action)