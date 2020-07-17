guests = ["Nurayim", "Dastan", "Janar"]
letter = "You are invited to home party "
message = "Sorry, but I can invite just two people, "
invitation = "My invitation is still on go, " 
b = guests.insert(0, "Asan")
# print(guests)

c = guests.insert(2, "Begimai")
# print(guests)

d = guests.append("Ainura")
print(guests)


c = guests.pop()
print(guests)
print(message + "Ainura")

d = guests.pop()
print(guests)
print(message + "Janar")

e = guests.pop()
print(guests)
print(message + "Dastan")1

g = guests.pop()
print(guests)
print(message + "Begimai")

print(invitation + "Asan")
print(invitation + "Nurayim")


del guests[ : ]
print(guests)