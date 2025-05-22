print("----- Terraria Biome Calculator -----")
while (True):
    #Grabbing the user's horizontal position
    posHorizontal = int(input("Position displayed by Compass (use negative for West, positive for East):"))
    borderLeft = posHorizontal - 168
    borderRight = posHorizontal + 168

    #Grabbing the user's vertical position
    posVertical = int(input("Position displayed by Depth Meter (use negative for Underground/Caverns, positive for Surface/Space):"))
    borderUpper = posVertical + 126
    borderLower = posVertical - 120

    #Function for returning coordinates as how they appear in-game
    def readableOutput(coordinateX, coordinateY):
        readableHorizontal = "Center"
        readableVertical = "Level Surface"

        if (coordinateX < 0):
            readableHorizontal = "West"
        elif (coordinateX > 0):
            readableHorizontal = "East"

        if (coordinateY < 0):
            readableVertical = "Underground/Caverns"
        elif (coordinateY > 0):
            readableVertical = "Surface/Space"

        return f"{abs(coordinateX)}' {readableHorizontal}, {abs(coordinateY)}' {readableVertical}"

    print("\nWhile standing on a platform at each corner, you should see these coordinates:")
    
    #Outputting four corner coordinates
    print(f"Top left: {readableOutput(borderLeft, borderUpper)}")
    print(f"Top right: {readableOutput(borderRight, borderUpper)}")
    print(f"Bottom left: {readableOutput(borderLeft, borderLower)}")
    print(f"Bottom right: {readableOutput(borderRight, borderLower)}\n")

    print("Now, place the desired biome block directly above each platform.")
    print("Place the remaining blocks within this rectangle.")
    print(f"If done correctly, your artificial biome will be centered on {readableOutput(posHorizontal, posVertical)}.")

    input("Press Enter to restart...\n")
