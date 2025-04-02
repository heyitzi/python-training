tog = {
    1: "The Assassin's Blade",
    2: "Throne of Glass",
    3: "Crown of Midnight",
    4: "Heir of Fire",
    5: "Queen of Shadows",
    6: "Empire of Storms",
    7: "Tower of Dawn",
    8: "Kingdom of Ash"
}

acotar = {
    1: "A Court of Thornes and Roses",
    2: "A Court of Myst and Fury",
    3: "A Court of Wings and Ruin",
    4: "A Court of Frost and Starlight",
    5: "A Court of Silver Flames"
}

cc = {
    1: "House of Earth and Blood",
    2: "House of Sky and Breath",
    3: "House of Flame and Shadow"
}

print("Sarah J. Maas Bibliography:")
print("-----")

print("TOG Series")
for i in tog:
    print(i, tog[i])
print("-----")

print("ACOTAR Series")
for i in acotar:
    print(i, acotar[i])
print("-----")

print("Crescent City Series")
for i in cc:
    print(i, cc[i])

# TODO methods() .keys(), values and items - repite ejercicio usandolos