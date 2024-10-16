# Define the function named custom_song
def custom_song(name, place, adjective1, adjective2, noun1, noun2, verb, emotion):
    # Use f-strings to incorporate parameters into the song's lyrics
    song = f"""
    {name} went to {place}
    It was a {adjective1} day
    The {noun1} was {adjective2}
    And everyone wanted to {verb} and play

    Suddenly, a {noun2} appeared
    Making everyone feel {emotion}
    {name} knew this adventure
    Would be something to cheer
    """
    print(song)

# Collect user input
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb = input("Enter a verb: ")
emotion = input("Enter an emotion: ")

# Call the function with user inputs as named arguments
custom_song(name=name, place=place, adjective1=adjective1, adjective2=adjective2, noun1=noun1, noun2=noun2, verb=verb, emotion=emotion)
