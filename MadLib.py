prompts = [
    "adjective",
    "noun",
    "adjective",
    "noun that's a place",
    "adjective",
    "adjective",
    "plural noun that's a vehicle",
    "adjective",
    "adjective",
    "plural noun",
    "adjective",
    "plural noun",
    "plural noun",
    "adjective",
    "noun",
    "verb",
    "adjective",
    "verb",
    "plural noun",
    "plural noun that's a job",
    "adjective",
    "verb",
    "adjective"
]

words = []
for prompt in prompts:
    words.append(input("Enter a(n) " + prompt + ": "))

print("Star Wars is a " + words[0] + " " + words[1] + " of " + words[2] + " versus evil in a " + words[3] + " far far away. ")
print("There are " + words[4] + " battles between " + words[5] +" " + words[6] + " in " + words[7] + " space and " + words[8] + " duels with " + words[9] + " called " + words[10] + " sabres. ")
print("" + words[11] + " called droids are helpers and " + words[12] + " to the heroes. ")
print("A " + words[13] + " power called The " + words[14] + " " + words[15] + "s people to do " + words[16] + " things, like " + words[17] + " " + words[18] + ".")
print(" The jedi " + words[19] + " use The Force for the " + words[20] + " side and the Sith " + words[21] + " it for the " + words[22] + " side. ")

