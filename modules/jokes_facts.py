from modules.tts import speak
import random # Function to tell a joke or riddle


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the math book look sad? Because it had too many problems!",
        "What did the ocean say to the beach? Nothing, it just waved.",
        "Why can't you trust an atom? Because they make up everything!",
        "Why don't programmers like nature? It has too many bugs.",
        "What do you call fake spaghetti? An impasta!",
        "Why was the broom late? It swept in!",
        "What did one wall say to the other wall? I'll meet you at the corner.",
        "Why do cows wear bells? Because their horns don't work!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
        "What do you call an alligator in a vest? An investigator!",
        "Why don’t oysters donate to charity? Because they’re shellfish.",
        "What do you call a pile of cats? A meow-tain.",
        "Why did the computer go to the doctor? It had a virus!",
        "Why was the math teacher suspicious of prime numbers? They just seemed odd.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "What do you call a snowman with a six-pack? An abdominal snowman.",
        "Why did the bicycle fall over? Because it was two-tired."
    ]
    
    joke = random.choice(jokes)
    speak(joke)


# Function to provide a daily quote
def daily_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Don’t let yesterday take up too much of today. - Will Rogers",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "Act as if what you do makes a difference. It does. - William James",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You miss 100% of the shots you don’t take. - Wayne Gretzky",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
        "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
        "It always seems impossible until it’s done. - Nelson Mandela",
        "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill",
        "Don’t be afraid to give up the good to go for the great. - John D. Rockefeller",
        "The harder you work for something, the greater you’ll feel when you achieve it. - Anonymous",
        "It’s not whether you get knocked down, it’s whether you get up. - Vince Lombardi",
        "The secret of getting ahead is getting started. - Mark Twain"
    ]
    
    quote = random.choice(quotes)
    speak(f"Here’s a motivational quote for you: {quote}")


# Function to tell a random fact
def tell_fact():
    facts = [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!",
        "A group of flamingos is called a 'flamboyance'.",
        "Bananas are berries, but strawberries are not!",
        "Sharks have been around longer than trees, existing for over 400 million years.",
        "The Eiffel Tower can grow by 6 inches during the summer because of the expansion of metal in heat.",
        "A day on Venus is longer than a year on Venus.",
        "Cleopatra lived closer in time to the moon landing than to the construction of the Great Pyramid of Giza.",
        "Wombat poop is cube-shaped to prevent it from rolling away.",
        "The human nose can detect over 1 trillion different scents.",
        "A 'jiffy' is an actual unit of time, equal to 1/100th of a second.",
        "Octopuses have three hearts and blue blood.",
        "The longest hiccuping spree lasted 68 years.",
        "Humans share about 60% of their DNA with bananas.",
        "The heart of a blue whale is as big as a small car.",
        "There are more stars in the universe than grains of sand on all of Earth's beaches.",
        "Polar bear skin is black, even though their fur appears white.",
        "Sloths only poop once a week and can lose up to one-third of their body weight during that process.",
        "You can't hum while holding your nose.",
        "A cockroach can live for weeks without its head.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes."
    ]
    
    fact = random.choice(facts)
    speak(f"Here’s a random fact for you: {fact}")
