questions = ['1. You hit snooze. What happens?',
            '2. You open the fridge. Why?',
            '3. Three dots vanish. You feel:',
            '4. Your password fails. You try:',
            '5. You browse Netflix. You watch:',
            '6. "Unexpected item." You feel:',
            '7. It charges only if you:',
            '8. Away for an hour. You return to:',
            '9. You went for milk. You leave with:',
            '10. What lives on your chair?',
            '11. First words of a work call:',
            '12. "Five minutes" at midnight leads to:',
            '13. Your custom drink receipt looks like:',
            '14. A 9-minute voice note. You:',
            '15. GPS says "Recalculating." You feel:',
            '16. Online menu checked 4 days early to:'
]

correct_answers = (
    "B",
    "A",
    "C",
    "D",
    "A",
    "B",
    "C",
    "C",
    "B",
    "B",
    "B",
    "C",
    "C",
    "B",
    "B",
    "B"
)

question_options = [
    (
        "A. You wake up 9 minutes later feeling fully refreshed and ready to conquer the day.",
        "B. You enter a multi-layered dream within a dream and wake up in a panic 45 minutes late.",
        "C. You accidentally turn off the alarm completely and sleep through your entire life.",
        "D. You stare at the ceiling wondering why you did that."
    ),
    (
        "A. You just checked it 3 minutes ago, but you're hoping new food magically spawned.",
        "B. You are genuinely hungry and plan to cook a balanced, nutritious meal.",
        "C. You need to put something back that you shouldn't have taken out.",
        "D. You are looking for the light bulb."
    ),
    (
        "A. Deeply relaxed and patient about the flow of human conversation.",
        "B. Indifferent because texting is overrated anyway.",
        "C. A sudden surge of betrayal, panic, and curiosity about what they deleted.",
        "D. Excited that they are writing a novel."
    ),
    (
        "A. Calmly retrieve your password manager and log in with your master key.",
        "B. Accept that your account is gone forever and change careers.",
        "C. Cry and call tech support immediately.",
        "D. Type it slightly faster and with more aggressive key-mashing, hoping it works."
    ),
    (
        "A. A mediocre documentary about a weird cult you'll forget by tomorrow.",
        "B. That acclaimed 10-season drama you saved months ago.",
        "C. The same comfort sitcom episode you have seen 47 times.",
        "D. The credits of a movie before turning off the TV."
    ),
    (
        "A. Vindicated and happy to wait for an assistant to help you.",
        "B. A rush of pure criminal anxiety as if security alarms are about to blast.",
        "C. Proud that you managed to sneak an extra item through.",
        "D. Bored and ready to abandon the cart."
    ),
    (
        "A. Plug it in normally like any standard electronic device.",
        "B. Blow on the port like an old Nintendo cartridge.",
        "C. Prop it up at a 37-degree angle with a heavy book resting on the connector.",
        "D. Pray to the tech gods softly."
    ),
    (
        "A. An impeccably clean room with everything right where you left it.",
        "B. A completely remodeled apartment.",
        "C. Total, unexplained chaos or a pet sitting on something highly inappropriate.",
        "D. A quiet, peaceful void."
    ),
    (
        "A. Only a single gallon of milk, as originally intended.",
        "B. A scented candle, seasonal snacks, a houseplant, but no milk.",
        "C. A new outfit and groceries for a feast.",
        "D. Just a basket full of impulse candy."
    ),
    (
        "A. An ergonomic cushion used strictly during working hours.",
        "B. The 'chair-drobe' — a pile of clothes that are too clean for the hamper, too dirty for the closet.",
        "C. A very comfortable sleeping cat.",
        "D. A stack of unread self-help books."
    ),
    (
        "A. Good morning, team, let's dive straight into our key performance metrics.",
        "B. Can you hear me? Am I on mute?",
        "C. Sorry, I was having trouble with my audio.",
        "D. I didn't realize the camera was on."
    ),
    (
        "A. Dropping your phone gracefully and falling asleep on the dot.",
        "B. Turning off the lights and meditating.",
        "C. An involuntary 3-hour deep dive into the history of medieval architecture.",
        "D. Getting up to make a midnight snack."
    ),
    (
        "A. A simple black coffee with a splash of milk.",
        "B. A blank ticket with a smiley face.",
        "C. An absolute manifesto of dietary modifications, syrups, and temperatures.",
        "D. Just a glass of water."
    ),
    (
        "A. Listen to every second with undivided attention and enthusiasm.",
        "B. Stare at it in dread and reply with a simple thumbs-up emoji.",
        "C. Speed it up to 2x and treat it like a podcast.",
        "D. Call them back immediately to ask for a summary."
    ),
    (
        "A. Confident that you are exploring a wonderful new shortcut.",
        "B. A cold sweat of betrayal as you realize you missed the exit 3 miles back.",
        "C. Amused by the polite robotic voice.",
        "D. Ready to turn off the engine and surrender."
    ),
    (
        "A. Check allergen ingredients and dietary restrictions.",
        "B. Plan your exact order so you don't panic under pressure when the waiter arrives.",
        "C. See if they serve breakfast at night.",
        "D. Look at the aesthetic photos of the decor."
    ),
    (
        "A. Complete the transaction because you definitely need industrial-grade foam rollers.",
        "B. Close the tab in sudden clarity and financial guilt before checkout.",
        "C. Send the cart link to a friend with no context.",
        "D. Fall asleep with the screen on your face."
    )
]

user_answers = []
score = 0

def scored(score) :
    match score:
        case 0:
            return "Rs. 0"
        case 1:
            return "Rs. 1,000"
        case 2:
            return "Rs. 2,000"
        case 3:
            return "Rs. 3,000"
        case 4:
            return "Rs. 5,000"
        case 5:
            return "Rs. 10,000"
        case 6:
            return "Rs. 20,000"
        case 7:
            return "Rs. 40,000"
        case 8:
            return "Rs. 80,000"
        case 9:
            return "Rs. 1,60,000"
        case 10:
            return "Rs. 3,20,000"
        case 11:
            return "Rs. 6,40,000"
        case 12:
            return "Rs. 12,50,000"
        case 13:
            return "Rs. 25,00,000"
        case 14:
            return "Rs. 50,00,000"
        case 15:
            return "Rs. 1,00,00,000"
        case 16:
            return "Rs. 7,00,00,000"

print("KBC".center(25, "-"))
for i in range(0, 16):
    print(questions[i])
    for j in question_options[i]:
        print(j)
    print()
    choice = input("Enter your choice (A/B/C/D): ").upper()
    if choice.upper() == correct_answers[i]:
        score += 1
        print("Correct")
    else :
        score += 0
        print("The correct answer was: ", correct_answers[i])
    print("\n\n")
print("_"*50)
print("Congrats!!! ",scored(score))
if (score==16):
    print("Saath Karore")
print("_"*50)
