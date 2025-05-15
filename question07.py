def blastoff(seconds):
    if seconds > 0:
        print(seconds)
        blastoff(seconds - 1)
    else:
        print("Blastoff!!")

blastoff(11)