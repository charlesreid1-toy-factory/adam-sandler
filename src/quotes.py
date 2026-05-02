import random

QUOTES = [
    {
        "text": "The price is wrong, bitch!",
        "movie": "Happy Gilmore",
        "character": "Happy Gilmore",
    },
    {
        "text": "You can do it! Cut his freakin' head off!",
        "movie": "The Waterboy",
        "character": "Bobby Boucher",
    },
    {
        "text": "I'd like to dedicate this song to a very special lady.",
        "movie": "The Wedding Singer",
        "character": "Robbie Hart",
    },
    {
        "text": "I am the smartest man alive!",
        "movie": "Billy Madison",
        "character": "Billy Madison",
    },
    {
        "text": "That's your big plan? You're just gonna keep hitting me?",
        "movie": "Punch-Drunk Love",
        "character": "Barry Egan",
    },
    {
        "text": "This is how I win.",
        "movie": "Uncut Gems",
        "character": "Howard Ratner",
    },
    {
        "text": "I'm a pretty, pretty princess.",
        "movie": "Happy Gilmore",
        "character": "Halderbrand",
    },
    {
        "text": "Stay here. Stay as long as you can. You'll have to pump the blood.",
        "movie": "Click",
        "character": "Morty",
    },
    {
        "text": "What the hell is a gigawatt?",
        "movie": "Jack and Jill",
        "character": "Al Pacino",
    },
    {
        "text": "I'm kinda a big deal. People know me.",
        "movie": "Uncut Gems",
        "character": "Howard Ratner",
    },
    {
        "text": "Just put the ball in the hole. It's really quite simple.",
        "movie": "Happy Gilmore",
        "character": "Chubbs Peterson",
    },
    {
        "text": "Suck my white ass, ball!",
        "movie": "Happy Gilmore",
        "character": "Happy Gilmore",
    },
    {
        "text": "I have emotional problems!",
        "movie": "The Waterboy",
        "character": "Bobby Boucher",
    },
    {
        "text": "I'm not a pervert! I'm just looking for a tube.",
        "movie": "Big Daddy",
        "character": "Sonny Koufax",
    },
    {
        "text": "Now you will go to sleep, or I will put you to sleep.",
        "movie": "Happy Gilmore",
        "character": "Ben Stiller",
    },
]


def random_quote():
    return random.choice(QUOTES)
